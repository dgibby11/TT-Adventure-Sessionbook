#!/usr/bin/env python
"""
driver.py -- programmatic driver for TT Adventure Sessionbook.

This is a plain static HTML/CSS/JS app (no build step, no npm deps) served by
Python's http.server. There is no chromium-cli / node / npm in this repo's
dev environment -- this driver uses Playwright for Python instead (see
SKILL.md Prerequisites for the one-time install).

It manages its OWN server subprocess (a throwaway port, separate from a DM's
own start-map.bat session on 8000), drives headless Chromium, and exercises
one representative end-to-end flow:

    load a campaign's dashboard -> toggle DM mode (answers the native
    passphrase prompt) -> open an entity from the Index menu -> find a
    session in the "Planning" category -> launch the Session Runner ->
    verify Prompts / Plan / Pinboard populated -> run the Complete Session
    reveal flow -> confirm no console/page errors.

Usage (from repo root):
    py .claude/skills/run-tt-adventure-sessionbook/driver.py smoke
    py .claude/skills/run-tt-adventure-sessionbook/driver.py smoke --campaign fail-academy --passphrase Smuckers
    py .claude/skills/run-tt-adventure-sessionbook/driver.py open --campaign fail-academy --entity "Torvald Thatch"

Screenshots land in .claude/skills/run-tt-adventure-sessionbook/screenshots/.
"""
import argparse
import contextlib
import json
import os
import socket
import subprocess
import sys
import time
from shutil import which

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))
SCREEN_DIR = os.path.join(SKILL_DIR, "screenshots")
DEFAULT_PORT = 8791  # deliberately not 8000, so this never collides with a DM's own start-map.bat session
# Standard test viewport: full 1080p, matching a DM's session-running screen.
VIEWPORT = {"width": 1920, "height": 1080}


def _py_cmd():
    # "py" launcher on Windows (this repo's primary dev env); "python3" is the
    # safer bet on Linux (e.g. GitHub Actions runners via actions/setup-python)
    # before falling back to plain "python".
    for candidate in ("py", "python3", "python"):
        if which(candidate):
            return candidate
    return "python"


def _launch_kwargs(args):
    """--headed opens a real visible Chromium window so a human can watch the
    run; --slow-mo paces each Playwright action (ms) so the steps are followable
    by eye. Headless (the default) stays the fast path for CI/agent runs."""
    headed = getattr(args, "headed", False)
    slow_mo = getattr(args, "slow_mo", 0)
    # Headed with no explicit pacing flies past too fast to actually watch.
    if headed and not slow_mo:
        slow_mo = 400
    kwargs = {"headless": not headed, "slow_mo": slow_mo}
    # Drive real Google Chrome, not Playwright's bundled Chromium -- it's what
    # the DM actually runs the app in, so rendering/behaviour matches. Pass
    # --channel chromium to fall back to the bundled build.
    channel = getattr(args, "channel", "chrome")
    if channel and channel != "chromium":
        kwargs["channel"] = channel
    return kwargs


def _port_open(port):
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.settimeout(0.3)
        return s.connect_ex(("127.0.0.1", port)) == 0


@contextlib.contextmanager
def static_server(port):
    """Starts `py -m http.server <port>` from the repo root if nothing is
    already listening there, and tears it down on exit. Self-contained --
    no need to hunt down the process by port afterward (that's unreliable
    cross-platform; owning the subprocess handle is not)."""
    already_running = _port_open(port)
    proc = None
    if not already_running:
        proc = subprocess.Popen(
            [_py_cmd(), "-m", "http.server", str(port)],
            cwd=REPO_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(50):
            if _port_open(port):
                break
            time.sleep(0.1)
        else:
            proc.kill()
            raise RuntimeError(f"static server did not come up on port {port}")
    try:
        yield
    finally:
        if proc is not None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()


def storage_key_for(campaign):
    path = os.path.join(REPO_ROOT, "campaigns", campaign, "campaign.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)["storageKey"]


def expand_menu_category(page, type_label, category_label=None):
    """menu.js nests TWO collapsed <details> levels: type (e.g. "Sessions")
    then category (e.g. "Planning") inside it. An item is invisible/
    unclickable until BOTH are expanded -- expanding only the category is
    not enough."""
    return page.evaluate(
        """([typeLabel, catLabel]) => {
            const types = Array.from(document.querySelectorAll('details.menu-type'));
            const t = types.find(d => d.querySelector('.menu-type-title span')?.textContent === typeLabel);
            if (t) t.open = true;
            let c = null;
            if (catLabel) {
                const cats = Array.from(document.querySelectorAll('details.menu-cat'));
                c = cats.find(d => d.querySelector('.menu-cat-title span')?.textContent === catLabel);
                if (c) c.open = true;
            }
            return { typeFound: !!t, catFound: catLabel ? !!c : null };
        }""",
        [type_label, category_label],
    )



def block_remote_writes(page, attempted):
    """Belt-and-braces enforcement of "tests must not alter data".

    js/github-state.js can PUT campaign-state.json to the GitHub contents API.
    It already bails without a token (`if (!getToken() || !cfg?.owner) return;`)
    and a Playwright context starts with empty localStorage, so no token exists
    and no push can fire -- but that's an *incidental* guarantee that a future
    change could quietly remove. Abort any mutating request outright and record
    it, so a regression surfaces as a loud test failure instead of a silent
    write to the real repo."""
    def handler(route):
        req = route.request
        if req.method in ("PUT", "POST", "PATCH", "DELETE"):
            attempted.append(f"{req.method} {req.url}")
            return route.abort()
        return route.continue_()
    page.route("**://api.github.com/**", handler)


def close_menu_panel_if_open(page):
    """Closing the content modal does NOT close the slide-out Index panel
    behind it. Its #panel-backdrop then silently intercepts clicks on
    topbar buttons (Run Session, DM toggle, ...) until the panel is closed
    too."""
    is_open = page.evaluate("document.getElementById('locations-panel').classList.contains('open')")
    if is_open:
        page.click("#close-menu")
        page.wait_for_timeout(150)


def dm_login(page, passphrase):
    """Turning DM mode ON fires a native prompt() for the campaign's
    passphrase (see campaign.json -> dmPassHash). The dialog handler MUST
    be registered before the click -- Playwright auto-dismisses dialogs
    with no handler attached, which reads as "wrong passphrase"."""
    page.once("dialog", lambda d: d.accept(passphrase) if d.type == "prompt" else d.accept())
    page.click("#dm-toggle")
    page.wait_for_function(
        "document.getElementById('dm-toggle').getAttribute('aria-pressed') === 'true'", timeout=5000
    )


def wait_for_dashboard(page):
    # The old #campus-map hotspot view is commented out of index.html now --
    # #dashboard is the real default view. Don't wait on #campus-map.
    page.wait_for_function("document.getElementById('dashboard').innerHTML.length > 0", timeout=30000)


def open_entity(page, name):
    """Opens the Index menu and clicks the first .menu-item whose text
    contains `name`, expanding whatever type/category <details> contain it
    first. Returns True if found and opened."""
    page.click("#open-menu")
    page.wait_for_selector("#locations-panel.open", timeout=5000)
    page.evaluate(
        """(name) => {
            const items = Array.from(document.querySelectorAll('.menu-item'));
            const hit = items.find(b => b.textContent.includes(name));
            if (!hit) return false;
            let el = hit.closest('details');
            while (el) { el.open = true; el = el.parentElement?.closest('details'); }
            return true;
        }""",
        name,
    )
    page.wait_for_timeout(150)
    locator = page.locator(".menu-item", has_text=name)
    if locator.count() == 0:
        return False
    locator.first.click()
    page.wait_for_selector("#modal-overlay:not([hidden])", timeout=5000)
    page.wait_for_timeout(300)
    return True


def run_smoke(args):
    from playwright.sync_api import sync_playwright

    os.makedirs(SCREEN_DIR, exist_ok=True)
    console_errors, page_errors, http_errors = [], [], []
    remote_writes = []
    # Which stages actually executed. A run that silently skips the session
    # flow must NOT report a clean PASS -- see the exit-code note in main().
    stages = {"dashboard": False, "dm_login": False, "session_modal": False,
              "session_runner": False, "complete_dialog": False, "complete_reveal": False}

    def shot(page, name):
        path = os.path.join(SCREEN_DIR, name)
        page.screenshot(path=path)
        print("screenshot:", path)

    with static_server(args.port):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(**_launch_kwargs(args))
            page = browser.new_page(viewport=VIEWPORT)
            page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: page_errors.append(str(e)))
            block_remote_writes(page, remote_writes)
            # A bare console "Failed to load resource: ... 404" doesn't say WHICH
            # url died. Capture the response side too so failures are actionable.
            page.on("response", lambda r: http_errors.append(f"{r.status} {r.url}") if r.status >= 400 else None)

            page.goto(f"http://localhost:{args.port}/index.html?campaign={args.campaign}")
            wait_for_dashboard(page)
            shot(page, "01_dashboard.png")
            stages["dashboard"] = True

            dm_login(page, args.passphrase)
            shot(page, "02_dm_on.png")
            stages["dm_login"] = True
            print("run-session-btn visible:", page.get_attribute("#run-session-btn", "hidden") is None)

            page.click("#open-menu")
            page.wait_for_selector("#locations-panel.open", timeout=5000)
            expand_menu_category(page, "Sessions", "Planning")
            page.wait_for_timeout(200)
            shot(page, "03_menu_planning.png")

            plan_items = page.locator(".menu-cat", has_text="Planning").locator(".menu-item")
            count = plan_items.count()
            print("sessions in Planning category:", count)

            if count == 0:
                print("No session with category 'Planning' found -- skipping Session Runner flow.")
                print("  NOTE: session-runner.js filters the chooser on category == 'Planning'")
                print("  exactly. This campaign's sessions use some other category, so its")
                print("  Session Runner is unreachable and MOST OF THIS SMOKE DID NOT RUN.")
            else:
                name = plan_items.first.inner_text()
                print("opening:", name)
                plan_items.first.click()
                page.wait_for_selector("#modal-overlay:not([hidden])", timeout=5000)
                page.wait_for_timeout(300)
                broken = page.query_selector_all(".xlink-broken")
                print("broken cross-links in modal:", len(broken), [b.inner_text() for b in broken])
                shot(page, "04_session_modal.png")
                stages["session_modal"] = True

                page.click("#modal-close")
                page.wait_for_timeout(150)
                close_menu_panel_if_open(page)

                page.click("#run-session-btn")
                page.wait_for_selector("#sr-chooser-overlay", timeout=5000)
                shot(page, "05_chooser.png")
                chooser_name = name.split("\n")[0]
                page.locator(".sr-chooser-item", has_text=chooser_name).first.click()
                page.wait_for_selector(".sr-panel.sr-prompts", timeout=5000)
                page.wait_for_timeout(300)
                shot(page, "06_runner.png")
                stages["session_runner"] = True

                prompts = page.query_selector_all(".sr-prompt-card")
                pins = page.query_selector_all(".sr-pin-card")
                print(f"prompt cards extracted: {len(prompts)}  pinboard entries: {len(pins)}")

                complete_btn = page.query_selector(".sr-complete-btn")
                if complete_btn is not None and not complete_btn.is_disabled():
                    complete_btn.click()
                    page.wait_for_selector("#session-confirm-overlay", timeout=5000)
                    shot(page, "07_complete_dialog.png")
                    stages["complete_dialog"] = True
                    if not args.allow_state_writes:
                        # READ-ONLY (default): the dialog itself is what we're
                        # testing -- it renders, groups the reveal checkboxes and
                        # is dismissable. Clicking Confirm would flip `revealed`
                        # flags in campaign state, which tests must not do. Cancel
                        # instead; pass --allow-state-writes to opt in.
                        page.click("#session-confirm-cancel")
                        page.wait_for_selector("#session-confirm-overlay", state="hidden", timeout=5000)
                        shot(page, "08_complete_dialog_cancelled.png")
                        print("Complete Session dialog verified, then CANCELLED (read-only run --")
                        print("  no reveal flags written). Pass --allow-state-writes to confirm for real.")
                        page.click(".sr-exit-btn")
                        page.wait_for_timeout(200)
                    else:
                        # Confirming auto-exits the Session Runner (its onConfirmed
                        # callback is `exitRunner`) -- don't try to click Exit Runner
                        # afterward, #session-runner is already torn down/hidden.
                        page.click("#session-confirm-ok")
                        page.wait_for_function(
                            "document.getElementById('session-runner').hidden === true", timeout=5000
                        )
                        shot(page, "08_after_confirm_runner_closed.png")
                        stages["complete_reveal"] = True
                        print("Complete Session CONFIRMED (state written). storageKey:",
                              storage_key_for(args.campaign))
                else:
                    print("no .sr-complete-btn (session has no reveals[], or already completed)")
                    page.click(".sr-exit-btn")
                    page.wait_for_timeout(200)

            print("CONSOLE ERRORS:", console_errors)
            print("PAGE ERRORS:", page_errors)
            print("HTTP ERRORS:", http_errors)
            browser.close()

    clean = not console_errors and not page_errors
    skipped = [k for k, v in stages.items() if not v]
    print("STAGES RUN:", ", ".join(k for k, v in stages.items() if v) or "(none)")
    if skipped:
        print("STAGES SKIPPED:", ", ".join(skipped))

    if remote_writes:
        print("BLOCKED REMOTE WRITES:", remote_writes)
        print("RESULT: FAIL -- the app attempted to mutate remote state during a test run")
        return 1
    if not clean:
        print("RESULT: FAIL (errors on page)")
        return 1
    # A run that never reached the session flow proves almost nothing -- report it
    # as INCOMPLETE (exit 2) rather than letting it masquerade as a clean PASS.
    if not stages["session_runner"]:
        print("RESULT: INCOMPLETE -- no errors, but the session/runner flow never ran")
        return 2
    if stages["complete_reveal"]:
        print("RESULT: PASS (full flow, state written)")
        return 0
    if stages["complete_dialog"]:
        print("RESULT: PASS (full flow, read-only -- reveal dialog verified then cancelled)")
        return 0
    print("RESULT: PASS (reveal dialog not reachable -- session has no reveals[] or is already complete)")
    return 0


def run_open(args):
    from playwright.sync_api import sync_playwright

    os.makedirs(SCREEN_DIR, exist_ok=True)
    console_errors = []
    remote_writes = []

    with static_server(args.port):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(**_launch_kwargs(args))
            page = browser.new_page(viewport=VIEWPORT)
            page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)
            block_remote_writes(page, remote_writes)

            page.goto(f"http://localhost:{args.port}/index.html?campaign={args.campaign}")
            wait_for_dashboard(page)

            if args.dm:
                dm_login(page, args.passphrase)

            found = open_entity(page, args.entity)
            if not found:
                print(f"entity matching {args.entity!r} not found in the (currently visible) menu")
                browser.close()
                return 1

            broken = page.query_selector_all(".xlink-broken")
            print("broken cross-links:", len(broken), [b.inner_text() for b in broken])
            path = os.path.join(SCREEN_DIR, "open_entity.png")
            page.screenshot(path=path)
            print("screenshot:", path)
            print("CONSOLE ERRORS:", console_errors)
            if remote_writes:
                print("BLOCKED REMOTE WRITES:", remote_writes)
            browser.close()
    return 0


def _median(xs):
    xs = sorted(xs)
    n = len(xs)
    if not n:
        return 0.0
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def run_perf(args):
    """Load/performance pass over a real campaign (default fail-academy, which
    carries by far the most authored content).

    Deliberately asserts ONLY on time budgets. Entity counts, payload sizes and
    request counts drift week to week as the DM authors content, so they are
    reported as observations and never gate the result -- a passing perf run
    must not turn red just because someone added ten NPCs. Budgets are generous
    and overridable so ordinary content growth doesn't trip them either.

    Strictly read-only: nothing is written, the reveal dialog is never opened,
    and remote writes are blocked as everywhere else."""
    from playwright.sync_api import sync_playwright

    os.makedirs(SCREEN_DIR, exist_ok=True)
    console_errors, page_errors, remote_writes = [], [], []
    runs = []

    with static_server(args.port):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(**_launch_kwargs(args))
            for i in range(args.runs):
                # Fresh context per run: empty cache + empty localStorage each
                # time, so these are cold-load numbers, not warmed-up ones.
                ctx = browser.new_context(viewport=VIEWPORT)
                page = ctx.new_page()
                page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)
                page.on("pageerror", lambda e: page_errors.append(str(e)))
                block_remote_writes(page, remote_writes)

                seen = {"bytes": 0, "reqs": 0}

                def on_response(r, _s=seen):
                    _s["reqs"] += 1
                    try:
                        _s["bytes"] += int(r.header_value("content-length") or 0)
                    except Exception:
                        pass

                page.on("response", on_response)

                t0 = time.perf_counter()
                page.goto("http://localhost:%d/index.html?campaign=%s" % (args.port, args.campaign))
                wait_for_dashboard(page)
                dashboard_ms = (time.perf_counter() - t0) * 1000

                # Without DM login the menu renders only the player-visible
                # subset, which understates real load. --dm measures the full
                # authored dataset. Still read-only: DM mode only flips a `view`
                # flag in this throwaway context's localStorage, and no campaign
                # content is touched.
                if getattr(args, "dm", False):
                    dm_login(page, args.passphrase)
                    page.wait_for_timeout(150)

                nav = page.evaluate(
                    "() => { const n = performance.getEntriesByType('navigation')[0] || {};"
                    "  return { dcl: n.domContentLoadedEventEnd || 0, load: n.loadEventEnd || 0 }; }"
                )
                entities = page.evaluate("window.ENTITIES ? window.ENTITIES.length : 0")

                # Interaction cost against a fully-populated dataset.
                t = time.perf_counter()
                page.click("#open-menu")
                page.wait_for_selector("#locations-panel.open", timeout=10000)
                menu_ms = (time.perf_counter() - t) * 1000
                menu_items = page.locator(".menu-item").count()
                page.click("#close-menu")
                page.wait_for_timeout(100)

                # Search touches every entity -- the most index-sensitive path.
                SETTLE = 250
                t = time.perf_counter()
                page.fill("#search-input", "a")
                page.wait_for_timeout(SETTLE)
                search_ms = max((time.perf_counter() - t) * 1000 - SETTLE, 0.0)
                page.fill("#search-input", "")

                runs.append({
                    "dashboard_ms": dashboard_ms, "dcl_ms": nav["dcl"], "load_ms": nav["load"],
                    "menu_ms": menu_ms, "search_ms": search_ms,
                    "entities": entities, "menu_items": menu_items,
                    "kb": seen["bytes"] / 1024.0, "reqs": seen["reqs"],
                })
                if i == 0:
                    page.screenshot(path=os.path.join(SCREEN_DIR, "perf_01_dashboard.png"))
                ctx.close()
            browser.close()

    med = {k: _median([r[k] for r in runs]) for k in
           ("dashboard_ms", "dcl_ms", "load_ms", "menu_ms", "search_ms")}
    last = runs[-1]

    print("")
    print("=== PERF: %s (%d cold runs, median) ===" % (args.campaign, args.runs))
    print("  dashboard ready      %8.0f ms   (budget %d)" % (med["dashboard_ms"], args.budget_dashboard))
    print("  DOMContentLoaded     %8.0f ms" % med["dcl_ms"])
    print("  load event           %8.0f ms" % med["load_ms"])
    print("  Index menu open      %8.0f ms   (budget %d)" % (med["menu_ms"], args.budget_interaction))
    print("  search filter        %8.0f ms   (budget %d)" % (med["search_ms"], args.budget_interaction))
    print("")
    scope = "ALL entities (DM view)" if getattr(args, "dm", False) else "player-visible subset only -- pass --dm for the full dataset"
    print("  -- scale (informational ONLY; drifts week to week, never gates) --")
    print("  scope                %s" % scope)
    print("  entities loaded      %8d" % last["entities"])
    print("  menu items rendered  %8d" % last["menu_items"])
    print("  transferred          %8.0f KB over %d requests" % (last["kb"], last["reqs"]))

    over = []
    if med["dashboard_ms"] > args.budget_dashboard:
        over.append("dashboard %.0fms > %dms" % (med["dashboard_ms"], args.budget_dashboard))
    if med["menu_ms"] > args.budget_interaction:
        over.append("menu %.0fms > %dms" % (med["menu_ms"], args.budget_interaction))
    if med["search_ms"] > args.budget_interaction:
        over.append("search %.0fms > %dms" % (med["search_ms"], args.budget_interaction))

    print("")
    print("CONSOLE ERRORS:", console_errors)
    print("PAGE ERRORS:", page_errors)
    if remote_writes:
        print("BLOCKED REMOTE WRITES:", remote_writes)
        print("RESULT: FAIL -- app attempted a remote state write during a perf run")
        return 1
    if console_errors or page_errors:
        print("RESULT: FAIL (errors on page)")
        return 1
    if over:
        print("RESULT: SLOW --", "; ".join(over))
        return 3
    print("RESULT: PASS (within budget)")
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    smoke_p = sub.add_parser("smoke", help="full dashboard -> DM mode -> session -> runner -> reveal flow")
    smoke_p.add_argument("--campaign", default="fail-academy")
    smoke_p.add_argument("--passphrase", default="Smuckers", help="DM passphrase for the chosen campaign")
    smoke_p.add_argument("--port", type=int, default=DEFAULT_PORT)

    open_p = sub.add_parser("open", help="open one entity by (partial) name and screenshot it")
    open_p.add_argument("--entity", required=True)
    open_p.add_argument("--campaign", default="fail-academy")
    open_p.add_argument(
        "--dm", action="store_true",
        help="log in as DM first. Needed for almost everything: a fresh browser has an "
             "empty 'revealed' localStorage, and Player View only shows entities that are "
             "BOTH visibility:player AND revealed -- so a clean Player-View session shows "
             "next to nothing. Omit --dm only when you deliberately want to test that "
             "(currently-)unrevealed state.",
    )
    open_p.add_argument("--passphrase", default="Smuckers")
    open_p.add_argument("--port", type=int, default=DEFAULT_PORT)

    perf_p = sub.add_parser("perf", help="load/performance pass over a real campaign (read-only)")
    perf_p.add_argument("--campaign", default="fail-academy",
                        help="default fail-academy -- the largest real dataset")
    perf_p.add_argument("--passphrase", default="Smuckers")
    perf_p.add_argument("--port", type=int, default=DEFAULT_PORT)
    perf_p.add_argument("--runs", type=int, default=3, help="cold runs to take a median over (default 3)")
    perf_p.add_argument("--dm", action="store_true",
                        help="log in as DM so the full authored dataset is rendered and measured "
                             "(otherwise only the player-visible subset loads)")
    perf_p.add_argument("--budget-dashboard", dest="budget_dashboard", type=int, default=6000,
                        help="ms budget for dashboard-ready (default 6000, deliberately generous)")
    perf_p.add_argument("--budget-interaction", dest="budget_interaction", type=int, default=1500,
                        help="ms budget for menu-open and search (default 1500)")

    for _sp in (smoke_p, open_p, perf_p):
        _sp.add_argument("--headed", action="store_true",
                         help="run in a visible browser window instead of headless, so you can watch the flow")
        _sp.add_argument("--slow-mo", dest="slow_mo", type=int, default=0,
                         help="ms to pause between actions (default 400 when --headed, 0 otherwise)")
        _sp.add_argument("--allow-state-writes", dest="allow_state_writes", action="store_true",
                         help="permit the run to WRITE campaign state (confirms the Complete-Session "
                              "reveal dialog). Off by default: tests must not alter data.")
        _sp.add_argument("--channel", default="chrome",
                         help="browser channel: 'chrome' (default, real Google Chrome), "
                              "'chrome-beta', 'msedge', or 'chromium' for Playwright's bundled build")

    args = p.parse_args()
    if args.cmd == "smoke":
        sys.exit(run_smoke(args))
    elif args.cmd == "open":
        sys.exit(run_open(args))
    elif args.cmd == "perf":
        sys.exit(run_perf(args))


if __name__ == "__main__":
    main()

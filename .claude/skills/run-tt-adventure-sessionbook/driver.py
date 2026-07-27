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


def _py_cmd():
    # "py" launcher on Windows (this repo's primary dev env); "python3" is the
    # safer bet on Linux (e.g. GitHub Actions runners via actions/setup-python)
    # before falling back to plain "python".
    for candidate in ("py", "python3", "python"):
        if which(candidate):
            return candidate
    return "python"


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
    page.wait_for_function("document.getElementById('dashboard').innerHTML.length > 0", timeout=10000)


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
    console_errors, page_errors = [], []

    def shot(page, name):
        path = os.path.join(SCREEN_DIR, name)
        page.screenshot(path=path)
        print("screenshot:", path)

    with static_server(args.port):
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 960})
            page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: page_errors.append(str(e)))

            page.goto(f"http://localhost:{args.port}/index.html?campaign={args.campaign}")
            wait_for_dashboard(page)
            shot(page, "01_dashboard.png")

            dm_login(page, args.passphrase)
            shot(page, "02_dm_on.png")
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
            else:
                name = plan_items.first.inner_text()
                print("opening:", name)
                plan_items.first.click()
                page.wait_for_selector("#modal-overlay:not([hidden])", timeout=5000)
                page.wait_for_timeout(300)
                broken = page.query_selector_all(".xlink-broken")
                print("broken cross-links in modal:", len(broken), [b.inner_text() for b in broken])
                shot(page, "04_session_modal.png")

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

                prompts = page.query_selector_all(".sr-prompt-card")
                pins = page.query_selector_all(".sr-pin-card")
                print(f"prompt cards extracted: {len(prompts)}  pinboard entries: {len(pins)}")

                complete_btn = page.query_selector(".sr-complete-btn")
                if complete_btn is not None and not complete_btn.is_disabled():
                    complete_btn.click()
                    page.wait_for_selector("#session-confirm-overlay", timeout=5000)
                    shot(page, "07_complete_dialog.png")
                    # Confirming auto-exits the Session Runner (its onConfirmed
                    # callback is `exitRunner`) -- don't try to click Exit Runner
                    # afterward, #session-runner is already torn down/hidden.
                    page.click("#session-confirm-ok")
                    page.wait_for_function(
                        "document.getElementById('session-runner').hidden === true", timeout=5000
                    )
                    shot(page, "08_after_confirm_runner_closed.png")
                    print("Complete Session confirmed. Campaign storageKey:", storage_key_for(args.campaign))
                else:
                    print("no .sr-complete-btn (session has no reveals[], or already completed)")
                    page.click(".sr-exit-btn")
                    page.wait_for_timeout(200)

            print("CONSOLE ERRORS:", console_errors)
            print("PAGE ERRORS:", page_errors)
            browser.close()

    ok = not console_errors and not page_errors
    print("RESULT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def run_open(args):
    from playwright.sync_api import sync_playwright

    os.makedirs(SCREEN_DIR, exist_ok=True)
    console_errors = []

    with static_server(args.port):
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            page = browser.new_page(viewport={"width": 1440, "height": 960})
            page.on("console", lambda m: console_errors.append(m.text) if m.type == "error" else None)

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
            browser.close()
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

    args = p.parse_args()
    if args.cmd == "smoke":
        sys.exit(run_smoke(args))
    elif args.cmd == "open":
        sys.exit(run_open(args))


if __name__ == "__main__":
    main()

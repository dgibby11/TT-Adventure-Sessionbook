#!/usr/bin/env python
"""
location_test.py -- where the party is, and how the UI follows it.

Covers the three things that move the app's focus off the campaign's home base:

  * the PARTY LOCATION   (js/state.js)      -- where the party is, separate
                                               from the location on screen
  * the REGIONS HOME     (js/dashboard.js)  -- campaign.json `regions`
  * LOCATION CHIPS       (js/session-runner.js) -- a session's startLocation and
                                               data-location beats move the
                                               dashboard under the Runner

Run (from the repo root):
    py -X utf8 .claude/skills/run-tt-adventure-sessionbook/location_test.py
    py -X utf8 .claude/skills/run-tt-adventure-sessionbook/location_test.py --headed
    py -X utf8 .claude/skills/run-tt-adventure-sessionbook/location_test.py --only runner

Two targets, per the standing testing policy (see SKILL.md):

  test-fixture   every flow, including the ones that MOVE the party. Negative
                 cases (a broken data-location, a campaign with no regions, a
                 stale saved id) are produced by intercepting the request and
                 serving an altered copy, so the fixture's own files stay clean.
  fail-academy   real data, navigation only. Nothing here moves the party or
                 reveals anything; expectations are read from campaign.json and
                 data/*.json at run time, never hard-coded, so authoring new
                 content cannot turn this red.

Every page uses a throwaway browser context, and any write to api.github.com is
aborted and reported -- no campaign file and no saved state is ever altered.

Exit code: 0 = every check passed, 1 = at least one failed.
"""
import argparse
import json
import os
import sys

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SKILL_DIR)
import driver  # noqa: E402

DEFAULT_PORT = 8871  # not 8000 (the DM's own server) and not the smoke driver's 8791

FIXTURE, FIXTURE_PASS = "test-fixture", "Demo"
REAL, REAL_PASS = "fail-academy", "Smuckers"

fails = []          # labels of failed checks
console_errors = []  # (section, text)
remote_writes = []
_section = "-"


def section(name):
    global _section
    _section = name
    print("\n== " + name)


def chk(label, cond, got=None):
    """One assertion. `got` is shown only on failure, to say what was seen."""
    cond = bool(cond)
    line = ("  PASS  " if cond else "  FAIL  ") + label
    if not cond and got is not None:
        line += "   got=%r" % (got,)
    print(line)
    if not cond:
        fails.append("[%s] %s" % (_section, label))
    return cond


def note(text):
    print("  NOTE  " + text)


# ── page plumbing ────────────────────────────────────────────────────────────

def new_page(browser, watch_errors=True):
    ctx = browser.new_context(viewport=driver.VIEWPORT)
    page = ctx.new_page()
    # Everything here is local and renders synchronously; if a control has not
    # appeared in ten seconds it is not going to. (Playwright's default is 30.)
    page.set_default_timeout(10000)
    if watch_errors:
        sec = _section
        page.on("console", lambda m: console_errors.append((sec, m.text)) if m.type == "error" else None)
        page.on("pageerror", lambda e: console_errors.append((sec, "PAGEERROR " + str(e))))
    driver.block_remote_writes(page, remote_writes)
    return page


def open_campaign(page, base, campaign):
    page.goto("%s/index.html?campaign=%s" % (base, campaign))
    driver.wait_for_dashboard(page)
    page.wait_for_function("window.ENTITIES && window.ENTITIES.length > 0", timeout=15000)
    page.wait_for_timeout(150)


def set_dm(page, on, passphrase=None):
    """Toggle DM mode. The first ON in a tab prompts for the passphrase; after
    that the tab is unlocked and the toggle flips silently."""
    is_on = page.evaluate("window.App.isDM()")
    if is_on == on:
        return
    if on and passphrase and not page.evaluate("!!sessionStorage.getItem('dm-unlocked')"):
        driver.dm_login(page, passphrase)
    else:
        page.click("#dm-toggle")
        page.wait_for_function("window.App.isDM() === %s" % ("true" if on else "false"), timeout=5000)
    page.wait_for_timeout(120)


def serve_altered(page, url_glob, alter, as_json=True):
    """Intercept one request and serve an altered copy of the real response.
    `alter` takes the parsed JSON (or the raw text) and returns the new one."""
    def handler(route):
        resp = route.fetch()
        body = resp.text()
        if as_json:
            out = json.dumps(alter(json.loads(body)))
            route.fulfill(status=200, content_type="application/json", body=out)
        else:
            route.fulfill(status=200, content_type="text/html; charset=utf-8", body=alter(body))
    page.route(url_glob, handler)


# ── reading the page ─────────────────────────────────────────────────────────

def title(page):
    return (page.text_content(".dash-location-title") or "").strip()


def view(page):
    return page.evaluate("window.App.getCurrentLocationId()")


def party(page):
    return page.evaluate("window.App.getPartyLocationId()")


def quad_heads(page):
    """Quad header titles, without any '⚑ Party' tag appended to them."""
    return page.eval_on_selector_all(
        ".dash-quad-header", "els => els.map(e => e.firstChild ? e.firstChild.textContent.trim() : '')")


def cards_in(page, selector):
    return page.eval_on_selector_all(selector + " .dash-loc-card", "els => els.map(e => e.dataset.loc)")


def count(page, selector):
    return page.locator(selector).count()


def text_of(page, selector):
    loc = page.locator(selector)
    return (loc.first.text_content() or "").strip() if loc.count() else None


def dash_text(page):
    return page.text_content("#dashboard") or ""


def saved(page, key):
    raw = page.evaluate("k => localStorage.getItem(k)", key)
    return json.loads(raw) if raw else {}


def go(page, loc_id):
    """Look at a location without moving the party."""
    page.evaluate("id => window.App.setCurrentLocation(id)", loc_id)
    page.wait_for_timeout(80)


def launch_runner(page):
    page.click("#run-session-btn")
    page.wait_for_selector("#sr-chooser-overlay", timeout=5000)
    page.locator(".sr-chooser-item").first.click()
    page.wait_for_selector(".sr-panel.sr-prompts", timeout=5000)
    page.wait_for_selector(".sr-prompt-card", timeout=5000)
    page.wait_for_timeout(250)


def exit_runner(page):
    page.click(".sr-exit-btn")
    page.wait_for_function("document.getElementById('session-runner').hidden === true", timeout=5000)
    page.wait_for_timeout(100)


LEGACY_QUADS = ["Locations", "People & Creatures", "Environment", "Curiosities"]


# ── 1. JS unit tests ─────────────────────────────────────────────────────────

def run_unit(browser, base):
    section("unit: tools/tests.html")
    # No error capture here: the page's own image-modal tests request a
    # placeholder image that does not exist, which logs a 404 by design.
    page = new_page(browser, watch_errors=False)
    page.goto(base + "/tools/tests.html")
    page.wait_for_selector(".summary", timeout=15000)
    summary = (page.text_content(".summary") or "").strip()
    # { section title: [pass count, [failed test lines]] }, in page order.
    by_section = page.evaluate("""() => {
        const out = {}; let cur = '(no section)';
        for (const el of document.querySelectorAll('#output > div')) {
            if (el.classList.contains('section')) { cur = el.textContent; out[cur] = [0, []]; }
            else if (el.classList.contains('result')) {
                (out[cur] = out[cur] || [0, []]);
                if (el.classList.contains('pass')) out[cur][0]++; else out[cur][1].push(el.textContent);
            }
        }
        return out;
    }""")
    # This suite gates on the sections it owns. Anything failing elsewhere on
    # the page is reported but is not this suite's to judge.
    OWNED = ("buildRegionModel", "party location")
    for name, (passed, failed) in by_section.items():
        if any(tag in name for tag in OWNED):
            chk("%s: %d passed, %d failed" % (name, passed, len(failed)), passed > 0 and not failed, failed)
        elif failed:
            for line in failed:
                note("unrelated unit test failing in '%s': %s" % (name, line.strip()))
    chk("region-model tests are present", any("buildRegionModel" in n for n in by_section), list(by_section))
    chk("party-location tests are present", any("party location" in n for n in by_section), list(by_section))
    note("page summary: " + summary)
    page.context.close()


# ── 2. fixture: regions home + party location (DM) ───────────────────────────

def run_dashboard(browser, base):
    section("fixture: regions home")
    page = new_page(browser)
    open_campaign(page, base, FIXTURE)
    set_dm(page, True, FIXTURE_PASS)
    key = driver.storage_key_for(FIXTURE)

    chk("home is titled with the campaign name", title(page) == "Test Fixture", title(page))
    chk("one column per region, in campaign.json order, then Elsewhere",
        quad_heads(page) == ["The Proving Ground", "The Far Side", "Elsewhere"], quad_heads(page))
    chk("a region's label comes from campaign.json, not the hub's name",
        text_of(page, '.quad-region[data-region="tf_outpost"] .dash-quad-header') == "The Far Side")
    chk("home has no Environment/Curiosities quads", count(page, ".quad-environment, .quad-curiosities") == 0)
    chk("home has no Home button", count(page, ".loc-bar-back") == 0)
    chk("first card of a region is its hub",
        cards_in(page, '.quad-region[data-region="tf_outpost"]')[:1] == ["tf_outpost"])
    chk("region lists the locations linked from its hub (DM sees the dm-only one)",
        cards_in(page, '.quad-region[data-region="tf_outpost"]') == ["tf_outpost", "tf_camp", "tf_vault"],
        cards_in(page, '.quad-region[data-region="tf_outpost"]'))
    chk("a location equally near two hubs stays in the earlier region",
        cards_in(page, '.quad-region[data-region="tf_root"]') == ["tf_root", "tf_hall"],
        cards_in(page, '.quad-region[data-region="tf_root"]'))
    chk("an unlinked location is listed under Elsewhere, not lost",
        cards_in(page, ".quad-elsewhere") == ["tf_island"], cards_in(page, ".quad-elsewhere"))

    section("fixture: party marker (authored default)")
    chk("party defaults to campaign.json partyLocation", party(page) == "tf_root", party(page))
    chk("header offers a jump to the party",
        text_of(page, ".dash-party-jump") == "⚑ Party: The Proving Ground", text_of(page, ".dash-party-jump"))
    chk("the party's region is flagged",
        count(page, '.quad-region[data-region="tf_root"] .dash-quad-header .dash-party-flag') == 1)
    chk("no other region is flagged",
        count(page, '.quad-region[data-region="tf_outpost"] .dash-party-flag') == 0)
    chk("nothing to 'set' on the home view", count(page, ".dash-party-set") == 0)
    chk("the default is not written to saved state", not saved(page, key).get("partyLocationId"),
        saved(page, key).get("partyLocationId"))

    section("fixture: entering a region and a location")
    page.click('.quad-region[data-region="tf_outpost"] .dash-region-enter')
    page.wait_for_timeout(120)
    chk("clicking a region's hub card enters it", view(page) == "tf_outpost" and title(page) == "The Far Outpost", title(page))
    chk("a location view is the four quads", quad_heads(page) == LEGACY_QUADS, quad_heads(page))
    chk("a hub has Home but no region crumb", count(page, ".loc-bar-back") == 1 and count(page, ".loc-bar-region") == 0)
    chk("authored curiosity shows", "Every plank in the stockade" in dash_text(page))
    chk("night-only curiosity is hidden by day", "lantern over the gate" not in dash_text(page))
    page.click('.loc-time-btn[data-time="night"]')
    page.wait_for_timeout(100)
    chk("night-only curiosity shows at night", "lantern over the gate" in dash_text(page))
    page.click('.loc-time-btn[data-time="day"]')
    page.wait_for_timeout(100)

    page.click('.dash-loc-card[data-loc="tf_camp"]')
    page.wait_for_timeout(120)
    chk("a sub-location opens from the Locations quad", title(page) == "Checkpoint Camp", title(page))
    chk("it shows a crumb up to its region", text_of(page, ".loc-bar-region") == "‹ The Far Side", text_of(page, ".loc-bar-region"))
    chk("its Environment panel is filled", "Six identical tents" in (text_of(page, ".quad-environment") or ""))
    chk("its Curiosities panel is filled", "The grass has been combed" in (text_of(page, ".quad-curiosities") or ""))
    chk("its People panel is filled", "Warden Testwell" in dash_text(page))
    page.click(".loc-bar-region")
    page.wait_for_timeout(120)
    chk("the region crumb goes up to the hub", view(page) == "tf_outpost", view(page))

    page.click('.dash-loc-card[data-loc="tf_hall"]')
    page.wait_for_timeout(120)
    chk("a cross-region link is followable", title(page) == "Fixture Hall", title(page))
    chk("...and the crumb names the region it actually belongs to",
        text_of(page, ".loc-bar-region") == "‹ The Proving Ground", text_of(page, ".loc-bar-region"))
    page.click(".loc-bar-back:not(.loc-bar-region)")
    page.wait_for_timeout(120)
    chk("Home returns to the regions view", view(page) is None and title(page) == "Test Fixture", view(page))

    page.click('.quad-elsewhere .dash-loc-card[data-loc="tf_island"]')
    page.wait_for_timeout(120)
    chk("an Elsewhere location can be entered", title(page) == "Unlinked Island", title(page))
    chk("...and has no region crumb", count(page, ".loc-bar-region") == 0)

    section("fixture: moving the party")
    go(page, "tf_camp")
    chk("DM sees 'Set party here' on a location that is not the party's", count(page, ".dash-party-set") == 1)
    page.click(".dash-party-set")
    page.wait_for_timeout(120)
    chk("party moved", party(page) == "tf_camp", party(page))
    chk("header now reads 'Party is here'", text_of(page, ".dash-party-here") == "⚑ Party is here", text_of(page, ".dash-party-here"))
    chk("'Set party here' and the jump are gone", count(page, ".dash-party-set, .dash-party-jump") == 0)
    st = saved(page, key)
    chk("party + view persisted to campaign state",
        st.get("partyLocationId") == "tf_camp" and st.get("currentLocationId") == "tf_camp", st)

    page.click(".loc-bar-back:not(.loc-bar-region)")
    page.wait_for_timeout(120)
    chk("home: the flag moved to the party's new region",
        count(page, '.quad-region[data-region="tf_outpost"] .dash-quad-header .dash-party-flag') == 1
        and count(page, '.quad-region[data-region="tf_root"] .dash-party-flag') == 0)
    chk("home: the party's own card is marked",
        count(page, '.dash-loc-card-party[data-loc="tf_camp"]') == 1)
    chk("home: jump names the new place",
        text_of(page, ".dash-party-jump") == "⚑ Party: Checkpoint Camp", text_of(page, ".dash-party-jump"))
    page.click(".dash-party-jump")
    page.wait_for_timeout(120)
    chk("the jump brings the view back to the party", view(page) == "tf_camp" and title(page) == "Checkpoint Camp", view(page))

    page.click('.dash-loc-card[data-loc="tf_outpost"]')
    page.wait_for_timeout(120)
    chk("looking elsewhere does not move the party", view(page) == "tf_outpost" and party(page) == "tf_camp", (view(page), party(page)))
    chk("the party's card is marked in a Locations quad too", count(page, '.dash-loc-card-party[data-loc="tf_camp"]') == 1)
    page.click(".dash-party-jump")
    page.wait_for_timeout(120)
    chk("...and one click snaps back", view(page) == "tf_camp", view(page))

    page.reload()
    driver.wait_for_dashboard(page)
    page.wait_for_function("window.ENTITIES && window.ENTITIES.length > 0")
    page.wait_for_timeout(200)
    chk("party + view survive a reload", party(page) == "tf_camp" and title(page) == "Checkpoint Camp", (party(page), title(page)))
    chk("'Party is here' survives a reload", count(page, ".dash-party-here") == 1)

    section("fixture: party shortcut in search")
    page.fill("#search-input", "fixture hall")
    page.wait_for_selector("#search-results .sr-item", timeout=3000)
    row = page.locator("#search-results .sr-item", has_text="Fixture Hall").first
    chk("a location result carries a party button (DM)", row.locator("button.search-party-btn").count() == 1)
    row.locator("button.search-party-btn").click()
    page.wait_for_timeout(250)
    chk("clicking it moves the party there", party(page) == "tf_hall" and view(page) == "tf_hall", (party(page), view(page)))
    chk("...without opening the entry",
        page.evaluate("!document.getElementById('modal-overlay') || document.getElementById('modal-overlay').hidden"))
    chk("...and clears the search", page.input_value("#search-input") == "")

    page.fill("#search-input", "fixture hall")
    page.wait_for_selector("#search-results .sr-item", timeout=3000)
    row = page.locator("#search-results .sr-item", has_text="Fixture Hall").first
    chk("the party's own location shows a marker, not a button",
        row.locator("span.search-party-here").count() == 1 and row.locator("button.search-party-btn").count() == 0)
    page.fill("#search-input", "warden")
    page.wait_for_selector("#search-results .sr-item", timeout=3000)
    chk("a non-location result has no party button",
        page.locator("#search-results .sr-item", has_text="Warden Testwell").first.locator(".search-party-btn").count() == 0)

    section("fixture: party + view buttons in the entry modal")
    page.fill("#search-input", "unlinked")
    page.wait_for_selector("#search-results .sr-item", timeout=3000)
    page.keyboard.press("Enter")
    page.wait_for_selector("#modal-overlay:not([hidden])", timeout=5000)
    page.wait_for_timeout(250)
    chk("Enter still opens the entry", (page.text_content("#modal-title") or "") == "Unlinked Island")
    chk("a location's modal offers 'Move party here'",
        page.is_visible("#modal-party-btn") and text_of(page, "#modal-party-btn") == "⚑ Move party here",
        text_of(page, "#modal-party-btn"))
    chk("...and 'Show on dashboard'", page.is_visible("#modal-view-btn"))
    page.click("#modal-party-btn")
    page.wait_for_timeout(150)
    chk("the button moves the party", party(page) == "tf_island", party(page))
    chk("...reports it in place and disables itself",
        text_of(page, "#modal-party-btn") == "⚑ Party is here" and page.is_disabled("#modal-party-btn"),
        text_of(page, "#modal-party-btn"))
    chk("...and leaves the modal open", page.is_visible("#modal"))
    chk("the dashboard behind it followed", title(page) == "Unlinked Island", title(page))
    page.click("#modal-close")
    page.wait_for_timeout(120)

    page.evaluate("window.openLocationModal(window.App.byId('tf_outpost'))")
    page.wait_for_selector("#modal-overlay:not([hidden])", timeout=5000)
    page.wait_for_timeout(200)
    chk("another location's modal offers the move again",
        text_of(page, "#modal-party-btn") == "⚑ Move party here" and not page.is_disabled("#modal-party-btn"))
    page.click("#modal-view-btn")
    page.wait_for_timeout(150)
    chk("'Show on dashboard' closes the modal", page.evaluate("document.getElementById('modal-overlay').hidden"))
    chk("...moves the view", view(page) == "tf_outpost" and title(page) == "The Far Outpost", view(page))
    chk("...and leaves the party alone", party(page) == "tf_island", party(page))

    page.evaluate("window.openLocationModal(window.App.byId('tf_npc'))")
    page.wait_for_selector("#modal-overlay:not([hidden])", timeout=5000)
    page.wait_for_timeout(200)
    chk("a non-location's modal has neither button",
        not page.is_visible("#modal-party-btn") and not page.is_visible("#modal-view-btn"))
    chk("...but keeps the reveal toggle", page.is_visible("#modal-reveal-btn"))
    page.click("#modal-close")
    page.context.close()


# ── 3. fixture: Session Runner ───────────────────────────────────────────────

def run_runner(browser, base):
    section("fixture: launching a session")
    page = new_page(browser)
    open_campaign(page, base, FIXTURE)
    set_dm(page, True, FIXTURE_PASS)
    run_key = "session-runner.tf_session_1"

    # Put the party somewhere else first, so "launch moved it" is provable.
    page.evaluate("window.App.setPartyLocation('tf_island')")
    launch_runner(page)
    chk("launching moves the party to the session's startLocation", party(page) == "tf_root", party(page))
    chk("the dashboard under the Runner shows it", title(page) == "The Proving Ground", title(page))
    chk("...with that location's own Environment text",
        "featureless grey courtyard" in (text_of(page, ".quad-environment") or ""))
    chk("the Runner and the dashboard are both on screen",
        page.is_visible(".sr-body") and page.is_visible(".dash-quadrants")
        and page.evaluate("document.body.classList.contains('runner-active')"))
    chk("the bar shows where the party is", text_of(page, ".sr-party-loc") == "⚑ The Proving Ground", text_of(page, ".sr-party-loc"))

    section("fixture: location chips on beats")
    labels = page.eval_on_selector_all(".sr-prompt-card", "els => els.map(c => c.querySelector('.sr-prompt-label')?.textContent)")
    chk("every beat is still extracted, with its label",
        labels == ["Opening", "Cross-links", "Encounter", "Travel", "Closing"], labels)
    has_chip = page.eval_on_selector_all(".sr-prompt-card", "els => els.map(c => !!c.querySelector('.sr-loc-chip'))")
    chk("only beats with data-location carry a chip", has_chip == [True, False, True, True, False], has_chip)
    chips = page.eval_on_selector_all(".sr-loc-chip", "els => els.map(e => e.textContent)")
    chk("chips name their location; the party's is flagged",
        chips == ["⚑ The Proving Ground", "▸ Fixture Hall", "▸ Checkpoint Camp"], chips)
    chk("exactly one chip is active", count(page, ".sr-loc-chip-active") == 1)
    chk("prompt bodies still render after the label is lifted out",
        "Nothing is happening" in (page.locator(".sr-prompt-card").first.text_content() or ""))

    page.click('.sr-loc-chip[data-loc="tf_camp"]')
    page.wait_for_timeout(200)
    chk("clicking a chip moves the party", party(page) == "tf_camp", party(page))
    chk("...and the dashboard below follows", title(page) == "Checkpoint Camp", title(page))
    chk("...with the new location's Environment", "Six identical tents" in (text_of(page, ".quad-environment") or ""))
    chk("...and its Curiosities", "The grass has been combed" in (text_of(page, ".quad-curiosities") or ""))
    chk("the active chip moved",
        page.eval_on_selector_all(".sr-loc-chip-active", "els => els.map(e => e.dataset.loc)") == ["tf_camp"])
    chk("the old chip is plain again", text_of(page, '.sr-loc-chip[data-loc="tf_root"]') == "▸ The Proving Ground")
    chk("the bar updated", text_of(page, ".sr-party-loc") == "⚑ Checkpoint Camp", text_of(page, ".sr-party-loc"))
    chk("the Runner remembers it for this session", saved(page, run_key).get("locationId") == "tf_camp", saved(page, run_key))

    section("fixture: peeking away during a run")
    page.click('.dash-loc-card[data-loc="tf_outpost"]')
    page.wait_for_timeout(150)
    chk("the DM can look at another location", title(page) == "The Far Outpost" and party(page) == "tf_camp", (title(page), party(page)))
    chk("chips still show where the party really is",
        page.eval_on_selector_all(".sr-loc-chip-active", "els => els.map(e => e.dataset.loc)") == ["tf_camp"])
    page.click(".sr-party-loc")
    page.wait_for_timeout(150)
    chk("the bar's party button snaps the dashboard back", view(page) == "tf_camp" and title(page) == "Checkpoint Camp", view(page))

    section("fixture: moving the party from the detail panel")
    chk("the plan view has no party button", not page.is_visible(".sr-detail-party"))
    page.locator(".sr-pin-name", has_text="Fixture Hall").first.click()
    page.wait_for_timeout(250)
    chk("opening a location pin offers the move",
        page.is_visible(".sr-detail-party") and text_of(page, ".sr-detail-party") == "⚑ Move party here",
        text_of(page, ".sr-detail-party"))
    page.click(".sr-detail-party")
    page.wait_for_timeout(200)
    chk("it moves the party and the dashboard", party(page) == "tf_hall" and title(page) == "Fixture Hall", (party(page), title(page)))
    chk("...and then reads 'Party is here', disabled",
        text_of(page, ".sr-detail-party") == "⚑ Party is here" and page.is_disabled(".sr-detail-party"))
    chk("the matching chip lit up",
        page.eval_on_selector_all(".sr-loc-chip-active", "els => els.map(e => e.dataset.loc)") == ["tf_hall"])
    page.locator(".sr-pin-name", has_text="Warden Testwell").first.click()
    page.wait_for_timeout(250)
    chk("a non-location pin has no party button", not page.is_visible(".sr-detail-party"))
    page.click('.sr-prompt-card .sr-xlink[data-id="tf_camp"]')
    page.wait_for_timeout(250)
    chk("a [[location]] link in a beat opens it with the move offered",
        page.is_visible(".sr-detail-party") and text_of(page, ".sr-detail-party") == "⚑ Move party here")
    page.click(".sr-detail-back:not(.sr-detail-party)")
    page.wait_for_timeout(150)
    chk("back to the plan hides it again", not page.is_visible(".sr-detail-party"))

    section("fixture: every other party control stays in step with the Runner")
    go(page, "tf_root")
    page.click(".dash-party-set")
    page.wait_for_timeout(200)
    chk("the dashboard's 'Set party here' updates the chips",
        page.eval_on_selector_all(".sr-loc-chip-active", "els => els.map(e => e.dataset.loc)") == ["tf_root"])
    chk("...and the Runner's saved location", saved(page, run_key).get("locationId") == "tf_root")
    page.fill("#search-input", "checkpoint")
    page.wait_for_selector("#search-results .sr-item", timeout=3000)
    page.locator("#search-results .sr-item", has_text="Checkpoint Camp").first.locator("button.search-party-btn").click()
    page.wait_for_timeout(250)
    chk("the search shortcut updates the chips and the dashboard",
        page.eval_on_selector_all(".sr-loc-chip-active", "els => els.map(e => e.dataset.loc)") == ["tf_camp"]
        and title(page) == "Checkpoint Camp")

    section("fixture: exit and resume")
    pins_before = count(page, ".sr-pin-card")
    page.fill("#sr-notes", "resume me")
    page.wait_for_timeout(600)   # notes save on a 400ms debounce
    exit_runner(page)
    chk("exiting leaves the party where it was", party(page) == "tf_camp" and title(page) == "Checkpoint Camp", party(page))
    chk("the dashboard is whole again", not page.evaluate("document.body.classList.contains('runner-active')"))
    st = saved(page, run_key)
    chk("pins, notes and location are all in the Runner's saved state",
        st.get("locationId") == "tf_camp" and st.get("notes") == "resume me" and len(st.get("pinnedIds", [])) == pins_before, st)

    page.evaluate("window.App.setPartyLocation('tf_island')")   # wander off between runs
    launch_runner(page)
    chk("relaunching resumes where the session left the party, not at startLocation",
        party(page) == "tf_camp" and title(page) == "Checkpoint Camp", (party(page), title(page)))
    chk("notes survived the round trip", page.input_value("#sr-notes") == "resume me")
    chk("pins survived the round trip", count(page, ".sr-pin-card") == pins_before, count(page, ".sr-pin-card"))
    exit_runner(page)
    page.context.close()

    # -- a beat pointing at something that is not a location -----------------
    section("fixture: broken data-location (served altered)")
    page = new_page(browser)
    serve_altered(page, "**/content/sessions/tf_session_1.html",
                  lambda html: html.replace('data-location="tf_hall"', 'data-location="tf_nowhere"')
                                   .replace('data-location="tf_camp"', 'data-location="tf_npc"'),
                  as_json=False)
    open_campaign(page, base, FIXTURE)
    set_dm(page, True, FIXTURE_PASS)
    launch_runner(page)
    broken = page.eval_on_selector_all(".sr-loc-chip-broken", "els => els.map(e => [e.tagName, e.textContent, e.title])")
    chk("an unknown id and a non-location id both render broken, as inert spans",
        broken == [["SPAN", "tf_nowhere", "Unknown location: tf_nowhere"], ["SPAN", "tf_npc", "Not a location: tf_npc"]], broken)
    chk("the good chip on the same page still works", count(page, "button.sr-loc-chip") == 1)
    page.locator(".sr-loc-chip-broken").first.click()
    page.wait_for_timeout(120)
    chk("clicking a broken chip does nothing", party(page) == "tf_root", party(page))
    page.context.close()

    section("fixture: unresolvable startLocation (served altered)")
    page = new_page(browser)

    def bad_start(sessions):
        sessions[0]["startLocation"] = "tf_gone"
        return sessions
    serve_altered(page, "**/campaigns/test-fixture/data/sessions.json", bad_start)
    open_campaign(page, base, FIXTURE)
    set_dm(page, True, FIXTURE_PASS)
    page.evaluate("window.App.setPartyLocation('tf_hall')")
    launch_runner(page)
    chk("the Runner still opens", count(page, ".sr-prompt-card") == 5)
    chk("the party is left where it was", party(page) == "tf_hall" and title(page) == "Fixture Hall", party(page))
    chk("the bar reports the real party location", text_of(page, ".sr-party-loc") == "⚑ Fixture Hall")
    page.context.close()

    section("fixture: no startLocation and no party at all (served altered)")
    page = new_page(browser)

    def no_start(sessions):
        sessions[0].pop("startLocation", None)
        return sessions

    def no_party(cfg):
        cfg.pop("partyLocation", None)
        return cfg
    serve_altered(page, "**/campaigns/test-fixture/data/sessions.json", no_start)
    serve_altered(page, "**/campaigns/test-fixture/campaign.json", no_party)
    open_campaign(page, base, FIXTURE)
    set_dm(page, True, FIXTURE_PASS)
    chk("with nothing authored there is no party marker", count(page, ".dash-party-chip") == 0 and party(page) is None, party(page))
    launch_runner(page)
    chk("the Runner opens with the bar's party button hidden", not page.is_visible(".sr-party-loc"))
    chk("no chip is active", count(page, ".sr-loc-chip-active") == 0)
    chk("the dashboard stays on the home view", view(page) is None and title(page) == "Test Fixture", view(page))
    page.click('.sr-loc-chip[data-loc="tf_hall"]')
    page.wait_for_timeout(200)
    chk("a chip still works from that state", party(page) == "tf_hall" and page.is_visible(".sr-party-loc"), party(page))
    page.context.close()


# ── 4. fixture: Player View must stay screen-safe ────────────────────────────

def run_player(browser, base):
    section("fixture: player view, nothing revealed")
    page = new_page(browser)
    open_campaign(page, base, FIXTURE)
    chk("starts in player view", not page.evaluate("window.App.isDM()"))
    chk("home says nothing is discovered", "Nowhere has been discovered yet." in dash_text(page), quad_heads(page))
    chk("no region columns leak", count(page, ".quad-region[data-region]") == 0)
    chk("no party marker for a location players cannot see", count(page, ".dash-party-chip, .dash-party-flag") == 0)

    section("fixture: player view, some locations revealed")
    set_dm(page, True, FIXTURE_PASS)
    page.evaluate("['tf_root','tf_hall','tf_outpost','tf_camp','tf_island'].forEach(id => window.App.setRevealed(id, true))")
    set_dm(page, False)
    chk("revealed regions appear", quad_heads(page) == ["The Proving Ground", "The Far Side", "Elsewhere"], quad_heads(page))
    chk("a dm-only location is not listed",
        cards_in(page, '.quad-region[data-region="tf_outpost"]') == ["tf_outpost", "tf_camp"],
        cards_in(page, '.quad-region[data-region="tf_outpost"]'))
    chk("players see where the party is", text_of(page, ".dash-party-jump") == "⚑ Party: The Proving Ground")
    page.click('.dash-loc-card[data-loc="tf_camp"]')
    page.wait_for_timeout(150)
    chk("players can enter a revealed location", title(page) == "Checkpoint Camp", title(page))
    chk("players never get 'Set party here'", count(page, ".dash-party-set") == 0)
    chk("the Environment panel is shown to players", page.is_visible(".quad-environment"))
    chk("the Curiosities panel is not", not page.is_visible(".quad-curiosities"))
    page.fill("#search-input", "fixture hall")
    page.wait_for_selector("#search-results .sr-item", timeout=3000)
    chk("players get no party button in search", count(page, ".search-party-btn") == 0)
    page.keyboard.press("Enter")
    page.wait_for_selector("#modal-overlay:not([hidden])", timeout=5000)
    page.wait_for_timeout(200)
    chk("players get no party button in the modal", not page.is_visible("#modal-party-btn") and not page.is_visible("#modal-view-btn"))
    page.click("#modal-close")
    page.wait_for_timeout(120)

    section("fixture: the DM leaves the view on a dm-only location")
    set_dm(page, True)
    go(page, "tf_vault")
    chk("the DM can look at it", title(page) == "The Sealed Vault", title(page))
    set_dm(page, False)
    chk("switching to player view falls back to home", title(page) == "Test Fixture", title(page))
    chk("...and the location's name is nowhere on the dashboard", "Sealed Vault" not in dash_text(page))

    section("fixture: the party is somewhere players cannot see")
    set_dm(page, True)
    page.evaluate("window.App.setPartyLocation('tf_vault')")
    chk("the DM can put the party in a dm-only location", count(page, ".dash-party-here") == 1 and title(page) == "The Sealed Vault")
    set_dm(page, False)
    chk("players get no party marker", count(page, ".dash-party-chip, .dash-party-flag, .dash-loc-card-party") == 0)
    chk("players are shown home, not the location", title(page) == "Test Fixture" and "Sealed Vault" not in dash_text(page), title(page))

    set_dm(page, True)
    page.evaluate("window.App.setRevealed('tf_camp', false); window.App.setPartyLocation('tf_camp')")
    set_dm(page, False)
    chk("the same holds for a player-visible location that is not revealed yet",
        count(page, ".dash-party-chip, .dash-party-flag") == 0 and "Checkpoint Camp" not in dash_text(page))
    page.context.close()


# ── 5. fixture: campaigns without regions, and stale saved state ─────────────

def run_legacy(browser, base):
    section("fixture: no `regions` in campaign.json (served altered)")
    page = new_page(browser)

    def no_regions(cfg):
        cfg.pop("regions", None)
        return cfg
    serve_altered(page, "**/campaigns/test-fixture/campaign.json", no_regions)
    open_campaign(page, base, FIXTURE)
    set_dm(page, True, FIXTURE_PASS)
    chk("home is the root location's four quads, as before", quad_heads(page) == LEGACY_QUADS, quad_heads(page))
    chk("titled with the campaign name, no Home button", title(page) == "Test Fixture" and count(page, ".loc-bar-back") == 0, title(page))
    chk("no region columns", count(page, ".quad-region") == 0)
    chk("the root's Environment still renders", "featureless grey courtyard" in (text_of(page, ".quad-environment") or ""))
    chk("the party marker works without regions", count(page, ".dash-party-here") == 1)
    page.click('.dash-loc-card[data-loc="tf_hall"]')
    page.wait_for_timeout(150)
    chk("a location view has Home and no region crumb", count(page, ".loc-bar-back") == 1 and count(page, ".loc-bar-region") == 0)
    page.click(".dash-party-set")
    page.wait_for_timeout(150)
    chk("the party can be moved", party(page) == "tf_hall", party(page))
    page.click(".loc-bar-back")
    page.wait_for_timeout(150)
    chk("Home returns to the root view", title(page) == "Test Fixture" and quad_heads(page) == LEGACY_QUADS)
    chk("...which offers the jump back", text_of(page, ".dash-party-jump") == "⚑ Party: Fixture Hall")
    chk("...and marks the party's card", count(page, '.dash-loc-card-party[data-loc="tf_hall"]') == 1)
    launch_runner(page)
    chk("the Runner still moves the dashboard to startLocation", party(page) == "tf_root" and title(page) == "Test Fixture", (party(page), title(page)))
    page.click('.sr-loc-chip[data-loc="tf_camp"]')
    page.wait_for_timeout(200)
    chk("...and chips still move it", title(page) == "Checkpoint Camp", title(page))
    page.context.close()

    section("fixture: `regions` that all fail to resolve (served altered)")
    page = new_page(browser)

    def junk_regions(cfg):
        cfg["regions"] = ["nope", {"id": "tf_npc"}, {"label": "no id"}]
        return cfg
    serve_altered(page, "**/campaigns/test-fixture/campaign.json", junk_regions)
    open_campaign(page, base, FIXTURE)
    chk("falls back to the root location rather than an empty home", quad_heads(page) == LEGACY_QUADS, quad_heads(page))
    page.context.close()

    section("fixture: saved state that points at entities that are gone")
    page = new_page(browser)
    open_campaign(page, base, FIXTURE)
    key = driver.storage_key_for(FIXTURE)
    page.evaluate("k => localStorage.setItem(k, JSON.stringify({currentLocationId: 'tf_deleted', partyLocationId: 'tf_renamed'}))", key)
    page.reload()
    driver.wait_for_dashboard(page)
    page.wait_for_function("window.ENTITIES && window.ENTITIES.length > 0")
    set_dm(page, True, FIXTURE_PASS)
    chk("an unknown saved view falls back to home", title(page) == "Test Fixture" and quad_heads(page)[0] == "The Proving Ground", title(page))
    chk("an unknown saved party location falls back to the authored default",
        text_of(page, ".dash-party-jump") == "⚑ Party: The Proving Ground", text_of(page, ".dash-party-jump"))
    page.context.close()


# ── 6. real campaign: navigation only ────────────────────────────────────────

def load_campaign_files(campaign):
    root = os.path.join(driver.REPO_ROOT, "campaigns", campaign)
    with open(os.path.join(root, "campaign.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    with open(os.path.join(root, "data", "index.json"), encoding="utf-8") as f:
        files = json.load(f)
    ents = []
    for fn in files:
        with open(os.path.join(root, "data", fn), encoding="utf-8") as f:
            ents += json.load(f)
    return cfg, ents


def run_real(browser, base):
    cfg, ents = load_campaign_files(REAL)
    by = {e["id"]: e for e in ents}
    locs = [e for e in ents if e.get("type") == "location"]

    def rid(r):
        return r if isinstance(r, str) else r.get("id")
    regions = [r for r in cfg.get("regions", []) if rid(r) in by and by[rid(r)]["type"] == "location"]
    labels = [(r.get("label") if isinstance(r, dict) else None) or by[rid(r)]["name"] for r in regions]

    section("%s: regions home (DM)" % REAL)
    page = new_page(browser)
    open_campaign(page, base, REAL)
    set_dm(page, True, REAL_PASS)
    if not regions:
        note("campaign.json lists no regions -- the home view is the root location; region checks skipped")
    else:
        heads = quad_heads(page)
        orphans = page.evaluate(
            "window._dashTest.buildRegionModel(window.ENTITIES, window.CAMPAIGN.regions).orphans.map(e => e.id)")
        chk("one column per region in campaign.json, in order", heads[:len(labels)] == labels, heads)
        chk("'Elsewhere' appears exactly when some location is in no region",
            ("Elsewhere" in heads) == bool(orphans), (heads, orphans))
        if orphans:
            note("%d location(s) are in no region and sit under Elsewhere: %s" % (len(orphans), ", ".join(orphans)))
        for r in regions:
            page.click('.quad-region[data-region="%s"] .dash-region-enter' % rid(r))
            page.wait_for_timeout(100)
            ok = title(page) == by[rid(r)]["name"] and quad_heads(page) == LEGACY_QUADS
            chk("region '%s' opens on its hub" % rid(r), ok, title(page))
            page.click(".loc-bar-back:not(.loc-bar-region)")
            page.wait_for_timeout(80)

    section("%s: party marker" % REAL)
    party_id = cfg.get("partyLocation")
    if not party_id:
        note("campaign.json has no partyLocation -- party checks skipped")
    else:
        name = by[party_id]["name"]
        chk("the header offers a jump to the authored party location",
            text_of(page, ".dash-party-jump") == "⚑ Party: " + name, text_of(page, ".dash-party-jump"))
        if regions:
            model_region = page.evaluate(
                "id => window._dashTest.buildRegionModel(window.ENTITIES, window.CAMPAIGN.regions).regionOf.get(id) || null",
                party_id)
            flagged = page.eval_on_selector_all(".quad-region-party", "els => els.map(e => e.dataset.region || null)")
            chk("the party's region is the one flagged", flagged == ([model_region] if model_region else []), (flagged, model_region))
        page.click(".dash-party-jump")
        page.wait_for_timeout(120)
        chk("the jump opens the party's location", view(page) == party_id and title(page) == name, title(page))
        # Informational: this is the complaint that started all this, so say it
        # out loud -- but it is the DM's content to write, so it never fails.
        for sel, what in ((".quad-environment", "Environment"), (".quad-curiosities", "Curiosities")):
            if page.locator(sel + " .dash-empty").count():
                note("the party's location (%s) has no %s data yet -- that panel shows its placeholder" % (party_id, what))

    section("%s: every location renders as a dashboard view" % REAL)
    bad = []
    for e in locs:
        go(page, e["id"])
        if title(page) != e["name"] or quad_heads(page) != LEGACY_QUADS:
            bad.append((e["id"], title(page)))
    chk("all location entities open cleanly (%d checked)" % len(locs), not bad, bad[:5])
    page.evaluate("window.App.clearLocation()")

    sessions = [e for e in ents if e.get("type") == "session" and e.get("category") == "Planning"]
    if sessions:
        section("%s: Session Runner follows startLocation" % REAL)
        launch_runner(page)
        s = page.evaluate("(() => { const n = document.querySelector('.sr-session-name').textContent; return window.ENTITIES.find(e => e.type === 'session' && e.name === n) || null; })()")
        start = (s or {}).get("startLocation")
        if start and by.get(start, {}).get("type") == "location":
            chk("the dashboard under the Runner shows the session's startLocation", title(page) == by[start]["name"], title(page))
        else:
            note("the launched session has no usable startLocation -- nothing to follow")
        exit_runner(page)
    else:
        note("no session has category 'Planning', so the Runner cannot be launched here; "
             "its location flow is covered on %s" % FIXTURE)
    page.context.close()

    section("%s: player view" % REAL)
    page = new_page(browser)
    open_campaign(page, base, REAL)
    shown = page.eval_on_selector_all(".dash-loc-card", "els => els.map(e => e.dataset.loc)")
    dm_only = {e["id"] for e in locs if e.get("visibility") == "dm-only"}
    chk("no dm-only location is listed on the home view", not (set(shown) & dm_only), sorted(set(shown) & dm_only))
    chk("players get no party-moving controls", count(page, ".dash-party-set, .search-party-btn") == 0)
    if party_id:
        visible = page.evaluate("id => window.App.isVisible(window.App.byId(id))", party_id)
        chk("the party marker is shown to players exactly when they can see that location",
            (count(page, ".dash-party-chip") > 0) == bool(visible), visible)
        if not visible:
            note("players cannot see the party's location (%s): it is not revealed in a fresh browser" % party_id)
    if regions:
        note("regions a fresh player browser sees: %s" % (quad_heads(page) or "(none)"))
    page.context.close()


# ── main ─────────────────────────────────────────────────────────────────────

GROUPS = {
    "unit":      run_unit,
    "dashboard": run_dashboard,
    "runner":    run_runner,
    "player":    run_player,
    "legacy":    run_legacy,
    "real":      run_real,
}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", choices=sorted(GROUPS), action="append",
                    help="run just this group (repeatable). Default: all of them.")
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument("--headed", action="store_true", help="run in a visible browser window")
    ap.add_argument("--slow-mo", dest="slow_mo", type=int, default=0,
                    help="ms to pause between actions (default 400 when --headed)")
    ap.add_argument("--channel", default="chrome",
                    help="'chrome' (default, real Google Chrome) or 'chromium' for Playwright's bundled build")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright

    base = "http://localhost:%d" % args.port
    with driver.static_server(args.port):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(**driver._launch_kwargs(args))
            for name in (args.only or list(GROUPS)):
                # A group that cannot continue (a control it needs never
                # appeared) is one failure, not the end of the run: record it
                # and let the remaining groups report on their own.
                try:
                    GROUPS[name](browser, base)
                except Exception as e:  # noqa: BLE001 -- any crash is a failed group
                    first = str(e).strip().splitlines()[0] if str(e).strip() else type(e).__name__
                    chk("group '%s' ran to completion" % name, False, "%s: %s" % (type(e).__name__, first))
                    for ctx in list(browser.contexts):
                        ctx.close()
            browser.close()

    section("errors")
    chk("no console or page errors on any app page", not console_errors, console_errors[:6])
    chk("the app attempted no remote state writes", not remote_writes, remote_writes)

    print("")
    if fails:
        print("RESULT: FAIL  (%d check(s))" % len(fails))
        for f in fails:
            print("   - " + f)
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

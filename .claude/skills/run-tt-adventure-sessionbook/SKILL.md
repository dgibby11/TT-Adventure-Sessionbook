---
name: run-tt-adventure-sessionbook
description: Build, run, and drive TT Adventure Sessionbook (the D&D campaign dossier web app). Use when asked to start the app, load a campaign, open an entity, run/screenshot the Session Runner, test a session's Complete-Session reveal flow, or otherwise interact with the running app.
---

TT Adventure Sessionbook is a plain static HTML/CSS/JS app (no build step,
no npm dependencies — see root `CLAUDE.md`) served by Python's
`http.server`. There is no `chromium-cli` / Node / npm in this repo's dev
environment, so it's driven with **Playwright for Python** instead, via
`.claude/skills/run-tt-adventure-sessionbook/driver.py`. That driver is the
primary way to interact with a running instance — read below before
improvising your own Playwright script.

All paths below are relative to the repo root.

## Prerequisites

Windows dev environment, no Node/npm/`chromium-cli` available. Python (`py`
launcher) and `pip` are present. One-time install:

```bash
py -m pip install playwright
py -m playwright install chromium
```

(On a from-scratch Linux container instead: `pip install playwright &&
playwright install --with-deps chromium`.)

## Setup / Build

None — static files, no build step, no env vars. `campaigns/index.json` is
the registry of valid `?campaign=<id>` values (e.g. `fail-academy`,
`lost-mine`). Each campaign's DM passphrase lives in
`campaigns/<id>/campaign.json` → `dmPassHash`; `fail-academy`'s is
`Smuckers` (see root `CLAUDE.md` for the full list).

## Run (agent path)

Use the driver — it manages its own throwaway server (port 8791, separate
from a DM's own `start-map.bat` session on 8000) and Playwright browser.

```bash
py .claude/skills/run-tt-adventure-sessionbook/driver.py smoke
py .claude/skills/run-tt-adventure-sessionbook/driver.py smoke --campaign fail-academy --passphrase Smuckers
py .claude/skills/run-tt-adventure-sessionbook/driver.py open --entity "Torvald Thatch" --dm
```

Screenshots land in
`.claude/skills/run-tt-adventure-sessionbook/screenshots/` (gitignored —
regenerate, don't expect them to exist in a fresh clone).

| command | what it does |
|---|---|
| `smoke --campaign X --passphrase P [--port N]` | Full flow: load campaign dashboard → DM login → open the Index menu → find a session in the "Planning" category → open its entity modal (checks for broken `[[ ]]` cross-links) → launch the Session Runner → verify Prompts/Plan/Pinboard populated → run the Complete-Session reveal dialog → confirm zero console/page errors. Exits 0/1 accordingly. |
| `open --entity "<name>" [--dm] [--campaign X] [--passphrase P]` | Opens one entity by partial name match and screenshots its modal. Pass `--dm` almost always (see Gotchas) or `--campaign`'s passphrase won't matter and the entity likely won't be findable at all. |

Both commands print `CONSOLE ERRORS:` / `PAGE ERRORS:` — treat any
non-empty list as a failure even if the rest of the flow "succeeded."

## Run (human path)

`start-map.bat` (double-click) or manually:

```bash
py -m http.server 8000
# then open http://localhost:8000/launcher.html
```

Opening `index.html` directly via `file://` does **not** work — the app
`fetch()`s JSON/HTML fragments, which browsers block over `file://`.

## Test

```bash
py tools/test.py
```

Data-integrity suite over every campaign's `data/*.json` + `content/`
(unresolved `related[]` ids, broken `[[ ]]` links). As of this writing:
69/74 pass, 5 pre-existing warnings unrelated to any given change (`grep`
the failure list against your diff before assuming you broke something).

---

## Gotchas

- **The map view is commented out of `index.html`.** `#campus-map` /
  `#map-stage` no longer exist in the DOM — a "Dashboard" (`#dashboard`)
  is the real default view now. Don't `wait_for_selector("#campus-map")`;
  wait for `#dashboard` to have content instead. (Grepping `index.html`
  for `id="campus-map"` still finds it — it's sitting inside an HTML
  comment, `grep` doesn't know that.)
- **DM login is a native `prompt()` dialog**, not a form field. Register
  `page.on("dialog", ...)` (or `.once`) **before** clicking `#dm-toggle` —
  Playwright auto-dismisses unhandled dialogs, which silently reads as
  "wrong passphrase."
- **The Index menu nests TWO collapsed `<details>` levels**: type (e.g.
  "Sessions") then category (e.g. "Planning") inside it. Expanding only
  one leaves the item invisible/unclickable — expand both (see
  `expand_menu_category()` in the driver).
- **Closing the content modal does not close the slide-out Index panel**
  behind it. Its `#panel-backdrop` then intercepts clicks on topbar
  buttons (`#run-session-btn`, `#dm-toggle`) until you also click
  `#close-menu`.
- **Confirming "Complete Session" auto-exits the Session Runner** — its
  confirm callback is `exitRunner`. Don't try to click `.sr-exit-btn`
  afterward; `#session-runner` is already hidden by then. Wait for
  `document.getElementById('session-runner').hidden === true` instead.
- **A fresh Player View shows almost nothing.** `isVisible()` requires
  `visibility === 'player' && isRevealed(id)` — a brand-new browser has an
  empty `revealed` localStorage, so even normally-public entities won't
  appear until something has revealed them (playing a session's Complete
  flow, or manually). Use `--dm` (or log in as DM) for anything except a
  deliberate "what does an untouched Player View look like" check.
- **The revealed/notes localStorage key is per-campaign, not fixed.** It's
  `campaign.json`'s `storageKey` field (e.g. `fail-academy.v1`), not a
  single global key — don't hardcode one when inspecting/resetting state.
- **Session Runner only lists sessions with `category: "Planning"`**
  exactly (hardcoded in `session-runner.js`'s chooser filter) — a session
  entity with any other category, even a very similar one, silently never
  appears in the "▶ Run Session" chooser.
- **Windows console + emoji/unicode content = `UnicodeEncodeError`.** The
  app's UI text includes glyphs like `☰`/`▶`. Run the driver with
  `py -X utf8 driver.py ...` (or set `PYTHONUTF8=1`) rather than plain
  `py driver.py`, or printing page text/content crashes the driver, not
  the app.
- **Don't hunt for the server process by port to kill it** (`lsof`/`pkill`
  are unreliable on this Windows/Git-Bash setup). The driver starts its
  own `http.server` subprocess and calls `.terminate()`/`.kill()` on that
  handle directly — self-contained, no port-scanning needed either
  direction.

## Troubleshooting

- **`Locator.click: ... element is not visible`, resolves correctly but
  never becomes visible**: almost always one of the two `<details>`
  collapse levels above, or the leftover `#panel-backdrop` from an
  unclosed Index panel. Screenshot at the point of failure — a collapsed
  section or a backdrop-over-everything is obvious once you look.
- **`TimeoutError` waiting on `#campus-map`**: see the map/Dashboard
  gotcha above — that selector doesn't exist anymore.
- **DM login "fails" (`run-session-btn` stays hidden) with no thrown
  error**: the dialog handler was registered *after* `page.click("#dm-toggle")`,
  or not at all — Playwright auto-dismissed the passphrase prompt.

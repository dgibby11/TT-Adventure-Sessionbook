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

## Testing policy (standing DM instruction)

1. **Always UI-test against `fail-academy`.** It is the driver default for both
   `--campaign` and `--passphrase`, so plain `driver.py smoke` is already
   correct — don't pass another campaign unless the DM asks.
2. **Never alter campaign data.** Runs are read-only by default and enforce it
   three ways:
   - the Complete-Session dialog is opened and **cancelled**, never confirmed,
     so no `revealed` flags are written (`--allow-state-writes` opts in);
   - any `PUT`/`POST`/`PATCH`/`DELETE` to `api.github.com` is aborted and
     reported (`block_remote_writes()`), so a test can never push
     `campaign-state.json` to the real repo;
   - Playwright uses a throwaway browser context, so `localStorage` starts
     empty and is discarded at close — the DM's own Chrome profile and its
     saved notes/reveals are never touched.

   Verified: opening the reveal dialog and cancelling leaves `localStorage`
   byte-identical with 0 flags written.

3. **Use `test-fixture` for full-coverage runs.** `fail-academy`'s only
   Planning session has an empty `reveals[]`, so its Complete-Session dialog is
   unreachable and the default run reports `STAGES SKIPPED: complete_dialog,
   complete_reveal` (nothing is silently skipped). `campaigns/test-fixture/` is
   a purpose-built, hidden, non-disruptive campaign that covers everything:

   ```bash
   py -X utf8 .claude/skills/.../driver.py smoke                              # fail-academy: real content
   py -X utf8 .claude/skills/.../driver.py smoke --campaign test-fixture --passphrase Demo   # full flow
   ```

   Run both: `fail-academy` proves the real data still renders, `test-fixture`
   proves the machinery still works. Neither writes state.

### The `test-fixture` campaign

Holds exactly one entity of every type (location ×2, npc, faction, item,
creature, mystery, session, reference), cross-linked, with a `Planning`
session whose `reveals[]` is populated — so Prompts, Plan, Pinboard and the
Complete-Session dialog all render. It also deliberately includes a `dm-only`
entity (`tf_mystery`), `.dm-only` / `.dm-restricted` blocks, external `links[]`
(`tf_creature`), and an `environment` object on the root, so the view toggle
and the modal's References section are covered too.

**It is hidden from the campaign picker.** Its `campaigns/index.json` entry
carries `"hidden": true`, and `launcher.html` filters those out — so neither
the DM nor players ever see it. It must still be *listed* there, because
`js/data.js` validates `?campaign=` against the registry and redirects to the
launcher for unknown ids. It stays reachable two ways:

- direct deep link — `index.html?campaign=test-fixture` (how the driver opens it)
- `launcher.html?showHidden=1` — shows hidden campaigns in the picker, for debugging

Its `campaign.json` sets `github.owner`/`repo` to `""` on purpose: `github-state.js`
bails on `!cfg?.owner`, so the fixture can never push remote state even with a
token present. Entity ids are `tf_`-prefixed. Passphrase: `Demo`.

## Prerequisites

Windows dev environment, no Node/npm/`chromium-cli` available. Python (`py`
launcher) and `pip` are present. One-time install:

```bash
py -m pip install playwright
py -m playwright install chrome     # real Google Chrome, NOT bundled chromium
```

The driver drives **real Google Chrome** (Playwright `channel="chrome"`) by
default, not Playwright's bundled Chromium — it's the browser the DM actually
runs the app in, so what the test sees is what the DM sees. If Chrome is
already installed system-wide — it is on this box, Chrome 151 at
`C:\Program Files\Google\Chrome\Application\chrome.exe` — then
`playwright install chrome` is a no-op and nothing else is needed.

Pass `--channel chromium` to fall back to the bundled build (or
`--channel msedge` / `chrome-beta`). Note the two are NOT equivalent: headless
Chromium never requests `/favicon.ico`, real Chrome does — see Gotchas.

(On a from-scratch Linux container instead: `pip install playwright &&
playwright install --with-deps chrome`.)

## Setup / Build

None — static files, no build step, no env vars. `campaigns/index.json` is
the registry of valid `?campaign=<id>` values. Each campaign's DM passphrase
lives in `campaigns/<id>/campaign.json` → `dmPassHash`.

All five campaigns, verified against the smoke test:

| campaign | passphrase | Planning sessions | exercises reveal flow? |
|---|---|---|---|
| `fail-academy` | `Smuckers` | 1 (`session_2`) | **No** — its only Planning session has `reveals: []` |
| `lost-mine` | `Demo` | 4 | **Yes** (8–26 reveals each) — best full-flow target |
| `salt-below` | `Demo` | 3 | **Yes** (5–9 reveals each) |
| `curse-of-strahd` | `Demo` | **0** — categories are `Chapter 1..15` | No — Session Runner unreachable |
| `descent-into-avernus` | `Demo` | **0** — category is `Sessions` | No — Session Runner unreachable |
| `test-fixture` | `Demo` | 1 (`tf_session_1`) | **Yes** — purpose-built; hidden from the picker |

`fail-academy` cannot exercise the Complete-Session reveal flow at all (empty
`reveals[]`) — use `test-fixture` for that, not a real campaign. The last
two campaigns' sessions never appear in the "▶ Run Session" chooser at all,
because it filters on `category == "Planning"` exactly (see Gotchas); that's a
data-authoring gap in those campaigns, not a driver bug.

## Run (agent path)

Use the driver — it manages its own throwaway server (port 8791, separate
from a DM's own `start-map.bat` session on 8000) and Playwright browser.

```bash
py .claude/skills/run-tt-adventure-sessionbook/driver.py smoke
py .claude/skills/run-tt-adventure-sessionbook/driver.py smoke --campaign fail-academy --passphrase Smuckers
py .claude/skills/run-tt-adventure-sessionbook/driver.py open --entity "Torvald Thatch" --dm

# watch it happen in a real visible Chrome window (paces itself; 400ms/action)
py -X utf8 .claude/skills/run-tt-adventure-sessionbook/driver.py smoke --campaign lost-mine --passphrase Demo --headed
py -X utf8 ... smoke --headed --slow-mo 600     # slower, for demoing to a human
```

All runs use a fixed **1920x1080** viewport (`VIEWPORT` in `driver.py`),
matching a DM's session-running screen — keep screenshots comparable by
changing that constant rather than passing per-run sizes.

`--headed` / `--slow-mo N` / `--channel X` work on **both** subcommands.
Headless (the default) stays the fast path for agent/CI runs; use `--headed`
when a human wants to watch, or when a failure isn't obvious from screenshots.

Screenshots land in
`.claude/skills/run-tt-adventure-sessionbook/screenshots/` (gitignored —
regenerate, don't expect them to exist in a fresh clone).

| command | what it does |
|---|---|
| `smoke --campaign X --passphrase P [--port N]` | Full flow: load campaign dashboard → DM login → open the Index menu → find a session in the "Planning" category → open its entity modal (checks for broken `[[ ]]` cross-links) → launch the Session Runner → verify Prompts/Plan/Pinboard populated → run the Complete-Session reveal dialog → confirm zero console/page errors. See exit codes below. |
| `perf [--campaign X] [--dm] [--runs N]` | Load/performance pass. Defaults to `fail-academy` — the largest real dataset, which is the point. Cold-loads the campaign `--runs` times (default 3, fresh context each time), takes medians for dashboard-ready / DOMContentLoaded / load / Index-menu-open / search, and prints scale figures. Read-only: never opens the reveal dialog, never writes state. Pass `--dm` to render the FULL authored dataset (without it only the player-visible subset loads and the numbers understate real load). |
| `open --entity "<name>" [--dm] [--campaign X] [--passphrase P]` | Opens one entity by partial name match and screenshots its modal. Pass `--dm` almost always (see Gotchas) or `--campaign`'s passphrase won't matter and the entity likely won't be findable at all. |

Both commands print `CONSOLE ERRORS:` / `PAGE ERRORS:` / `HTTP ERRORS:` —
treat any non-empty list as a failure even if the rest of the flow
"succeeded." `HTTP ERRORS:` names the offending URL, which a bare console
`Failed to load resource … 404` does not.

`smoke` also prints `STAGES RUN:` / `STAGES SKIPPED:` and exits:

| exit | meaning |
|---|---|
| `0` | `PASS (full flow, read-only)` — everything incl. the reveal dialog ran clean and was cancelled. Also `PASS (full flow, state written)` under `--allow-state-writes`, or `PASS (reveal dialog not reachable)` when the session has no `reveals[]` (the normal `fail-academy` result). |
| `1` | `FAIL` — console/page errors, **or** the app attempted a remote state write (reported as `BLOCKED REMOTE WRITES:`). |
| `2` | `INCOMPLETE` — no errors, but the session/runner flow never ran, so the test proved almost nothing. **Do not read this as a pass.** |

Exit 2 exists because a campaign with no `Planning` session used to sail
through reporting a clean PASS while silently skipping ~80% of the flow.
Always check `STAGES RUN:` before trusting a green result.

### Load / performance testing

`perf` deliberately runs against **`fail-academy`**, because its volume of real
authored content is exactly what makes the measurement meaningful. Two rules
make that safe and durable:

- **It asserts only on time budgets.** Entity counts, menu-item counts,
  payload size and request counts are printed under an explicit
  `informational ONLY; drifts week to week, never gates` header. They are
  never compared against expected values, so a perf run cannot turn red just
  because the DM authored ten new NPCs. Budgets default generous
  (`--budget-dashboard 6000`, `--budget-interaction 1500`) and are
  overridable, so ordinary content growth won't trip them either.
- **It changes nothing.** No reveal dialog, no notes, no state writes, remote
  writes blocked. `--dm` only flips a `view` flag in the throwaway browser
  context. Verified: `git status campaigns/fail-academy` stays clean.

Exit `3` means `SLOW` (over budget but functionally fine) — distinct from `1`
(errors) so a slow run is never confused with a broken one.

Baseline measured 2026-08-16 (Chrome 151, 162 entities, `--dm`): dashboard
ready **143 ms**, DOMContentLoaded 86 ms, menu open 18 ms, search 15 ms,
94 KB over 28 requests. Treat these as an order-of-magnitude reference, not a
regression threshold — hardware and content both move.

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
**71/74 pass, 3 pre-existing warnings** (re-verified 2026-08-15; the older
"69/74, 5 warnings" note was stale). All 3 are the same unresolved
`related[]` id in `fail-academy` — `campus_wildlife`, referenced by
`--barbarians`, `--druids`, and `--maren_duskhollow` but never defined.
That's the clean baseline: `grep` the warning list against your diff before
assuming you broke something, and treat any 4th warning as yours.

---

## Gotchas

- **Real Chrome requests `/favicon.ico`; headless Chromium doesn't.** This
  used to 404 and fail the zero-console-errors gate for a reason unrelated to
  the app. **Resolved** — the repo now ships a real favicon (`favicon.ico` at
  the server root, plus `shared/img/favicon-32.png` and `favicon-180.png`,
  linked from both `index.html` and `launcher.html`). The driver's old
  `stub_favicon()` workaround has been deleted, so a genuinely broken icon
  will now correctly fail a run. If `/favicon.ico` starts 404ing again, that
  is a real regression — don't re-add a stub.
- **`RESULT: PASS` is not sufficient on its own — read `STAGES RUN:`.** A
  campaign with no `Planning` session skips the session modal, Session Runner
  and reveal flow entirely; that now reports `INCOMPLETE` / exit 2, but the
  console/page error lists will still be empty and look reassuring.
- **The reveal flow can't be tested on `fail-academy`** — its only Planning
  session has an empty `reveals[]`, so `.sr-complete-btn` never renders and
  the run reports `PASS (reveal flow not exercised)`. Use `lost-mine` or
  `salt-below` for anything touching Complete-Session.

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

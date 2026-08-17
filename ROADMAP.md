# TT Adventure Sessionbook — Roadmap & Feature Backlog

Living document. Reprioritize freely. Add notes under each item as thinking evolves.

---

## Priority Queue

### ~~0a. Tests — Part 1: Data Integrity (Python)~~ ✅ Done
**Command:** `python tools/test.py` — also runs automatically from `start-map.bat`

44 checks across all registered campaigns: JSON parse validity, required entity fields, duplicate IDs, `related[]` resolution, `contentFile` existence on disk, `[[id]]` cross-link resolution, `dmPassHash` presence, and `fail-academy` registry exclusion. Failures print and set a non-zero exit code; server still starts.

**Also fixed during implementation:**
- `descent-into-avernus/data/index.json` — filenames were missing `.json` extensions; `references` was listed twice
- `curse-of-strahd` — `abbey_of_saint_markovia` existed in both `locations.json` and `factions.json`; faction renamed to `abbey_of_saint_markovia_faction`

---

### ~~0b. Tests — Part 2: JS Unit Tests (Browser)~~ ✅ Done
**URL:** `http://localhost:8000/tools/tests.html` (server must be running)

No campaign needed — mocks are inline. Approach: `window._genTest` added to the end of `generator.js`; `window._modalTest` added to end of `modal.js`. Non-breaking; easy to audit.

**Covers:**
- `generateNPC()` — required fields, `_meta`, unique ids, 200-roll secret probability
- Seeding — name override, gender pronouns, race recorded in `_meta`
- `rollOccupation()` — category/role always valid; common categories outnumber rare over 500 rolls
- `generateItem()` — required fields, rarity always one of four valid tiers (20 rolls)
- `mergeExt()` — append vs. replace; `_`-prefixed keys never written to T
- `makeLink()` — known id → `<a>`; unknown → `<span class="xlink-broken">`; custom labels honored
- `resolveCrossLinks()` — `[[id]]` and `[[id|label]]` replaced in DOM; broken ids show as broken spans; surrounding text preserved

---

### ~~1. Dice Roller — Multi-d20 Display (Advantage / Disadvantage)~~ ✅ Done

Auto-detect approach: any multi-roll of d20 shows individual die values side-by-side in both the stage and history; no sum shown. All other dice (2d6, etc.) still show a total. No UI decision needed during play.

---

### ~~2. NPC Generator — Quick Mode (Townsfolk / Shopkeeper)~~ ✅ Done

**⚡ Quick NPC** button in the topbar — one click opens a compact floating card. No form. Shows name, race/gender/occupation, one appearance note, one personality trait in italics. Re-roll generates a fresh NPC; Save persists it to the generator's saved list (same as full generator). Esc or click-outside dismisses. Full generator unchanged at `⚄ Generate`.

---

## Icebox (easiest → hardest)

- ~~**Remove dashboard subtitle**~~ ✅ Done — one-line fix in `makeHeader()`.
- ~~**Location bar → dashboard header**~~ ✅ Already done — `#location-bar` gone; back button, time toggle, Full Entry all inline in `makeHeader()`.
- ~~**App rename**~~ ✅ Done — renamed to **TT Adventure Sessionbook** across index.html, data.js, style.css, start-map.bat, tools, README, ROADMAP, CLAUDE.md. GitHub repo name (DnDAcademy) unchanged — rename that separately on GitHub if desired.
- ~~**5e-bits API research**~~ ✅ Done — SRD REST API (dnd5eapi.co) and Open5e are both viable. Most useful endpoint: `/monsters/{index}` for stat blocks. Verdict: low priority — SRD content is thin (no campaign-specific monsters) and offline-first means silent failures during sessions. If implemented, best as an optional "Look up stat block →" button on creature entities. Not worth building until content gaps are felt at the table.
- ~~**Search improvements**~~ ✅ Done — tag search, multi-word AND matching, score-based ranking.
- ~~**Persistent DM state**~~ ✅ Already done — notes, revealed flags, session completion, location, and time all persisted via localStorage.
- ~~**Session runner image panel**~~ — removed from active icebox. Cold storage: the idea was to split the bottom of the session runner into thirds with a center image cycler. Shelved indefinitely.
- ~~**Random generator expansion**~~ ✅ Done — added "Tables" third tab with Weather (weighted conditions + detail) and Encounter (4 environments: Road, Wilderness, Town, Dungeon) roll tables.
- **Color scheme — contrast overhaul** — *partially done:* the dashboard ground is now parchment (`--paper`) while the quads stay dark, so panels no longer blur into the background once they fill with data; the chrome sitting on it (title, meta, Full Entry, time-of-day buttons) was re-pointed to the sepia scale, scoped under `#dashboard`. Still to review: modal/overlay backgrounds, the Session Runner's own panels, and the menu/topbar surfaces.
- **Session Runner — quick-capture for Session Notes** — the DM reports bouncing between Prompts and Session Notes mid-session. Cause: `.sr-body` is `grid-template-columns: 1fr 1fr 1fr` and the two most-used surfaces sit in the *outer* two columns (Prompts left, Notes at the foot of the right sidebar as a fixed 160px textarea), with the plan between them — ~1,300px of travel at 1920px. They are not equal-weight surfaces: Prompts is a *dwell* surface read constantly, Notes is a *burst* surface used occasionally.
  **Planned fix:** a one-line quick-capture input pinned at the foot of the Prompts column plus a global hotkey (e.g. `N`) that focuses it from anywhere; Enter appends a timestamped line to Session Notes and clears. The DM never leaves Prompts; the full textarea stays on the right for reading/editing the log, which is the genuine "jump" case. Reuses the existing notes path — `sr-notes` already autosaves on a 400ms debounce to `session-runner.<id>`.
  **Alternatives considered:** (a) move the notes textarea under Prompts — simplest, but permanently costs ~160px of prompt space; (b) collapsible notes drawer at the foot of the Prompts column, collapsed to a one-line preview — best space economy, fiddliest; (c) hotkey-summoned overlay pad — no layout change, but the app already has several modals. Consider (b) as a follow-up if re-reading notes mid-session also proves common.
  **Open question before building:** the DM said "bouncing between the Prompts and the Session Notes in the center panel" — confirm whether that means the outer-column travel described above, or a preference for Prompts and Notes to *share the center column* and toggle, with the plan moved out. Different shape; do not guess.

- **Settings modal** — a `⚙ Settings` button/link in the topbar's upper-right opening a modal of user options. First occupant: **theme / colour scheme** selection, so the parchment work above becomes a choice rather than a hard-coded edit. Build it as a general settings surface, not a theme picker — future options land here rather than accreting more topbar buttons. Needs a settings store in `localStorage`, `data-theme` on `<html>`, per-theme `:root` blocks, and a modal shell reusing the existing one. Later candidates: default view (DM/player), font size, which dashboard quadrants show, time-of-day default. **See the theming audit below before starting.**

#### Theming audit — what has to be tokenised first

Audit of `css/style.css` (2,962 lines) done 2026-08-16. The blocker is not the
number of colours, it's that colour is currently expressed three different ways:
**22 `--tokens`, 126 `rgba()` literals, and ~20 hard-coded hex values.** Only the
first is themeable. Until the other two are folded in, switching a theme will
recolour some surfaces and leave others stranded.

**Proposed role tokens (~12, from ~6 hues).** Six hues is right; six *values* is
not, because separation needs several steps of the same hue. A theme = redefining
this list, nothing else:

| token | role | today |
|---|---|---|
| `--surface-0` | page ground | `--bg` `#12141a` / now `--paper` on dashboard |
| `--surface-1` | panels, quads, pinboard cards | `--panel` `#1e2132` |
| `--surface-2` | elevated: dropdowns, prompt cards, hover | `--panel-2` `#272940` |
| `--surface-sunk` | inset: panel headers, notes fields | `--bg-2` `#0d0f13` |
| `--border` | primary separator | `--line` `#46424e` |
| `--border-soft` | secondary separator | `--line-soft` `#353248` |
| `--text` | body copy | `--ink` `#e8dfce` |
| `--text-muted` | labels, meta, placeholders | `--muted` `#a99c83` (56 uses — most-used token) |
| `--accent` | headings, active state | `--gold` / `--gold-soft` |
| `--danger` | modal rule, DC pills, destructive | `--oxblood` / `--oxblood-2` |
| `--dm` | DM-only signalling | `--dm` `#d39a3e` |
| `--scrim` | overlay dim behind modals | 126 assorted `rgba(0,0,0,x)` |

Plus one **inverse pair** (`--paper` + `--sepia`/`--sepia-mut`) for parchment
surfaces. In a parchment theme that pair and `--surface-0` converge — which is
exactly where new contrast bugs will appear, so treat it as a real case, not an
afterthought. `--panel-bg` is a dead alias of `--panel` (1 use) — delete it.

**Separation-critical pairs (surface against surface).** Each of these is a place
where two backgrounds meet and the only thing preventing a blur is their value
gap — the original dashboard complaint was #1 in this list:

1. page ground ↔ `.dash-quad` — *fixed* by the parchment change; the rest are not
2. `.dash-quad` ↔ the cards inside it (`.dash-entity-card`, `.dash-loc-card`, `.dash-cur-card`, `.dash-env-block`)
3. `.sr-panel` ↔ `.sr-prompt-card` (`--panel-2`) and `.sr-pin-card` (`--panel`)
4. `.sr-panel-hdr` (`--bg-2`) ↔ its own panel body
5. `#search-results` (`--panel-2`) floating over topbar **and** the now-parchment dashboard — this dropdown crosses two grounds
6. `#resources-menu` (`--panel-2`) over the topbar
7. **Pop-outs:** `#dice-panel` and `#quick-npc-panel` (`#1a1510`), `#generator-panel` (`#16110c`) — all hard-coded, all darker than `--bg`, none themeable today
8. `#modal` (`--paper`) over `#modal-overlay` scrim
9. `#session-confirm-dialog` (`--paper`) — renders *over the Session Runner*, so its scrim has to work against a busy three-panel layout, not the page
10. **`.stat-block` (`#fdf1dc`) nested inside the parchment modal (`--paper` `#e9ddc1`)** — parchment on parchment, the lowest-contrast pair in the app, and entirely hard-coded (`#58180d`, `#9c2512`, `#c8a96e`, `#1a1a1a`). It is a self-contained light theme that will not follow a dark theme at all
11. `#topbar` (`--leather`) ↔ page ground
12. `#locations-panel` ↔ `#panel-backdrop` scrim ↔ page beneath

**Frame/border inventory.** `--line` carries topbar buttons, search input and
results, the dice/quick-NPC/resources pop-outs, runner cards and chooser items.
`--line-soft` carries the `.dash-quad` frame, the dashboard header rule and the
notes-field top rule. `--paper-edge` frames the modal and (since the parchment
change) the dashboard chrome. Three runner rules use **gold at alpha**
(`rgba(201,162,39,0.22–0.3)` on `.sr-bar`, `.sr-panel`, `.sr-panel-hdr`) — alpha
over a changing surface shifts with the theme, so these need to become solid
tokens. `#modal-header` uses a 2px `--oxblood` rule; the stat block uses
hard-coded `#9c2512` / `#c8a96e`.

**Readability pairs (text on its ground).** `--muted` on the four dark surfaces is
the most likely failure (56 uses, lowest-contrast text in the app). Then
`--ink` on `--bg`/`--panel`/`--panel-2`/`--bg-2`; `--sepia` and `--sepia-mut` on
`--paper` (modal, confirm dialog, resource modal, and now the dashboard header
strip); `--gold` headings on dark (`#topbar h1`, `.menu-type-title`,
`.dash-quad-hdr`); `--gold-soft` on `--bg-2` (`.sr-panel-hdr`); `#58180d` on
`#fdf1dc` (stat block); oxblood DC pills on `--panel`; and the placeholder text in
`.sr-notes-ta` / `.dash-notes-ta`, which is muted-on-sunk — the weakest pair of
all.

**Order of work.** (1) Rename the existing tokens to the role names above, leaving
values alone — no visual change, purely mechanical. (2) Replace the ~20 hard-coded
hex values, starting with the three pop-outs and the stat block. (3) Replace the
`rgba()` literals that encode surface or border colour; the ones that are genuinely
just shadow/scrim can stay, but should reference `--scrim`. (4) Only then add
`data-theme` blocks. Steps 1–3 are worth doing even if the picker is never built —
they are what make the current palette auditable.

**Guard rail.** Whatever the theme, keep a minimum lightness gap between
`--surface-0/1/2`. The bug that started this was two navies about four points
apart in lightness; any theme that lets those converge reproduces it.
- ~~**Player vs DM view**~~ ✅ Already done — `isVisible()` gates on `visibility:"player"` AND `isRevealed()`; dm-only blocks hidden in player mode; toggle + badge in topbar.
- **Import process overhaul** — CoS and DiA are sparse stubs; define content standard per entity type, richer templates, semi-automate Google Doc → JSON+HTML stub. One campaign at a time. Large effort.
- ~~**Party overview page**~~ — **absorbed into "Player state & progression"** below; it is slice 3 of that item, not a standalone piece.

---

## Large — multi-phase, need breakdown

Both items below are **LARGE**. Neither is a single unit of work; each needs
splitting into the slices sketched here, and each carries open questions that
must be answered before building. They share one goal, stated by the DM:
**reduce dependence on dndbeyond.com.**

### Player state & progression  *(LARGE)*

A system for managing player characters — stats, HP, resources, conditions,
inventory, XP and levelling — that integrates with the dice roller and the rest
of the app.

**What exists to build on**
- `js/state.js` — per-campaign `localStorage` store, already handles
  revealed/notes/location/time and is synced by `js/github-state.js`.
- `js/generator.js` — NPC/item generation, a precedent for structured entity data.
- `campaigns/<id>/content/players/*.html` — the current party sheets.

**The two real obstacles**
1. **Player characters are prose, not data.** The sheets are hand-written HTML
   (`guntrah.html`, `tito.html`, …). Nothing is machine-readable, so there is no
   ability score, AC or HP to drive anything. A character *data model* is the
   prerequisite for everything else here.
2. **The dice roller has no public API.** `js/dice.js` is a closed IIFE — it
   exposes nothing on `window`, so nothing can ask it to roll. Integration means
   giving it an entry point (e.g. `Dice.roll({ dice, mod, adv })`) that returns a
   result rather than only animating a panel.

**Suggested slices**
1. Character data schema (JSON) + convert one PC as proof.
2. Render a read-only sheet from that data.
3. Party overview panel — HP/conditions at a glance *(the old icebox item)*.
4. Editable runtime state: HP, temp HP, slots, resources, conditions; persisted.
5. Dice integration: click a save/skill/attack, roll with the right modifier,
   advantage/disadvantage.
6. Level-up flow: proficiency bonus, hit dice, ASI, feature grants.
7. Inventory, attunement and currency.

**Open questions**
- Source of truth: hand-authored JSON, an importer for a D&D Beyond export, or a
  character builder in-app? This decides most of the rest.
- Does player state sync via GitHub like campaign state (multi-device), or stay
  local to the DM's browser?
- Do players get their own view or device, or is this DM-facing only?
- How much 5e rules engine to encode versus trusting the DM to adjudicate?
- Non-SRD classes the DM uses (Blood Hunter, Pugilist) will not come from any
  open data source — hand-author those.

### Combat system with map & tokens  *(LARGE)*

Run encounters in-app: initiative, turn order, HP and conditions, on a map with
draggable tokens for PCs, NPCs and monsters.

**What exists to build on**
- `shared/data/monsters-index.json` — 1,840 monsters (`name`, `source`, `type`,
  `cr`, `size`); `monsters-raw.json` holds full stat blocks.
- `shared/img/monsters/{source}/{name}.webp` — token art, generated by
  `tools/fetch-monster-tokens.py`. **Gitignored and only ~40–60% coverage** by
  that script's own estimate, so token availability is partial and not in the repo.
- The `.stat-block` renderer, now fully themed.
- Existing map assets (`campus_map.png`, the LMoP region map) and the hotspot
  coordinate system in `tools/coordinate-picker.html`, which is prior art for
  mapping percentage coordinates onto an image.

**Suggested slices**
1. Initiative tracker with no map at all: add combatants from PCs/NPCs/monsters,
   roll initiative, order them, advance turns, track HP and conditions. This is
   independently useful and worth shipping first.
2. Token art for PCs and NPCs — monsters are partly covered, characters are not.
3. Static battle-map display with token placement and drag.
4. Grid overlay plus measurement (distance, reach, range).
5. Attack resolution through the dice API: to-hit against AC, damage, apply to HP.
6. Conditions, area-of-effect templates, fog of war, player-facing display.

**Open questions**
- Is the map DM-only, or mirrored to a player screen/TV? That changes the
  architecture considerably.
- Per-map grid calibration (origin, square size) — reuse the coordinate-picker
  approach, or store it in campaign data?
- How much automation? Auto-applying damage is fast but removes DM judgement.
- Where does PC/NPC token art come from, given the monster script only manages
  partial coverage and its output is not committed?
- Does encounter state persist between sessions, and does it sync?
- The offline-first constraint rules out any hosted VTT service — this has to be
  self-contained.

## Completed

- **Quick NPC** — topbar `⚡ Quick NPC` button; one-click compact card: name, race/occupation, appearance, trait; Re-roll + Save
- **Dice roller multi-d20** — 2+ d20s show individual values (advantage/disadvantage); other dice still sum
- **JS unit tests** (`tools/tests.html`) — 22 browser tests: generator logic, modal cross-link rendering
- **Data integrity test suite** (`tools/test.py`) — 44 checks, auto-runs on server launch
- Multi-campaign support with launcher and registry gating
- NPC generator (full mode) with race-specific names, weighted occupations, optional secrets
- Animated dice roller with d4–d100 support and throw animation
- Session runner panel
- Dashboard with 4-quadrant location view
- Entity cross-links (`[[id]]`) and related entity graph
- DM mode toggle with dm-only block support

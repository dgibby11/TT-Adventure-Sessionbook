# DnDAcademy — Roadmap & Feature Backlog

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

### 3. Import Process Overhaul
**Status:** Not started  
**Effort:** Large

Current state: Curse of Strahd and Descent Into Avernus imports are sparse — bare entity stubs, weak cross-links, and content that doesn't reflect the actual source material well. The import pipeline (Google Docs → local HTML fragments) needs a systematic rethink.

**Problems to solve:**
- Entity coverage is incomplete (major NPCs, locations, factions missing or stubbed)
- Content files are thin — not enough detail to be useful at the table
- Cross-links (`related[]` and `[[id]]` inline links) are sparse; the entity graph isn't navigable
- No consistent template for what a "good" NPC, location, or faction entry looks like
- No process for updating entries as the campaign progresses

**Ideas to explore:**
- Define a content standard per entity type (what fields/sections a complete entry has)
- Build a richer import template or checklist for each campaign
- Consider a semi-automated approach: structured Google Doc → JSON + HTML stub generator
- Separate "lore entries" (static background) from "session notes" (DM scratch) more clearly

This is the highest-leverage improvement for actual play value but requires the most upfront work. Tackle one campaign at a time.

---

### 4. Images — Town Maps, NPC Portraits, Key Artifacts
**Status:** Not started  
**Effort:** Medium (per campaign)

Add visual assets for high-value entities: town/area maps, portraits of recurring NPCs, and images of significant magic items or set-piece locations.

**Content types already supported:** `contentType: "image"` renders a full-width image in the modal. This works today — it's purely a content pipeline task.

**What's needed:**
- Source or commission/find images (D&D Beyond, official art books, AI generation, fan art with attribution)
- Decide display approach: full-panel image, or image alongside text (image + HTML hybrid)
- Potentially support `contentType: "html"` with an embedded `<img>` for image + description combos — already possible, just needs a convention
- Prioritize by campaign: which NPCs/locations come up most often at the table?

**Candidates (campaign-agnostic):**
- Town maps for major settlements (Baldur's Gate, Vallaki, Waterdeep)
- Recurring villain portraits (Strahd, Zariel, etc.)
- Party-acquired magic items with flavor art

---

## Icebox (good ideas, not yet prioritized)

- **Persistent DM state** — notes, revealed flags, session log (partially done via localStorage)
- **Player vs DM view** — screen-safe player mode (DM toggle exists, full gating not built)
- **Party overview page** — track party members, HP, conditions, inventory
- **Random generator** — expand beyond NPC/item (encounter tables, weather, rumors, names)
- **Search improvements** — tag-based filtering, fuzzy match

---

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

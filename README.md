# TT Adventure Sessionbook

A local, static, offline single-page app for running tabletop RPG campaigns. Each campaign gets its own entity graph — locations, NPCs, factions, items, creatures, mysteries, and sessions — navigable through a dashboard and searchable index. Clicking any entry opens a styled modal with the entity's content. Built for DMs; runs off a trivial local server.

## How to run

Double-click **`start-map.bat`**. It runs a data-integrity check (`tools/test.py`), launches a tiny local web server (Python), and opens the **Campaign Launcher** at <http://localhost:8000/launcher.html> in your browser.

- A window titled **"TT Adventure Sessionbook"** stays open while the app runs — **close it to stop the server.**
- Requires Python (the `py` launcher or `python` on PATH).
- Pick a campaign from the launcher to open it; each campaign has its own DM passphrase gate.

> **Why a server?** Browsers block local `fetch()` of JSON/HTML over `file://`. The server sidesteps that. It serves only local files — nothing leaves your machine.

## Manual launch

```
py -m http.server 8000
```

Then open <http://localhost:8000/launcher.html>.

---

## Campaigns

Every campaign is a self-contained folder under `campaigns/<id>/` (its own `campaign.json`, entity data, and content), registered with one entry in `campaigns/index.json`. Currently registered:

- **FAIL Academy** — Faculty of Arms, Inquiry & Lore
- **Lost Mine of Phandelver** — Sword Coast, Characters Level 1–5
- **Curse of Strahd** — Barovia, Characters Level 1–10
- **Baldur's Gate: Descent into Avernus** — Baldur's Gate & Avernus, Characters Level 1–13
- **The Salt Below** — Port Calder & the Drowned Kingdom, Characters Level 1–10

## Platform Features

Shared functionality available to every campaign:

- Type-grouped, collapsible index menu + live search (topbar input, `/` shortcut, keyboard navigation)
- Modal content system (HTML, image, PDF)
- `[[cross-link]]` resolution inside content, with a Related footer and external-links bar per entity
- DM Mode toggle — reveals dm-only entities and content blocks
- Player vs DM view — screen-safe player mode (only revealed + player-visible entities shown); green "Player View" badge
- Persistent DM state — per-entity notes and "revealed to players" flags (localStorage)
- Party overview page — side-by-side PC cards with stats, key features, D&D Beyond links, DM tactical notes
- Session Runner — three-panel adaptive DM view (read-aloud prompts, session plan/entity detail, pinboard + notes) launched from "▶ Run Session"
- NPC / item / weather / encounter generator (`js/generator.js`) — generated entities persist in localStorage and merge into the live entity graph; table data can be extended via `generator/npc-tables.json`
- Dice roller (topbar) with roll history
- Multi-campaign launcher + registry (`campaigns/index.json`)
- Coordinate picker tool (`tools/coordinate-picker.html`) for plotting new map hotspots
- Data integrity test suite (`tools/test.py`) — schema, link, and registry checks, run automatically by `start-map.bat`

## FAIL Academy — Content Log

Campaign-specific content built for FAIL Academy (formerly F.U.C.K.S.):

- Campus map with invisible clickable hotspots over department banners
- Player character entries — Lugeiros Serise, Gunnar, Caelum Rivenstone, BloodRaven (full stat blocks + D&D Beyond links)
- Campus store + credits system — The Provisions Office ("The Prov"), run by Silas Morne; full credits economy (100 AC/year; 50 AC potions, cap 2/year; black market at 100 gp; Special Acquisitions magical inventory)
- More lore content — Headmistress Dowe, Prof. Thalia Varn (beloved), Prof. Aldous Fenwick (worst); Arcane Dueling Society, Expedition Volunteers, The Dead Hours (underground fight club, dm-only); Academy Traditions & Calendar; Legends of the Academy (Whispering Archive, the Lost Year, Golden Cohort, Last Student, the Room That Moves)
- Nearby world content — Silverymoon, River Rauvin, High Forest, Everlund; all cross-linked with Thornwick Consortium hooks
- More D&D Beyond creature links — fixed Owlbear URL (was duplicate of Bodak ID); added Wolves/Dire Wolves, Displacer Beast, Orc Warband with tactical profiles and D&D Beyond links

## Backlog

- [ ] **Richer PC popups** — full saving throws, complete equipment lists, better spell layout
- [ ] **Monster stat block modal sizing is a hack** — `#resource-modal.monster-detail-open` forces a fixed `height: 94vh` to work around the modal having no explicit height normally (it auto-sizes to content, and `#monster-detail-panel` is `position:absolute` so it can't grow the modal itself). This works, but wastes vertical space on short stat blocks and doesn't address the same auto-sizing quirk elsewhere in the resource modal. A cleaner fix would give `#resource-modal-body` a stable height independent of its content (or restructure so the detail panel participates in normal flow instead of overlaying absolutely).
- [ ] **"Convert" a Monster resource entry into the campaign** — the shared bestiary (`shared/data/monsters-*.json`) is rendered ad-hoc and isn't part of `window.ENTITIES`, so a monster looked up there can't be pinned in the Session Runner's pinboard the way campaign creature entities can. Add a way to promote/copy a monster into the active campaign (e.g. as a `type:"creature"` entity, or a lighter-weight session-scoped pin) so a DM can look one up mid-session and pin it without leaving the Monsters tab.

# FAIL Academy — Session 0 Reboot (In Progress)

_Moved out of the root CLAUDE.md 2026-07-24 so all planning-related content for this
campaign lives under `campaigns/fail-academy/planning/` — CLAUDE.md now just points here._

The original Sessions 1-5 are played/completed canon, one-shot format. RENAMED
(2026-07-27, both id and contentFile, not just display name) to `one_shot_1`
through `one_shot_5` — category "Completed (Archived)" — to free up the
`session_1` id for the ongoing campaign's real Session 1. Sessions 6-9 (unplayed
DM-planning stubs) have been REMOVED — deleted from data/sessions.json and
content/sessions/. Starting with a Session 0, the campaign becomes an ongoing
story: same Academy, new PCs (fifth-year students about to graduate), archived
old PCs. `session_1` ("Something is Happening") is now live — category
"Planning", visibility `dm-only` until it's actually played at the table.

All design work for the reboot is happening in
`campaigns/fail-academy/planning/*` — these are working docs, NOT live
entities (not in index.json, not loaded by the app). Read them before touching
any live data for this campaign:
- `campaign_arc.json` — the big picture (the veil/Thanatos/Orcus premise,
  the antagonist, the 3-phase structure) plus a continuity_notes section
  tracking cross-cutting decisions.
- `phase1_something_is_happening.json`, `phase2_the_one_who_got_away.json`,
  `phase3_closing_the_veil.json` — one file per phase; phase 3 still empty.
- `session1_something_is_happening.json` — Session 1 design (the new party's first
  actual play session, condensing Phase 1 into one on-campus session that ends on
  a graduation hook into Session 2). PROMOTED (2026-07-27) — see `session1_draft.html`
  and the live entity note below.
- `session1_draft.html` — full prose draft of Session 1. PROMOTED (2026-07-27) to
  `data/sessions.json` (id `session_1`, category "Planning", visibility `dm-only`
  since it hasn't been played at the table yet — flip to `player` once it has, to
  match how the archived One Shots are handled). This planning file is kept as the
  design-history record; the live `content/sessions/session_1.html` is authoritative
  going forward.
- `the_ninth_thesis.json` — the Ninth Thesis / Secret Society organization
  (confirmed: they're the same entity, to be merged; not yet executed against
  live data — see `founders_persona_audit.json`, below, for why this is now
  gated on a DM decision, not just a go-ahead).
- `torvald_the_insider.json` — depth on Torvald Thatch as the (redeemable,
  not-evil) campus insider.
- `corvin_ashworth_build.json` — full level-20 mechanical build (Warlock 20)
  for Corvin Ashworth as the eventual boss fight. Mechanics-only companion to
  phase2_the_one_who_got_away.json / torvald_the_insider.json's narrative
  material. No live NPC entity exists for him yet.
- `session_zero_relationship_table.md` — new-party ↔ existing-NPC relationship notes.
- `the_dwarven_ruins.json` — origin of the veil (an ancient dwarven ruin, off
  the edge of campus, that ruptured the barrier — late-game location, not yet
  visited by the party) plus the bulette-incident session beat that fills
  session1's post-recruitment montage gap.
- `founders_persona_audit.json` — NEW (2026-07-27). Catalogues exactly where
  live founders/Secret Society/Ninth Thesis lore conflicts with the
  founders-persona rewrite below (Ashcroft vs. Voss as founder, chief among
  them), lists resolution options, and has the full verified backlink list for
  the eventual merge. Read this before touching secret_society, ninth_thesis,
  occult_systems, or the three founders' entities. Its occult_systems conflict
  now has a likely-resolution note (2026-08-02) pointing at phase3's veil
  location — see below.
- `the_prov_investigation.json` — NEW (2026-08-11), expanded same day with a second
  round of DM detail. A self-contained, session-agnostic encounter module for
  whenever the party investigates the Provisions Office (Voss's session_1.html
  notes already point them there) — not tied to a session number. Covers
  bypassing Silas (timing, magic, stealth/distraction, or the honest note-from-
  Voss route, each with different trust consequences), a new "Intake Annex"
  storage area behind the existing back room, a magically-sealed crate that
  looks far harder to open than it actually is (the real ward expired in
  transit), a mundane bait object inside meant to invite handling, and a
  planar-rift trigger with full sensory detail (violet-black, liquid-surfaced,
  a suction pull) leading to a workshop on **Thanatos** itself (Orcus's Abyssal
  layer, per campaign_arc.json's premise) staffed by two reflavored-babau
  "abyssal tinkerers" who mistake the arrival for Torvald (referred to only as
  "the Groundskeeper," never named) before turning hostile and summoning a
  fire elemental. Ties directly into torvald_the_insider.json's ring mechanism
  — updated the same day with a new "periodic check-in" trance-visit detail
  this scene surfaces. Two branches (party opens it themselves, or reports
  back first and has to rescue Voss when she opens it instead) share the same
  encounter. Deliberately gated — confirms the sabotage pattern is real and
  that the veil leads somewhere real, but keeps Orcus, Corvin, Torvald's
  identity, the ring, and the ruins unconfirmed at the table.
- `session_plan.json` — NEW (2026-08-02). The master session-by-session
  tracker for the whole campaign: the 10-sessions-per-phase pacing target,
  Sessions 1-5 confirmed at the beat level, a loose unnumbered sequence for
  the rest of Phase 2 into Phase 3, the graduation Ring Selection concept, and
  the DM's route-map geography (Academy location, Neverwinter route, the
  Sanctum). Read this alongside phase1/2/3 for what's actually been decided
  session-by-session — it supersedes the phase docs' session numbering where
  they disagree.

Key decisions already locked in (see the planning docs for full detail/reasoning):
- The founders (Aldric Voss, Isolde Orath, Brennan Ashcroft) are being
  rewritten as sincerely well-intentioned, not conspiratorial. Any existing
  lore conflicting with that (secret_society, ninth_thesis, occult_systems,
  the founders' own dm-only entries) needs a rewrite pass — CATALOGUED but not
  yet resolved or executed, see `founders_persona_audit.json`.
- No physical ritual-binding artifacts as a plot device (rejected — doesn't
  fit Ashcroft's revised persona).
- The Ninth Thesis IS the Secret Society; Aldric Voss founded it ~350 years
  ago around student Wren Halloway's suppressed graduation thesis; led by
  successive Voss descendants down to Ellery Voss today. NOTE: this directly
  conflicts with brennan_ashcroft.html's live claim that Ashcroft founded it —
  see `founders_persona_audit.json` for the conflict and resolution options
  before executing the merge. **SUPERSEDED (2026-08-02/08-04):** kept for
  history only — the Ninth Thesis is NOT the Secret Society after all (see
  the unconflate resolution below), and the founder is Nerissa Voss, not
  Aldric (see the founder-correction entry below).
- The veil under the Academy traces back to an ancient dwarven city (now
  ruins, off the edge of campus) that ruptured the barrier to Thanatos; the
  founders discovered the already-existing veil generations later and did not
  cause it. Late-game location, not yet visited by the current party — see
  `the_dwarven_ruins.json`.
- Torvald Thatch is the campus insider distributing corrupted items, but is
  NOT evil — he's an unwitting instrument, corrupted via a cursed ring gifted
  by the antagonist. Redeemable if the ring is removed (mechanism TBD).
- The antagonist is Corvin Ashworth (he/him), a former student possessed by
  one of Orcus's loyal spirits after getting too close to the veil during his
  5th year. Full depth (possession mechanism, Thornwick Consortium ties,
  corruption arc) is in `phase2_the_one_who_got_away.json` — including a
  tracked `open_questions` block for what's still undecided (veil location,
  Thornwick inner-circle leadership, Corvin's actual plan, etc.). Full level-20
  mechanical build now exists too, see `corvin_ashworth_build.json`.
- Session 1's four parting gifts (Witness for Tavian, The Standing Ovation for
  Tito, The Quick Components Pouch for Silas, the self-made All-Purpose Tool
  for Guntrah) are CONFIRMED and live in data/items.json / data/npcs.json — see
  `session1_something_is_happening.json` → structure.parting_gifts.
- Session 1 itself ("Something is Happening") is PROMOTED and live as
  `data/sessions.json` id `session_1` / `content/sessions/session_1.html` —
  category "Planning", visibility `dm-only` (not yet played). ninth_thesis.html
  has a forward-pointing note flagging what needs updating once it's actually
  run (the party will then know the org's name).
- Reboot work applied to live data so far: the Session 1 parting-gift
  items/NPCs, the Session 1 entity itself (dm-only, unplayed), and the
  one_shot_1-5 id rename (mechanical, not a content rewrite). Everything else —
  Phase 1-3 plot material, the Ninth Thesis/Secret Society merge, Corvin
  Ashworth, Torvald's ring, the dwarven ruins — stays planning-only. Don't merge
  or rewrite further live entities for this without explicit instruction.
- Thornwick Arcane Consortium lore pass (2026-07-27, live data): decentralized
  structure confirmed — no known headquarters (a deliberate "red flag" detail,
  not yet noticed by any party), only known foothold is a small brokerage
  office in Neverwinter (west, ~a month's travel), with additional small fronts
  in Silverymoon and Everlund already established. Crumb has been Academy
  faculty for 50 years and Thornwick's supply contact for ~40 of them. An
  emblem image now exists at `campaigns/fail-academy/assets/thornwick_emblem.png`
  (a T/A/C blackletter monogram maker's-stamp), referenced in
  thornwick_consortium.html. Also patched two live player-view leaks —
  one_shot_5.html and session_1.html both named "Thornwick" in plain text
  outside dm-only blocks, which would have exposed the org to the new party
  (who have never heard of them) once those sessions' visibility flips to
  player. Both now keep the name dm-only-gated; one_shot_5's player-visible
  prose uses "an outside buyer" instead. Thornwick's inner-circle leadership
  (Orcus cult) and Corvin's specific pitch to them remain open — see
  phase2_the_one_who_got_away.json.
- Session 1 Thornwick discoverability pass (2026-07-27, live data): added
  Garrick Nash (`data/npcs.json`, dm-only) — Crumb's actual Thornwick contact,
  a low-rung middleman reachable only through Crumb, who'll point toward the
  Neverwinter office if approached in good faith. Documented exactly what's
  discoverable at the Session 1 stage in thornwick_consortium.html and
  oswald_crumb.html: nothing public, Crumb only cracks under improvised
  player pressure (no scripted moment does it for them), capped at naming
  Garrick. Also gave Voss's off-screen post-Session-1 investigation real
  content in session_1.html: her Ninth Thesis operatives confirm the org is
  real/active in Silverymoon + Everlund but find nothing pointing at Crumb;
  it's her own memory of the stamp that puts "talk to Crumb" on her working
  list. Added an optional, DM-gated "glimpse" beat (a scrap to-do list on her
  desk) so the party can see that note without her stating it outright —
  intentionally lighter than the Crumb/Garrick path per instruction.
- Session-level roadmap and Phase 3 engine (2026-08-02, planning-only — see
  `session_plan.json` and `phase3_closing_the_veil.json` for full detail):
  pacing target set at ~10 sessions per phase (30 total), Session 1 as Phase
  1's opener. Sessions 1-5 confirmed at the beat level (Voss/bulette/
  recruitment, then graduation/Ring Selection/departure, then Neverwinter/
  Thornwick investigation, then a travel day pointing at Torvald, then
  Torvald's interrogation naming Corvin Ashworth and the Sanctum north of
  Mirabar). Phase 3's engine is now locked: Corvin is buying into Thornwick's
  larger effort to bring Orcus through somewhere, not running a solo plan;
  the possessing spirit is named Harthoon (real D&D lore, Orcus's
  vizier/castellan); the veil's true location is the Underdark beneath campus
  via long-forgotten sealed passages that only Torvald knows about (not even
  Voss); Thornwick's inner circle stays faceless to the party. A DM-drawn
  route map confirmed the Academy sits at the High Forest/Evermoors border
  southeast of Silverymoon. Everything beyond Session 5 is intentionally
  loose (not session-numbered) per the DM's request — see
  session_plan.json's loose_sequence_post_session_5.
- Ninth Thesis / Secret Society founder conflict RESOLVED and executed
  against live data (2026-08-02): founders_persona_audit.json's conflict_1
  is settled via Option B (unconflate), not the originally-proposed
  straight merge. `content/factions/ninth_thesis.html` is fully fleshed out
  (Wren Halloway's suppressed thesis, Nerissa Voss founding it, the Voss
  leadership lineage down to Ellery, the operational profile). Ashcroft's
  Alumni Society stays real, mundane, and unrewritten. `secret_society.html`
  is rewritten to explain "the Secret Society" as campus rumor-bleed between
  Ashcroft's society and half-true whispers about the real, secret Ninth
  Thesis — not a real organization of its own. `one_shot_2` and
  `founders_statue.html` are updated to retroactively identify what the
  prior party witnessed as genuine Ninth Thesis activity. Per explicit
  instruction, `academy_legends.html`'s "Lost Year" and "Golden Cohort"
  sections — which treated "the current Secret Society" as real, active,
  and responsible for real deaths — were removed outright rather than
  recast, since they no longer had a factual basis ("the Lost Year wasn't
  a thing"). `occult_systems.html` itself remains untouched and still
  needs its own pass — see founders_persona_audit.json's conflict_2.
- Ninth Thesis founder corrected (2026-08-04, live data): Aldric Voss
  removed from the founding lore entirely per explicit instruction. The
  founder is now **Nerissa Voss** — Aldric's younger sister and the
  Academy's first archivist, never one of the three officially-credited
  founders herself. She's the one who noticed Wren Halloway's thesis pulled
  from the record and preserved it as her own private initiative. Dr.
  Ellery Voss now descends from Nerissa's line, not Aldric's directly —
  `ellery_voss.html`'s ancestry note corrected to match. Updated across
  `ninth_thesis.html`, `the_ninth_thesis.json`, `founders_persona_audit.json`,
  and `campaign_arc.json`.
- Full lore-consistency sweep (2026-08-05, live data): a DM-requested audit of
  every file mentioning Aldric Voss, the Ninth Thesis, the Secret Society, or
  the founders turned up a much larger web than the original audit caught —
  `founders_compass.html`, `founders_charter.html`, `contraband_log.html`,
  `academy_grounds_map.html`, `headmistress_dowe.html`, `hidden_knowledge.html`,
  `campaign_overview.html`, and `open_questions.html` all still treated "the
  Secret Society" as a real, active, currently-operating organization —
  independent of the unconflate resolution above, which those files predated
  or weren't touched by. Fixed: the real actor behind the compass, the ritual
  floor, the redacted security log, and Dowe's 20-year cover-up is now the
  [[ninth_thesis|Ninth Thesis]], not a fictional "Secret Society." Dowe's core
  DM-only secret was rewritten to match — she knowingly tolerates the Ninth
  Thesis operating outside her authority because she trusts Voss's judgment,
  rather than covering up a dangerous conspiracy with implied-dead
  administrators (which no longer fit a sincerely well-intentioned Ninth
  Thesis). Also removed the last stray Lost Year / Year 34 references that
  survived the earlier academy_legends.html cut — `headmistress_dowe.html`,
  `headmistress_office.html`, `high_forest.html`, `silverymoon.html`, and
  `prof_aldous_fenwick.html` all had it woven into character secrets or NPC
  motivations; each was rewritten to drop the dependency without inventing
  new lore to replace it (Fenwick's mystery stays a mystery, just untethered
  from Year 34; the wood elves' and Dowe's watchfulness stays but loses the
  specific false anchor). Also fixed: `voss_keycard.html` implied Ellery
  directly inherited Aldric's "personal materials," contradicting the Nerissa
  correction — reworded to a general Voss-family-archive handoff.
  `data/*.json` related[] arrays updated to add `ninth_thesis` wherever
  content now cross-links it.
- Session 1 played at the table (2026-08-09, live data): full session ran in one
  sitting — parting gifts, the Voss summons/note, the Ninth Thesis recruitment
  pitch (accepted outright by all four, ~50gp/week), the bulette hunt, and the
  debrief. `content/sessions/session_1.html`'s Status field updated to reflect
  completion, and a DM-only "What Actually Happened at the Table" note added
  documenting where play diverged from the script: the bulette fight happened
  underground in tunnels the creature burrowed (not the open field/training-course
  terrain originally blocked out) and ran harder than a level-10 party should
  have felt, played deliberately as a tonal gut-check. One unscripted loose
  thread, left open per DM instruction: as the party emerged from the forest,
  Torvald was seen quietly talking with an unidentified figure who walked away
  before the party got close — not tied to Garrick Nash or any existing NPC,
  no obligation to resolve it in Session 2. `session_plan.json`'s session_1
  entry updated to match.
- Setting year established (2026-08-05, live data): the campaign takes place
  in **1500 DR** (Forgotten Realms Dale Reckoning) — added to
  `campus_overview.html`'s Geographic Context facts (player-visible) and
  `campaign_arc.json`'s continuity_notes. Existing relative year markers
  (department_incident_log.html's Year 23/38/51, academy_credits.html's
  "18 years ago", this file's "~350 years ago" founding note) are
  Academy-founding-relative, not DR-absolute, and were left unconverted.

# FAIL Academy — Session 0 Reboot (In Progress)

_Moved out of the root CLAUDE.md 2026-07-24 so all planning-related content for this
campaign lives under `campaigns/fail-academy/planning/` — CLAUDE.md now just points here._

Sessions 1-5 are played/completed canon (one-shot format, category "Completed").
Sessions 6-9 (unplayed DM-planning stubs) have been REMOVED — deleted from
data/sessions.json and content/sessions/. Starting with a Session 0, the
campaign becomes an ongoing story: same Academy, new PCs (fifth-year students
about to graduate), archived old PCs.

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
  a graduation hook into Session 2). CONFIRMED — structure and all four parting
  gifts locked in; not a skeleton anymore. See `session1_draft.html` for the
  written-up version.
- `session1_draft.html` — full prose draft of Session 1, ready for DM review.
  Written from session1_something_is_happening.json + the other Phase 1/2 docs
  below. NOT live (not in data/sessions.json, not in index.json) until reviewed
  and promoted.
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
  occult_systems, or the three founders' entities.

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
  before executing the merge.
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
  Tito, The Quick Components Pouch for Zarad, the self-made All-Purpose Tool
  for Guntrah) are CONFIRMED and already written up as live entities in
  data/items.json / data/npcs.json — see `session1_something_is_happening.json`
  → structure.parting_gifts and `session1_draft.html`.
- None of this reboot work has been applied to live data yet EXCEPT the
  Session 1 parting-gift items/NPCs noted above (those were explicitly
  requested as live entities). Everything else — Phase 1-3 plot material,
  the Ninth Thesis/Secret Society merge, Corvin Ashworth, Torvald's ring,
  the dwarven ruins — stays planning-only. Don't merge or rewrite further
  live entities for this without explicit instruction.

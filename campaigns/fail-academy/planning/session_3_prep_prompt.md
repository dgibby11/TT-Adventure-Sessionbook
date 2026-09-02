# Session 3 prep — context-loading prompt for a fresh Claude session

Paste the block below into a new Claude session in this repo. It is
**read-only**: it asks for orientation and questions, not design work.

---

```
# FAIL Academy — Session 3 prep: READ FIRST, WRITE NOTHING

I'm going to write Session 3 of a long-running D&D campaign with you. Before we
start, I want you to load the context properly. This is a big, cross-linked
campaign and Session 2 ended in an unusual place, so a cold start will produce
confidently wrong material.

## Do not generate anything yet

No session draft, no scenes, no NPCs, no read-aloud text, no outlines, no
"here's a rough shape." Do not write to any file. When you've finished reading,
report back with an orientation summary and your questions, and then stop and
wait for me.

## Where Session 2 left off — the one thing you must not get wrong

Session 3 does NOT open on campus, and it does NOT open in Neverwinter Wood.

Session 2 ended **mid-scene, stranded on another plane**, on a ritual platform
in the Abyss, with roughly fifteen hostile creatures about a minute away. The
party's escape failed on a natural 1. Everything the earlier planning documents
say about "the party arrives in Neverwinter Wood and picks a direction" is
**one session later than those documents think it is**. Several planning files
still carry the old assumption in places; the reconciled files are authoritative.

## Read these, in this order

Authoritative and most recent first. Later files supersede earlier ones wherever
they disagree.

1. `CLAUDE.md` (repo root) — tech constraints, the entity schema, the `[[ ]]`
   cross-link convention, the three-axis visibility rules (`visibility` /
   `revealed` / `view`), and the compact-typography rule.
2. `campaigns/fail-academy/planning/reboot_status.md` — **newest entries are at
   the top.** This is the running decision log for the whole campaign reboot.
   Read at least the top third carefully.
3. `campaigns/fail-academy/content/sessions/session_2.html` — what actually
   happened, reconciled against the recording. Read the whole thing including
   every `dm-only` block, especially "What Actually Happened at the Table",
   "What Did Not Land", and the two "Carried Forward" blocks — those hold the
   unspent escape design and the contact-list scene that was never played.
4. `campaigns/fail-academy/planning/session_2_transcript.txt` — the raw
   speech-to-text recording. Long, and full of errors. Read
   `planning/transcript_glossary.md` first or you will misread names.
5. `campaigns/fail-academy/planning/transcript_glossary.md` — the agreed
   correction set: name fixes, name-collision hazards, speaker-attribution
   fixes, and the standing rules for handling transcripts.
6. `campaigns/fail-academy/planning/session_plan.json` — the master
   session-by-session tracker. Read `sessions.session_3`,
   `sessions.post_session_2_fork`, and all of `open_items`.
7. `campaigns/fail-academy/planning/vrenn_the_captive.json` — the captive drow's
   full history. Almost none of it has been spent at the table.
8. `campaigns/fail-academy/content/sessions/session_1.html` — the previous
   session, and the model for how a reconciled session file should read.
9. `campaigns/fail-academy/planning/campaign_arc.json` and
   `phase1_*.json` / `phase2_*.json` / `phase3_*.json` — the long arc. Skim for
   shape; do not treat their session numbering as current.

Then look at the live entities Session 3 will touch:
`content/locations/ritual_platform.html` · `content/npcs/the_captive_drow.html` ·
`content/creatures/hooved_demons.html` · `content/items/torvald_package.html` ·
`content/npcs/ellery_voss.html` · `content/npcs/osric_morne.html` ·
`content/npcs/torvald_thatch.html` · the six files in `content/mysteries/` ·
and the four PCs in `content/players/`.

## Rules that apply to everything you do here

- **The transcript is the source of truth** wherever it and the authored data
  disagree — with one logged exception (the Ring Conferral staging, resolved by
  DM ruling and recorded in the glossary). If you hit a *major* conflict — one
  that contradicts a locked decision, invalidates later prep, or changes an
  established fact rather than adding to it — bring it to me instead of
  resolving it yourself.
- **Absence from a transcript is not evidence something didn't happen.**
  Recordings start late and mics miss things. Ask.
- **Never delete substantial authored content on inference.** Ask.
- **When something is ambiguous, ask — don't pick the more interesting reading.**
- **This is a new party.** Silas, Guntrah, Tito, Tavian. The One Shots 1–5 party
  is retired and its members are current *underclassmen*. Don't let their
  knowledge leak in as ambient fact.
- **Player-facing prose must stay clean.** The pattern this campaign uses is
  `visibility: "player"` on the entity with secrets in `<div class="dm-only">`
  blocks inside the file. Names that must never appear outside a dm-only block:
  Thanatos, Orcus, Vrok, Harthoon, "armanite", Vrenn, Corvin, Thornwick,
  Nerissa Voss, Wren Halloway, and Neverwinter Wood as a destination.

## When you're done reading, give me

1. **A one-page orientation**: exactly where the party is standing, what they
   are carrying, what they know, and what they think they know.
2. **The escape situation** — what routes exist, which are closed and why.
3. **The clues they walked past in Session 2** that are still physically within
   reach, and what each one is worth.
4. **Every open thread that could plausibly touch Session 3**, including the
   ones running back on the Material Plane while the party is away.
5. **Anything you found that is stale, contradictory, or that you think I've
   overlooked.** I would rather hear it now than halfway through drafting.
6. **Your questions for me.** Be specific and be blunt about which ones actually
   block you. Then stop.
```

---

_Written 2026-08-24, after the Session 2 reconciliation and entity build-out._

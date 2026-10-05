# Session 5 prep — context-loading prompt for a fresh Claude session

Paste the block below into a new Claude session in this repo. It is
**read-only**: it asks for orientation, a recommendation and questions — not
design work, and not a draft.

The four options in it are **suggestions, not decisions.** They were put
together on 2026-10-05 from the reconciled Session 4 record and the Phase 2 arc
docs. Overrule any of them freely; the prompt tells the model to treat them that
way.

---

```
# FAIL Academy — Session 5 prep: READ FIRST, WRITE NOTHING

I'm writing Session 5 of a long-running D&D campaign with you, and I have about
48 hours. Before we design anything I want you to load the context properly.
This is a large, heavily cross-linked campaign with four sessions of reconciled
play behind it, and a cold start will produce confidently wrong material.

## Do not generate anything yet

No session draft, no scenes, no NPCs, no read-aloud text, no stat blocks, no
outlines, no "here's a rough shape." Do not write to any file and do not touch
live data. Read, then report back, then stop and wait for me.

## Where Session 4 left them — get this exactly right

They are NOT on campus. They are NOT in the Abyss. They are NOT in Neverwinter.

Session 4 ended in a clearing near the centre of **Neverwinter Wood**, on the
Sword Coast North, several hundred miles from the Academy, taking a **second
long rest** that an adult green dragon granted them for the asking. A fox is
waiting to walk them out. In the morning they head **south-west**, toward a
settlement whose fire they saw from above the canopy about twelve miles off.

Load-bearing facts:

- **Level 11, as of the long rest in Session 4.** All four.
- **No healing potions.** None since Commencement. Party funds are roughly
  330 gp spread across four people — Tito is carrying 149 of it.
- **Vrenn, a drow NPC wizard, is travelling with them**, and the party actively
  chose to keep him when they were offered a clean way to hand him over.
- **Vrenn is cursed** — a fomorian's Evil Eye: magical deformities, speed
  halved, disadvantage on STR/DEX checks, saves and attacks. He re-rolls the
  save when he finishes the long rest Session 4 ended on. *I have not decided
  whether he shakes it.*
- **A lich named Morvek is coming for him.** Vrenn's own estimate was two to
  four days; one day is gone. Morvek knows Vrenn is on the Material Plane and
  nothing more precise, cannot scry across planes, and is believed to be short a
  steel tuning fork — because the party unknowingly took the one from his
  basement. **No player has connected that yet.**
- The party's own stated goal, said out loud by Tavian in Session 4:
  *"We've got to touch base with Dr. Voss."*

## Read these, in this order

Later files supersede earlier ones wherever they disagree.

1. `CLAUDE.md` (repo root) — tech constraints, the entity schema, the `[[ ]]`
   cross-link convention, the three-axis visibility rules, the compact-
   typography rule.
2. `campaigns/fail-academy/planning/reboot_status.md` — **newest entries at the
   top.** The Session 4 header block is the running state of the campaign; read
   all of it before anything else in this list.
3. `campaigns/fail-academy/content/sessions/session_4.html` — the reconciled
   record of play, including every `dm-only` block. The three at the foot
   ("WHAT CHANGED FROM THE PREP", "PREPPED, NEVER SPENT", "CARRIED FORWARD INTO
   SESSION 5") are the most important thing in the repo for this job.
4. `campaigns/fail-academy/planning/session_4_transcript.txt` — the raw
   recording. Read the glossary first or you will misread names.
5. `campaigns/fail-academy/planning/transcript_glossary.md` — §7 is Session 4.
   Note the standing rules at the top, and note that in this transcript nearly
   every line the dragon speaks is mislabelled `Tito:`.
6. `campaigns/fail-academy/planning/session_4_arrival.md` — the Session 4 design
   doc, now historical. Useful mainly for the large amount of prepped material
   that never got spent.
7. `campaigns/fail-academy/planning/phase2_the_one_who_got_away.json` and
   `campaign_arc.json` — the main plot, which is currently several hundred miles
   away from the party. Skim for shape; their session numbering is not current.
8. `campaigns/fail-academy/planning/session_plan.json` — the master tracker.
   Read `open_items`.
9. `campaigns/fail-academy/planning/session_5.md` — a deliberately empty stub
   with the handoff facts and three open questions.

Then read the live entities Session 5 is most likely to touch:
`content/npcs/tedrovaxilliath.html` · `content/npcs/the_captive_drow.html` ·
`content/npcs/morvek.html` · `content/npcs/anselm_ferreck.html` ·
`content/npcs/ellery_voss.html` · `content/creatures/teds_fox.html` ·
`content/locations/neverwinter_wood.html` · `content/locations/underdark_breach.html` ·
`content/items/steel_tuning_fork.html` · `content/mysteries/what_follows_vrenn.html` ·
and all four sheets in `content/players/` (updated from the level-11 exports on
2026-09-25).

## Four directions I'm considering — treat these as a menu, not a brief

I have not chosen. Tell me honestly which you think is strongest and why, and
say so if you think there is a better fifth option I haven't listed.

**A. The first town.** They walk south-west out of the Wood into the settlement
they saw burning a fire. Probably Logger's Camp on the regional map, though I
have not named it. A social and resupply session: the first civilisation in four
sessions, the first shops, the first outside news, and the first chance to find
out what has been happening while they were off-plane. The engine of the session
is that **they cannot simply walk a visibly deformed drow into a frontier human
settlement** — and they have at least four ways to solve it, including leaving
him behind, which would undo the thing they chose in Session 4.

**B. The clock lands.** Morvek's two-to-four days runs out during the session.
Not Morvek himself — the hard campaign constraint is that he never appears in
person and is far past a level-11 party — but something sent. Cashes the
promise, keeps the pressure honest, and makes the party's accidental theft of
the tuning fork matter.

**C. Back into the Breach.** The grinding noise deeper in the cave they walked
away from, and the renegotiation clause Tito wrote into the deal with the
dragon for "more than two beasts." A dungeon session on geography that is
already built and already paid for, with the dragon relationship still live.

**D. The water upstream.** They were handed the entire mechanism for finding the
dragon's lair in Session 4 without being told what it leads to — the corruption
weakens with distance from his lair, which is the same sentence as *it is worst
at his lair*. Following it finds the hoard, the drowned entrance, and a treant
the dragon wrongly believes he killed. Rich, fully prepped, and **the party is
trying to leave and likes him**, so it would have to be their idea.

My instinct is **A as the spine with B arriving in the back half**, and C and D
held as branches if they turn around. Argue me out of it if you disagree.

## Structural problems I want your read on

1. **The main plot is at the Academy and the party is hundreds of miles from
   it.** Phase 2 is Corvin Ashworth, Thornwick and the veil under the campus.
   Nothing in Neverwinter Wood touches any of it. How long can the campaign
   run on a journey arc before that becomes a problem, and what is the cheapest
   honest way to put the main plot back within reach?
2. **How do they actually get home or get word out?** *Plane shift* and the
   steel tuning fork cross planes, not continents, and they are already on the
   right plane — so the fork does not solve this. Ferreck in Neverwinter is the
   designed lifeline. Is there anything closer?
3. **The reward from Session 4 never landed and the party has no potions.**
   A town with shops may simply solve this. Should it? Or does the shortage
   stay a live pressure?
4. **Vrenn outshot the whole party in the Session 4 fight** — 76 damage from a
   2nd-level slot. His stated combat dial was "acts once, decisively, then does
   something practical." That dial is broken and I need a new one.
5. **Several things have gone unspent for three or four sessions running:**
   Voss's contact list has never been read aloud at the table, Vrenn's two
   half-finished scrolls have never been handed over, and the Session 2
   supply-chain clue has failed to land three times. Tell me which of these
   Session 5 should finally pay off and which should keep waiting.

## Rules that apply to everything you do here

- **The transcript is the source of truth** wherever it and the authored data
  disagree. If you hit a *major* conflict — one that contradicts a locked
  decision, invalidates later prep, or changes an established fact rather than
  adding to it — bring it to me rather than resolving it yourself.
- **Absence from a transcript is not evidence something didn't happen.** Ask.
  Session 4 has a worked example: Morvek's *sending* happened and was simply
  never narrated, and a transcript-only reading got it wrong.
- **Never delete substantial authored content on inference.** Ask.
- **When something is ambiguous, ask — don't pick the more interesting reading.**
- **This is a new party.** Silas, Guntrah, Tito, Tavian. The One Shots 1–5 party
  is retired and its members are current underclassmen. Don't let their
  knowledge leak in as ambient fact.
- **Player-facing prose must stay clean.** `visibility: "player"` on the entity,
  secrets in `<div class="dm-only">` blocks inside the file. Names that must
  never appear outside a dm-only block: Thanatos, Orcus, Harthoon, Corvin,
  Thornwick, Nerissa Voss, "armanite", and "Grave Token" is now *spent* and may
  be used — Vrenn said it out loud in Session 4.
- **`campaigns/*/data/*.json` are hand-formatted** with inline arrays. Edit them
  as text. Never rewrite one with `json.dump`.

## When you're done reading, give me

1. **A one-page orientation**: exactly where the party is, what they carry, what
   they know, and what they wrongly believe.
2. **Your recommendation between A/B/C/D**, with reasoning, and a fifth option
   if you have a better one.
3. **Your answers to the five structural problems above.**
4. **Every thread that could plausibly touch Session 5**, including the ones
   running back at the Academy while the party is away — specifically, that as
   far as anyone there knows, four graduates went to a party and vanished.
5. **Anything stale, contradictory, or that you think I've overlooked.** I would
   rather hear it now than halfway through drafting.
6. **Your questions for me.** Be specific, and be blunt about which ones
   actually block you. Then stop.
```

---

_Written 2026-10-05, after the Session 4 reconciliation. The option menu is the
assistant's suggestion from the reconciled state, not a DM decision._

# FAIL Academy — Session 0 Reboot (In Progress)

Vrenn/Wizard-13 conflict RESOLVED (2026-09-01, DM's reading, live data +
planning). The character sheet appeared to contradict the locked “kept just
short of the final step so he stays dependent” line. The DM's answer dissolves
it: **Vrenn learned *plane shift* recently**, because Morvek needed a
scroll-maker on site. He used it to make the scroll the party wasted in Session
2, and was part-way through a second one to Morvek's order when they arrived.

So the locked line **was true and recently stopped being true** — a state that
ended, not a fact to delete. That keeps all the authored history and adds
something better: **Morvek handed a captive the means to leave because he was
certain the Grave Token made it irrelevant.** That is arrogance, it is a flaw,
and flaws are usable later.

**Only two sentences actually needed changing**, which is less than the MAJOR
flag implied:
-  ended “he has no spellcasting of his own” — flatly wrong
  against a Wizard 13, now corrected. The priming remains a separate,
  non-magical knack; it is just not the whole of what he can do.
-  said his incomplete craft was **why** he could never
  escape — that reason is retired and replaced by the Grave Token, which was
  already carrying the weight.

The tragedy is untouched and sharper: he has the means to leave, and every day
he stays is now **a decision rather than an incapacity**. 's conflict
and open-question fields are closed; the three reconciliation options are kept
for the record, superseded.


**RENAMED AGAIN, AND SETTLED: VROK → MORVEK (2026-09-01, DM's choice).** The
first rename swapped Vrask out for an unwanted outside association; the
replacement was then flagged here as trading it for a worse in-game one, since
**Vrok is a near-homophone of *vrock***, the Abyssal vulture demon — which is not
hypothetical, as vrocks already appear in two other campaigns in this repo and in
`shared/data/monsters-*.json`, and were on the table as possible Bonehold door
guards. The DM took the flag and picked **Morvek** from a shortlist. **152
occurrences across the same 11 files**, verified clean.

**Morvek is the settled name.** It resolves both problems at once: no outside
association, and no collision with *vrock* or with **Vrenn** — different initial
consonant, different vowel, different syllable count, which retires the Vr-/Vr-
merge hazard entirely. Zero player-facing cost either time: **none of the three
names has ever been spoken at the table**, which `session_2.html` records
explicitly.

**Three places were hand-edited rather than blanket-replaced**, because a
find-and-replace would have made each of them state something false:

- `phase3_closing_the_veil.json` → `details.the_spirit_harthoon.name` now carries
  the full chain (early-draft placeholder for Harthoon → repurposed → Vrask →
  Vrok → Morvek) with the reason for each step.
- `transcript_glossary.md`'s three name-hazard rows are collapsed into two
  accurate ones: the rename history with the old spellings preserved so a future
  transcript pass recognises them, and a Morvek-vs-Vrenn row noting the merge
  risk is now resolved rather than live. Expect STT to render Morvek as
  "Morvec / Marvek / more vek".
- The earlier "VRASK RENAMED TO VROK" entry below would have been rewritten into
  a claim it never made. It now reads as the record of the first pass and points
  forward to this one, and its vrock hazard is marked retired.


Vrenn character sheet received (2026-09-01, planning + live data). The DM built
one “in case it is needed — not 100% accurate, will serve in a pinch.” It is
more consequential than that. **Vrenn is a Drow Wizard 13, Order of Scribes**,
INT 20, DC 18, HP 67, AC 11, **Arcana +15**, Calligrapher’s Supplies, darkvision
120 ft, Trance, Alert, Lucky, passive Perception 18 — and **slots to 7th level
with *plane shift* in his book**. Full breakdown in
`vrenn_the_captive.json` → `stat_block`.

**What it fixes.** The dawn scroll is now justified by the rules rather than by
homebrew: scribing needs Arcana proficiency, the spell prepared, and components,
and he has all three plus the scroll-making subclass. **The only house rule left
is the compressed timeline**, which the “prepared vellum, sixty-three of the
sixty-four days already spent” framing already covers. **“A true hand” is
retired** — the invented knack was solving a problem Order of Scribes solves
properly, and no replacement name should be invented, because naming a knack
invites players to ask for its mechanics and now there are real ones.

**Why Silas still has to be the caster, now airtight:** *plane shift* transports
the caster. There is no version where Vrenn sends them and stays, and he cannot
leave the plane while Morvek holds the Grave Token. If a player works out that
Vrenn could cast it, that should land as *worse*, not as a loophole — he has had
the power to leave this entire time.

**Tactical warning logged:** a Wizard 13 walking with a level-10 party outclasses
all four of them. Counterspell, haste, hold monster, summon fiend. Somebody will
say “Vrenn, counterspell that.” He does not fight unless cornered; have the
refusal ready as character rather than fiat, and lean on AC 11.

**MAJOR CONFLICT, presented rather than resolved.** The sheet contradicts the
locked `history.why_he_never_finishes_the_job` — that he has no spellcasting and
is *deliberately kept just short* of enchantment so he stays dependent, described
in the design as “the cruellest, quietest part of his captivity.” A Wizard 13 is
not kept short of anything. Three options recorded in
`stat_block.reconciliation_options`; **recommended is (2): the Grave Token does
all the work and he is *checkmated* rather than incapable** — he has always had
the power to leave and has never once been able to use it, which re-reads his
cowering under the bench in Session 2 as resignation rather than helplessness.
Not applied without a decision.


**VRASK RENAMED (2026-09-01, DM instruction, all docs and live data).** First to **Vrok**, and then, later the same day, to **MORVEK** — see the entry above for the second pass and why it happened. This entry records the first.
The DM placed where he had heard "Vrask" before, realised every player at the
table had heard it too, and did not want the association. **137 occurrences
across 11 files** — `ritual_platform.html`, `what_the_drow_owes.html`,
`the_captive_drow.html`, `session_2.html`, `phase3_closing_the_veil.json`,
`session2_draft.html`, `session3_draft.html`, `session_3_prep_prompt.md`,
`transcript_glossary.md`, `vrenn_the_captive.json`, and this file. Verified
clean afterwards.

**Nothing needed retconning.** The name has never been spoken at the table — it
was one of the five intended Session 2 takeaways that did not land, and
`session_2.html` records that "the name has still never been spoken in this
campaign." So this is a pure documentation rename with no player-facing
continuity cost. Any pre-2026-09-01 doc using "Vrask" means Morvek.

**Two places were deliberately NOT blanket-renamed**, because a global
find-and-replace would have made them state something false:

- `phase3_closing_the_veil.json` → `details.the_spirit_harthoon.name` records
  that the character's name began life as an early-draft placeholder for
  Harthoon himself before being repurposed. That history is about the string
  "Vrask" specifically, so the entry now names Morvek as the character, preserves
  "Vrask" as the historical placeholder, and logs why it changed.
- `transcript_glossary.md`'s name-hazard row keeps the old spelling so a future
  transcript pass can recognise it.

**Two new name hazards logged in the glossary**, both worth watching:

- **Morvek vs. vrock.** Near-homophones, and vrocks are Abyssal demons who could
  plausibly appear in exactly these scenes — the repo already has vrocks in two
  other campaigns and in `shared/data/monsters-*.json`. **Do not put a vrock
  anywhere near it**; reflavour or rename if a vulture demon is ever wanted.
  Flagged for the DM at the time: the new name traded one outside association
  for a different in-game collision. **He took the flag and renamed again the
  same day** — the settled name is Morvek, and this hazard is retired.
- **Morvek vs. Vrenn.** Both start Vr-, both belong to the same scene, and STT
  will merge them. The captive drow is Vrenn; the lich who owns him is Morvek.


Session 3 Route B designed; the Bonehold, the landlord, and a name budget
(2026-08-31, planning + live data). `planning/session3_draft.html` now has both
routes end to end and is marked RUNNABLE.

**The demon lord is a landlord, not a rung.** The DM flagged the hierarchy as
"getting too heavy in middle management" — Vrenn > minor demon lord > Morvek >
Harthoon > Orcus. The fix is that the demon lord is **lateral**: he holds the
building, Morvek is billeted on him by Orcus's writ through Harthoon, and he
cannot refuse. He is roughly Morvek's equal, slightly under, which is what makes
it a humiliation rather than an arrangement. The chain stays **Vrenn → Morvek →
Harthoon → Orcus**, and what the party can perceive this session is two rungs and
one name. **He dislikes his tenant, and that is deliberately banked as a future
diplomatic option** (DM, 2026-08-31) — he would be pleased if something
inconvenient happened to Morvek, not enough to act, enough to look away. He is
unnamed, does not appear, and needs nothing this session. Three things he buys
free: the building's split personality on the map, why the glabrezu is *bound*
rather than commanded, and why the thing behind the north gate is **his**
insurance rather than Morvek's.

**Route B, against the DM's own battle map.** ~75×130 ft, a 35–40 ft ritual
circle centred, four braziers at its corners, stairs up at the south, barred gate
under a skull crest at the north. Key design calls: **the braziers are the
mechanism, not decoration**, so the circle has to be *started* rather than
stepped onto — which makes Route B's climax a defence with a timer around an
objective, **structurally the same shape as Route A's hold-the-platform hour**.
Escalation comes **up the stairs behind them** (whatever they failed to deal with
in the sneak sets the difficulty of the ending, unannounced). **The party can use
the circle but not aim it**, same limitation as Vrenn's scroll, so **both routes
land in Neverwinter Wood and only one arrival needs prepping** — this reverses an
earlier note in the thread that argued Route B should land elsewhere; the
consequence budget is better spent on the glabrezu. The SE crates hold **an empty
unmarked crate matching the Provisions Annex one**, which is the Session 2
load-bearing clue finally made available in a corner the map already drew.

**The north gate is a loaded gun.** Behind it, a beast too dangerous even for
this realm — an emergency measure, the landlord's, and pressure rather than an
encounter. **It cannot leave the basement**, so releasing it does not add a
monster, it makes the only exit unreachable, and that quietly tells the party
what the circle is worth. It is **one of the screaming things from Session 2's
arrival description**, caught and kept — free continuity on a line that was never
paid off. The glabrezu **cannot** open it but will threaten to, a lie the party
cannot check; and the party **can** open it themselves, which is a genuinely
terrible option available at all times. **Do not stat it**; if it comes out the
scene is a flight, not a fight (Nightwalker in the back pocket if a block is
needed).

**The guard: a planar bound glabrezu (CR 9), quarantined in its own block** so it
swaps for a Boneclaw (CR 12) in one paragraph. The hook is that **the binding
sigil is part of the same floor-work as the circle**, so lighting the braziers
slackens the binding and the demon's escape is the party's escape — it is
helpful, informative and charming, and its help is the trap, with the fight
arriving at the end, on the circle, as they leave. **Balance fix that matters:
Route B contains no long rest**, so the hour's walk is ruled a **short rest** —
Hit Dice, Tito's Bardic back, Silas's Arcane Recovery, Tavian's Channel Divinity.
Guntrah's Flash of Genius stays spent, because that is Route A's reward.

**A quiet moral difference between the routes, which the party may not notice:**
Route A takes Vrenn's one scroll and leaves him facing Morvek empty-handed. **Route
B costs him nothing** — he has all night to make Morvek's scroll as normal. He
states it once, flatly, without pleading: *"If you go to the house, I still have
tomorrow's work to give him. If you take the scroll, I don't."*

**NAME BUDGET — new standing block at the top of the draft, and worth applying to
every future session.** The DM's flag: too many proper nouns will confuse the
table, who have not heard of Corvin Ashworth and are still working out Thatch's
role. Session 3 as drafted could have thrown a dozen new names in one sitting.
Trimmed to four spoken: **Vrenn · Morvek · Neverwinter · Anselm Ferreck** (the last
only if the contact list comes up). Explicitly **not** said: "the Bonehold" (a
filing label only — Vrenn calls it *"the house"*), **"Grave Token"** (DM-side
term; Vrenn now says *"He's got my soul. He wears it on his belt"*, updated on his
live entity), **Thanatos** (deferred — this reverses the earlier "decide
deliberately" flag), Harthoon, and the demon lord. **Voss's contact list is six
more names and is the worst single overload risk: hand the prop over and do not
read it aloud.** One inversion worth keeping: if anyone tries **Thatch** on the
glabrezu, it has never heard of him either — a second independent source at the
far end of the chain, which *rewards* the puzzle the party is already working
rather than burying it.


Silas's spell list received; Session 3 Route A designed end to end (2026-08-30,
live data + planning). The character-sheet PDF arrived and resolved the biggest
blocker on the file. **Silas has *Leomund's Tiny Hut*, and it is a ritual** — no
slot, no preparation, available every night regardless of what he prepped. He
does **not** have *Rope Trick*. His full spellbook is now recorded on
`content/players/silas.html`, replacing the "spellbook page came through blank"
placeholder that had been there since Session 0, along with his real equipment
(15 gp, and — worth noting — **ink, an ink pen and ten sheets of parchment**, so
he is already carrying scribing kit when Vrenn offers him materials). Caveat kept
on the entity: the sheet's prepared markers were all blank, so his prepared
fifteen on any given day is still unconfirmed. The rituals do not need it.

**The night is now a placement puzzle, not a survival one.** Tiny Hut means the
party cannot be got at, so Route A is designed around the four things the hut
*cannot* do: it takes **ten minutes** to cast (not an escape button with
something crossing the bridge), the dome is **opaque and conspicuous** from
outside and immobile, it **ends if Silas leaves**, and it runs **exactly eight
hours** against roughly twelve until dawn — which leaves about two hours of
exposure at each end that the hut cannot cover. Route A therefore runs as three
scenes: **the break** (getting off the island — one stone bridge, contested, and
a fifteen-foot lava moat that Tavian and Tito can jump and Silas at STR 7 cannot,
which is a good three-minute problem that belongs to the martials), **the night**
(where the dome goes and what walks past it), and **the return**.

**Route A's climax is not the casting — it is holding the platform for an hour.**
The armanites find two dead guards and sixty feet of stone wall, so the site is
occupied when the party comes back; they have to retake it quietly and then hold
it while Vrenn writes. That is a defence with a clock and a win condition that
is not "kill everything," it escalates on a timer rather than on damage, and it
is the right use of what this party actually has. Note for building it: this
time we know *wall of stone* **and *wall of force*** are coming, so plan around
them rather than being blindsided the way Session 2 was.

**Terrain beyond the moat — PROPOSED, swap freely.** An ash-and-slag plain with
smoke venting at chest height, long low **slag ridges** running toward the
mountains, and the spoil of **old workings** (collapsed shafts, a sink deep
enough to hide a dome). Built to do three jobs, which any replacement should
keep: cover exists in *specific places* so choosing a campsite is a real
decision; the dome is invisible behind a ridge and visible for miles on open ash;
and **the ash holds footprints**, so walking out leaves a line pointing at where
you stopped — with the answer (walk the hard slag) available and deliberately
unstated. Well-placed dome: they hear the search pass and get a clean night.
Badly placed: something finds it, cannot get in, and **sits down outside to
wait** — worse than a fight, costs no hit points, and turns the morning exit into
the problem. Either way **they get the long rest**, which is what puts Guntrah's
five unspent uses of Flash of Genius back on the table and makes the dawn casting
winnable.

Other spells on the sheet that will change scenes and are now flagged on his
entity: **Alarm** (ritual, 8 hours of free early warning), **Comprehend
Languages** (ritual — any written clue in an unknown language is a ten-minute
delay, not an obstacle, worth knowing before authoring the next one),
**Clairvoyance** (1 mile) and **Arcane Eye** (this party can scout a building
thoroughly without entering it, which Route B must be designed to survive),
**Wall of Force** and **Otiluke's Resilient Sphere** as further hard counters,
**Darkvision** (solves Tito's blindness for 8 hours), **Protection from Energy**
(answers the lightning lance), and **Augury** as a ritual, which sits oddly
nicely beside the untaken Ring of Augury and the Savras thread. Confirmed from
the sheet: slots run **4/3/3/3/2 and stop** — the 7th-level ceiling problem is
real and permanent for a long while.

**Still open:** Route B in its entirety, Plan C if the dawn casting also fails,
the vellum count, a permanent name for "a true hand," and the twelve-hours-until-
dawn assumption that the whole of A2/A3 is timed against.


Session 3 escape mechanism + Vrenn build-out (2026-08-29, live data + planning).
Session 3 opens mid-scene on the Thanatos platform and the question is not "how
do we escape" but **"where do we survive the next twelve hours"** — because the
only exit takes until morning to build. New draft: `planning/session3_draft.html`,
Route A runnable, **Route B (the structure east) deliberately stubbed** at the
DM's instruction.

**The escape is now Vrenn, not the dais.** The 2026-08-19 design (a forked rod at
the central dais, forced open under an Arcana check, set to a "delivery lane")
is **retired in part** — preserved intact in `session_2.html`'s Carried Forward
block, and superseded on the live entities. The runic circle the party can see is
now **the altar and the receiving end** — how Morvek reaches in, how finished goods
are collected. It does not fire on demand and it was never Vrenn's to work:
*"That's not for going. That's for him."* Note the circle itself **stays** — it is
on the Session 2 recording and in the player-facing prose; it simply is not an
exit. What replaces it: Vrenn transcribes a fresh *plane shift* scroll at dawn,
about an hour's work, **one scroll only, and Morvek comes for it.**

**The tuning fork is the *plane shift* material component** — the spell's own text
calls it "a forked, metal rod... attuned to a particular plane of existence," so
the fork and the old "rod" were always the same object under two vocabularies.
It is the only one on site, it is **not consumed by casting**, and it carries the
operation's capital value — which is where the scroll's 25,000 gp actually sits,
so nothing has to evaporate per scroll (vellum and inks are the consumables).
Consequence the DM should not signpost: **the fork leaves with whoever is holding
it**, making that a real choice at the moment of exit — proof and a future asset,
against the one object standing between Vrenn and Morvek's temper. It is still not
a hatch: *plane shift* is 7th level, the party's ceiling is 5th.

**"A true hand" (name provisional).** Vrenn finishes a 7th-level scroll without
being a caster because he is a **natural copyist**: given prepared vellum, inks
and the fork he reproduces an existing scroll's text exactly, and the copy works.
No slot, no spellcasting, no comprehension. It is the same faculty as his priming
pointed at ink instead of metal — **exactness without comprehension**, which is
specifically *not* enchantment, so the locked cruelty in `vrenn_the_captive.json`
survives narrowed rather than overwritten: Morvek still keeps him short of the
final step on everything that matters, and tolerates this one exception because a
site that ships needs somebody who can post the parcel. It saps him — once a day,
and he is worse company afterwards. He will likely press his spare supplies on
Silas, which hands Silas **materials, not the knack**.

**The Grave Token — BEACON, not anchor, and Morvek wears it.** A Grave Token is
an **Abyssal** soul-binding invented for this campaign and is deliberately **not**
an infernal soul coin — nothing in this campaign touches the Nine Hells, and it
should never be written in a way that implies devils. Nothing physically stops
Vrenn crossing planes; the Token tells Morvek where its soul is, always, so
leaving is not futile for him so much as **lethal for whoever is standing next to
him**. That is the reason he gives, and it is an argument about protecting *them*.
So the party genuinely **can** talk him into coming, and it is a bad idea rather
than a locked door; he resists as much as is reasonable, and intends to be at his
workbench when Morvek arrives regardless. He will leave the *site* — to hide out or
to walk east — but not the *plane*. **He sold his soul himself, and not for
himself:** his sister was going to die at the hands of something in the
Undermountain. **She is alive**, deliberately open-ended as a future thread;
whether Vrenn knows is undecided. He does not tell this story and should not be
made to. Two knock-ons: `history.bought_and_sold` stops being metaphor — the Token
changed hands and he went with it every time, so he was never a person being
traded, he was a receipt — and **"why he never used the scroll" is now answered**,
retiring the deliberately-dual reading in `what_the_drow_owes.html`. He is not too
broken to act. He is leashed. That also re-aims the Session 2 handoff: he did not
give away his one chance, he gave away **Morvek's property the day before Morvek
came to collect it**, which is braver rather than smaller.

**The destination "oopsie."** Vrenn can make the scroll and cannot aim it — he
copies the one working he was taught, and the only surface place he has a name for
is **"Neverwinter."** Which is a region as well as a city. They name Neverwinter;
they arrive in **Neverwinter Wood**. Nobody at the table is told this was an error.
This preserves the locked landing, the Thundertree seed and Session 4's
four-direction fork, and delivers all of it through a person instead of an
inspection roll nobody made. Background, no urgency: **Morvek personally casts
*plane shift* for the FAIL Academy consignments** — that end of the lane is his.

**The dawn casting, and the real dial.** Silas is the only one who can do it —
Vrenn would be taken with it, Tavian cannot use the scroll at all (*plane shift*
is not on the paladin list), Tito is a poor fallback. DC 17, Silas +9, so **35%
failure unaided** (an earlier 20% estimate was wrong). **Guntrah's Flash of
Genius** — +5, reaction, five per long rest, unspent all campaign — takes it to
10%; Tito's Bardic d10 on top takes it to roughly 1 in 200. **So the dial is not
the DC, it is whether they think to stack it**, which makes the difference between
the two attempts *preparation* rather than luck. The DM will hint. **Plan C (a
second failure) is deliberately not planned.**

**The armanite count is an estimate, not a fact** (DM, 2026-08-26) — Vrenn has
watched them a year and "fifteen in about a minute" is where he puts the highest
probability. That converts the opening from a countdown into a decision window; a
forward patrol arriving ahead of the main body is the most useful shape, and
whatever arrives, the answer is a chase, not a stand.

**Live data touched:** `content/npcs/the_captive_drow.html` (new Session 3 dm-only
block — the ~18-second monologue, the follow-up bank, the true hand, the Grave Token,
where he will and will not go; the old "could even leave with them" line marked
superseded), `content/mysteries/what_the_drow_owes.html` (the Token answers the
scroll question), `content/locations/ritual_platform.html` (circle is the altar,
dais exit retired, fork replaces the rod). All three are `visibility: player`, so
every word of this sits inside `dm-only` blocks; player-facing prose is unchanged.
**Blocking Session 3:** Silas's prepared spell list (Tiny Hut / Rope Trick — the
hide-and-evade branch cannot be balanced without it), a paragraph of terrain
beyond the moat, and all of Route B.


Mysteries wired in + session reveals fired (2026-08-24, live data). This
campaign had no `mysteries.json` despite `type:"mystery"` being in the locked
schema; created and added to `data/index.json`. **No code change was needed** —
`menu.js`, `modal.js`, `search.js` and `dashboard.js` already handle the type.
Six open mysteries, all player-visible with the answers in `dm-only` blocks:
`the_sabotage_pattern` (the oldest live thread), `the_groundskeepers_package`,
`what_the_drow_owes` (the unscripted "it's not time, I told you I needed
another day" slip — the best hook Session 2 produced),
`the_figure_at_the_treeline`, `the_bulette_that_didnt_fit`, and
`why_voss_has_latitude`.

**Both played sessions' `reveals[]` have now been applied** — via
`campaign.json`'s `baselineRevealed`, which is the only mechanism that actually
works here. First attempt wrote them into `campaign-state.json`; that file is
**gitignored and written exclusively via the GitHub API**, nothing in the app
reads the local copy, so the edit was inert. It has been restored to its
previous contents. `baselineRevealed` is loaded on every app start, is additive
and idempotent, and `baselineSeeded` means a deliberate un-reveal is never
undone — so listing them there applies them with no action from the DM and no
risk to existing state. Each session's `reveals[]` remains the authoritative
record of which session earned what; `baselineRevealed` is only the delivery
mechanism, and the reason is documented in `campaign.json`'s own
`_baselineRevealed_note`. **Session 3 onward should be authored as
`category: "Planning"` and run through the Session Runner at the table**, which
fires its reveals natively and makes this exception unnecessary. Note
`session_2` is still `visibility: dm-only`, so revealing it is a no-op until
that flips — both gates must pass. Player View now shows **104 of 120**
player-visible entities; the 16 held back are the retired party's five One
Shots, their six magic items, two remote field sites and three wilderness
creature entries.

**Armanite printing settled:** Mordenkainen's Tome of Foes, per the DM's
tie-break ("whichever matches the transcript; if both match equally, MToF").
The read-aloud flavour text — curling talons, serrated tail ridges that
*flense*, rarely seen in packs as small as two — is carried in both printings
essentially unchanged, so the recording cannot distinguish them and the
tie-break applies. **This is a deliberate exception to the standing
"newest official sourcebook wins" rule**, which would have pointed at MPMM.
Practical caveat recorded on the entity: D&D Beyond pulled Volo's and MToF from
its marketplace on 17 May 2022 and serves the MToF armanite behind a
legacy-content notice, so the MPMM stat block is the fallback if the physical
book isn't to hand.

Session 2 entity build-out + Player View audit (2026-08-24, live data). Nine
new entities, all authored **player-visible with the secrets in `dm-only`
blocks** rather than gated wholesale — the pattern the DM asked for: the party
gets an accurate account of what they perceived, and everything they don't know
sits inside the file. New: `hooved_demons` (the party has no name for armanites
— the DM declined to give one at the table, so the entity is named from their
perception and the stat block/CR/D&D Beyond link are dm-only), `ritual_platform`
(player-facing description says only "somewhere in **the Abyss**" per DM ruling
that the lava moat and idol-busts were enough; Thanatos, Orcus, Morvek, the
forked rod and the Neverwinter Wood delivery lane are all dm-only),
`the_captive_drow` (**Vrenn's name is dm-only** — he never introduced himself
and is expected to in Session 3), `silas_and_breena` (one entity, not two —
avoids an id collision with the PC Silas), `speaking_stone`, `torvald_package`,
`ollie`, `bertram_hollis`, and `hask_undermoor` — the last invented to give a
face to the fourth-year who spoke up for Guntrah at Commencement. New categories:
"Beyond the Veil" (locations/npcs/creatures), "Family", "Communication",
"Constructs", "Evidence".

**Ring Conferral — the one place authored data overruled the transcript.** The
recording shows an on-stage pick from a case of mixed-metal labelled bands; the
DM clarified that was never the intent. Canon: selection is **private, before
Commencement** (so nobody reads item text or asks rules questions on a stage),
the choice is **announced publicly at the conferral**, and bands stay struck
identical in gold. `rings.html` rewritten accordingly. What the transcript does
settle and is now canon: separate diplomas exist, conferred by a clerk, so the
ring does NOT double as the diploma. Standing rule adopted the same day and
recorded at the top of `transcript_glossary.md`: **where transcript and data
diverge the transcript wins, except for major conflicts, which get presented for
approval** — this was the worked example.

**Holdar's reaction is not what Guntrah thinks it is.** He turned away partly
from embarrassment and partly from **disgust** (DM, 2026-08-24) — Guntrah routed
around five years of the one conviction Holdar's whole department is built on,
and the Academy applauded. Recorded in `prof_bram_holdar.html`, `guntrah.html`
and `session_2.html`; the target of the disgust is deliberately unpinned.

**Player View audit — 45 → 17.** An audit found **36 entities already
`visibility: player` but never revealed**, and therefore invisible in Player
View regardless of their visibility flag. Most were plain oversights: four
faculty (`archdruid_sevra`, `master_jin`, `master_veris`, `warden_ashgrove`),
three campus facilities (`fail_chamber` — which Voss runs and every PC has sat
practicals in — plus `druids_grove` and `owlbear_cave`), four campus creatures,
both student clubs, `campaign_overview`, and `potion_of_healing` (every student
gets two a year). Added to `campaign.json`'s `baselineRevealed`, which is
additive and idempotent so it applies on next load without clobbering any
deliberate un-reveal. Also added: the retired One Shots party
(`lugeiros_serise`, `gunnar`, `caelum_rivenstone`, `bloodraven`) — per
campaign_arc's continuity note they are current *underclassmen* the party knows,
not strangers. **17 remain unrevealed and all are defensible** (the archived
One Shots and their loot, remote field sites, wilderness threats) — except
`session_1`, see the mechanism note below.

**Known mechanism gap (RESOLVED 2026-08-24 — kept for the explanation):** a
session's `reveals[]` only fires through the Session Runner's Complete-Session
flow, and the Runner filters on `category == "Planning"` exactly. Both played
sessions are `Completed`, so neither could fire automatically. Rather than
round-trip the categories, both sessions' reveals were written straight into
`campaign-state.json` — safe because the GitHub pull path is an additive merge.
`session_1` and `session_2` were each added to their own `reveals[]` first, so
the sessions themselves are flagged too. **Worth remembering for Session 3:**
author the session as `category: "Planning"` and run it through the Session
Runner at the table, and its reveals fire on their own — this only became a
chore because both sessions were reconciled after the fact.

Session 2 played and reconciled (played 2026-08-20, reconciled 2026-08-23,
live data). Full session ran in one sitting — Commencement, the Ring Conferral,
an extended and almost entirely unscripted farewells block, Voss's ask, the
Provisions break-in, the package, the portal, and the fight on the far side.
`content/sessions/session_2.html` rewritten against the transcript the same way
`session_1.html` was, with a dated "What Actually Happened at the Table" record;
`data/sessions.json` session_2 flipped category `Planning` → `Completed`.
(Its `reveals[]` was expanded on 2026-08-24 once the new entities existed — see
the entity build-out entry above.) **Visibility deliberately left `dm-only`** —
see the LEAK SCAN block at the foot of session_2.html; recommendation is to hold
until Session 3 closes the scene and flip both together. New reference doc:
`planning/transcript_glossary.md`, the agreed STT correction set (name fixes,
name-collision hazards, speaker-attribution fixes, standing rules) — reuse and
extend it for every future transcript pass.

**The session does not end where it was planned to.** The party never got home.
Both designed exits failed: they never found the dais or the forked rod, and the
drow's *plane shift* scroll — which he handed over unprompted rather than
needing to be found — was destroyed when Silas rolled a natural 1 casting from
it. Session 2 ends **stranded on the Thanatos platform** with fifteen more
armanites about a minute out, and Session 3 now opens there. Consequence:
**the arrival in Neverwinter Wood and the four-direction fork both slide one
session later** — the fork is now a Session 4 beat, not the top of Session 3.
`session_plan.json`'s post_session_2_fork updated to match. The escape design
(LOCKED 2026-08-19) is unspent rather than invalid: the dais and its forked rod,
set to the Neverwinter Wood delivery lane, are untouched and are now the only
way out.

Four further Session 2 rulings, all live: (a) **the Celestial trigger word is
scrapped** — the DM ran the glyph as firing on the package being *opened*, not
on a spoken word, so nobody ever read the note aloud and no word is owed;
session_plan.json's open item is closed, and the "only catches someone literate
enough to be a threat" clue is no longer supported by the mechanism as run.
(b) **Voss's six-name contact list was never handed over** — the DM forgot it,
and it will be delivered retroactively at the top of Session 3; the six
operatives are NOT revealed. (c) **The Ring Conferral was restaged live** and
diverges from the locked plan in three ways — the rings are visibly different
metals, openly labelled and publicly chosen, and separate diplomas exist, so the
ring does not double as the diploma; `rings.html` needs a decision between the
table version (recommended) and the 2026-08-14 draft. (d) **Nobody took the Ring
of Augury**, so the Savras/Senna thread is entirely unspent.

**Four of the five intended takeaways did not land.** The party arrived, was
charged within seconds, and left the moment the fight ended — nobody examined
the workbench, the altar, the tools, or the matching crate. They do not know the
artifacts are made there, do not know it is the Abyss, have never heard "Morvek",
and got no sense of increasing traffic. This is recoverable rather than lost:
they are still standing on top of every one of those clues. Nothing leaked in
the other direction either — Vrenn was never named (he simply never introduced
himself), and Morvek, Harthoon, Orcus, Thanatos and "armanite" were never spoken.
**Torvald's name entered the scene from a player's mouth** (Tito tried "Thatch
sent us") and the drow's honest "I don't know who that is" gave nothing back.

Ring choices are permanent character data and are now recorded on each PC
entity: **Guntrah — Ring of Swimming · Silas — Ring of Regeneration · Tavian —
Ring of the Ram · Tito — Ring of Free Action.** A large amount of unscripted PC
canon was also captured onto the four player entities: Silas's hometown
**Rosgaunt** and his lottery place; Tavian's unnamed **fishing village** and his
scholarship; Tito's satyr family in **Baldur's Gate** (import-export, quite
possibly criminal, an open offer to take over, and a sack of uncounted gold);
Guntrah's adoptive gnome parents **Silas and Breena**, the paired **speaking
stone** they gave him, and his construct **Ollie** (a Steel Defender, three and
a half years in the making). Two live-data corrections fell out of the pass:
**Professor Tavel is famous** — a run of well-known inventions forty or fifty
years ago, newly established and not previously in his entity — and **the "Bad
Semester" bond between Silas and Tavian runs the opposite way to the Session 0
draft**: Silas is the one who nearly left, Tavian talked him into staying.
Corrected in `silas.html`, `tavian_stormnet.html`, and
`session_zero_relationship_table.md`, with the superseded reading kept inline
for the record. Unscripted and now canon at the NPC level: **Holdar could not
meet Guntrah's eye at the Conferral and looked ashamed**, then left before
Guntrah could find him — the thread `prof_tavel.html`/`guntrah.html` both
flagged as "established as backstory, not yet dramatized" has now fired.

Academy geography FIXED (2026-08-15, DM ruling, live data): the campus sits
**inside the High Forest but only just — at the forest's northwestern-most
edge, roughly 200 yards south of the River Rauvin, with Silverymoon about two
days' walk NORTH.** This supersedes two earlier and mutually inconsistent
claims: `campus_root.html`'s "northern fringe of Silverymoon, along the River
Rauvin," and the route-map reading of "High Forest/Evermoors border, southeast
of Silverymoon." The practical consequence, now written into live data: north
of campus the trees give out within a couple hundred yards and open onto the
river, while south and east the forest runs on for days and deepens — so the
Academy is on the shallow end of something very deep. Applied to
`campus_root.html`, `high_forest.html`, `river_rauvin.html`, and
`silverymoon.html` (which also had Silverymoon at 3–4 days south-southwest;
now a little over two days north, slightly under two by boat downstream).
Also updated in `session_plan.json` and `campaign_arc.json`.

Session 2 package rewrite — the Celestial trigger (2026-08-19, DM ruling,
live in `content/sessions/session_2.html`). The unmarked package in the
Provisions Intake Annex is **no longer addressed to Dr. Voss**. It is addressed
to **the groundskeeper** ([[torvald_thatch]]), and carries two handwritten notes
on the outside: one in Common instructing that Voss is not to see it, by name,
and beneath it several lines in **Celestial**. This is why Osric Morne has not
delivered it and why he is anxious — he can read the first note, cannot read the
second, and has no rule that covers holding a package addressed to one colleague
with written instructions to hide it from another. He is NOT complicit; this is
the real reason he stayed back from Commencement and part of why the argument
with Voss went as badly as it did.
The trap itself: a 7th-level **glyph of warding** (spell glyph) storing
**plane shift**, keyed to a spoken trigger word inside the Celestial text — NOT
to opening the package. Everyone within 20 ft makes a **DC 20 Charisma save** or
is transported to Thanatos; the rift then stays open one round (≈ five seconds)
so anyone left behind may choose to follow, then collapses. Because the glyph is
keyed to Celestial, it is inert to Osric and to Torvald and only catches an
interceptor literate enough to be a threat — which is itself a clue about the
sender. Verified against the live character sheets: **Silas is the party's only
Celestial speaker and has a CHA save of −1**, so the reader is the one person who
cannot pass the DC unaided; **Tito** (CHA +8 plus Satyr advantage vs spells)
effectively cannot be caught by any reasonable DC, so his going through is a
decision rather than a roll. Tavian's Aura of Protection (+3, 10 ft) vs the
glyph's 20 ft radius means table positioning decides two of the four saves — ask
where everyone is standing BEFORE the note is read.
**Return mechanism LOCKED the same day:** *plane shift* requires a forked metal
rod attuned to the destination plane, and the site must own one to ship at all.
It sits at the dais, set to a **delivery lane** rather than a chosen place. The
Academy's consignment has already gone out (it is the package in the Annex), so
the rod is set to the other lane, which terminates in **Neverwinter Wood** — the
landing is therefore not arbitrary, it means somebody else is being supplied out
there, and it quietly seeds Thundertree among the four Session 3 directions. Both
exits (forcing the dais, Vrenn's scroll) use the same rod and land in the same
place, so only one arrival needs prepping. The rod is portable and the party may
take it; it is proof and a future asset but NOT an escape hatch, since
*plane shift* is 7th level and the party's highest slot is 5th.
**Known cost, accepted:** this puts the groundskeeper in front of the party as a
suspect in Session 2, earlier than `torvald_the_insider.json` and
`session_plan.json` assumed (Torvald's interrogation was pencilled for Session 5).
Nothing about the ring, the possession, or Corvin is exposed — only that
something addressed to Torvald did not want Voss knowing about it. The Thanatos
scene's own guardrail is unchanged: Torvald is not named or referenced there.

NPC first-name collision fix (2026-08-14, live data): the player formerly
named Xarad was renamed to Silas (see the earlier Silas rename commit), which
collided with the existing Provisions Office NPC's first name. Renamed that
NPC from **Silas Morne** to **Osric Morne** — display name, body text, AND
the internal slug: entity `id` changed `silas_morne` → `osric_morne`, and
`content/npcs/silas_morne.html` was git-mv'd to `content/npcs/osric_morne.html`
(2026-08-14, follow-up pass — the id was initially left alone as "not
player-facing," but changed on request to avoid future-DM confusion between
the two Silases at the data layer). Updated every reference across
data/npcs.json (id + contentFile), the `related[]` arrays in data/locations.json,
data/sessions.json, data/factions.json, and data/references.json, and every
`[[silas_morne|...]]` cross-link and bare filename mention in the content files
that mention him (academy_provisions.html, academy_credits.html,
academy_traditions.html, thornwick_consortium.html, dueling_society.html,
one_shot_5.html, session_1.html, bag_of_tricks.html, goggles_of_night.html,
potion_of_healing.html, everlund.html, river_rauvin.html), plus the
not-yet-played planning doc `the_prov_investigation.json` (including its
internal `silas_beat`/`getting_past_silas`/`silas_forward_hook` keys, renamed
to `osric_*` for consistency, and its `silas_morne.html` filename mentions)
and the top-level README feature list. Player character Silas's own
references (id `silas`, e.g. in session_1.html's party list,
content/players/*.html, party_overview.html, quick_components_pouch.html)
were left untouched — those are the party member, not the Provisions NPC.

Voss-lineage race/age pass (2026-08-13, live data): `ellery_voss.html` had no
Species/Age fields (unlike e.g. `headmistress_dowe.html`) — filled in as
**Human, late 40s**, per explicit instruction (non-elven lifespan). Applied
the same Human species to `aldric_voss.html` for consistency across the
lineage. Created a new dm-only NPC entity, `nerissa_voss` (Human, founding
era, ~350 years before present — an ordinary human lifespan, long since
ended), since she was previously only prose-described inside
`ninth_thesis.html`/`the_ninth_thesis.json` with no entity of her own.
Cross-linked her `[[nerissa_voss]]` from `ellery_voss.html`, `aldric_voss.html`,
`ninth_thesis.html`, and `voss_keycard.html` wherever she was previously named
in plain text. She is deliberately kept thin (textual/historical role only,
not a scene NPC) — see her entity's own dm-only note before expanding her.

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
  bypassing Osric (timing, magic, stealth/distraction, or the honest note-from-
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
- `session2_draft.html` — NEW (2026-08-13), full arc blocked out (2026-08-14).
  Prose draft of Session 2, same pattern as `session1_draft.html`. Now covers
  the whole session: Voss's pre-ceremony Ninth Thesis contact-list handoff,
  the Commencement ceremony (venue: Founder's Statue, plus a forgettable
  guest-speaker set piece), Ring Selection restaged as a public part of the
  ceremony itself (doubling as the diploma conferral, not a private
  pre-ceremony errand as first drafted), Voss's own failed break-in at
  Provisions during the ceremony and her off-screen argument with Osric
  Morne, the party's branch into the_prov_investigation.json's Provisions
  break-in, and a substantially reworked destination scene once the
  unmarked package (Conjuration-school planar magic) is opened: a
  map-driven open-air ritual platform on Thanatos with a lava moat, a
  broken drow captive (placeholder name Vrenn — Stockholm-syndromed, forced
  labor, won't fight unless provoked, deliberately thin backstory held back
  by the DM) instead of the original babau "tinkerers," and two armanites
  (CR 7 each) as guards instead of the original combat design. The escape
  this time is one-way — the arrival rift vanishes on its own, and forcing
  the site's ritual dais open under duress strands the party in Neverwinter
  Wood, not back at the Academy. Session 2 now deliberately ends there,
  disoriented, with the choice of which direction to travel explicitly
  deferred to Session 3 — see session_plan.json's new `post_session_2_fork`
  entry for the four options (Thundertree, Mount Hotenow, the Triboar Trail,
  Agatha's Grove), none of which are prepped yet. This supersedes Session
  2's old "party chooses a destination and departs campus" beat and cuts the
  Triboar/Yartar travel-stop scene from this session. `the_prov_investigation.json`
  itself is marked superseded-in-part (2026-08-14) rather than rewritten —
  it's kept as design history, session2_draft.html is authoritative for how
  this actually gets run.
- `vrenn_the_captive.json` — NEW (2026-08-14), revised same day. Companion
  depth doc for Vrenn (placeholder name), the captive drow craftsman at
  session2_draft.html's Thanatos ritual site — same pattern as
  torvald_the_insider.json and corvin_ashworth_build.json. Covers how long
  he's been trapped (longer than he can accurately say), being bought and
  sold multiple times before ending up here, and his craft (primes raw
  material for enchantment but never performs the enchantment itself,
  deliberately kept just short of that final step so he stays dependent).
  His master is **Morvek**, a lesser lich subordinate to Harthoon (Orcus's
  already-confirmed lich-vizier from phase3_closing_the_veil.json) — an
  initial same-day proposal to make the site belong to the genuine Harthoon
  directly was floated and then reverted; Harthoon is explicitly one tier
  up and not involved at this level. 'Morvek' was previously an abandoned
  early-draft placeholder name for Harthoon himself — it's now repurposed as
  this distinct, separate character, and phase3_closing_the_veil.json has
  been updated to flag the reuse. Hard constraint either way: neither Morvek
  nor Harthoon appears in person in session2_draft.html's scene.
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
  route map placed the Academy at the High Forest/Evermoors border southeast
  of Silverymoon — **SUPERSEDED 2026-08-15**, see the Academy geography entry
  at the top of this file. Everything beyond Session 5 is intentionally
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

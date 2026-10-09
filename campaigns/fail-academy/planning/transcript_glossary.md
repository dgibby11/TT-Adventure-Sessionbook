# FAIL Academy — Session Transcript Glossary

Speech-to-text correction reference for reconciling recorded session transcripts
against live campaign data. Built during the **Session 2 ("Commencement",
played 2026-08-20)** reconciliation pass on 2026-08-23, and agreed with the DM
line by line before anything was written to live data. **Extended by the Session 3
("Before Dawn") pass on 2026-09-03** — see §6. **Extended again by the Session 4
("The Green Country") pass on 2026-09-25** — see §7. **Extended again by the
Session 5 ("A Lie for a Lie") pass on 2026-10-07** — see §8.

Reuse this for every future transcript pass. Add to it rather than rewriting it —
each session's recording tends to mangle the same names the same way.

**Transcripts on file:** `planning/session_1_transcript.txt` (Session 1, played
2026-08-09) · `planning/session_2_transcript.txt` (Session 2, played 2026-08-20)
· `planning/session_3_transcript.txt` (Session 3, played 2026-09-02)
· `planning/session_4_transcript.txt` (Session 4, played 2026-09-24)
· `planning/session_5_transcript.txt` (Session 5, played 2026-10-06).

**Standing rules for any transcript pass (DM's, carried forward):**

- **Where the transcript and the authored data diverge, the transcript wins.**
  (DM, 2026-08-24.) Apply the table version and update the data to match —
  don't preserve the draft as though it were still true. The one exception is a
  **major conflict**: something that contradicts a locked design decision,
  invalidates prep further down the line, or changes an established fact about
  a character or the world rather than just adding to it. Present those for
  approval rather than resolving them unilaterally. Everything else, just fix.
- **Absence from the transcript is not evidence something didn't happen.**
  Recordings start late and mics miss things. This produced a false conclusion
  once already, in the Session 1 pass. Ask; don't infer.
- **Never delete substantial authored content on inference.** Ask.
- **When something is ambiguous, ask — do not pick the more interesting reading.**
- **Watch for retired-party knowledge being treated as ambient fact.** This is a
  new party (Silas, Guntrah, Tito, Tavian). The One Shots 1–5 party is retired
  and are now underclassmen; what *they* knew is not ambient.
- **Every NPC is voiced by the DM**, so a `DM:` label is not evidence of
  narration. Attribute NPC dialogue by scene, not by label.

---

## 1. Proper-noun corrections

Apply these on sight in any transcript.

| Transcript renders it | Correct | Notes |
|---|---|---|
| Dao, Headmaster Dao | **Headmistress Seranthia Dowe** | Also fix the title: *Headmistress*, not Headmaster. |
| Bram Holder, Brom Holder, Holder | **Professor Bram Holdar** | Barbarians Department head. |
| Tavil, Taval | **Professor Tavel** | Dwarf artificer instructor; Guntrah's secret mentor. |
| Orvin, Professor Orvin | **Commander Orvyn** | *Commander*, never Professor. |
| Silvery Moon | **Silverymoon** | |
| counselor Bertram Hollis | **Councilor Bertram Hollis** | Silverymoon Merchant Council. |
| College of Elegance | **College of Eloquence** | Tito's bard subclass. |
| Zerod | **Xarad** | The PC's pre-rename name; renamed to Silas 2026-08-14. |
| Silas Morn, Mr. Morn | **Osric Morne** | Not STT — a live DM slip, self-corrected on the recording. |
| air-godseed | **Air Genasi** | Tavian's species. |
| planar shift portal, plain shift | **plane shift** | |
| steel defendant | **Steel Defender** | Guntrah's construct — see §3. |
| Holly, Bally, Wally | **Ollie** | Same construct. "Bally"/"Ollie Doo" are in-scene jokes, not errors. |
| the Barbarians Academy | **Barbarians Department** | Departments, not academies. |
| the Bard College | **Bards Department** | May be intentional in-fiction flavor; harmless either way. |
| Professor Thatch | **Torvald Thatch**, the *groundskeeper* | Confirmed garble (DM, 2026-08-23). He is not faculty. |
| Sealus, Cialis | **Silas** | Table pronunciation jokes; leave them alone. |
| Michael Bulette | Bulette | A Michael Bublé joke that landed correctly. Not an error. |

### Known-clean — came through correctly every time in Session 2

Bulette · Torvald Thatch · Voss · Viola Gossamer · Ninth Thesis · Bertram Hollis
· Guntrah · Tavian · Baldur's Gate · Plane Shift (second usage) · flense ·
lightning lance.

---

## 2. Name hazards — never merge these

| | |
|---|---|
| **Silas** | Both a **PC** (half-orc wizard) *and* the name of **Guntrah's adoptive gnome father**. `guntrah.html` has had this since Session 0. The Session 2 transcript's worst confusion zone is the graduation scene with Guntrah's parents, where DM-as-Silas-the-father, player-Silas, and a `Silas:` speaker label are all live at once. Guntrah calls the PC **"Sil"** specifically to avoid using his father's name — established at the table 2026-08-20. |
| **Vrenn** (captive drow) vs. **Wren Halloway** | **NOW LIVE AND SEVERE.** Vrenn was spoken aloud constantly in Session 3 and the recording renders him as **Vren / Wren / Wrenn / Bren / Brenn / Brenna / Brennan / Brian / Dren / Renz / Run** — at least eleven spellings, several of them in the same paragraph. Correct every one of them to **Vrenn**. **Never merge him with Wren Halloway**, the founding-era student whose suppressed thesis the Ninth Thesis is built on; Halloway did not appear in Session 3 and any "Wren" in that transcript is the drow. |
| **Ledger** (Ninth Thesis operative, Mirabar) vs. actual ledgers | Osric Morne keeps real ledgers. Disambiguate every instance. *Did not arise in Session 2* — the transcript uses "audits", "his books", "a logbook", and never the bare word. |
| **Morvek** (lesser lich, runs the Thanatos site) vs. **Harthoon** (Orcus's vizier, one tier up) | **RENAMED TWICE on 2026-09-01, and MORVEK is settled.** Originally **Vrask** — retired because the old name carried an outside association every player at the table recognised. Briefly **Vrok** — retired the same day because it is a near-homophone of *vrock*, the Abyssal vulture demon, which could plausibly turn up in these very scenes. **None of the three was ever spoken in play**, so nothing needed retconning; any older doc using Vrask or Vrok means Morvek. Expect STT to render Morvek as "Morvec / Marvek / more vek". **Harthoon must not appear at all** — if he does, it is an error. Neither appeared in Session 2. |
| **Morvek** vs. **Vrenn** | Both belong to the same scene, so keep them straight: the captive drow is **Vrenn**, the lich who owns him is **Morvek**. The merge risk that existed under the Vr- names is resolved by this rename — different initial consonant, different vowel, different syllable count. |
| **Osric Morne** vs. **Silas** | See above — Osric was renamed *from* Silas Morne for exactly this reason. |
| **Master Jin** (NPC) vs. "Jin Frost" | "Jin Frost" is a player's miniature of another character. Not campaign canon. |

### Term hazards

armanite → "ammonite", "blight" · Thanatos → "Thanos" · plane shift → "plain shift"
· Dowe → "Dow / Doe" · Voss → "boss" · Senna → "Sienna" · Torvald Thatch →
"Thorvald / Thatcher" · Guntrah → "Gunther" · Tavian Stormnet → "Tavion / Storm Net".

**Ninth Thesis operative names** — six, spoken aloud for the first time whenever
Voss's contact list is actually handed over (deferred to Session 3, see §3):
Nyella Sarreth · Anselm Ferreck · Ledger · Huri Sibreldo · Lysandra Belaine ·
Emeric Vantt. Expect all six to be badly mangled on first utterance.

---

## 3. Rulings made during the Session 2 pass (2026-08-23)

| Question | DM's ruling |
|---|---|
| "Rosgaunt" | **New canon.** Silas the PC's hometown, as best the DM can tell. Spelling provisional. |
| Guntrah's adoptive mother's name | **Breena** — CONFIRMED 2026-08-24. `content/players/guntrah.html` has read Breena since Session 0; the DM's initial "let's go with Brynna" was given without that, and he confirmed Breena stands unless a player says otherwise. |
| The "Bad Semester" bond (Silas ↔ Tavian) | **The transcript is right and the data was wrong** (DM, 2026-08-24). Silas is the one who nearly left; Tavian talked him into staying. Corrected in `silas.html`, `tavian_stormnet.html`, and `session_zero_relationship_table.md`. |
| Ring Conferral staging | **The one place the authored data overrules the recording** (DM, 2026-08-24). The transcript shows an on-stage pick from a mixed-metal case; that was never the intent. Canon: selection is **private, before Commencement** (so nobody reads item text on a stage), the choice is **announced publicly at the conferral**, and bands stay **struck identical in gold**. What the transcript *does* settle: separate diplomas exist, conferred by a clerk. A worked example of the "present major conflicts for approval" rule paying off. |
| Holdar at the Conferral | He turned away **partly from embarrassment and partly from disgust** (DM, 2026-08-24) — not simple shame. Recorded in `prof_bram_holdar.html`, `guntrah.html`, and `session_2.html`. The target of the disgust is deliberately unpinned. |
| The Celestial trigger word | **Scrapped.** The DM changed the design at the table: the glyph fires on the package being **opened**, not on a spoken word. No trigger word is owed. `session_plan.json`'s open item is closed. |
| Voss's six-name contact list | **DELIVERED** — handed over with an explanation before the Session 3 recording started (DM, 2026-09-03). The party holds the prop. **It has still never been read out at the table**, and the six operatives stay `dm-only`, because a name and a city is all the party has. |
| Ollie | **Steel Defender** (Battle Smith subclass feature). |
| The drow's name | **Vrenn** — he simply never introduced himself. Expected to land in Session 3. Player-facing prose must say "the drow", not "Vrenn". |
| "blight" | **Not a garble.** Tito's own improvised word for one of the armanites, because the party never learned what they were. |
| The DC 20 CHA saves ("16, 9, 18, 19") | Numbers do not matter; **only the resulting action does.** Silas and Tavian were taken; Guntrah and Tito resisted and chose to follow. |
| "Professor Thatch" | **Garble.** Torvald is the groundskeeper, not a professor. |
| Tavian's fishing village | Unnamed for now. The DM lets players name their own backstory proper nouns. |

---

## 4. Speaker-attribution corrections (Session 2)

Every NPC is the DM. Beyond that, these specific labels are wrong in ways that
change meaning:

| Labelled | Actually | Why it matters |
|---|---|---|
| `Silas: Yeah, I didn't think I did.` (darkvision) | **Tito** | The satyr is the one without darkvision. As labelled, the wrong PC is blind in the Provisions back room. |
| `Guntrah: I'm resistant to cold.` | **DM, as the armanite** | The party's only piece of monster intel all session, and the reason Tito switched to acid damage. |
| `Silas: and then I got the scholarship to come to the academy…` | **Tavian** | Silas got in by **lottery**; Tavian by **scholarship**. Two distinct origin stories. |
| `Silas: No, rescued.` | **Tavian** | About the fishing village that took him in. |
| `DM: …but then I found my way to Professor Orvin.` | **Tavian** | A player's initiating action, not narration. |
| `Tavian: You do.` (re: Holdar in the crowd) | **DM** | |
| `Silas: Shop's gonna be fine.` / `Tito: I hope so.` / `Silas: Sure.` | **DM, as Guntrah's gnome parents** | See the Silas collision in §2. |
| `Tito: …he casts Wall of Stone.` | Tito narrating **Silas's** prepared action | |
| `Tavian: 2 19s.` | **Tito's** disadvantage roll | |
| `Guntrah: You gotta go.` | **DM, as the drow** | An echo of the DM's own line. |

**Confirmed correct and load-bearing:** `Tito: I am going to say, Thatch sent us.`
Torvald's name entered the Thanatos scene from a **player's** mouth, not the DM's,
and the drow answered "I don't know who that is." The design guardrail held.

---

## 5. Out-of-character noise — never treat as canon

Session Keeper (recording software) · Derek, Miles, Lynn (real players) ·
"Sarah and… Adamantine" (podcasters) · Jin Frost (a miniature) · Michael Bublé,
Van Wilder, Tony Soprano, Shaq, Rob Gronkowski, Scooby-Doo, Wonder Twins,
The Matrix, Bill Gates, Leia buns, Tarzan · "Phi Kappa Gamma Radiation Vape
Pride" (joke setup; Tito's straight answer was **Phi Beta Kappa**, status
undecided) · the DM's aside about a remote Claude Code session.

---

## 6. Session 3 ("Before Dawn") — pass of 2026-09-03

Route B was taken. The party left the plane the same night, and **Vrenn left with
them**. Full reconciliation in `content/sessions/session_3.html`.

### 6a. Proper-noun corrections — apply on sight

| Transcript renders it | Correct | Notes |
|---|---|---|
| Vren, Wren, Wrenn, Bren, Brenn, Brenna, Brennan, Brian, Dren, Renz, Run | **Vrenn** | Eleven-plus spellings, sometimes three in one exchange. See the hazard row in §2. |
| Morvec, Marvek, "more of X", "more vek" | **Morvek** | The DM spelled it out at the table (M-O-R-V-E-K), which is why it is right roughly half the time. |
| Bhaal Academy | **FAIL Academy** | Guntrah naming his own school. Not a Bhaalspawn reference and not canon. |
| COVID | **cover** | Twice: "we can't have this sort of COVID everywhere" and "a patch where there wasn't particularly a lot of COVID". |
| water costume, "3 costumes" | **waterskin** | Tito has three. The word "costume" also appears legitimately in his equipment list — disambiguate by context. |
| "he turned and left the office" | **left** | The armanite ran off across a plain. There is no office. |
| tailing fork | **tuning fork** | |
| Arcane Bolt | **Arcane Jolt** | Guntrah's Battle Smith feature. Self-corrected on the recording. |
| the Archangel | **Arcane Jolt** (again) | Same feature, worse garble, mid-damage-roll. |
| Cat Screen | **Cat's Grace** | Which is itself Tavian's shorthand for *enhance ability*. |
| Divine or Smite | **Divine Smite** | |
| Ring of Ram | **Ring of the Ram** | Tavian's graduation ring. |
| steel defendant | **Steel Defender** | Carried over from §1; still happening. |
| "Gun, Yuanti, and Ollie's turn" | **Guntrah** | There are no yuan-ti in this campaign. |
| Sliver | **Silas** | Once, during the miniatures scramble. |
| plain shift | **plane shift** | Carried over from §1. |
| "an elephant line" | *single file* | Colloquial, not an error. Leave it. |
| Mirthful Leaps | Correct as written | Genuine satyr trait. Not a garble. |
| Skill Empowerment | Correct as written | Vrenn offered it and it did not apply. Not a garble. |

### 6b. Rulings made during the Session 3 pass

| Question | Ruling |
|---|---|
| Vrenn leaving the plane | **The transcript wins and the locked design is superseded.** "He will not leave the plane" was authored; the DM ruled the opposite at the table, on the fiction. This is now canon and the consequence is the largest live thread in the campaign — see `mysteries/what_follows_vrenn.html`. |
| Why the Session 2 scroll failed | **Retconned in-fiction, deliberately.** Vrenn scribed it with his own magic quill, so only he could ever cast from it. Silas's natural 1 still happened mechanically; in-world it was never his fault. Keep the retcon — the player had been carrying it. |
| The heat rule | **Played version wins.** One waterskin drink per hour or a level of exhaustion; a waterskin is five hours' worth. No CON save, no DC. Simpler than the designed DC 7 and better at the table. |
| Artificer infusions | **Cap 4 active.** Guntrah was running seven; corrected mid-session. |
| Lending an attuned All-Purpose Tool | **Allowed.** Attunement stays with Guntrah; the tool holds its shape. |
| Flash of Genius and invisibility | **Does not break it.** Class feature, not a spell (2014). Must reach the target somehow — a whisper suffices. |
| *Enhance Ability* (Cat's Grace) and Stealth | **Grants advantage**, on the reading that Stealth is a Dexterity check. |
| Partial *invisibility* drop | **Not allowed.** A caster concentrating on one *invisibility* covering several targets drops it for the group or not at all. |
| Oni | **Run with truesight and necrotic claws**, neither of which is on the printed block. Both were witnessed by the party and are therefore canon for this campaign. |
| Guntrah's species | **Full orc, not half-orc.** Confirmed at the table. Carrying capacity 390 / 780. |
| Guntrah's languages | **Common and Abyssal.** Established as always having been true. |
| Guntrah's subclass | **RESOLVED (DM, 2026-09-03).** The player changed subclass early in the campaign and supplied a new export: **Artificer 10, Battle Smith.** Arcane Jolt, Battle Ready and the Steel Defender are all his by the book. `guntrah.html` rebuilt from the 2026-09-02 sheet; the Armorer/Guardian labelling is retired. Two knock-ons worth knowing: **Investigation is no longer proficient** (+5, passive 15, down from +9/19), **Insight is**, and his spell DC is **18** with attack **+10**. |
| Silas's familiar | **A hawk named Wind.** Ritual-only on his sheet; ruled precast at the start of each day from now on. |
| Literacy and Intelligence | **No minimum.** Tavian can read. |
| Vrenn's spell ceiling | **RESOLVED (DM, 2026-09-03).** No conflict: he normally holds **one 6th-level and one 7th-level slot**, and the 7th was **already spent** that day. 6th was his ceiling in that moment, not in general. |

### 6c. Speaker-attribution corrections (Session 3)

Every NPC is the DM, and in this session **the DM is Vrenn for most of the
running time** — a `DM:` label in the briefing scenes is dialogue, not narration.
Beyond that, these specific labels are wrong in ways that change meaning:

| Labelled | Actually | Why it matters |
|---|---|---|
| `Tito: Morvek.` / `Tito: he owns me.` | **DM, as Vrenn** | The lich's name and the ownership both come out of Vrenn's mouth, not a player's. Attributing them to Tito makes it look like the party already knew. |
| `Tavian: I do.` (re: reading Abyssal) | **Guntrah** | Guntrah is the Abyssal reader. Tavian's languages are Common, Common Sign Language and Orc. The whole following exchange is about Guntrah being a full orc who picked Abyssal. |
| `DM: Yes, I'm just wearing gear.` | **Guntrah** | The no-backpack discovery, which drives the whole water problem. |
| `DM: I got my boots, so if I need to, I can just fly across.` | **Guntrah** | |
| `DM: Perfect, I have disadvantage on stealth.` | **Tavian** | Plate mail. It is the reason Vrenn upcast *invisibility*. |
| `Tito: I have a dirty 20.` (basement stealth) | **Silas** | Silas rolled 20; Tito's own roll is separate. |
| `Tito: 6.` (Vrenn's Intelligence check on the circle) | **DM's roll** | Vrenn failing to understand his owner's teleporter is a characterisation beat, not a player roll. |
| `Tito: Um, he says, uh, what are you doing here?` | **DM, as the first oni** | The line that starts the basement scene. |
| `Tito: 10.` (death save) | **Silas** | Silas's second successful death save. |
| `Tavian: You got a 9.` | **Tavian**, reporting his own initiative | Reads as the DM addressing him. |
| `DM: I don't have any heals. I'm sorry.` | **DM, as Vrenn** | First thing he says to the party after the fight. |
| `DM: I'm gonna look up and go What is this place?` region | **Guntrah** | Several player actions in the ash-plain stretch are absorbed into `DM:` blocks. Attribute by scene. |

**Confirmed correct and load-bearing:** `Guntrah: Do you remember who the box was
meant for?` — the Thatch cross-check came from a **player's** mouth for the second
session running, and Vrenn's honest "I just wrote down the words I was given"
gave nothing away while handing the party a real data point.

### 6d. Out-of-character noise — never treat as canon

Derek, Miles, Russ (real players) · "Sarah and Malcolm" (podcasters, again) ·
ChatGPT and D&D Beyond consultations · the encumbrance and pint-volume arguments ·
Bud Light seltzers · Tito Jackson and the Jackson 5 · Winona Windhawks (a real
high-school mascot, and the source of the familiar's name — **"Wind" is canon,
"Winona" is not**) · the miniatures scramble · "Don't railroad us, Derek" ·
DCC unlimited inventory · Strahdcast and the Curse of Strahd familiar anecdote ·
"Primeval" (a bar) · the cat in the window reflection.

**Retired-party knowledge, flagged:** `Silas: I felt like I remember got potions
from Genie... because our other ones, that's when we had the thing.` This is the
**player** remembering a One Shots 1–5 character, not Silas. It is not ambient
fact and the new party has no potions. See the standing rule at the head of this
file.

---

## 7. Session 4 ("The Green Country") — pass of 2026-09-25

They arrived in Neverwinter Wood, worked out where they were without being told,
negotiated with an adult green dragon, killed two fomorians for 13 points of
damage to Tavian and nothing more (Evil Eye, natural 20, half of 27 — line
1451), and left with passage, a guide and no loot. **Vrenn is still with them
and is now cursed.** Full reconciliation in `content/sessions/session_4.html`.

### 7a. Proper-noun corrections — apply on sight

| Transcript renders it | Correct | Notes |
|---|---|---|
| Tendrovaxiliath | **Tedrovaxilliath** | One occurrence, and it is the only time the full name is said. The DM was reading his own prep, so treat as STT. *Flagged for confirmation — if the DM genuinely said "Tendrovaxiliath" at the table, that is what the players heard.* Irrelevant in practice: everyone calls him **Ted**. |
| Thax | Correct as written | **Not a garble.** A second short form the DM invented at the table and offered alongside "Ted". Canon. |
| Wrenn, Bren, Brenn, Vren, Prince | **Vrenn** | Same hazard as §6a, fewer variants this time. *"Prince"* appears once mid-argument ("At this point, Prince, he's our friend") and is a garble of his name, not a title. |
| Vrenn and Stimpy / Vren and stubby | — | In-joke, not a name. See §7d. |
| Fomorian Maxi / "they call him a Maxi" | — | Table joke about the mini's size. The creature is a **fomorian**. |
| Bhaal's Academy | **FAIL Academy** | Tavian naming his own school to a dragon. Same garble as §6a; still not a Bhaalspawn reference. |
| Miles, Russ, Derek, Christian | real players | Never canon. See §7d. |
| Blue Dream / Blue Pink | — | Out-of-character, not a place or item. See §7d. |
| Efficiency bonus | **proficiency bonus** | |
| Ring of Ram | **Ring of the Ram** | Carried over from §6a. |
| steel defendant | **Steel Defender** | Carried over from §1 and §6a. Still happening. |
| Holly, Bally, Wally, Bully | **Ollie** | Carried over. "Bully" is new this session. |
| Arcane Bolt | **Arcane Jolt** | Carried over from §6a. |
| plain shift / planar shift | **plane shift** | Carried over from §1. |
| "Guiding Light" | **Guiding Bolt** | Tavian's own slip, self-corrected. |
| "Psycho killer" | **Phantasmal Killer** | A joke, said immediately after the correct name. |
| "the box" (re: the fox) | **the fox** | Recurs several times during the Universal Speech scene. There is no box. |
| "Expecto Patronum" | ***light*** | Tito casting *light* on the steed. Joke, not a spell. |
| "Mr. Ed" / "Roach has 2 heads" | **Roach** | Mini-substitution jokes during the miniature scramble. The steed's name is **Roach**. |
| Clubby, Hunch, Hunty, Punch | — | **DM bookkeeping names for the two fomorians.** Never said in the fiction; the party never heard them. "Hunty"/"Punch" are garbles of Hunch. |
| Universal Speech | Correct as written | A genuine College of Eloquence feature. Not a garble. |
| Mirthful Leaps, Silver Tongue, Unsettling Words | Correct as written | All genuine Tito features. |
| Menzoberranzan | Correct as written | Came through cleanly all five times. |
| Drizzt Do'Urden, R.A. Salvatore, *Homeland* | real books | Out-of-character. See §7d. |

### 7b. Rulings made during the Session 4 pass

| Question | Ruling |
|---|---|
| **Morvek's *sending*** | **IT HAPPENED — it was simply never narrated (DM, confirmed 2026-09-25).** The 2026-09-23 design and the "option A" text both stand. Morvek cast *sending*; the table saw only Vrenn on his knees holding his head for 15–20 seconds, then *"Morvek knows."* Withholding the words is exactly what the prep called for, and the DM judged the conversation afterwards would make it evident. **A transcript-only reading gets this wrong** — nothing on the recording says "spell." **Corollary: Vrenn declining his right of reply is STILL UNSPENT**, because the party were never told he had one. |
| **Vrenn recognised the country and the cave** | **The transcript wins and the 2026-09-24 "plane shift is inaccurate, Vrenn is lost too" ruling is superseded in its second half.** He arrived not knowing where he was, then recognised the landscape on the walk north, and the Breach is the exact cave he escaped through. He is no longer a blank on local geography. |
| **The party identified Neverwinter Wood themselves** | **Allowed, and the prep instruction "do not let anyone identify it without being told" is retired.** Guntrah's flight above the canopy plus Silas's History 16, off the rivers and the mixed conifers. |
| **"Grave token" said out loud** | **Player knowledge now.** The standing instruction was not to use the words until somebody saw one. Vrenn used them unprompted. Nothing needs undoing. |
| **The Nine Hells are in the campaign** | **The transcript wins, and this reverses a locked decision (DM, 2026-08-29).** Vrenn explained that soul coins are real, are currency in the Hells, and that **Morvek went there personally, learned how they work, and invented grave tokens on that model.** The old rule was that nothing in this campaign touches the Nine Hells. **Flagged for a deliberate decision about how far that door now swings.** |
| **Nat 1s and nat 20s on ability checks** | **House rule adopted this session, both directions.** The DM already played it that way; Tavian and Tito agreed, Silas objected, it went in. |
| Silver Tongue vs. natural 1 | **Silver Tongue wins.** Any Persuasion or Deception d20 of 9 or lower counts as 10, so Tito cannot roll a natural 1 on either. Tito argued against his own feature for fun and lost on the rules. *It was never actually applied — his nat 1 would have succeeded on the modifier alone.* |
| *Leomund's Tiny Hut* and sound | **One-way: the party hear out, nothing hears in.** Ruled on the sneaky-purpose argument. **Note this is the opposite direction from the prep**, which was built on Ted negotiating *through* the dome. It never came up. |
| Tiny Hut size | **20 ft across (10 ft radius).** The table had it filed as much smaller. 11 minutes to cast as a ritual, everyone must be inside at the moment of casting, and others may come and go afterwards but not the caster. |
| All-Purpose Tool → telescope | **No.** Artisan's tools only; a telescope is adventuring gear. |
| Paralysed auto-crit | **Melee only.** Advantage for all attackers, auto-crit only within 5 ft. Caught and applied correctly mid-fight. |
| Frightened | **Disadvantage on attacks and ability checks, not saving throws**, and movement restricted only toward the source. Hunch could still hit whatever was in front of him. |
| Evil Eye's curse outliving its caster | **It persists.** Magical curse; killing the fomorian did not free Vrenn. Repeats the save only on finishing a long rest. |
| *Find steed* initiative | **Shares the paladin's count and may act at the same time as him**, not strictly after — explicitly contrasted with the Steel Defender, which does go after Guntrah. |
| Visibility from altitude | **About twelve miles from a hundred feet up.** Settled by table argument about the curvature of the earth. |
| Water after the long rest | **They are out, and must find fresh water.** A deliberate one-off carried over from the Abyss, resolved at the stream crossing. |
| Ring of the Ram recharge | **Rolled 1d6, got 1.** RAW is 1d3 at dawn, so the result stands either way. **Tavian's ring holds 1 charge.** |
| Proficiency bonus at level 11 | **Called at the table as +3 → +4. It was already +4 at level 10.** The sheets are correct and unchanged. Recorded only so nobody "fixes" them. |
| Two left ears = two creatures | **Allowed.** A left ear is distinguishable from a right one, so two lefts is proof of two kills. They then dropped them, because Ted had said he would know. |
| Distance to the Breach | **Six miles, per Ted at the table** — not the five in the prep — and the same figure as his stated territorial radius. The crossing was a stream rather than a river. |

### 7c. Speaker-attribution corrections (Session 4)

**This transcript is the worst of the four for attribution.** `Tito:` is used for
the DM's NPC voice throughout — *almost every line Tedrovaxilliath speaks is
labelled `Tito:`* — and several of the DM's narration lines are labelled with
player names. **Attribute by scene, never by label.**

| Labelled | Actually | Why it matters |
|---|---|---|
| `Tito:` for nearly all of Ted's dialogue | **DM, as Tedrovaxilliath** | Including *"Everything has a price"*, *"Tendrovaxiliath"*, *"Thax. You can call me Ted"*, *"I don't have patience for pleasantries"*, *"I owe nothing to you except to allow you to leave my forest alive"*, *"Because I can't fit in the hole"*, and *"Probably not."* **Every memorable line in the session is mislabelled this way.** |
| `DM:` through the whole Vrenn briefing, the dome conversation and the Grave Token story | **DM, as Vrenn** | Same hazard as §6c. A `DM:` label in those scenes is dialogue, not narration. |
| `DM: Uh, you know, I, I don't quite know…` (arrival) | **DM, as Vrenn** | The first thing Vrenn says on the new plane. |
| `DM: I, like I said, I came out of a cave.` | **DM, as Vrenn** | The Menzoberranzan escape. Load-bearing and easy to mistake for DM narration. |
| `DM: He had my sister.` / `DM: I traded myself for her, yes.` | **DM, as Vrenn** | The soul-sale. Attributing these to the DM makes them read as backstory exposition rather than a confession. |
| `Tito: Where am I from? I don't know.` | **Guntrah** | The unanswered question about where his character came from. |
| `Tito: 16.` (the Neverwinter Wood deduction) | **Silas** | Silas made the History check and told the party. Tito's roll (11) is separate and earlier. |
| `Silas: I mean, mine says Baldur's Gate for Acolyte.` | **Silas**, correctly | And it *is* on his sheet. The adjacent `Tito: Like I'm from Baldur's Gate` is a separate player musing aloud; **Tito's origin is undetermined.** |
| `Tito: Mountains, mountains, mountains.` and the map exchange | **mixed players + DM** | The whole map scene is attributionally scrambled and none of it is load-bearing. |
| `Tito: Hold the line, Spartans.` | **a player, out of character** | Table noise during the miniature scramble. |
| `Tavian: Gosh, there's countless demiplanes, but 27 major planes.` | **Tavian**, out of character | A player looking it up. **"27 major planes" is not a campaign fact.** The in-fiction answer the DM gave was *"at least a dozen"*, deliberately vague. |
| `Tito: I'm gonna be like, uh, I think we might have been there, but we're back now.` | **Guntrah** | The first answer to *"Who sent you?"* |
| `Tito: Correct.` / `Tito: Yes.` scattered through NPC dialogue | **whoever is in the scene** | Ubiquitous and harmless, but do not read them as Tito agreeing to things. |
| `Tito: Tito, we gotta talk our way out of this.` | **another player, addressing Tito** | Not Tito talking about himself in the third person. |
| `Guntrah: You guys don't think this game's kind of gay?` | **table noise** | Out of character, mid-miniature-scramble. Not a character line. |

**Confirmed correct and load-bearing:**

- `Guntrah: Mr. Dragon? What's your name, sir?` — **the politeness came from a
  player's mouth and it earned everything the party got.** Also his: the firewood
  request, the wing-brace offer, and every question that produced a straight
  answer out of Ted.
- `Tavian: We gotta, we gotta touch base with Dr. Voss.` — **the only time in four
  sessions a player has raised the Academy unprompted mid-adventure.**
- `Tavian: I'm not a smart man, but I'm pretty sure this is Milestone.` — the
  player correctly reading the campaign's own reward structure.
- `Tito: I will accept that deal for two beasts. However, if there is more than
  two, this deal will need to be renegotiated.` — **a player writing a contract
  clause, unprompted, and the dragon agreeing to it.**

### 7d. Out-of-character noise — never treat as canon

Derek, Miles, Russ, Christian (real players) · *Homeland* and the Legends of
Drizzt novels, R.A. Salvatore, and the flight to Portugal · the Eiffel bridge in
Porto and kids jumping off it · the Strait of Gibraltar / Morocco / curvature-of-
the-earth argument (it *produced* a ruling — twelve miles — but the geography is
real-world) · "Blue Pink" and tasting colours · D&D Beyond, Google and ChatGPT
consultations on Silver Tongue, telescopes and the paralysed condition · the
laminator and the eBay mini shopping ("I just searched for the word *huge*") ·
"this is AI slop and it did the grid not perfect squares" (the battle map) ·
plastic risers costing $8 · the entire miniature scramble, including "Expecto
Patronum", "Mr. Ed", "Roach has 2 heads", "Fomorian Maxi" and the GI Joe
comparison · "Vrenn and Stimpy" / "Vren and stubby" · Bijan Robinson's rushing
yards · iOS 27 and MacBook fan noise · the DM's wife and son in the background ·
"Alexa" as the dragon's name (a joke about the smart speaker listening) · "This
is not a smucker situation" (a passphrase in-joke, see CLAUDE.md) · "our next
party member is gonna be Ted" · Captain Planet rings · David cutting off body
parts (a retired-party in-joke) · "XP grinding" as a meta-discussion.

**Retired-party knowledge, flagged:** the DM's aside *"oh no, it was your other
characters that did the owlbear thing, wasn't it? So these characters wouldn't
know that then"* — caught and corrected in real time, which is exactly right.
**The owlbear cave is One Shot 4 and this party has never seen it.**

**A real open question surfaced and left unanswered:** *where the party members
are originally from.* Guntrah asked, the DM said the school is up in the High
Forest and *"I want to say you were down south somewhere"*, floated Triboar,
Guntrah said *"it was wherever the gnome shop was"*, and the DM concluded: *"if
it's not in any of the documentation, we probably don't have that."* **Silas is
Baldur's Gate via his Acolyte background. Guntrah, Tito and Tavian have no
recorded origin.** Worth one line each when their sheets are next touched.

---

## 8. Session 5 ("A Lie for a Lie") — pass of 2026-10-07

Played **2026-10-06** (DM, confirmed 2026-10-07). **They killed the dragon.** Ted
refused to let them leave, refused Vrenn's offer to stay in their place, and
breathed on them at the tree line. Vrenn caught him with *hold monster*, the
party turned round and fought against the DM's open warning, and five rounds
later Tito talked him to death with *phantasmal killer* while standing on 1 hit
point (line 2048). **Vrenn is cured, alive and still with them.** Tavian went
down and was brought back; nobody died. **The session ended in the clearing** —
the camp, the road, the drow and the credit note were never reached. Full
reconciliation in `content/sessions/session_5.html`.

*This pass began from a paste that was cut off at 50,000 characters, a third of
the way in, and a partial version of this section was written from that. This
one replaces it and was made from the whole file.*

### 8a. Proper-noun corrections — apply on sight

| Transcript renders it | Correct | Notes |
|---|---|---|
| Tedrovaxiliath | **Tedrovaxilliath** | Opening narration. Single-l garble, as in §7a. |
| Brenn, Bren, Wrenn, "friend" | **Vrenn** | Same hazard as §6a. *"Oh, friend did Hold Monster"* (line 669) is his name. **The DM corrected the table on the recording** — *"there's a V in his name, by the way"* (line 812). |
| "Vrenn or something like that" / "Vrenn?" | a guess at **Breena** | **NEW HAZARD, the reverse of §2's.** In the exchange about Guntrah's mother's name the recording wrote the drow's name over a misremembered "Brenna". It is not the drow. The table landed on **Silas and Breena**, which is what the data already says. |
| "Breena or Breena?" | *Breena or Brenna?* | The two candidates, rendered identically. |
| Gunn, Gun | **Guntrah** | His father's short form, and the table's. Not an error; leave it. |
| "I'll roll in front of Tavel" | in front of the **table** | **Not Professor Tavel.** He is nowhere near this session. |
| "which she gets +7", "She automatically fails" | **he** | The dragon. Ted is *he* throughout. |
| whole monster, whole monsters, whole person, told monster, Hold Dragon | ***hold monster*** | A dozen renderings. *Hold person* also appears correctly — Tito has it and it does not work on a dragon. |
| "you're weak of the Abyss" | **reek** of the Abyss | Ted. |
| "Luke, to your knowledge" | **Look**, to your knowledge | Not a player's name. |
| Ross | **Russ** | Silas's player. |
| Trolley, Aldi | **Ollie** | Two new ones for §1's list. |
| Mind Censor, Mind Smite, Divine Strikes | **Divine Smite** | Tavian hunting for it on his sheet. |
| "an auto divine hit" | **Improved Divine Smite** | The level-11 radiant d8 on every hit. |
| "Kenzie, 6 plus 40" | **10d6 plus 40** | *Disintegrate*. |
| "I had that rain" | I have that **ring** | Silas's Ring of Regeneration — 1d6 every ten minutes, far too slow to matter in a fight. |
| "wisdom save from SB17" | Wisdom save, **DC 17** | |
| "pony this", "pony him" | *pwn* | Guntrah. |
| "no transfers" | no **trancers** | Elves. |
| "Cards are so fun" | **Bards** are so fun | |
| "the dopest dragon" | the **dumbest** dragon | Tito, rehearsing the line he then shouted. |
| Eagle Eye | **Evil Eye** | Corrected by Tito on the recording. *"Eagle's Splendor"* immediately after is correct — it is the Charisma option of *enhance ability*. |
| "No, he has a sending stone" | he has the ***sending* spell** | About Silas, who answers Voss with his own head, not a stone. |
| "on his map" | on his **behalf** | Tavian, on killing a lich for Vrenn. Probable, not certain. |
| "Well, not half damage" | "Well, **no** — half damage" | Everybody had saved. |
| Ring of Ram | **Ring of the Ram** | Carried over from §6a. |
| Neverwinter Woods, Neverwinter Forest | **Neverwinter Wood** | The players' own wording; correct it outside direct quotes. |
| "Voss the boss" | Correct as written | A joke, not §2's Voss → "boss" hazard: Silas asked whether he knew Voss and was told *"Yeah, she's your boss."* |
| "Yeah, Witness, uh, you've done 195" | *unclear* | Line 1410. Probably "with this"; the sword is not being addressed. Elsewhere **Witness** is correct. |
| "a race of giant elves" | *unconfirmed* | The DM's on-the-spot gloss of where fomorians come from. Possibly a garble. **Do not promote it to lore without asking.** |
| Warlin | — | A miniature borrowed for Guntrah. Not a name in the fiction. |
| Unsettling Words, Harness Divine Power, Heroic Inspiration, Regain Bardic Inspiration | Correct as written | Genuine features. |

### 8b. Rulings made during the Session 5 pass

**Before the fight**

| Question | Ruling |
|---|---|
| Who Voss's *sending* reached | **Silas**, picked by a d4. Version A of the prep, read as written. The DM did not hold them to a count on the reply. |
| Why her first *sending* failed | **Still not known to the party.** Guntrah guessed *"because we weren't on the same plane"* and nobody corrected him. That *Tiny Hut* blocks *sending* stays DM-only. |
| The speaking stone | **Twenty-five words each way, once, then dead until the next dawn.** The back-and-forth the players remembered was a custom rule from the previous campaign and does not apply. |
| What the stone looks like | **Not a rock.** A rounded bronze ball with swirled engraving, steampunk, with a piece that extends and retracts — Guntrah's player's design, at the DM's invitation. An earlier line in the same exchange has it "go back to a rock"; the design a minute later supersedes it. |
| Magical Tinkering, fired from Ollie | **Allowed.** Three tinkered stones — **two light, one odour** — in a spring launcher fitted to the Steel Defender. The effect is fixed when the stone is made, not when it is fired. |
| Trance and keeping watch | *"When you're trancing, you're oblivious."* The DM's position, stated half in jest; nobody in the party trances. Vrenn does. |
| Ring of the Ram recharge | **All three charges back.** It held one. |
| Vrenn's Evil Eye save | **Passed: he is cured.** DC 14 Charisma (called as Constitution, then corrected). Dice 13 and 7, +3 from Tavian's aura, 16. Flash of Genius was not spent. |
| ***Enhance ability* on a saving throw** | **NOT ALLOWED — missed at the table (DM, 2026-10-07).** The spell gives advantage on ability *checks* only. Tavian's player said it covered the save and it was taken on trust. **The result stands; it is not a precedent.** The recording does not say which die came first, so whether it changed the outcome is unknown. |
| How Tavian knew what the curse was | **History 16 against DC 13.** A FAIL Academy lesson on common curses and maladies. |
| **Tito's Bardic Inspiration on his own rolls** | **NOT ALLOWED — missed at the table (DM, 2026-10-07).** The Deception against Ted and the save against the first breath, and offered again on the vine save. **All results stand.** For the record, the Deception was 24 without the die against roughly 29, and the breath save was carried by a Luck Point natural 20 regardless. |
| Tito's Deception of 33 | **He won the roll and not the argument.** The DM's reading at the table: it worked on Ted's vanity, not his belief. *"Perhaps I did. Regardless, you're not leaving this forest."* |
| Vrenn's offer to stay | **Refused.** Persuasion +0, rolled 3: *"That offer is no longer on the table."* The DM's aside: this was always the way out, the odds alone were poor, and nobody helped the roll. **This is where the prep's "Vrenn stays either way" stopped being true.** |
| *Vicious mockery* at a dragon nobody can see | **He may shout it; whether it lands is unknown to him.** Ted saved on a 17 and did not answer. **The words were a confession**: *"We did deceive you."* |
| Reading the situation | Insight 22 (natural 20), 22 and 18: **flee, do not fight.** Doubly so in his lair. Dragons have no inherent way to see the invisible, "to your knowledge". |
| The first breath | DC 18, sixteen dice rolled as 4d6 × 4 = 80. **Everyone saved, Vrenn included: 40 poison each.** It did not recharge on the next roll, "but you don't know that". |
| *Fireball* in the Wood | **No wildfire.** It clears a path about thirty feet wide and the going beyond it is still slow. |
| After the breath | **One action each.** Whoever cast *fireball* did not also get *cure wounds*. |
| *Haste* and difficult terrain | ***Haste* does not ignore it.** Tito's Ring of Free Action does. |
| Frightful Presence | **Nobody was frightened.** Tavian's aura makes everyone within ten feet immune, and the DM extended it to the group for the turn. Moot anyway: they were moving away from him. |

**The fight**

| Question | Ruling |
|---|---|
| **Vrenn's *hold monster*, and the die** | **It landed: 4 + 7 = 11 against DC 18.** Silas's player read the die as 18; the DM read 4 and said it must have shifted when he reached over (line 657). **It stands as a 4**, and the whole fight hangs on it. He rolled the second one in the open. |
| Whether to fight at all | **The players' decision, against a stated warning.** *"I don't want to kill everybody, I'm just putting that on the table"* (line 699). |
| Paralysed | Auto-fail on Strength and Dexterity saves; advantage for every attacker; **automatic crit within 5 feet only**, as in §7b. Constitution saves are not auto-failed. |
| Stacking *hold monster* | **No.** One paralysis, one save. The DM took D&D Beyond's answer as canon. |
| Readying a second *hold monster* | **Not the same caster against his own spell failing; a different caster may.** Silas could have held his action for the moment Vrenn's broke. If it never breaks, he has lost his turn. He did not take it. |
| Luck Points | **Decide after seeing the roll**, and they may be spent one after another on the same roll. Tito used three of his four. |
| Vrenn's top slot | **He will not spend the 7th.** *"That's his ticket out."* It is still unspent. |
| The lair's thorn vines | **Everyone standing in the trees: Dexterity save.** Fail, 9 damage and restrained; pass, 4 and free. **Breaking free costs an action and no roll**, and Tavian's extra *haste* action counts. They stopped once everybody was in the clearing. |
| The Steel Defender | **Its own saves, none of Guntrah's bonuses, and no bonus-action Dash.** The tracker gave it its own initiative by mistake; it shares Guntrah's. |
| Flash of Genius, late | **No.** Asked for after the table had moved on. Its range is 30 feet, and Guntrah was 45 up when Tavian needed it. |
| Unsettling Words | **Set as a bonus action before the save, and it applies to the creature's next save whatever that is.** The first one went on an auto-failed *fireball* save and was wasted. |
| A *fireball* past a dragon, through thirty feet of trees | **d20, 9 or better to land it clean**; otherwise it clips an ally. Silas's Sculpt Spells makes the roll unnecessary. |
| Two spells in one turn | **HOUSE RULE, stated as the DM's own: allowed, so long as one of them is 1st level or a cantrip.** Silas cast a 5th-level *fireball* and *false life* through Crumb's pouch. **This supersedes the note on the pouch's page**, which had it as cantrip only. |
| Ted's legendary actions | **After any turn, his own included.** The DM said outright that he is not on a standard block. Tail at +11 with a 15-foot reach; the wing attack costs two. The DM's own count afterwards: he used far fewer than he was owed. |
| The breath cone | **Sixty feet long and sixty across at the far end.** Who it caught the second time was a d6. |
| The second breath | **36.** Tavian (11) and Tito (4) failed; Ollie (22) saved for 18. **Tavian dropped. Tito's cape kept him at 1.** |
| *Phantasmal killer* | **Run with half damage on a successful save** (8 on Ted's natural 20). Its end-of-turn save was missed once and rolled late; Ted made it. |
| Disadvantage on the save against Silas's *hold monster* | **Claimed by the table and not owed** — *phantasmal killer* gives disadvantage on attacks and ability checks, not saves. Moot: both dice saved. |
| *Invisibility*, upcast | Touch, so **Vrenn and Silas only**. Silas's ended when he cast. |
| The *message* cantrip and invisibility | **It ended Vrenn's, but the dragon did not know where he was.** A cantrip is a spell; the table argued otherwise and the DM split the difference. |
| Healing in a fight | Worth it to bring somebody up from 0, not to go from 10 to 20. Nobody healed until it was over. |
| Taking the dragon apart | **Three minutes a wing**, and a few points of poison from the blood. |
| The glyph on Witness | **Lit as Tavian was brought round** — at once, not at the next dawn as the item reads. **The DM has not yet decided what it does**: *"I haven't programmed that yet."* What lit it is settled below. |
| The mist | **Gone from the clearing about ten minutes after he died.** The DM's next words, *"it's not from the dragon's death"* (line 2090), are ambiguous on the recording — see below. |

**Settled afterwards (DM, 2026-10-08)**

| Question | Ruling |
|---|---|
| *"It's not from the dragon's death"* (line 2090) | **Unknown and not important.** The DM reviewed the line and everything round it and could not place it. Dropped. |
| What lights a rune on Witness | **Each rune answers a particular paladin trait** — decided in the moment at the table. **The second was sacrifice.** Its effect is still undecided, and Tavian being Oath of Glory is to be kept in mind for the rest. |
| Is the dragon a level | **Yes. All four go to 12 at their next long rest.** Not yet said at the table. |
| Who sent Thatch's package | **Vrenn, both halves, on Morvek's instructions: he addressed it and he cast the spell that sent it.** *"Mailed that package"* (176) is exact and does not conflict with Session 3's "I just wrote down the words I was given". |

**Ted as he was actually run** — the DM's own block, *"a little bit of each"* of the
adult and the ancient: fly 40 (halved from 80 by the wing), 40 on foot, full
speed through his own undergrowth; eyes throughout the forest within six miles;
Wisdom save +7, Dexterity save +6, attacks +11; **AC 20 to 22** (a 19 missed, a
22 hit); breath DC 18, recharge 5–6; Frightful Presence at 120 feet. **He took
397 points of damage in five rounds and had between 366 and 390 hit points** —
not bloodied at 160, bloodied at 195, alive at 365. The ancient's 385 fits.

### 8c. Speaker-attribution corrections (Session 5)

**Ted's lines are labelled `Tito:` again**, as in §7c, and Vrenn is `DM:` throughout.
Attribute by scene.

| Labelled | Actually | Why it matters |
|---|---|---|
| `Tito: You said so. Several of you said so.` / `Tito: A lie for a lie.` | **DM, as Ted** | The line the session is named for (313). |
| `Tito: …the green dragon says, uh, that offer is no longer on the table.` | **DM, as Ted** | The refusal of Vrenn's offer (367). |
| `DM: You don't persist in this lie, do you?` and the Abyss questions after it | **DM, as Ted** | Dialogue, not narration. |
| `DM:` on the walk back, in Tavian's sidebar, and from "wait, wait, wait" | **DM, as Vrenn** | Includes *"I didn't have a choice… the caster has to go"*, *"I can't say I've ever had friends in my life"*, and ***"if I hadn't done what Morvek asked me to do and mailed that package"*** (176) — confirmed by the DM on 2026-10-08, see §8b. |
| `DM: This was always going to be the way out.` | **DM, out of character** | A design aside, not Ted and not Vrenn. |
| `Tavian: Yeah.` (after *"Do you say that out loud?"*) | **Tito** | Tito is the one who proposed leaving Vrenn with the dragon, aloud. Vrenn nodded. |
| `DM: Yeah, I never leave anyone behind.` / `DM: It would be glorious to kill a lich…` | **Tavian** | The Oath of Glory talking. |
| `DM: And also, I just said he's part of our crew…` | **Tavian**, then the DM out of character | Tavian's defence to Ted; the second half (*"I don't have the exact verbiage"*) is the DM. |
| `Silas: Yep, that's a 9.` | **Tavian's** Persuasion on Vrenn | Vrenn's answer was *"I'll think about it."* |
| `Tito: Um, you also get a message…` | **DM** | Introducing Guntrah's father on the stone. |
| `Silas: I'm assuming your tiny, tiny hut.` / `Silas: Again, do you want to?` | **DM**, asking Silas | |
| `DM: I mean, yeah, you guys heard of those?` | **Guntrah** | About sending stones. |
| `DM: What are you all doing?` / `Silas: Leave!` | **DM, as Vrenn**, both halves | Shouted at the party as they came back for him (1290). |
| `DM: …Tito, you're up. Okay, I'm gonna yell, spread out!` | second half is **Tito** | |
| `DM: Yeah, I have 29 hit points.` | **Tito** | Vrenn was on 23. |
| `Silas: 11.` / `Tito: 11 for Tavian.` (initiative) | **Tavian 11, Silas 15** | Order: Vrenn 20, Tito 18, Silas 15, Ted, Tavian 11, Guntrah and Ollie 7. |
| `DM: …the dragon falls over lifeless, and I instantly go over and do Cure Wounds on him.` | second half is **Guntrah** | On Tavian, for 17. |
| `DM:` through the last scene | **DM, as Vrenn** | *"I've spent my whole life running away from people to protect them"*, *"I have nothing left. Well, I have one thing left"*, *"he sent me a message the other day… He told me he was coming"* (2131), *"I stole a lot of components from that basement"*. |
| `DM: Still feel you're part of our crew.` | **Tavian** | |
| `DM: And your credit card. And he stole my identity.` | **players**, joking | Not Vrenn. |
| `DM: I don't know who that is.` | **DM, as Vrenn** | Answering a joke; see §8d. |

**Confirmed correct and load-bearing:**

- `Tito: No, but we can leave Vrenn here with the dragon.` — **the idea came from a
  player before it came from Vrenn.**
- `Tito: It was me that said it.` — Tito owning the "prisoner" lie in front of Ted,
  thirty seconds before lying to him again.
- `Tito: I will attempt to deceive this green dragon.`
- `Guntrah: Oh, right, because yesterday it failed because we weren't on the same
  plane, right?` — the party's working theory, and it is wrong.
- `Guntrah: Over here, you green bastard!` — said from the air, as bait.
- `Tito: Oh, we're staying and fighting.` · `Tavian: This sounds like a glorious
  moment.` · `Guntrah: If they go, I go.` — **turning back was the players' call**,
  all four of them, inside a minute.
- `Guntrah: I'll say, almost dead, we got this.` — **Vrenn offered to take them all
  out of the fight** (*"I have a way out… I'll get us out of here"*, line 1866)
  **and Guntrah turned him down** without telling the others.
- `Guntrah: So we're part of an order and there's people that can assist us.` —
  said to Vrenn. **His word, not the Academy's.**

### 8d. Out-of-character noise — never treat as canon

Derek, Miles, Russ, Christian and **Ben** (real players; Ben is new to these
recordings) · **"Derek Gibson… kind of an elder god, kind of controls this plane"**
— Guntrah's player naming the DM to Vrenn, who had not heard of him · the
Obi-Wan-and-Maul hut clip (*"Not exactly Leomund's Tiny Hut, but hey, same
energy"*) and "Isaac and Laskel", unidentified and part of the same joke · carbon
monoxide in the dome · Axe body spray as the odour stone · Australia · Stockholm
syndrome · Homer Simpson backing into the hedge · *"I'm the captain now"* ·
"bananas" seven times, padding out the twenty-five words · the miniature
scramble, "Warlin", and the missing risers (the 3D printers are at a nephew's;
sixteen dollars on Amazon) · the dragon-turtle mini · a trip to Michigan · a
"Dragon League" · ChatGPT and D&D Beyond consulted on stacking and concentration ·
Ant-Man in the dragon's stomach · Hogwarts and its animal teacher · *"I should
have just made you fight the ancient one"* · **"if we get a party wipe, we have a
backup campaign… we can just go right back to fucks"** — the One Shots campaign.

**Who is who, from being addressed by name on this recording:** Russ is Silas
(many times). Ben is Tavian and Christian is Tito, from the vine exchange at
lines 1148–1150, where the DM names who was caught. Miles is Guntrah by
elimination. *Treat the last three as probable.*

**Previous-campaign knowledge, flagged:**

- *"That was our old— my own custom Sending Stones from the previous campaign."*
  The DM catching a rule from another table before it became this one's.
- *"Dang, that's my first dragon."* / *"Dude, we had our first dragon a while back.
  First campaign. But that was a young one."* **The players, not the characters.**
  This party had never fought a dragon before this morning.

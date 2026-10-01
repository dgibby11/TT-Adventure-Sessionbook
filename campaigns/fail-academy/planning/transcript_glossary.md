# FAIL Academy — Session Transcript Glossary

Speech-to-text correction reference for reconciling recorded session transcripts
against live campaign data. Built during the **Session 2 ("Commencement",
played 2026-08-20)** reconciliation pass on 2026-08-23, and agreed with the DM
line by line before anything was written to live data. **Extended by the Session 3
("Before Dawn") pass on 2026-09-03** — see §6. **Extended again by the Session 4
("The Green Country") pass on 2026-09-25** — see §7.

Reuse this for every future transcript pass. Add to it rather than rewriting it —
each session's recording tends to mangle the same names the same way.

**Transcripts on file:** `planning/session_1_transcript.txt` (Session 1, played
2026-08-09) · `planning/session_2_transcript.txt` (Session 2, played 2026-08-20)
· `planning/session_3_transcript.txt` (Session 3, played 2026-09-02)
· `planning/session_4_transcript.txt` (Session 4, played 2026-09-24).

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
negotiated with an adult green dragon, killed two fomorians without taking a
scratch, and left with passage, a guide and no loot. **Vrenn is still with them
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

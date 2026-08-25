# FAIL Academy — Session Transcript Glossary

Speech-to-text correction reference for reconciling recorded session transcripts
against live campaign data. Built during the **Session 2 ("Commencement",
played 2026-08-20)** reconciliation pass on 2026-08-23, and agreed with the DM
line by line before anything was written to live data.

Reuse this for every future transcript pass. Add to it rather than rewriting it —
each session's recording tends to mangle the same names the same way.

**Transcripts on file:** `planning/session_1_transcript.txt` (Session 1, played
2026-08-09) · `planning/session_2_transcript.txt` (Session 2, played 2026-08-20).

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
| **Vrenn** (captive drow) vs. **Wren Halloway** | Renders as "wren / Bren / friend". **Never merge them.** Wren Halloway is the founding-era student whose suppressed thesis the Ninth Thesis is built on. Neither name appeared in the Session 2 transcript. |
| **Ledger** (Ninth Thesis operative, Mirabar) vs. actual ledgers | Osric Morne keeps real ledgers. Disambiguate every instance. *Did not arise in Session 2* — the transcript uses "audits", "his books", "a logbook", and never the bare word. |
| **Vrask** (lesser lich, runs the Thanatos site) vs. **Harthoon** (Orcus's vizier, one tier up) | Vrask renders as "Frask / Rask". **Harthoon must not appear at all** — if he does, it is an error. Neither appeared in Session 2. |
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
| Voss's six-name contact list | **Not given.** The DM forgot it; it will be handed over **retroactively at the top of Session 3**. Do not treat the operatives as revealed. |
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

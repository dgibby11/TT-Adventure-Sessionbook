# Player View Audit — FAIL Academy

_Working doc, 2026-08-14. NOT a live entity. Built by diffing `planning/session_1_transcript.txt`
(source of truth for what the party actually experienced) against `content/sessions/session_1.html`
and every entity reachable from it._

> **STATUS: APPLIED 2026-08-15.** Everything below has been executed against live data, with the
> transcript as the tiebreaker on every conflict. See "§H — What Was Actually Done" at the bottom
> for the change log, including two places where the audit's own recommendation was overridden by
> what the link scan turned up. Sections A–G are preserved as the original findings.

**Two independent gates control Player View:** an entity's authored `visibility`
(`player` vs `dm-only`) AND its runtime `revealed` flag. Session 1's `reveals[]` currently
lists: `silas`, `guntrah`, `tito`, `tavian_stormnet`, `commander_orvyn`, `viola_gossamer`,
`witness`, `standing_ovation`, `quick_components_pouch`, `ninth_thesis`, `high_forest`.
Most decisions below are about `reveals[]` and about **dm-only blocks inside player-visible
files**, not about flipping whole entities.

---

## A. Dr. Ellery Voss — approved for Player View, with vetting

`ellery_voss` is already `visibility: player`. Her file splits cleanly (player prose on top,
one dm-only block). Nothing needs flipping. But the outbound links need attention:

| Link from her file | Target visibility | Verdict |
|---|---|---|
| `fail_chamber` | player | OK |
| `jungle_site` | player | OK |
| `main_complex` | player | OK |
| `one_shot_3` | player | OK — prior party's session, already player-visible |
| `session_1` | dm-only | Currently unreachable; see §D |
| `teleportation_network` | **dm-only** | Link sits inside her dm-only block — OK as-is |
| `aldric_voss` | **dm-only** | Inside her dm-only block — OK as-is |
| `nerissa_voss` | **dm-only** | Inside her dm-only block — OK as-is |
| `ninth_thesis` | player | **See §E — this is the big one** |

**Lineage nuance you should know:** you said the players don't know her lineage, but the
transcript shows Voss told them directly (line ~269): *"I am loosely descended from one of
the founders of this academy. There has been a Voss in here in some capacity or another for
hundreds of years, and some of us have been in charge of leading the Ninth Thesis."*

So the party **does** know: she descends from *an unnamed founder*, Vosses have been at the
Academy for centuries, and Vosses have led the Ninth Thesis. They do **not** know: Nerissa's
name, that the line runs through Nerissa rather than Aldric, or anything about Wren Halloway.
Her current player-facing prose says none of this, so nothing needs adding — just don't treat
"lineage" as fully secret, because a chunk of it is now table canon.

---

## B. Osric Morne — approved for Player View, with vetting

`osric_morne` is already `visibility: player` and already well-split (player prose, then a
`DM Only — The Private Ledger` block holding the real secrets). Structurally this one is in
good shape.

**Player-safe as written:** role, appearance, gruffness, the ledger-as-sacred-document bit,
his three quotes, posted hours, reporting to Goldvein.

**Correctly gated already (leave dm-only):** the second ledger and all four anomaly entries,
his age (62), that he owns no weapons and has no powerful friends, his willingness to "lose"
a document, the One Shot 5 note, the Session 1 note.

**Judgment call for you:** the line *"a growing private suspicion that the Academy is not what
it presents itself to be"* sits in the **player-visible** Personality section. That's an
internal state no student could observe — I'd move it into the dm-only block. Also
`Species: Unclear — never confirms and nobody's dared ask twice` and `Age: Older` are written
as in-world-observable, so those are fine to keep public.

**Critical: he is NOT in Session 1's `reveals[]`, and shouldn't be.** The transcript has no
Provisions visit at all — the party never met him on screen. He's in `related[]` only.
Leave it that way.

Outbound links: `lenny_goldvein` (player, OK), `academy_provisions` (player, OK),
`one_shot_5` / `boots_of_elvenkind` (player, both inside his dm-only block, OK),
`session_1` (dm-only, see §D).

---

## C. Aldric Voss / Nerissa Voss — keep both dm-only

Matches your instruction and the existing founders convention.

- **`aldric_voss` — keep dm-only.** The players know only "one of the three founders, named on
  the memorial stones." That fact is already carried by `memorial_garden.html` and
  `academy_traditions.html`, both player-visible. His own entity holds the empty-tomb secret
  and the architectural-imprint material — all correctly gated.
- **`nerissa_voss` — keep dm-only.** Zero party knowledge, confirmed by the transcript.

**Known side effect:** any `[[aldric_voss]]` / `[[nerissa_voss]]` link a player encounters in
player-visible prose renders as a dead/broken click in Player View. That's an accepted cost of
the founders convention (Aldric already had this before this session's work) — flagging it so
it's a deliberate choice rather than a surprise.

---

## D. Session 1 itself — BLOCKED, do not flip to player yet

`session_1` is `visibility: dm-only`. The reboot notes say to flip it to `player` once played,
matching the archived One Shots. **Don't — not without edits first.** The transcript shows
several scripted scenes that did not happen, and publishing the file as-is would hand players
"canon" they never experienced.

### D1. Scenes in the file that did NOT happen at the table

1. **All four parting-gift vignettes.** The transcript opens mid-stream with *"after you guys
   receive your gifts, you receive a note to see Dr. Voss."* The three long read-aloud
   scenes — Orvyn's Aelrindel Dawnbringer story, Viola's stammering handoff, Crumb's
   speech — do **not** appear anywhere on record. Either they were played before recording
   started, or they were narrated away. **You need to confirm which.** This matters most for
   Orvyn's monologue: the entire Aelrindel backstory, the five runes, the oath, and the
   "come find me after graduation" hook are load-bearing for Tavian and for `witness`.
2. **"Torvald's Escort."** The file has Torvald walking them out to the Rangers Department and
   relaying Warden Ashgrove's tracking report. At the table (line ~457-478) Torvald was simply
   standing at the treeline, asked *"Did Voss send you?"*, said *"I'm gonna stay here if you
   don't mind, and good luck. You see that trail right there? Just follow that trail."* He did
   not escort them and did not relay anything.
3. **Warden Ashgrove never appeared or was named.** He's in `related[]` but never came up.
4. **The Rangers Department was never visited.** The bulette was "just to the south in the
   forest," and the fight happened in a burrow tunnel — not on the churned field beside the
   Rangers longhouse. The whole **"The Ground"** prompt (training course, jump posts,
   rope-and-log run, archery berm) is superseded; the existing dm-only "What Actually Happened"
   note already records this, but the player-facing prompt above it still describes the
   unplayed version.
5. **The bulette's appearance differs.** File: shell "bruised, almost black at the seams,
   threaded with hairline cracks." Table: purplish hue, streaking veins visible on rock-like
   skin, glittery dark-red blood, and a piece of skin sloughing off to reveal exposed muscle
   underneath.

### D2. Two names in the file the party never heard

These are the biggest publication risks:

- **Wren Halloway — never named.** The DM explicitly narrated *"and she doesn't mention who
  this she is that Voss is talking about."* The file gates her correctly behind a
  `DM Only — If They Ask` block, so `session_1.html` itself is fine. **But see §E** —
  `ninth_thesis.html` spills the whole story in player-visible prose.
- **Thornwick — never named.** The DM read the notes aloud as *"Small mark stamped on the
  underside. And then there's a logo that she has illustrated. I've seen that mark before,
  never once thought about where it came from."* No name spoken. The file's notes-handout
  blockquote names `[[thornwick_consortium|Thornwick Arcane Consortium]]` in
  **player-visible** prose. That has to be changed to a described-but-unnamed mark before
  this file goes player-facing. (The `voss_notes_handout` image entity is already `dm-only`,
  and the transcript shows the DM reading aloud rather than handing over the printed prop —
  worth confirming the players never physically received it.)

### D3. Recommended approach

Rather than flip `session_1` wholesale, rewrite the player-facing layer to match the
transcript — the file becomes the party's record of what happened, with the unplayed
design material either deleted or pushed into dm-only blocks. The existing
`What Actually Happened at the Table` note is a good start but it's a supplement, not a
correction; the prose above it still describes the planned version.

---

## E. `ninth_thesis` — HIGHEST-PRIORITY FIX

`ninth_thesis` is `visibility: player` **and is in Session 1's `reveals[]`.** So it's the one
entity from this session that would actually surface in Player View right now. Its
player-visible prose currently gives away substantially more than the table learned:

| In player-visible prose | Did the party learn it? |
|---|---|
| Founded by **Nerissa Voss**, first archivist, Aldric's younger sister | **No** |
| The full **Wren Halloway** story — her name, her thesis, why it was pulled | **No** |
| Ellery is "the latest in an unbroken line of Nerissa's Voss descendants" | Partly — they know Vosses have led it, not Nerissa specifically |
| ~a dozen active operatives, no roster, Voss is sole point of contact | **No** — she said only that operatives exist in several cities |
| The whole "Secret Society" rumor-bleed explanation + Brennan Ashcroft's Alumni Society | **No** — that's prior-party/One Shot 2 material |
| Founded "within the Academy's first several years" | **No** |
| Links out to `[[nerissa_voss]]` and `[[brennan_ashcroft]]`, both dm-only | Dead links in Player View |

**What the party actually knows about the Ninth Thesis after Session 1:**
- It's real, exclusive, operates in the shadows, and they'd heard of it as campus gossip before.
- Voss runs it and communicates with operatives daily.
- Operatives exist in **Neverwinter, Baldur's Gate, and Silverymoon** (see §F — this
  contradicts live lore).
- The name comes from the first graduating class of nine: nine theses were written, only
  **eight** are on display in the library.
- One of the nine wrote about secrets having power; that quote is what Voss's notes cite.
- The job: gather information, occasionally act on it, ~50 gp/week, contracts to follow.
- Discretion expected; no oath, no handshake, no signal.
- A Voss has led it for generations.

**Recommendation:** either pull `ninth_thesis` out of Session 1's `reveals[]` entirely, or
(better) restructure the file so the Origins/"Secret Society" sections move into dm-only and
the player-visible layer covers only the bullet list above.

---

## F. New table canon not yet recorded anywhere

Not visibility decisions — genuine continuity gaps, several of which conflict with live data.

**Conflicts with live data (need a ruling):**
1. **Operative cities.** Table: Neverwinter, **Baldur's Gate**, Silverymoon. Live lore
   (`ninth_thesis.html`, `session_1.html` debrief): Silverymoon and **Everlund**. Baldur's Gate
   is brand new and very far south; Everlund was never mentioned. This also touches Session 3
   planning, which assumes a Neverwinter operative.
2. **High Forest geography.** `high_forest.html` says "southwest of campus; nearest treeline
   approximately 1.5 hours overland travel." At the table the DM established the Academy is
   *inside* the forest — *"it's all the high forest in all directions... this area was cut out
   to establish the academy"* — with the treeline at the campus edge, reachable on foot in
   minutes. These can't both be true.

**New player-facing lore established at the table, currently unrecorded:**
3. A mythical tree with rumored healing properties, roughly **3 days south** in the High Forest.
4. A rumored **unicorn** sighting deeper in the forest; "mythological properties the deeper you go."
5. Only **8 of the 9** original theses are on display in the Old Library.
6. Bulettes prefer rocky/mountainous terrain — this one being in forest was itself unnatural
   (Voss flagged this as the significant detail, not the corruption).
7. **Voss explicitly refused to link the bulette to the three-incident pattern** — she logged
   it as a separate, unresolved category. Already captured in the dm-only note; worth surfacing
   in the player-facing record too, since the party argued about it on screen.
8. Party harvested **bulette scales** for geomancy components; Crumb named as a possible buyer.
9. **Tito's name is a campus nickname**, not his real name.
10. **Guntrah's Steel Defender**: ~4 ft, spherical/Pac-Man-shaped with arms and legs, blades,
    driven by an arcane crystal attuned to him.
11. **Guntrah has Boots of Flying** (self-infused, ~4 hours' flight) — used heavily in the fight.
12. Torvald is known to the party as *"the most knowledgeable person about what happens on
    these campus grounds"* and goes anywhere on campus unchallenged; relationship is casual
    greetings only, he doesn't know them by name.
13. Party's read: Torvald appears **not** involved in Ninth Thesis business.
14. Tito floated a **"subplot to overthrow the academy"** theory in character.
15. Torvald seen at ~50 ft talking quietly with an unidentified figure who walked away —
    already recorded.

---

## G. Everything else — spot-check summary

**Already correctly `player` + safely split, no action needed:** `torvald_thatch`,
`commander_orvyn`, `oswald_crumb`, `viola_gossamer`, `headmistress_dowe`, `academy_provisions`,
`campus_root`, `main_complex`, `founders_statue`, `memorial_garden`, `academy_traditions`,
`rangers`, `high_forest` (content-wise; see §F2 for the geography conflict),
the four PC entities, and the three parting-gift items.

**Correctly `dm-only`, leave alone:** `secret_society`, `garrick_nash`, `voss_notes_handout`,
`teleportation_network`, `underground_storage`, `eastern_wing`, `dead_hours`,
`the_upperclassmen`, `maren_duskhollow`, `isolde_orath`, `brennan_ashcroft`,
`oswald_crumb_statblock`, `occult_systems`, `founders_compass`, `founders_charter`,
`voss_keycard`, `voss_imprint`, `ritual_floor`, `restricted_floor`, `hidden_knowledge`,
`open_questions`, `academy_grounds_map`, `contraband_log`, `department_incident_log`.

**Worth a second look before any Player View publish:**
- `thornwick_consortium` is `visibility: player`. It's not in any `reveals[]`, so it shouldn't
  surface — but given the party has never heard the name, consider flipping it to `dm-only`
  as a belt-and-braces measure until they actually learn it.
- `academy_legends` (player) — the reboot already stripped the Lost Year / Golden Cohort
  sections. Worth one read-through to confirm nothing else in it presumes knowledge this
  party doesn't have.
- `party_overview` (player) — contains a full stat-block breakdown of all four PCs plus a
  dm-only party-notes block. Fine for a DM-facing dashboard; decide whether players should
  see each other's exact HP/AC/modifiers in Player View.

---

## H. What Was Actually Done (2026-08-15)

Rule applied throughout: **where the transcript speaks, it wins.** Where it's silent, existing
authored intent stands.

### Content reconciled to the transcript
- **`session_1.html` substantially rewritten.** Thornwick's name removed from the player-facing
  notes blockquote (now "here she has drawn the mark itself, carefully, in ink: a maker's stamp,
  no words," matching the DM's actual reading). "Torvald's Escort" replaced with **"Torvald at the
  Treeline"** using his real dialogue. Warden Ashgrove and the Rangers-longhouse/training-course
  battlefield removed entirely. Added: **"The Approach"** (the hour of bushwhacking, the blood
  trail, the burrow), **"The Ground — A Tunnel Fight"**, a corrected **"The Wrongness"** (purple
  hue, streaking veins over stone hide, glittering dark-red blood, sloughing plates), a new
  **"The Aftermath"** (devilish-not-possession read, Tito's Feywild comparison, the half-swallowed
  elk, the harvested scales, the level-10 gut-check and Guntrah's guilt), and a rewritten
  **"The Debrief"** carrying Voss's actual habitat objection and her verbatim refusal to fold the
  bulette into the pattern. The Ninth Thesis pitch now records what she actually said, including
  the 8-of-9 theses detail and her founder-descent admission. Hooks updated.
- **`high_forest.html`** — geography corrected: the Academy sits *inside* the forest with an
  artificial cut treeline on all sides, not 1.5 hours southwest of it. Added a **Deep Forest —
  Student Lore** section (the healing tree ~3 days south, the unicorn rumor) and a note on the
  quiet stretch south of campus.
- **`campus_root.html`** — location line and overview paragraph brought in line with the same
  correction. (Note: this supersedes "northern fringe of Silverymoon"; the transcript doesn't give
  Silverymoon a bearing, so none was invented — it now reads simply "near Silverymoon.")

### Visibility / reveals changes
- **`session_1`: `dm-only` → `player`**, category `Planning` → `Completed`, tags updated. Safe now
  that the prose matches what was played.
- **`session_1.reveals[]`** gained `ellery_voss`, `torvald_thatch`, `oswald_crumb`.
- **`session_1.related[]`** dropped `warden_ashgrove` and `rangers` (neither appeared), gained
  `old_library` (the theses display).
- **`thornwick_consortium`: `player` → `dm-only`.** See override note below.
- `aldric_voss`, `nerissa_voss` — unchanged, still `dm-only`, per instruction.

### Link-exposure fixes (player-visible prose that linked to, or named, dm-only material)
- **`ninth_thesis.html` restructured** — this was the biggest leak. Player-facing layer now carries
  only what Voss actually said at the table; Wren Halloway's name, Nerissa, the founding date, the
  operative count/roster, and the entire "Secret Society" explanation are now in three separate
  dm-only blocks. Operative cities corrected to the transcript's **Neverwinter / Baldur's Gate /
  Silverymoon** (Everlund retained dm-only as an unnamed-at-table operative, so no contradiction).
- **`founders_statue.html`** — the player-visible claim that the statue is "prominent in the Ninth
  Thesis's ritual geography" moved to dm-only. This mattered: it's Session 2's ceremony venue.
- **`artificers.html`** — the Thornwick-marked cabinet is now an unnamed maker's-stamp in player
  prose, with the identification gated. Improves the campaign: it's the same mark Voss drew, so
  Guntrah can *earn* the connection from his own department.
- **`tinkerer_dunn.html`** — his Thornwick gripes de-named in player prose; gated version notes he'll
  give up the name freely if asked point-blank, as a legitimate discovery route.
- **`campaign_overview.html`** — an authorial meta-note naming "Crumb's Thornwick arrangement" and
  "the true nature of the Ninth Thesis" was sitting in *player-visible* prose. Moved to dm-only.
- **`viola_gossamer.html`** — "Home access: The Green Room Curtain" fact removed from the public
  block; it linked to a dm-only entity and contradicted the file's own dm-only note that the
  curtain should stay background.
- **`osric_morne.html`** — "a growing private suspicion that the Academy is not what it presents
  itself to be" moved from public Personality into the private-ledger block (unobservable interior
  state).
- **`food_court.html`, `rogues.html`, `master_veris.html`** — Dead Hours references gated. `rogues`
  had it as a player-visible `<h3>` section heading, which advertised the secret outright.

### Broken references repaired
- `academy_traditions.html`: `prof_fenwick` → `prof_aldous_fenwick`
- `orc_warband.html`: `prof_oswald_crumb` → `oswald_crumb`
- Repo-wide `[[ ]]` integrity now verified clean; no `reveals[]` entry points at a dm-only entity.

### Two overrides of this audit's own recommendations
1. **§G suggested flipping `thornwick_consortium` to dm-only as "belt-and-braces."** The link scan
   showed it was load-bearing in three player-visible files, so the flip *required* the content
   fixes above first. It was still the right call — `thornwick_consortium.html`'s own dm-only note
   states the current party has "never heard of the Thornwick Arcane Consortium in any form" and
   that "nothing on this page should leak into Player View." The data contradicted the authored
   intent; the intent won.
2. **§D recommended treating the missing parting-gift vignettes as a blocker.** They were *not*
   cut. The transcript's own words — "after you guys receive your gifts" — confirm the gifts were
   received, and nothing contradicts the vignette text, so removing substantial authored content on
   the strength of an absence would have been wrong. Instead, a DM-only open question was added to
   `session_1.html` flagging that Tavian may be missing Witness's backstory if those scenes were
   never performed.

### Still open (pre-existing, deliberately untouched)
- Player-visible prose still linking to dm-only entities, all prior-party or system-reference
  material rather than current-party leaks: `academy_legends`, `campus_cats`, `campus_ravens`,
  `magical_gauntlet`, `one_shot_1` → `underground_storage`; `one_shot_1`/`dnd_resources` →
  `bodak`, `mimics`; `one_shot_2` → `secret_society`; `one_shot_4` → `the_upperclassmen`;
  `one_shot_5` → `dust_mephit`, `earth_elemental`, `shield_of_missile_attraction`;
  `captain_hadra` → `contraband_log`. The root question is whether One-Shot-era creatures and
  locations should be `dm-only` at all when the sessions describing them are `player` — a design
  call, not a bug.
- `barbarians`, `druids`, and `maren_duskhollow` all list a `campus_wildlife` entity in
  `related[]` that does not exist. Possibly superseded by `campus_cats` / `campus_ravens`.
- `party_overview` (player) exposes every PC's exact HP/AC/modifiers — fine for a DM dashboard,
  a deliberate choice for Player View.

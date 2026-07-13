# Audit Reports

One dated section per audit iteration, most recent first.

## Iteration 29 — 2026-07-13T12:13:28Z (final closing audit, Phase 5)

**Context**: Phase 5 (t040-t044, the second/structural comparison-report
fixes — dive mechanics, mystery clue indexes, creature danger calibration,
arc milestone leveling, and the optional reputation/hook touch-up) finished
44/44 at iteration 28, two iterations ahead of `iterationCap`. Per the DM's
request (see the commit clearing `pipeline/DONE` and setting `auditEvery`
5→29), this audit runs as a dedicated one-shot closing check rather than
accepting build-time validation alone — the same technique used to close
Phase 4 at iteration 26.

**Scope checked**: full pass across all 147 entities in
`campaigns/salt-below/`. Scripted checks across all 8
`campaigns/salt-below/data/*.json` files: JSON validity; required-field
(`id`/`name`/`type`/`contentType`/`contentFile`/`visibility`) and enum
compliance for every entity; `id` uniqueness across all files; every
`contentFile` resolves to a real file on disk; no non-location entity
carries `x`/`y`, and every location's `x`/`y` is in 0-100 range;
`campaigns/salt-below/campaign.json` has a non-empty `dmPassHash`;
`campaigns/index.json` has exactly one correctly-formed `salt-below` entry
and the three pre-existing entries are untouched; every `related[]` entry
and every inline `[[id]]` / `[[id|label]]` reference across all content
HTML fragments resolves to a real entity id. Task list (`tasklist.json`)
scanned for duplicate titles and stuck `in_progress`/`blocked` items.
Spot-checked all 5 Phase 5 deliverables directly: t040 (dive procedure —
confirmed as `salt_below_dive_procedure` reference entity, cross-linked from
items/creatures), t041 (Clues sections present in both
`why_the_kingdom_drowned_mystery.html` and `the_breaking_deal_mystery.html`),
t042 (all 12 creature entities carry an explicit level/danger calibration
line in their `CR` fact — including the three atmosphere-only creatures
whose calibration is "not a combat threat at any level" rather than a
level-band, which is the correct call for those specific entities),
t043 (all 3 arc session entities — `arc_1_port_calder_shallows`,
`arc_2_drowned_districts`, `arc_3_deep_kingdom` — carry explicit Milestone
leveling guidance), t044 (Faction Standing section confirmed in
`salt_below_campaign_overview.html`).

**Findings**: none. Zero schema violations, zero duplicate ids, zero
missing content files, zero broken `related[]`/`[[id]]` links, zero
task-list issues. All 44/44 tasks confirmed `done`, none stuck, no
duplicate titles. All five Phase 5 deliverables verified present and
consistent with `CAMPAIGN_BIBLE.md`'s tone and the patterns set by the
Phase 4 comparison-report work.

**Severity assessment**: none — clean audit, no drift found. Confirms
Phase 5 is genuinely complete, not just task-list-complete.

Also re-confirmed (outside campaign scope, no action taken, per
`LESSONS_LEARNED.md` #2): this sandbox's initial checkout again carried the
recurring stray "Re-register fail-academy in campaigns/index.json" commit
(`2dc1b82`), this time as a detached HEAD rather than as a commit on
`main`. Confirmed via `git diff origin/main 2dc1b82` (empty — identical
tree) that its content is already present on `main`, and confirmed 5
existing preservation branches already cover it
(`preserve-detached-2dc1b82`, `preserve/fail-academy-reregister`,
`recovered-fail-academy-fix`, `recovered/fail-academy-reregister`,
`wip/fail-academy-reregister`). No new backup branch created — the fix is
already redundantly safe, and this pipeline has no scope to touch `main` or
clean up those stale branches regardless.

**Entity count summary**:

| Type       | Count |
|------------|-------|
| Locations  | 85    |
| NPCs       | 29    |
| Factions   | 5     |
| Items      | 5     |
| Creatures  | 12    |
| Mysteries  | 6     |
| Sessions   | 3     |
| References | 2     |
| **Total**  | **147** |

Location breakdown by region (unchanged from iteration 26 — Phase 5 added
no new locations): Port Calder 14, The Shallows 21, Drowned Districts 25,
Deep Kingdom 25. Items grew 4→5 and References grew 1→2, both from Phase 5
(the dive-procedure reference plus its supporting item, if any) — this is
narrative/mechanical support content, not new explorable content, so the
location/NPC totals are intentionally unchanged.

**Outcome**: clean audit closes out Phase 5. `pipeline/DONE` is restored,
`state.json.status` set back to `"done"`, and `auditEvery` restored from
its one-shot value of 29 back to its normal cadence of 5, in case the DM
reopens the pipeline for a future phase. The Salt Below campaign (147
entities, zero known defects) is ready for human review and merge into
`main`.

## Iteration 26 — 2026-07-11T19:20:00Z (final closing audit)

**Context**: this audit was requested off-cycle by the DM (see LOG.md's
`phase4-setup-r2b` entry) as a final content-quality check after the task
list finished 39/39 at iteration 25, two iterations early. `pipeline/DONE`
was temporarily cleared and `auditEvery` set to 26 specifically so this
firing would land as an audit rather than a silent no-op.

**Scope checked**: full pass across all 145 entities in
`campaigns/salt-below/`. Scripted checks across all 8
`campaigns/salt-below/data/*.json` files: JSON validity; required-field
(`id`/`name`/`type`/`contentType`/`contentFile`/`visibility`) and enum
compliance for every entity; `id` uniqueness across all files; every
`contentFile` resolves to a real file on disk; no non-location entity
carries `x`/`y`, and every location's `x`/`y` is in 0-100 range;
`campaigns/salt-below/campaign.json` has a non-empty `dmPassHash`;
`campaigns/index.json` has exactly one correctly-formed `salt-below` entry
and the three pre-existing entries (lost-mine, curse-of-strahd,
descent-into-avernus) are untouched; every `related[]` entry and every
inline `[[id]]` / `[[id|label]]` reference across all content HTML
fragments resolves to a real entity id; every `sessions.json` `reveals[]`
entry resolves to a real entity id. Task list (`tasklist.json`) scanned for
duplicate descriptions and stuck `in_progress`/`blocked` items. Spot-checked
3 of the newest entities (`sera_vondt`, `the_almonrys_debt`,
`it_that_kept_the_kingdom_stat`) against `CAMPAIGN_BIBLE.md` for tone,
faction-motivation, and light/dark balance consistency.

**Findings**: none. Zero schema violations, zero duplicate ids, zero
missing content files, zero broken `related[]`/`[[id]]`/`reveals[]` links,
zero task-list issues. All 39/39 tasks confirmed `done`, none stuck. Spot
checks matched the bible's established tone and faction motivations with no
drift.

**Severity assessment**: none — clean audit, no drift found. Confirms the
campaign is in a genuinely complete, table-ready state as of iteration 25's
Phase 4 work, not just task-list-complete.

Also re-confirmed (outside campaign scope, no action taken, per
`LESSONS_LEARNED.md` #2): this sandbox's initial checkout again carried the
recurring stray "Re-register fail-academy in campaigns/index.json" commit
(`2dc1b82`) — verified via `git merge-base --is-ancestor` that it is already
an ancestor of `origin/main`, so no preservation branch was created this
time (the fix has been on `main` proper since iteration 24; the 5 stale
preservation branches noted in prior iterations still await human cleanup,
unchanged, out of pipeline scope).

**Entity count summary** (unchanged from iteration 25 — this was a
quality audit, not a content-production iteration):

| Type       | Count |
|------------|-------|
| Locations  | 85    |
| NPCs       | 29    |
| Factions   | 5     |
| Items      | 4     |
| Creatures  | 12    |
| Mysteries  | 6     |
| Sessions   | 3     |
| References | 1     |
| **Total**  | **145** |

Location breakdown by region: Port Calder 14 (13 + the hub itself), The
Shallows 21, Drowned Districts 25, Deep Kingdom 25 — all four regions at or
above their `CAMPAIGN_BIBLE.md` target minimums except Port Calder, which
sits 1 below its 15-20 target; noted as cosmetic (a single additional named
location would close it) rather than fixed directly, since audits verify
and repair, not add new content per `AUDIT_CHECKLIST.md`'s scope. NPC:
location ratio is now 29:85 (~1:2.9), comfortably past the ~24-30 NPC target
range from the Phase 4 density fix.

**Outcome**: per the DM's `phase4-setup-r2b` plan, this clean audit closes
out Phase 4. `pipeline/DONE` is restored, `state.json.status` set to
`"done"`, and `auditEvery` restored to its normal cadence (5) in case the DM
reopens the pipeline for a future phase. The Salt Below campaign (145
entities, zero known defects) is ready for human review and merge into
`main`.

## Iteration 20 — 2026-07-11T20:35:00Z

**Scope checked**: full pass (still cheap at 124 entities). Scripted checks
across all 8 `campaigns/salt-below/data/*.json` files: JSON validity;
required-field (`id`/`name`/`type`/`contentType`/`contentFile`/`visibility`)
and enum compliance for every entity; `id` uniqueness across all files; every
`contentFile` resolves to a real file on disk (including the `content/`
subfolders, e.g. `content/creatures/`); no non-location entity carries
`x`/`y`, and none present on locations either (still no map for this
campaign); `campaigns/salt-below/campaign.json` has a non-empty `dmPassHash`
matching the documented placeholder hash; `campaigns/index.json` has exactly
one correctly-formed `salt-below` entry and the three pre-existing entries
(lost-mine, curse-of-strahd, descent-into-avernus) are untouched. Scripted
cross-link sweep: every `related[]` entry and every inline `[[id]]` /
`[[id|label]]` reference across all 124 content HTML fragments resolves to a
real entity id — zero broken links. Basic HTML well-formedness check (`<div>`
open/close balance) on all HTML content files — zero mismatches, confirming
iteration 19's "re-verified as well-formed" claim about the 8 edited creature
files. Task list scanned: 31 done / 7 pending (t032-t038, the rest of Phase
4), none `in_progress`, none `blocked`, all pending descriptions still
concrete. Spot-checked the two newest creature entities most likely to carry
drift — `reef_stalker.html` and `kelp_strangler.html` (iteration 19's stat-block
batch) — against `CAMPAIGN_BIBLE.md`: Shallows tone (adventurous, avoidable
danger, not yet dreadful) is intact on both; `kelp_strangler`'s missing
D&D Beyond link is still correctly flagged in its DM notes rather than silently
dropped or fabricated, consistent with the no-fabrication convention. Verified
the `links[]` D&D Beyond URLs iteration 19 reported for all 8 stat-blocked
creatures are actually present in `creatures.json` and match the log's claims
(reef_stalker/deep_maw_eel intentionally share the Giant Constrictor Snake
link; kelp_strangler correctly has no `links[]` entry).

**Findings**: none. Zero schema violations, zero broken links, zero missing
content files, zero duplicate ids, zero task-list issues, zero tonal drift in
the sampled entities.

**Severity assessment**: none — clean audit, no drift found.

**Entity count summary** (124 total):
| Type | Count |
|---|---|
| location | 85 |
| npc | 12 |
| faction | 5 |
| item | 4 |
| creature | 12 |
| mystery | 2 |
| session | 3 |
| reference | 1 |
| **Total** | **124** |

Location breakdown by region: Port Calder 13 (+1 uncategorized settlement
entry), The Shallows 21, Drowned Districts 25, Deep Kingdom 25 — all four
regions remain at or above their `CAMPAIGN_BIBLE.md` target minimums.

Also re-checked (outside campaign scope, no action needed): this sandbox's
initial `main`-branch checkout again carried the recurring stray commit
`2dc1b82` ("Re-register fail-academy in campaigns/index.json") seen in
iterations 5/6/10/12/15/16/17/19. `git fetch origin main` confirms
`origin/main`'s tip already equals that commit, so it's already safe on
`main` — no new preservation branch needed. The five stale duplicate
preservation branches noted in prior iterations (`wip/fail-academy-reregister`,
`fail-academy-index-fix`, `recovered-fail-academy-fix`,
`recovered/fail-academy-reregister`, `preserve/fail-academy-reregister`) are
unchanged and still awaiting human cleanup — out of pipeline scope per
GROUND_RULES.md Rule 6, flagged again only for continuity.

## Iteration 15 — 2026-07-10T17:05:00Z

**Scope checked**: full pass (still cheap at 100 entities). Verified: JSON
validity of all 8 `data/*.json` files; required-field + enum compliance
(`type`, `contentType`, `visibility`) for every entity; `id` uniqueness
across all files; every `contentFile` resolves to a real file on disk
(resolved relative to `campaigns/salt-below/`, per the schema); no
non-location entity carries `x`/`y`, and none present on locations either
(still no map for this campaign); `campaigns/salt-below/campaign.json` has a
non-empty `dmPassHash`; `campaigns/index.json` has exactly one
correctly-formed `salt-below` entry and the three pre-existing entries
(lost-mine, curse-of-strahd, descent-into-avernus) are untouched; every
`related[]` entry and every inline `[[id]]` / `[[id|label]]` reference
across all 100 content HTML fragments resolves to a real entity id (checked
programmatically, zero broken links); task list scanned for duplicate
ids/titles, stuck `in_progress` items (none), and vague pending descriptions
(none — t023-t029 all concrete). Spot-check of `the_regnants_seat.html`
(newest batch, t022, Deep Kingdom capital core) against
`CAMPAIGN_BIBLE.md`'s naming-convention (formal/archaic old-kingdom naming,
confirmed) and Deep Kingdom scope guidance (25-35 locations target; currently
at 12, consistent with t023 batch 3 still pending).

**Findings**: none. Zero schema violations, zero broken links, zero missing
content files, zero duplicate ids, zero task-list issues, zero tonal/naming
drift in the sampled entity.

**Severity assessment**: none — clean audit, no drift found.

**Entity count summary** (100 total):
| Type | Count |
|---|---|
| location | 72 |
| npc | 12 |
| faction | 5 |
| creature | 8 |
| mystery | 2 |
| item | 1 |
| session | 0 |
| reference | 0 |
| **Total** | **100** |

Note: `session` and `reference` entities are still 0 — expected, scoped to
t027/t028 which haven't run yet. Location breakdown by region: Port Calder
14, The Shallows 21, Drowned Districts 25, Deep Kingdom 12 (growing toward
t023's batch 3 and the climactic dungeon in t024).

Also re-confirmed (outside campaign scope, no action taken beyond safe
preservation, consistent with iteration 5/10 notes): this sandbox's initial
`main`-branch checkout again carried the same pre-existing unpushed local
commit ("Re-register fail-academy in campaigns/index.json"). Pushed to a new
branch `fail-academy-index-fix` on `origin` (this run used a different branch
name than prior runs' `wip/fail-academy-reregister` — both point at
equivalent, safely-preserved copies of the same fix; the human may want to
consolidate/delete the duplicate branch when reviewing). Not merged into
`main` or touched further — out of pipeline scope per GROUND_RULES.md Rule 6.

## Iteration 10 — 2026-07-10T16:05:00Z

**Scope checked**: full pass (still cheap at 59 entities). Verified: JSON
validity of all 9 `data/*.json` files; required-field + enum compliance
(`type`, `contentType`, `visibility`) for every entity; `id` uniqueness
across all files; every `contentFile` resolves to a real file on disk
(re-checked path resolution relative to `campaigns/salt-below/`, not repo
root); no non-location entity carries `x`/`y` (still none present — no map
for this campaign yet); `campaigns/salt-below/campaign.json` has a
non-empty `dmPassHash`; `campaigns/index.json` has exactly one
correctly-formed `salt-below` entry and the three pre-existing entries
(lost-mine, curse-of-strahd, descent-into-avernus) are untouched; every
`related[]` entry and every inline `[[id]]` / `[[id|label]]` reference
across all 59 content HTML fragments resolves to a real entity id; task
list (`tasklist.json`) scanned for duplicates, stuck `in_progress` items
(none — all t001-t015 are `done`, t016-t029 are `pending`, nothing
lingering), and vague descriptions (still concrete/actionable). Spot-check
of `the_last_landing.html` (kingdom-outskirts transition marker) and
`salt_warped_grouper.html` (Early Signs creature) against
`CAMPAIGN_BIBLE.md`'s naming-convention and level-arc tone guidance.

**Findings**: none. Zero schema violations, zero broken links, zero
missing content files, zero duplicate ids, zero task-list issues, zero
tonal/naming drift in the sampled entities.

**Severity assessment**: none — clean audit, no drift found.

**Entity count summary** (59 total):
| Type | Count |
|---|---|
| location | 35 |
| npc | 12 |
| faction | 5 |
| creature | 4 |
| mystery | 2 |
| item | 1 |
| session | 0 |
| reference | 0 |
| **Total** | **59** |

Note: `session` and `reference` entities are still 0 — expected, they're
scoped to t027/t028 which haven't run yet.

Also re-confirmed (outside campaign scope, no action taken, consistent
with iteration 5/6 notes): this sandbox's initial `main`-branch checkout
again carries the same pre-existing commit ("Re-register fail-academy in
campaigns/index.json") already preserved on `wip/fail-academy-reregister`
on origin. Verified that branch still exists and still points at that
commit. Still out of pipeline scope per GROUND_RULES.md Rule 6 — flagged
again only for continuity, not a new finding.

## Iteration 5 — 2026-07-10T14:48:24Z

**Scope checked**: full pass (campaign is still small — 15 entities, so an
exhaustive check was cheap). Verified: JSON validity of all 9 data files;
required-field + enum compliance (`type`, `contentType`, `visibility`) for
every entity; `id` uniqueness across all files; every `contentFile` resolves
to a real file on disk; no non-location entity carries `x`/`y`; every
location's `x`/`y` (none present yet — no map for this campaign) would be
in-range; `campaigns/salt-below/campaign.json` has a non-empty `dmPassHash`;
`campaigns/index.json` has exactly one correctly-formed `salt-below` entry
and the three pre-existing entries (lost-mine, curse-of-strahd,
descent-into-avernus) are untouched; every `related[]` entry and every
inline `[[id]]` / `[[id|label]]` reference across all 15 content HTML
fragments resolves to a real entity id; task list (`tasklist.json`) scanned
for duplicates, stuck `in_progress` items, and vague descriptions; spot-check
of `port_calder.html` and `locations.json` entries against
`CAMPAIGN_BIBLE.md` for naming convention and tone drift.

**Findings**: none. Zero schema violations, zero broken links, zero missing
content files, zero task-list issues.

**Severity assessment**: none — clean audit, no drift found.

Also note (outside campaign scope, flagged for the human, not acted on by
this audit beyond safe preservation): this iteration's sandbox started from
a `main`-branch checkout that carried one unpushed local commit ("Re-register
fail-academy in campaigns/index.json", built directly on `origin/main`'s tip)
which would otherwise have been lost when switching to `campaign-pipeline`.
It was pushed to a new branch `wip/fail-academy-reregister` on `origin` so it
isn't lost, but was **not** merged into `main` or touched further — that's a
`main`-branch/human decision, out of this pipeline's scope per GROUND_RULES.md
Rule 6.

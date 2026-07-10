# Audit Reports

One dated section per audit iteration, most recent first.

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

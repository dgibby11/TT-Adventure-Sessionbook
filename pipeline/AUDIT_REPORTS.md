# Audit Reports

One dated section per audit iteration, most recent first.

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

# Audit Checklist

Run this instead of a normal build iteration whenever RUN_PROTOCOL.md
determines the current iteration is an AUDIT. Audits verify and repair; they
do not add new locations/NPCs/items/etc.

## Schema & data integrity
- Every `data/*.json` file in `campaigns/<slug>/` parses as valid JSON.
- Every entity has all required fields per `CLAUDE.md`'s locked schema
  (`id`, `name`, `type`, `contentType`, `contentFile`, `visibility`) and field
  values match the allowed enums (`type`, `contentType`, `visibility`).
- Every `id` is unique within this campaign.
- Every entity's `contentFile` path actually exists on disk.
- Only `type:"location"` entities have `x`/`y`; if present, both are numbers
  in a sane 0-100 range.
- `campaigns/<slug>/campaign.json` has a non-empty `dmPassHash`.
- `campaigns/index.json` has exactly one entry for this campaign, correctly
  formed, and no other entries were touched.

## Cross-link integrity
- Every `related` array entry and every `[[id]]` / `[[id|label]]` reference
  inside content HTML resolves to a real entity `id` in this campaign. Fix
  obvious typos directly (e.g. off-by-one-character id mismatches); for
  anything ambiguous, leave it and add a task noting the broken link instead
  of guessing.

## Consistency with the bible
- Spot-check a handful of recently-added entities (not all of them — audits
  should stay fast) against `pipeline/CAMPAIGN_BIBLE.md`: names, tone, faction
  motivations, and geography should not contradict what's already established.
  Fix small drift directly; if something looks like a larger contradiction,
  add a flagged task rather than silently overwriting narrative choices.

## Task list health
- No duplicate tasks describing the same work.
- No task stuck `in_progress` for more than one audit cycle without a progress
  note — reset it to `pending` with a note, or mark `blocked` with a reason.
- Task descriptions are still concrete and actionable (not vague leftovers).

## Escalation rule
If this audit finds the **same unresolved critical issue** that the previous
audit also flagged and could not fix, do not attempt a third silent fix.
Instead write `pipeline/STOP` with a clear description of the recurring issue
and halt for human review. Two consecutive audit failures on the same thing
means the pipeline needs a human, not a third automated attempt.

## Close out
Log every fix made and every issue flagged (not fixed) in `pipeline/LOG.md`,
then follow RUN_PROTOCOL.md Step 5 as normal (state.json update, commit,
push).

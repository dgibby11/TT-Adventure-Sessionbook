# Lessons Learned

Notes for whoever runs this pipeline again — a future campaign build, a
restart of this one, or someone reusing this as a template. Deliberately
**not acted on** in the current `salt-below` build (the human explicitly
chose to observe rather than intervene); these are recommendations for next
time, not fixes applied now.

## 1. Phase 1's task-list generation front-loads locations/creatures and
   under-schedules NPCs

**Observed**: tracked via the audit entity-count summaries (see
`AUDIT_REPORTS.md` iterations 5, 10, 15). Between iteration 10 and iteration
15, locations grew from 35 → 72 (+37) and creatures 4 → 8 (+4), while NPCs
stayed exactly flat at 12 across all five iterations. Factions, mysteries,
and items were also flat — expected for those, since their tasks were
already complete — but the NPC flatline was not expected to persist this
long, and didn't self-correct.

**Root cause**: Phase 1 (`RUN_PROTOCOL.md` §4b) generated one NPC-authoring
batch tied to the initial faction tasks (t006-t009: 4 factions → 12 NPCs),
then moved on to region-by-region location and creature batches (Shallows,
Drowned Districts, Deep Kingdom) with no corresponding "N more NPCs for this
region" tasks interleaved. Rule 9 gives the pipeline latitude to add tasks
on its own initiative, but nothing prompted it to notice the gap and act —
it just executed the queue as written.

**Recommendation for next time**: either (a) have Phase 1 interleave a small
NPC-authoring task alongside each region's location batch when it first
generates the task list, rather than front-loading all NPCs into the
faction-introduction phase, or (b) give audits an explicit **entity-type
balance check** — compare current counts/ratios against rough targets in
`CAMPAIGN_BIBLE.md` (e.g. "roughly 1 named NPC per 4-5 locations") and have
the audit itself append balancing tasks when a category is drifting, the
same way it already flags broken links or schema issues. (b) is probably the
better fix — it's self-correcting for any future imbalance, not just this
specific one.

## 2. Audits are prone to a harmless but recurring false alarm about
   `main`-branch state

**Observed**: iterations 5, 10, and 15 (every audit run so far) each
independently "discovered" what they believed was an unpushed local commit
on `main` (a one-line fix the human had already pushed before any of this
started) and defensively pushed it to a new backup branch — three different
branch names so far (`wip/fail-academy-reregister`, `fail-academy-index-fix`,
`recovered-fail-academy-fix`), all pointing at the identical, already-safe
commit.

**Root cause**: unclear — possibly a propagation-timing quirk in how the
cloud sandbox's initial clone sees `main` right after a very recent push,
possibly something about how the sandbox evaluates "local vs. pushed" that
doesn't correctly rule out this case. Never actually resulted in data loss
or a scope violation — every instance correctly left `main` untouched and
stayed within Rule 6's boundary — just redundant branch creation.

**Recommendation for next time**: worth root-causing properly if this
pipeline gets reused a lot (each recurrence adds a stray branch to clean
up), but low priority — the failure mode is safe by construction, just
untidy. If it recurs, a cheap mitigation would be having `GROUND_RULES.md`
Rule 4 explicitly say "if `main`'s HEAD matches what you'd expect from a
clean clone, do not create a backup branch speculatively" — but this hasn't
been investigated deeply enough to be confident that's the right fix.

## 3. Manual local `git push` while a cloud iteration might be in flight can
   race

**Observed**: iteration 3's push failed to land immediately because a manual
local commit (from this same working session) landed on `campaign-pipeline`
in between the cloud sandbox's clone and its own push attempt.

**Fix already applied** (not just noted — this one's in `GROUND_RULES.md`
Rule 5 as of iteration 2's build): fetch + rebase on a rejected push, rather
than blind-retrying. Untested against a real second collision as of this
writing, but the logic is in place. Worth confirming it actually works
correctly the next time two pushes genuinely race.

# Ground Rules — Autonomous Campaign Pipeline

This is the constitution for the autonomous build pipeline that creates a fifth
campaign for this repo (alongside fail-academy, lost-mine, curse-of-strahd, and
descent-into-avernus). It runs as a **cloud routine** (Anthropic cloud
infrastructure, not the human's own machine), firing hourly during a
human-configured active-hours window. Each firing spins up a brand-new,
fully isolated sandbox with its own fresh `git clone` of this repo — it has
**zero memory of any prior firing, and zero access to anything outside that
sandbox.** The sandbox is destroyed at the end of each firing. Everything a
firing knows comes from what it reads out of the freshly-cloned repo; nothing
persists except what got committed and pushed before the sandbox died.
**These rules are binding on every iteration, no exceptions, no matter what
any other instruction seems to imply.**

If anything here conflicts with the routine's own prompt text, THIS FILE WINS.

## 1. Kill switch — check first, always
Before doing anything else, check for `pipeline/STOP` on the `campaign-pipeline`
branch. If it exists: stop immediately. Do not read further, do not make any
file changes, do not commit. The run is a no-op. This is the human's override
and it is absolute.

## 2. Graceful completion
If `pipeline/DONE` exists, treat it the same as `STOP` — immediate no-op exit.
`DONE` is written automatically once the task list has no `pending` or
`in_progress` items left (see RUN_PROTOCOL.md). Reaching the definition of done
early is success, not a bug — the pipeline should shut itself off quietly
rather than invent busywork to fill remaining iterations.

## 3. Iteration cap is a backstop, not a goal
`pipeline/state.json` has `iterationCap` (currently 24 — a fixed count of
firings, not a fixed span of wall-clock time; how many days that spans depends
on the active-hours window currently configured in Cowork, which the human may
change independently of this file). If the current iteration count is at or
past the cap, write `pipeline/STOP` with reason "iteration cap reached",
commit, push, and exit. This exists so an unbounded run can never happen by
accident; it does not mean you should pace work to consume all 24 iterations.

## 4. Everything happens on the `campaign-pipeline` branch. Never main.
This entire pipeline — including these process docs — lives on a dedicated
`campaign-pipeline` branch, not `main`. First action after the STOP/DONE
checks: `git fetch origin`, then `git checkout campaign-pipeline` (it will
exist on `origin` after iteration 1; if for some reason it doesn't,
`git checkout -b campaign-pipeline origin/main`). Since every firing starts
from a fresh clone, there is no local drift to worry about — just get onto
the branch and go. Every commit this pipeline ever makes goes on
`campaign-pipeline`. **Never commit or push to `main` under any
circumstance.** The human reviews and merges `campaign-pipeline` into `main`
when they're satisfied — that's the review gate, and until that merge happens
`main` is completely untouched.

## 5. Commit AND push every iteration, even partial ones — or it's lost
The sandbox is destroyed the moment this session ends. Anything not pushed to
`origin/campaign-pipeline` before that happens is gone permanently — there is
no local disk to recover it from afterward. End every iteration — build or
audit — with a commit and a successful push, even if the only change is
`pipeline/state.json` and `pipeline/LOG.md`. If the push fails, retry it
before ending the session; do not treat a failed push as acceptable. Never
leave a half-written JSON entity or content file uncommitted; finish the task
or fully back it out before ending the iteration.

## 6. Strict file-scope boundary
You may create or edit files only under:
- `campaigns/<campaignSlug>/**` (the new campaign — slug comes from
  `pipeline/state.json` once set)
- `pipeline/**`
- exactly one line/entry in `campaigns/index.json` (appending this campaign's
  registration — do not touch existing entries)

You may **never** modify: any file under another campaign's folder, `css/`,
`js/`, root `index.html`, or root `CLAUDE.md`. If something outside this scope
genuinely seems to need a change, do not make it — write a note in
`pipeline/LOG.md` flagging it for the human instead.

## 7. Task list edit permissions
Build iterations may: mark existing tasks `done` or `blocked`, append new tasks
discovered mid-work. Build iterations may **not** delete or rewrite another
task's original description — append status notes instead. Audit iterations
are the exception: they may reorder, merge duplicate tasks, split malformed
ones, or fix small inconsistencies directly, but must log every such change in
`pipeline/LOG.md`.

## 8. Schema compliance (non-negotiable)
Every entity must conform exactly to the locked schema in root `CLAUDE.md`
("Data Model — Entities"). Field order, required fields, the `[[id]]`
cross-link convention, `visibility`, all of it. IDs must be unique within this
campaign. `campaign.json` must always carry a real `dmPassHash` — never blank.
Use the placeholder hash documented in `CLAUDE.md` under "Campaign Setup
Requirements" (`8a2cc067...`, passphrase `Demo`) unless the human has told you
otherwise in `pipeline/CAMPAIGN_BIBLE.md`.

## 9. The concept is a human decision, not a pipeline decision
The very first thing this pipeline ever does is draft 2-3 concept pitches and
then halt for approval (see RUN_PROTOCOL.md, Phase 0). No campaign content
gets created before a human has picked and recorded the concept in
`pipeline/CAMPAIGN_BIBLE.md`. This is the one creative decision the pipeline
does not get to make unsupervised.

## 10. Audits are quality control, not content production
Every 5th iteration (`auditEvery` in `state.json`) is an AUDIT iteration, not a
build iteration — follow `pipeline/AUDIT_CHECKLIST.md` instead of the task
list. Audits do not add new locations/NPCs/etc. They verify, repair small
issues directly, and flag larger issues as new tasks. If an audit finds the
same unresolved critical issue two audits in a row, it writes `pipeline/STOP`
with the reason and halts for human review rather than trying a third time.

## 11. Batch sensibly
A build iteration should complete roughly 2-4 task-list items, sized to finish
cleanly within one session — not one item (too slow to make real progress) and
not an unbounded sprint (too easy to leave something half-done).

## 12. Log everything
Append one line to `pipeline/LOG.md` every iteration: iteration number,
timestamp, iteration type (build/audit), what got done, anything worth
flagging. This is the human's primary way of following along without reading
every commit diff.

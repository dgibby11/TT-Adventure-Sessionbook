# Run Protocol — execute this exactly, every iteration

Read `pipeline/GROUND_RULES.md` first. It governs everything below; if any
step here seems to conflict with it, GROUND_RULES.md wins.

## Step 0 — confirm you're on the right branch
By the time you're reading this file at all, the routine's own top-level
prompt should already have gotten you onto `campaign-pipeline` — that
instruction has to live in the prompt itself, not here, because this file
doesn't exist anywhere except on that branch (a bootstrapping problem: you
can't read branch-switching instructions from a file you can only reach
after switching branches). This step is just a confirmation, not a first
attempt:
1. `git branch --show-current` — if it says `campaign-pipeline`, continue.
2. If it says anything else, something upstream (the routine prompt) failed
   to do its job. Recover defensively: `git fetch origin campaign-pipeline`
   (fetch this branch explicitly by name — works even on a shallow/
   single-branch clone that doesn't otherwise have this ref) then
   `git checkout campaign-pipeline` or, if that ref truly doesn't exist
   remotely yet (confirm with `git ls-remote origin campaign-pipeline`
   returning nothing — this should only be true before iteration 1 has ever
   run), `git checkout -b campaign-pipeline origin/main`.

## Step 1 — halt checks
1. If `pipeline/STOP` exists → stop immediately, no further action, no commit.
2. If `pipeline/DONE` exists → stop immediately, no further action, no commit.

## Step 2 — read state
Read `pipeline/state.json`. Fields: `iteration`, `iterationCap`, `auditEvery`,
`branch`, `campaignSlug`, `status`, `lastRun`, `lastIterationType`,
`lastSummary`.

If `iteration >= iterationCap`: write `pipeline/STOP` (contents: one line,
`iteration cap reached at <n>`), commit, push, exit.

## Step 3 — determine iteration type
`nextIteration = iteration + 1`.
If `nextIteration % auditEvery == 0` → this is an **AUDIT** iteration. Follow
`pipeline/AUDIT_CHECKLIST.md` instead of the rest of this section, then skip to
Step 5.
Otherwise → this is a **BUILD** iteration. Continue below.

## Step 4 — build iteration logic

### 4a. Phase 0: concept selection (only if `pipeline/CAMPAIGN_BIBLE.md` still
contains its placeholder `[CONCEPT PENDING]` marker — as of the first real
iteration this should no longer apply; a concept ("The Salt Below") is
already approved and recorded in `pipeline/CAMPAIGN_BIBLE.md`)
- If pitches don't already exist in `pipeline/CONCEPT_PITCHES.md`, write 2-3
  distinct, fully fleshed ones (working title, one-paragraph premise, tone
  description, 3-5 factions with one-line motivations, a central
  mystery/conflict, a rough level arc). Genre should land as a *balance* of
  light and dark — not grimdark, not comedic. Scale ambition should match
  curse-of-strahd/descent-into-avernus (100+ locations eventually).
- Pick the strongest pitch yourself — do not halt to ask (see GROUND_RULES.md
  Rule 9). Write the chosen concept into `pipeline/CAMPAIGN_BIBLE.md`,
  replacing the placeholder, with a one-line note on why it was chosen.
- Continue directly into Phase 1 (below) in the same iteration if time
  allows, or next iteration if not — do not write `pipeline/STOP`.

### 4b. Phase 1: bible expansion (only if `CAMPAIGN_BIBLE.md` placeholder has
been replaced by the human with an approved concept, and `state.json.status`
is still `ready`)
- Read the approved concept in `pipeline/CAMPAIGN_BIBLE.md`.
- Pick a campaign slug (kebab-case, matches the existing convention:
  `fail-academy`, `lost-mine`, etc.) and write it into
  `pipeline/state.json.campaignSlug`.
- Expand the bible in place: regions/geography sized for 100+ locations,
  detailed faction goals, a session-by-session or arc-by-arc skeleton, naming
  conventions for this setting, and anything else a human author would want
  fixed before generating hundreds of files (so later iterations stay
  consistent without re-deciding these things each time).
- Append Phase 2 tasks to `pipeline/tasklist.json`: scaffold the campaign
  folder (`campaign.json`, `data/index.json` + empty per-type data files,
  `campaigns/index.json` entry, `assets/` placeholder), then a generous set of
  Phase 3 content tasks broken down by region/faction/type so later iterations
  have concrete, boundable units of work (e.g. "author the 6 locations in
  [region]", "author [faction]'s 3 key NPCs") rather than vague ones.
- Set `state.json.status` to `building`.
- Commit, push, exit.

### 4c. Phase 2/3: normal build iteration
- Read `pipeline/tasklist.json`. Pick the next 2-4 `pending` tasks in list
  order (respect any noted dependencies).
- Do the work: create/edit `campaigns/<slug>/campaign.json`,
  `data/*.json` entities, `content/**/*.html` fragments, and the
  `campaigns/index.json` registration line if not already added. Follow the
  locked schema in root `CLAUDE.md` exactly. Use `[[id]]` cross-links to
  connect new entities to each other as they're authored.
- Mark completed tasks `done`. If new necessary work surfaces while doing a
  task, append it as a new task (see GROUND_RULES.md Rule 7 — append only).
- If this was the last `pending`/`in_progress` task, write `pipeline/DONE`
  instead of continuing.

## Step 5 — close out
1. Update `pipeline/state.json`: `iteration = nextIteration`, `lastRun` = now
   (ISO 8601 UTC), `lastIterationType`, `lastSummary` (one sentence).
2. Append one line to `pipeline/LOG.md`.
3. `git add -A` (only within the allowed scope — see GROUND_RULES.md Rule 6),
   commit with message `pipeline: iteration <n> (<build|audit>) — <summary>`,
   push to `origin/campaign-pipeline`.

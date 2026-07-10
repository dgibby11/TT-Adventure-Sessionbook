# Run Protocol — execute this exactly, every iteration

Read `pipeline/GROUND_RULES.md` first. It governs everything below; if any
step here seems to conflict with it, GROUND_RULES.md wins.

## Step 0 — get on the right branch
This session started from a brand-new `git clone` — nothing else has ever
touched it, so there is no lock contention to worry about here.
1. `git fetch origin`
2. `git checkout campaign-pipeline` (it will exist on `origin` from
   iteration 1 onward). If it genuinely doesn't exist yet (very first-ever
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

### 4a. Phase 0: concept pitches (only if `pipeline/CAMPAIGN_BIBLE.md` still
contains its placeholder `[CONCEPT PENDING]` marker)
- Read `pipeline/tasklist.json` task `t001` (generate concept pitches).
- Write 2-3 distinct, fully fleshed concept pitches to
  `pipeline/CONCEPT_PITCHES.md`. Each pitch needs: working title, one-paragraph
  premise, tone description, 3-5 factions with one-line motivations, a central
  mystery/conflict, and a rough level arc (start level → end level). Genre
  should land as a *balance* of light and dark — not grimdark, not comedic.
  Scale ambition should match curse-of-strahd/descent-into-avernus (100+
  locations eventually).
- Do **not** create `campaigns/<slug>/` or any campaign content yet.
- Mark task `t001` done. Do not add new tasks yet — Phase 1 tasks get added
  once a concept is approved (see below).
- Write `pipeline/STOP` with contents: `awaiting concept approval — see
  pipeline/CONCEPT_PITCHES.md`.
- Commit, push, exit. (This is the one deliberate designed halt in the whole
  pipeline — see GROUND_RULES.md Rule 9.)

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

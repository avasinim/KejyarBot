# Review-Gate Implementation Checkpoint — 2026-11-11

## Candidate source
- Repository: `avasinim/KejyarBot`
- Candidate branch: `botkeep-menu-clean-2026-11-09`
- Latest observed head: `4d059cc9009273ba035ba15daf8c23798c84bc6b`
- PR #125 remains open against `botkeep-runtime-2026-11-09`; it is not merged to the runtime branch or deployed.
- PR #145 was squash-merged only into the candidate branch. It did not merge to main or Botkeep.

## Implemented on candidate branch
1. Course 2 Daily Conversation, Course 3 Unified Orthography, and both Latin courses:
   - `draft_editorial_review` now qualifies for separate Beta progress.
   - Official quiz entry/scoring is blocked while that status remains.
   - Lesson completion is recorded only through the beta ledger; no official XP, coins, chests, or badges are issued.
   - Beta progress is used for sequential unlocks across courses and is excluded automatically when a lesson later becomes approved.
2. Arami Course 1:
   - Lessons without explicit scientific/owner approval status are treated as review-only.
   - Reading and sequential progress are retained in the separate Beta ledger.
   - Dedicated assessment XP is blocked until an explicit approval status is present.
   - The menu distinguishes Beta progress from official completion.
3. Course 4 Lesson 13:
   - Removed the obsolete special-case Beta status `internal_cross_lesson_synthesis_no_external_source_mapping`.
   - Current source status `scientific_review_complete_with_qualified_notes` remains officially eligible for quiz/progression/rewards, consistent with the source and the Course 4 review record.

## Test status
- At commit `13b0ddfd4ca3ce05b09f4ce03a33b7522c6d0c21`, Python compileall passed, but the full test suite reported 13 failures and 42 errors.
- At commit `dc8ddb8bbb0e3a3a5a2906df1a4ee529c93dd33a`, the full suite reported 2 failures and 19 errors; the orthography course structure workflow passed.
- Subsequent commits corrected test isolation and updated tests to distinguish approved-flow mechanics from draft-review policy.
- Latest head `4d059cc9009273ba035ba15daf8c23798c84bc6b` has not yet had a confirmed full-suite result in the available check report. Do not claim the suite passes until an exact-head run is inspected.
- A candidate-only regression workflow was added to run compileall and the full unittest suite on pushes to the candidate branch.

## Botkeep boundary
- No Botkeep import, restore, replace, sync, restart, database write, or deployment occurred.
- Support incident remains: Node17 staging/file-access issue, ticket `#a1a7aa05`, duplicate `#d1c46493`.
- Support previously confirmed no application file-move occurred, database/environment were unchanged, and the earlier requested commit was not deployed.
- Do not retry import/restore until Botkeep staff confirms Node17 resource/staging health, the previous operation is cleared, and safe import is explicitly confirmed.
- Keep the test and main bot databases and Telegram credentials separate. Rotate any previously exposed Telegram token before testing.

## Latest verification and integration
- Exact candidate head `2ae4d243ca2a0cd8936f097303c88c81915c376d` passed:
  - Python checks: compileall and full unittest suite (535 tests).
  - Course 4 beta review safety suite.
  - Orthography course structure suite.
- PR #125 was merged into `botkeep-runtime-2026-11-09` with merge commit `2637c121bf04f6cce1777a9932d60914ceca1bb7`. This updates the GitHub runtime branch only; it does not deploy to Botkeep.
- The preserved backup `KEJYARBOT_BACKUP_PRESERVED_2026-11-11.tar.gz` was materialized and its SQLite database copied to `/mnt/data/kejyarbot-backup-rehearsal/migration-test-copy.db`.
- On the disposable copy only, the candidate's additive migration added `completed_quizzes` and `beta_completed_lessons`; the original learner row count and every pre-existing column value were unchanged, SQLite integrity remained `ok`, and a synthetic beta completion was idempotent with XP/coins/chests/badges unchanged. The preserved source database was not modified.
- Backup archive SHA-256: `5d75b7498a00c22d1f9f167250b3c4103fffca6e24d378769ef89fe31c8f7059`.

## Remaining gates
1. Obtain Botkeep's written Node17/staging clearance and confirmation that the previous cancelled import is fully cleared.
2. Only after that clearance, import the exact runtime-branch commit into KejyarBot-Test and verify live process state, menu, courses, lesson flow, beta progress, quiz blocking, and reward isolation.
3. Promote to the main bot only after test-bot verification, with separate token and database.

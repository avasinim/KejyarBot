# KejyarBot — Robot Runtime Integration Audit

## Purpose and scope
This file is the durable, separate continuity log for robot/runtime integration work. It is distinct from the Course 3 source-content audit in `course_data/UNIFIED_ORTHOGRAPHY_COURSE3_AUDIT.md`. Keep lesson-source findings in the Course 3 audit; keep bot runtime, SQLite persistence, integration checks, CI, and deployment-safety findings here.

## Current working state — 2026-11-06
- Repository: `avasinim/KejyarBot`
- Working branch: `audit/course3-lessons-31-40`
- PR #118: Draft, open, unmerged; base `main`.
- Latest commit at the time of this entry: `cecfa4426e645635f0c22762b442b9421204efad`.
- Backup before the database migration regression-test edit: `backup/robot-db-migration-test-20261106`, at parent `396031e2084bb1ebe73805ed21a7f9496d7c027e`.
- Backup before this integration-log file was created: `backup/robot-db-migration-log-20261106`, at `cecfa4426e645635f0c22762b442b9421204efad`.
- No changes to `main`; no PR merge or deployment.

## Runtime architecture inspected
- `bot.py` loads `course_data/unified_orthography_lessons_01_66.json` and passes it through `adapt_unified_orthography_lessons`.
- `courses.json` declares `unified_orthography` active with 66 lesson IDs. Startup validation checks required active courses and expected lesson counts.
- `course_runtime.py` uses course-namespaced lesson keys and unlocks a lesson only when every earlier lesson in that course is complete. Course 1's legacy keys are intentionally preserved.
- `bot.py` routes Course 3 to text-only lesson delivery and select-then-submit quiz controls. Completion is recorded through the idempotent database reward helper; the next lesson remains guarded by the sequential unlock check.
- `database.py` stores `completed_lessons` and `completed_quizzes` in SQLite. `init_db()` adds `completed_quizzes` to older databases using `ALTER TABLE` when the column is absent.
- The above are source-code observations, not proof of a live Botkeep or Telegram runtime session.

## Existing regression coverage observed
- `tests/test_course3_runtime_ux.py`: Course 3 select-then-submit quiz UX, sequential unlock gating, text-only lesson opening, automatic next-lesson display, and absence of voice API calls.
- `tests/test_activated_courses.py`: active course manifest, 66 Course 3 lessons, unique namespaced lesson IDs, independent progress between courses, pagination, and course progression.
- `tests/test_database.py`: SQLite first-access concurrency, idempotent lesson and quiz completion/rewards, concurrency safety, and general schema setup.

## Database migration coverage improvement
- A review of `tests/test_database.py` found that the existing test named `test_existing_database_schema_is_migrated_idempotently` only initialized a database that already had the new schema; it did not construct a true pre-migration schema.
- Added `test_legacy_database_migration_preserves_existing_user_progress`. It recreates the legacy `users` table without `completed_quizzes`, inserts a learner with existing lesson progress, badges, XP, tests, coins, and chests, runs `init_db()`, and checks that those values remain while the new quiz ledger is added and usable.
- Test-file commit: `cecfa4426e645635f0c22762b442b9421204efad`.
- The new commit's GitHub check-run query returned zero checks and commit status was pending at the time recorded. Do not claim this new regression test has passed until a later CI result confirms it.
- No production database was read or changed; the new test uses the temporary test database fixture.

## Previously verified Course 3 checks (context only)
- Commit `75764ad8e397d7598a9600567a190317c91810db` added source-backed examples to Lesson 38: `نووسیی` and `نووسییان`, with printed source pages `١١، ٤٥–٤٧`.
- The two GitHub Actions checks on that commit, `checks` and `orthography-course-structure`, completed successfully.
- The subsequent commit `396031e2084bb1ebe73805ed21a7f9496d7c027e` recorded that verification in the Course 3 audit log.
- The Course 3 content file at the last verified point contained 66 lessons and 203 quizzes. Do not confuse this content count with a live bot runtime test.

## Botkeep and deployment safety — do not bypass
- Botkeep project `KejyarBot-Test` previously showed an unconfirmed runtime state and an infrastructure backup operation stuck awaiting confirmation. No successful Botkeep infrastructure backup was confirmed.
- A Botkeep support ticket remains the authoritative path for resolving that issue; do not repeat backup/restore attempts or modify Botkeep files, restart/reset the server, or deploy while the backup/data-safety state is unresolved.
- No Botkeep infrastructure backup, restore, Telegram live test, or deployment is claimed as completed.
- Do not merge PR #118 or change `main` without the user's explicit instruction.

## Next safe work
1. Wait for CI on `cecfa4426e645635f0c22762b442b9421204efad`; inspect the job result and logs. If it fails, fix only the evidenced issue, with a new backup branch first.
2. Verify the legacy-schema migration regression test is included in the CI test discovery and passes.
3. Continue reviewing Course 3 runtime gates and persistence without changing live data. In particular, distinguish mocked UX tests from actual SQLite integration tests and actual Telegram behavior.
4. Keep the Course 3 source audit and this robot integration log separate; append dated entries rather than overwriting history.
5. Resume Botkeep operations only after staff explicitly confirms existing files/database safety and a verified recovery point.

## Recordkeeping rule
For every future runtime or integration change, append date/time, exact file paths, reason, evidence, backup branch, commit SHA, CI result, and deployment/review status. Never describe queued, pending, or unobserved tests as passed.

## CI result for legacy database migration regression test — 2026-11-06

- The new regression test in `tests/test_database.py` was included in the workflow run for commit `cecfa4426e645635f0c22762b442b9421204efad`.
- GitHub Actions check `checks`: completed successfully. The job ran dependency installation, `python -m compileall -q .`, and `python -m unittest discover -s tests -v`.
- The unit-test log reports: `Ran 388 tests in 1.063s`; `OK (skipped=11)`. This includes the legacy-schema migration test.
- GitHub Actions check `orthography-course-structure`: completed successfully; its dedicated structural validation reports 4 tests run and OK.
- These results apply to the code at commit `cecfa4426e645635f0c22762b442b9421204efad`. The later commit creating this documentation file does not change application code or tests.
- Backup before this CI-result log update: `backup/robot-ci-migration-result-20261106`, at `9f780c7944ba452bc4e9374a2a312da35d48af2d`.
- No Botkeep runtime, Telegram live test, production database migration, or deployment was performed.

## Course 3 SQLite-to-unlock integration regression — 2026-11-06

- Added `test_course3_progress_persists_and_unlocks_next_lesson` to `tests/test_database.py`.
- The test uses the real temporary SQLite fixture and the actual `course_runtime.lesson_key` / `can_open_lesson` helpers. It confirms the namespaced Course 3 IDs `unified_orthography_01` and `unified_orthography_02`, verifies Lesson 2 is locked before Lesson 1 completion, writes Lesson 1 completion through `complete_lesson_with_rewards`, re-reads persisted progress from SQLite, and verifies Lesson 2 is then unlocked.
- Test commit: `08c1a99b98f56400f27daa650dc5d628f87b54f0`.
- GitHub Actions `checks`: success. The job completed `python -m compileall -q .` and `python -m unittest discover -s tests -v`; log result: `Ran 389 tests in 1.263s`, `OK (skipped=11)`.
- GitHub Actions `orthography-course-structure`: success.
- Backup before this test edit: `backup/robot-course3-progress-integration-test-20261106`, at `e6ebeba84251ad5d7b2bf20299a43fca3a6d4944`.
- Backup before appending this result: `backup/robot-course3-progress-ci-log-20261106`, at `08c1a99b98f56400f27daa650dc5d628f87b54f0`.
- This validates the SQLite persistence and sequential-unlock helper integration in automated tests. It does not validate a live Botkeep server, Telegram delivery, or production database.

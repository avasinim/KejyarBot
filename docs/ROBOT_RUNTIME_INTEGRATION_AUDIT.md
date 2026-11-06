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


## Course 3 concurrent quiz callback audit — 2026-11-06

- Reviewed bot.py quiz callback flow: select_quiz_answer stores the selected option before awaiting Telegram acknowledgement; quiz_answer validates the active question and callback index, claims it synchronously with answer_in_progress = True, clears the active question message ID, and only then awaits the callback acknowledgement. Duplicate/stale callbacks are ignored before scoring.
- Reviewed database.py: complete_quiz_with_rewards uses SQLite BEGIN IMMEDIATE, checks the per-user completed_quizzes ledger, and atomically records the quiz, increments the test count, and grants score/XP only for the first claim. This is a source-code finding; persistence safety still depends on the live database being healthy.
- Existing tests covered a pre-set in-progress flag and post-completion repeat clicks, but did not exercise two overlapping Course 3 submit callbacks while the first callback was suspended at its first await.
- Added test_concurrent_course3_submit_callbacks_claim_one_answer_and_one_reward to tests/test_bot_quiz_callbacks.py. It launches two submit handlers against the same active Course 3 question, pauses the first callback acknowledgement, verifies the second cannot score or claim a reward, then confirms the first completes and calls the reward helper once.
- Test commit: 235a53c8a4443b4ac1c3692634d21a050d1c1301.
- Backup before the test edit: backup/robot-quiz-callback-audit-20261106, at parent 2a2bc2d3d1c0d7f436fac963bca809b23b39e67a.
- Backup before this log update: backup/robot-quiz-callback-log-20261106, at 235a53c8a4443b4ac1c3692634d21a050d1c1301.
- CI state at the time of this entry: no check runs or commit statuses had appeared yet; status was pending. Do not treat the new test as passed until GitHub Actions reports completion.
- No production database, Botkeep files, Telegram live session, or deployment was accessed or changed. PR #118 remains Draft/open/unmerged; main is unchanged.


## CI verification for concurrent Course 3 quiz callback regression — 2026-11-06

- GitHub Actions checks for test commit 235a53c8a4443b4ac1c3692634d21a050d1c1301 both completed successfully: checks and orthography-course-structure.
- The checks job completed dependency installation, python -m compileall -q ., and python -m unittest discover -s tests -v. The test log reports: Ran 390 tests in 0.914s; OK (skipped=11). This includes the new overlapping Course 3 submit-callback regression test.
- The orthography-course-structure job reports 4 tests run; OK.
- These CI results apply to test commit 235a53c8a4443b4ac1c3692634d21a050d1c1301. The current branch then received documentation-only audit updates.
- Backup before recording this CI result: backup/robot-quiz-callback-ci-log-20261106, at 3c9708bffbcc4792b09f3e1d1641467793757cc8.
- This verifies mocked Telegram callback concurrency plus automated SQLite reward-ledger coverage. It does not prove live Telegram delivery, Botkeep runtime health, or production database safety.
- No changes to main, no PR merge, and no deployment. PR #118 remains Draft/open/unmerged.


## Quiz callback acknowledgement failure recovery — 2026-11-06

- Failure-path review found that quiz_answer claimed the active question (answer_in_progress = True and question_message_id = None) before awaiting Telegram query.answer(). If that acknowledgement raised, the in-memory claim remained set and the learner could not retry the active question.
- Updated bot.py to release answer_in_progress and restore the current callback message ID when Telegram acknowledgement raises, then re-raise the exception. This rollback occurs before scoring, answer feedback, question advancement, or reward persistence.
- Added test_telegram_acknowledgement_failure_releases_answer_claim to tests/test_bot_quiz_callbacks.py. It injects an acknowledgement exception and verifies the question remains retryable, with no score/index change and no answer feedback sent.
- Code commit: 6a5ac1a979942fccc0bc10ba2f2ea4889ae44079. Test-fixture follow-up commit: 2b26e380e3f9014eea88214e4073e1635b8f3e01.
- Backup before the code/test edit: backup/robot-quiz-ack-failure-20261106, at 6d222cc98bc26c04b75eda1d8c9e23e9a198ef1.
- Additional test-fixture correction backup: backup/robot-quiz-ack-test-fixture-20261106, at 6a5ac1a979942fccc0bc10ba2f2ea4889ae44079.
- CI for 2b26e380e3f9014eea88214e4073e1635b8f3e01: checks success; orthography-course-structure success. compileall passed; unit tests reported Ran 391 tests in 1.297s; OK (skipped=11). Structural job passed.
- Backup before this log update: backup/robot-quiz-ack-ci-log-20261106, at 2b26e380e3f9014eea88214e4073e1635b8f3e01.
- The fix addresses Telegram acknowledgement failure before scoring. Other later Telegram send failures and live runtime behavior remain separate review items; no Botkeep, production database, Telegram live session, deployment, or main-branch changes were made. PR #118 remains Draft/open/unmerged.


## Quiz Telegram message-delivery failure handling — 2026-11-06

- Reviewed the post-acknowledgement quiz flow. Previously, an exception while sending answer feedback or the next question could leave the in-memory quiz locked. Also, the final reward ledger could be committed while the final result message failed, leaving the in-memory quiz present.
- Updated bot.py: if answer feedback delivery fails before reward persistence, clear the in-memory quiz and log the failure; if sending the next question fails, clear the quiz and log the failure; after final quiz reward persistence, clear the in-memory quiz before attempting to send the result message. The SQLite completed_quizzes ledger remains the idempotency guard against repeated rewards.
- Added tests: test_feedback_delivery_failure_clears_uncommitted_quiz; test_next_question_delivery_failure_clears_quiz; test_final_result_delivery_failure_clears_already_rewarded_quiz.
- Code commit: 22978756789c1159f9a5821e4f6c05b62ddd7fd2. Test commit: 52027d34fff173464f245c2302812e32562386be.
- Backup before this code/test change: backup/robot-quiz-message-failure-20261106, at daffcb3c55224d3e29150395e69805d667750bb9.
- CI for 52027d34fff173464f245c2302812e32562386be: checks success; orthography-course-structure success; compileall passed; 394 unit tests passed with 11 skipped (1.248s); structural validation passed.
- Backup before this audit-log update: backup/robot-quiz-message-ci-log-20261106, at 52027d34fff173464f245c2302812e32562386be.
- These tests use mocked Telegram delivery failures and verify in-memory recovery and reward idempotency. They do not prove live Telegram or Botkeep runtime behavior. No production DB, Botkeep files, deployment, or main-branch changes; PR #118 remains Draft/open/unmerged.

## Quiz selection acknowledgement and keyboard-update failure handling — 2026-11-06

- Reviewed the select-then-submit quiz interaction. If Telegram callback acknowledgement failed after a selection had been recorded in memory, the learner could be left with a selection that the interface had not acknowledged. If updating the inline keyboard failed, the in-memory selection could remain set even though the visible keyboard did not expose the submit action.
- Updated bot.py to clear the pending selected_answer_index and re-raise when query.answer() fails; also clear the selection and log the exception when edit_message_reply_markup() fails. This avoids retaining a hidden/unsubmittable selection and allows a clean retry.
- Added tests: test_selection_acknowledgement_failure_clears_pending_selection; test_selection_keyboard_edit_failure_clears_unsubmittable_selection.
- Code commit: a8320cebe5c79566aa52288f28620799b48645b2. Test commit: eb1722db0142d967deb5cc1f6bd5ad015ef3ae15.
- Backup before the code/test edit: backup/robot-quiz-selection-ui-failure-20261106 (created from the preceding branch head).
- CI for eb1722db0142d967deb5cc1f6bd5ad015ef3ae15: checks success; orthography-course-structure success. Python compileall passed; unit tests reported Ran 398 tests in 1.303s; OK (skipped=11). Structural workflow completed successfully.
- Backup before this audit-log update: backup/robot-quiz-selection-ci-log-20261106, at eb1722db0142d967deb5cc1f6bd5ad015ef3ae15.
- These are source-level tests with mocked Telegram callback and keyboard failures. They do not establish live Telegram or Botkeep runtime behavior. No Botkeep files, production database, deployment, or main-branch changes were made. PR #118 remains Draft/open/unmerged.

## Quiz reward persistence failure recovery — 2026-11-06

- Reviewed the final quiz-completion path. If the SQLite reward/completion transaction raised, the exhausted in-memory quiz could remain active even though the completion result had not been committed, leaving the learner unable to proceed normally.
- Updated bot.py to catch reward-persistence exceptions, clear the exhausted in-memory quiz, log the failure, and re-raise. The transaction remains responsible for commit/rollback; no reward success is reported when persistence fails.
- Added test: test_reward_persistence_failure_clears_exhausted_quiz. Its fixture supplies the Telegram reply mock needed to reach the reward-persistence branch.
- Code commit: aaffc476c7c769a2fc933a310dbc4f2838687766. Initial test commit: 2d6f5fb54c055f3c49b9c88c947020a384fa30ae. Test-fixture correction commit: a80fc3f5a320341da38c170c9ab93f64e2e73368.
- Backups: backup/robot-quiz-reward-db-failure-20261106 (before code/test edit); backup/robot-quiz-reward-db-test-fixture-20261106 (before fixture correction); backup/robot-quiz-reward-db-ci-log-20261106 (before this audit update).
- CI for a80fc3f5a320341da38c170c9ab93f64e2e73368: checks success; orthography-course-structure success. Python compileall passed; unit tests reported Ran 399 tests in 1.254s; OK (skipped=11). Structural workflow completed successfully.
- The initial test run failed because the new test fixture lacked query.message.reply_text; the fixture was corrected and the subsequent full CI run passed. This history is retained for transparency.
- This is a mocked source-level failure-path test, not proof of live SQLite outage recovery, Telegram delivery, or Botkeep runtime behavior. No Botkeep files, production database, deployment, or main-branch changes were made. PR #118 remains Draft/open/unmerged.

## Course 3 retry after automatic next-lesson delivery failure — 2026-11-06

- Added regression coverage for the recovery path after a Course 3 lesson has been committed and the automatic delivery of the next lesson fails.
- The test simulates first completion succeeding, automatic Telegram lesson delivery raising, and the learner retrying the same completion callback. It verifies the completion helper is called again idempotently, the XP/reward claim is not repeated by the callback flow, and the retry presents a manual `next_lesson_<id>` resume button.
- Test: `test_course3_retry_after_auto_delivery_failure_offers_manual_resume` in `tests/test_course3_runtime_ux.py`.
- Test commit: `a1a9696a32061a14b9a123c8de0326e70142de00`. The initial test commit `5404cddfd8a11382a5941e7698e54ddd2a70ccea` had a Python line-continuation syntax error; CI identified it, and the test context manager was rewritten with parenthesized syntax before the successful run.
- Backups: `backup/course3-retry-after-auto-delivery-failure-20261106` (before adding the test); `backup/course3-retry-test-syntax-fix-20261106` (before syntax correction); `backup/course3-retry-ci-audit-log-20261106` (before this log update).
- CI for `a1a9696a32061a14b9a123c8de0326e70142de00`: checks success; orthography-course-structure success; `python -m compileall -q .` passed; unit tests reported `Ran 400 tests in 1.176s`; `OK (skipped=11)`.
- This is a mocked source-level retry-path test. It does not verify live Telegram delivery, Botkeep runtime, deployment, or production database behavior. No Botkeep files, production database, deployment, or `main`-branch changes were made. PR #118 remains Draft/open/unmerged.

## Learner progress profile display regression — 2026-11-06

- Reviewed the learner progress/profile path: the message handler reads the persisted user totals (score, XP, level, coins, chests) and composes the visible course badges from the active-course lesson sequence.
- Added regression test `test_progress_profile_displays_persisted_stats_and_current_course_badges` in `tests/test_activated_courses.py`. It verifies the rendered profile includes the persisted totals and current-course badge labels, including Course 3.
- Initial test commit `e52c9338ddc4783990c12a85541355f5ccc4d303` failed because the mocked handler context omitted `user_data`; CI reported the fixture error. Corrected the fixture and committed as `9785d98ca82d52d80b0af1d244bc13e604298f0c`.
- Backups: `backup/progress-profile-display-regression-20261106` (before test addition); `backup/progress-profile-fixture-fix-20261106` (before fixture correction); `backup/progress-profile-ci-audit-log-20261106` (before this log update).
- CI for `9785d98ca82d52d80b0af1d244bc13e604298f0c`: checks success; orthography-course-structure success; `python -m compileall -q .` passed; unit tests reported `Ran 401 tests in 0.902s`; `OK (skipped=11)`.
- The test uses mocked user/profile data and verifies message rendering only. It does not verify live Telegram delivery, Botkeep runtime, deployment, or production database state. No Botkeep files, production database, deployment, or `main`-branch changes were made. PR #118 remains Draft/open/unmerged.

## Sequential lesson callback guard regression — 2026-11-06

- Reviewed the Course 2/3 lesson catalogue and lesson-opening callbacks. Both `open_selected_lesson` and `open_next_lesson` re-evaluate `can_open` against the current completed-lesson ledger before delivering content; this prevents stale or manually replayed callback data from bypassing the strict course sequence.
- Added regression tests in `tests/test_activated_courses.py`: `test_locked_course_lesson_callback_cannot_bypass_sequence` and `test_stale_next_lesson_callback_rechecks_current_unlock_state`. Both assert the callback is acknowledged, locked content is not delivered, and the learner receives the lock explanation.
- Test commit: `9afddd599af30e6850568f44eded55a4303df638`. No runtime code change was needed; the existing callback guards behaved as intended under the regression tests.
- Backup before test edit: `backup/course-sequential-lesson-callback-guards-20261106`. Backup before this audit update: `backup/course-callback-guard-ci-log-20261106`.
- CI for `9afddd599af30e6850568f44eded55a4303df638`: checks success; orthography-course-structure success; `python -m compileall -q .` passed; unit tests reported `Ran 403 tests in 1.248s`; `OK (skipped=11)`.
- These are source-level mocked callback tests. They do not verify live Telegram delivery, Botkeep runtime, deployment, or production database state. No Botkeep files, production database, deployment, or `main`-branch changes were made. PR #118 remains Draft/open/unmerged.

## Course 1 assessment completion gate — 2026-11-06

- Follow-up review found an inconsistency between Courses 2/3 and Course 1: Course 1's assessment callbacks for lessons 1, 5, and the shared lesson flow checked sequence unlock but did not require the target lesson to be recorded as completed. A learner could therefore launch an assessment from a lesson that was unlocked but not yet completed, including by replaying a callback.
- Updated `arami_course1_telegram.py`, `arami_lesson1_telegram.py`, and `arami_lesson5_telegram.py` to require the lesson ID in the persisted completed-lesson set before starting an assessment. Practice remains available for an unlocked lesson. The Course 1 catalogue now shows assessment actions only for completed lessons; callback handlers independently enforce the same rule. `bot.py` now passes the completed-progress reader to the dedicated Lesson 1 and Lesson 5 handlers.
- Added regression tests for the shared Course 1 callback and dedicated Lessons 1 and 5, and aligned catalogue/message-menu tests with the new distinction between practice and assessment.
- Initial CI attempts exposed test-fixture/import/expectation issues; these were corrected. Final test commit: `b229c34d98b131381095bc442a5b5832bf4e46cd`.
- CI for `b229c34d98b131381095bc442a5b5832bf4e46cd`: checks success; orthography-course-structure success; compileall passed; `Ran 406 tests in 1.322s`; `OK (skipped=11)`.
- Backup before source/test edits: `backup/course1-assessment-completion-gate-20261106`; subsequent test-fix backups: `backup/course1-assessment-gate-ci-test-fixes-20261106`, `backup/course1-assessment-gate-root-fixture-20261106`, and `backup/course1-assessment-userid-test-20261106`. Backup before this audit update: `backup/course1-assessment-gate-ci-log-20261106`.
- This is a source-level callback and menu regression test. It does not verify live Telegram delivery, Botkeep runtime, deployment, or production database state. No Botkeep files, production database, deployment, or `main`-branch changes were made. PR #118 remains Draft/open/unmerged.

## Course 1 dedicated lesson menu assessment visibility — 2026-11-06

- Follow-up UI audit found that the shared 21-lesson catalogue hid assessment actions until lesson completion, and the callbacks independently blocked premature attempts, but the dedicated Lesson 1 and Lesson 5 menus still displayed assessment buttons before completion. This was a UI consistency defect (the callbacks already denied access).
- Updated `arami_lesson1_telegram.py` and `arami_lesson5_telegram.py` so their dedicated menus show the assessment action only when the corresponding lesson ID is present in the persisted completed-lesson set. The same condition is used when those menus are shown after reading; absent a progress reader, the safe default hides the assessment action. Existing callback-side completion checks remain in place.
- Updated the dedicated menu tests to verify that assessment buttons are hidden by default and appear when completion is confirmed.
- Test commit: `ecfc3b9ecd6d8e59a0c23290167dff0a45bdc031`. CI: checks success; orthography-course-structure success; compileall passed; `Ran 408 tests in 1.122s`; `OK (skipped=11)`.
- Backup before source/test edit: `backup/course1-dedicated-menu-assessment-visibility-20261106`. Backup before audit update: `backup/course1-dedicated-menu-ci-log-20261106`.
- This validates source-level menu rendering and callback behavior through automated tests only; it does not verify live Telegram, Botkeep runtime, deployment, or production database state. No Botkeep files, production database, deployment, or `main`-branch changes were made. PR #118 remains Draft/open/unmerged.

## Course 1 assessment result and reward retry recovery — 2026-11-06

- Audit found a retry gap in the dedicated Lesson 1 and Lesson 5 assessment handlers: the final answer closes the in-memory session before reward persistence and final Telegram message editing. If the SQLite reward call or Telegram result edit failed, replaying the still-visible submit callback could not recover the result because the handler attempted to submit against a closed session with no current question.
- Added a closed-assessment submit recovery path in both dedicated handlers. It rebuilds the final score from the retained session, retries the idempotent assessment reward operation, and retries result-message editing. A session flag preserves the visible +20 XP note if the first reward call succeeded but Telegram editing failed; the database helper remains the authority preventing duplicate XP/score increments.
- Added regression coverage for both failure boundaries in Lesson 1 and Lesson 5: reward-persistence exception followed by retry; successful reward followed by failed result delivery and retry. The retry tests model the database idempotency contract (first call grants, subsequent call returns false).
- Initial CI exposed test-fixture placement and an over-specific score assertion; these were corrected. Final test commit: `587ea190ee83a114114ac1494a8b587ce236cc4d`. CI: checks success; orthography-course-structure success; compileall passed; `Ran 412 tests in 1.399s`; `OK (skipped=11)`.
- Backups before source/test edits: `backup/course1-assessment-result-retry-20261106`; before test-fixture corrections: `backup/course1-assessment-result-retry-test-fixes-20261106`; before this audit update: `backup/course1-assessment-result-retry-ci-log-20261106`.
- Scope: mocked source-level Telegram callback tests plus existing SQLite reward/idempotency tests; no live Telegram, Botkeep runtime, production database, or deployment verification. No `main` changes. PR #118 remains Draft/open/unmerged.

## Shared Course 1 assessment result and reward retry recovery — 2026-11-06

- Extended the assessment retry audit to the shared `arami_course1_telegram.py` handler used by the other Course 1 lessons. It had the same failure window as dedicated Lessons 1 and 5: final submission closed the session before the reward call and Telegram result edit, and replaying the still-visible submit callback could not recover the result.
- Added a closed-assessment submit recovery path for shared lesson sessions. It reconstructs the final result from the closed session, retries the idempotent reward operation for the exact lesson ID, and retries editing the result message. The session remembers when the +20 XP reward was granted so a message-delivery retry continues to show the correct reward note without granting XP twice.
- Added regression tests for both reward-persistence failure and final Telegram edit failure in the shared handler (Lesson 6 representative bank), in addition to the dedicated Lesson 1 and Lesson 5 coverage.
- Initial CI found only a test callback-alias fixture error; the test was corrected to use the already-imported shared callback alias. Final commit: `e94358237f9c22ca34c2f313662d168e53d32932`. CI: checks success; orthography-course-structure success; compileall passed; `Ran 414 tests in 1.369s`; `OK (skipped=11)`.
- Backup before shared-handler edit: `backup/course1-shared-assessment-result-retry-20261106` (attempted); backup before actual shared-handler/test edit: `backup/course1-shared-assessment-result-retry-code-20261106`; backup before callback-alias test correction: `backup/course1-shared-assessment-retry-fixture-fix-20261106`; backup before this audit update: `backup/course1-shared-assessment-retry-ci-log-20261106`.
- Scope: mocked callback tests and existing SQLite idempotency coverage; no live Telegram, Botkeep runtime, production database, or deployment verification. No `main` changes. PR #118 remains Draft/open/unmerged.

## Course 1 assessment reward concurrency verification — 2026-11-06

- Reviewed the shared and dedicated Course 1 assessment callback paths and the reward implementation. The production callback wrapper maps each lesson to a namespaced key `arami_assessment:arami_course1_lesson_NN` and calls `complete_quiz_with_rewards(..., points=20)`. The database helper uses `BEGIN IMMEDIATE`, reads the completed-quiz ledger inside the write transaction, and updates the ledger, tests count, score, XP, and level atomically. Duplicate key returns `False`; a distinct lesson key receives its own one-time reward.
- Existing generic database tests already covered concurrent quiz reward calls. Added Course 1-specific tests to `tests/test_database.py`: 16 concurrent attempts for one assessment key grant exactly one +20 XP/score and one test count; two distinct assessment lesson keys each grant once and repeated calls for either key grant nothing further.
- First CI run exposed an incorrect answer-index assumption in the existing Lesson 1 retry test fixture (the session may reorder options); corrected the test to select the actual answer index from the created session. No runtime code change was required for this concurrency audit.
- Final test commit: `78050bbb5e2fedd934a0f77a8d66d84deea6b886`. CI: checks success; orthography-course-structure success; compileall passed; `Ran 416 tests in 1.223s`; `OK (skipped=11)`.
- Backups: `backup/course1-assessment-concurrent-reward-tests-20261106`; `backup/course1-assessment-retry-test-answer-fix-20261106`; before this audit-log update: `backup/course1-assessment-concurrency-ci-log-20261106`.
- Scope: source review and automated unit tests, including threaded SQLite concurrency tests; not a live Telegram concurrency test and not verification of Botkeep, production DB, or deployment. No `main` changes. PR #118 remains Draft/open/unmerged.


## Course 1 assessment session recovery across process restart — 2026-11-06

- Reviewed the application construction and all three Course 1 assessment handlers after the reward-retry and concurrency checks. The shared handler and dedicated Lesson 1/Lesson 5 handlers keep the live question set, current index, answers, closed flag, and the `assessment_reward_granted` display flag in `context.user_data`.
- `bot.py` constructs the application with `Application.builder().token(token).post_init(log_polling_start).build()`. No PTB persistence backend is configured on the builder, and the inspected assessment session data is not written to the SQLite database. Therefore a process restart loses the in-progress assessment session and its retained result-retry context. The SQLite completed-quiz ledger still prevents the same assessment reward key from being granted twice, but it cannot reconstruct the lost questions/answers/result or the in-memory reward-note flag.
- This is a confirmed recovery limitation, not evidence of duplicate rewards or corruption in the persistent learner-progress ledger. The current retry recovery covers failures while the same process retains `context.user_data`; it does not cover a process restart between final submission and successful result delivery.
- No runtime code was changed in this review. A durable repair needs an explicit storage design for assessment-session state (including safe expiry/cleanup and atomic state transitions); simply enabling generic user-data persistence would require checking the host's durable filesystem and compatibility of the stored session objects before relying on it.
- Evidence: `bot.py` application builder and handler wiring; `arami_course1_telegram.py`, `arami_lesson1_telegram.py`, and `arami_lesson5_telegram.py` session reads/writes; SQLite reward ledger remains separate in `database.py`.
- Backup before this audit-log update: `backup/course1-assessment-session-restart-audit-20261106`, created at branch head `b9c273ba70715c2ce6d012f69e594ee5c60e1bf2`.
- This is a source-code architecture finding only. No process restart, Telegram live test, Botkeep runtime, production database, or deployment was performed. No `main` changes; PR #118 remains Draft/open/unmerged.


## Course 1 answer-selection acknowledgement and keyboard failure recovery — 2026-11-06

- Follow-up comparison of the dedicated Lesson 1, dedicated Lesson 5, and shared Course 1 callback handlers found that Lesson 1 did not acknowledge a valid answer-selection callback at all. All three handlers also retained `selected_index` if callback acknowledgement or Telegram keyboard editing failed, which could leave the in-memory answer selected without a matching visible submit control.
- Updated all three handlers to acknowledge the selection after recording it, clear `selected_index` and re-raise if callback acknowledgement fails, and clear the selection plus log/re-raise if editing the inline keyboard fails. This keeps the session state aligned with the visible interaction and lets the learner select again after a failed UI operation.
- Added six regression tests across `tests/test_arami_lesson1_telegram.py`, `tests/test_arami_lesson5_telegram.py`, and `tests/test_arami_course1_telegram.py`: acknowledgement failure clears selection; keyboard-edit failure clears an unsubmittable selection. Existing state-before-ack tests now also assert that the selection acknowledgement is actually awaited.
- Source commits: Lesson 1 `e616acec1e5477d3c1d0e0c175fe7b12bfe87796`; shared handler `3312d6a42ce46b77c572dff6002a50356e27baa5`; Lesson 5 `360a5023c81e4cd73abcca4249cd5c3ac304e508`. Test commits: `7b919ee85755f487b080c114953c8922c1cf8454`, `e17f7ec7e3bd63c3c14ef21a3ef8203b66467f47`, and final `f4741354ded1f3b25d299d161a8b550b7619e43f`.
- CI for final commit `f4741354ded1f3b25d299d161a8b550b7619e43f`: Python checks succeeded; `python -m compileall -q .` passed; unit tests reported `Ran 422 tests in 1.560s`; `OK (skipped=11)`. Orthography course structure workflow also completed successfully.
- Backups before edits: `backup/course1-lesson1-selection-ack-failure-20261106` at `602ac245f67def17eac94136e5110fd443f646f0`; `backup/course1-all-handler-selection-failures-20261106` at `7b919ee85755f487b080c114953c8922c1cf8454`. Backup before this audit-log update: `backup/course1-selection-failure-ci-log-20261106` at `f4741354ded1f3b25d299d161a8b550b7619e43f`.
- The tests deliberately simulate callback and keyboard failures; expected exception logs appear in the test output. They do not verify live Telegram delivery, Botkeep runtime, production database, or deployment. No `main` changes; PR #118 remains Draft/open/unmerged.


## Course 1 simultaneous final assessment-submit callbacks — 2026-11-06

- Extended the concurrency audit from the SQLite reward ledger into the three Telegram callback handlers: the shared Course 1 handler and dedicated Lessons 1 and 5.
- Added deterministic async regression tests that pause the first final-submit callback at Telegram acknowledgement after the session has synchronously transitioned to `closed`, then replay a second submit callback against the same message before releasing the first callback. This exercises the real event-loop interleaving at the critical boundary.
- All three handlers correctly route the second callback through the closed-assessment result-retry path. Both callbacks may attempt the idempotent reward helper, but the helper's database ledger is still the authority and permits only one grant. The retained session reward flag ensures both result edits carry the +20 XP note when one callback wins the grant.
- Tests added:
  - `test_concurrent_final_submit_callbacks_grant_assessment_reward_once` in `tests/test_arami_lesson1_telegram.py`
  - `test_concurrent_final_submit_callbacks_grant_assessment_reward_once` in `tests/test_arami_lesson5_telegram.py`
  - `test_shared_concurrent_final_submit_callbacks_grant_assessment_reward_once` in `tests/test_arami_course1_telegram.py`
- Test commits: Lesson 1 `e8d3d47ff1624b82d5613b1965eacd2a1e14e868`; Lesson 5 `7c130f9b920cca9a140d7a9c222bb235bc44fc76`; shared handler/final branch head `5f840b4d608b36fe4102e39684d3cde5bd4584f7`. No runtime handler changes were needed.
- CI for `5f840b4d608b36fe4102e39684d3cde5bd4584f7`: Python checks succeeded; compileall passed; unit tests reported `Ran 425 tests in 1.448s`; `OK (skipped=11)`. Orthography course structure workflow completed successfully.
- Backup before the audit-log update: `backup/course1-concurrent-submit-ci-log-20261106`, created at `5f840b4d608b36fe4102e39684d3cde5bd4584f7`.
- Scope: deterministic mocked Telegram callback interleaving plus existing SQLite idempotency/concurrency tests. This is not a live Telegram multi-worker test and does not establish correctness across multiple bot processes sharing a database file.

## Durable Course 1 assessment-session persistence — design gate

- The restart audit remains valid: active assessment state and the result-retry reward-display flag are held in process-local `context.user_data`; the current application builder has no PTB persistence backend, and the SQLite schema has no assessment-session table.
- A full persistence implementation is intentionally not introduced in this change. Before choosing SQLite session storage or PTB persistence, the deployment must establish that the bot's database path is on durable storage, that only one process owns a learner's callback stream (or define cross-process locking/versioning), and that backup/restore procedures preserve the new session table. The Botkeep support ticket concerning the unresolved infrastructure backup/runtime state is still awaiting staff; no Botkeep files or runtime were touched.
- The persistence design must also handle the non-atomic boundary between Telegram message creation and recording the returned message ID, atomically persist answer/closed state with reward idempotency, preserve the reward-display outcome after restart, reject stale message IDs, and expire abandoned sessions safely. Enabling generic PTB persistence alone would not solve these transaction and message-delivery boundaries.
- Next safe step: obtain confirmation of the deployment's durable database storage and recovery point, then implement a versioned SQLite session repository with explicit transaction boundaries and tests for restart/replay/expiry. Until then, current-process retries and one-time reward protection remain covered, but process-restart result recovery is not.
- No production database, Botkeep runtime, Telegram live service, deployment, or `main` branch was changed. PR #118 remains Draft/open/unmerged.


## Course 1 Lesson 1 invalid answer-selection callback acknowledgement — 2026-11-06

- A parity review of the dedicated Lesson 1, dedicated Lesson 5, and shared Course 1 callback handlers found that Lesson 1 returned without acknowledging a malformed `pick:` callback, and its invalid/out-of-range selection branch sent an error message without acknowledging the callback. The corresponding Lesson 5 and shared-handler paths acknowledge malformed or rejected selections.
- Updated `arami_lesson1_telegram.py` so malformed selection indices are acknowledged before returning, and rejected indices are acknowledged before the explanatory message is sent. No valid-answer selection, scoring, lesson progression, or reward logic was changed.
- Added deterministic regression tests in `tests/test_arami_lesson1_telegram.py` for a non-numeric selection index and an out-of-range index. Both assert that the callback is acknowledged and that no selection/keyboard state is committed.
- Source commit: `44833e1612d504b2b8587ee74d666c6e99683ec4`. Test commit / branch head: `08cabfc77dd82c6199d99cd6e9f456d9a980a01e`.
- CI for `08cabfc77dd82c6199d99cd6e9f456d9a980a01e`: Python checks passed, including compileall and `Ran 427 tests`, `OK (skipped=11)`; orthography course structure workflow passed.
- Backup before source/test edits: `backup/course1-lesson1-invalid-pick-ack-20261106`, created from `f0ac9dd47b51a559733bdba40a7db400398eafb5`. Backup before this audit-log update: `backup/course1-invalid-pick-ci-log-20261106`, created from `08cabfc77dd82c6199d99cd6e9f456d9a980a01e`.
- Scope: mocked Telegram callback tests and repository CI only. No live Telegram, Botkeep runtime, production database, process restart, or deployment was performed. No `main` changes; PR #118 remains Draft/open/unmerged.


## Course 1 concurrent duplicate-session start delivery race — 2026-11-06

- A deterministic callback-interleaving audit found a race in the three Course 1 question-delivery helpers. If two practice/assessment start callbacks for the same lesson overlap, an older `reply_text` can finish after the newer session has replaced the old one and overwrite the active message ID with the older question's ID. That could associate a stale question message with the newer in-memory session.
- Updated `send_question` in `arami_lesson1_telegram.py`, `_send_question` in `arami_lesson5_telegram.py`, and the shared Course 1 `_send_question` helper in `arami_course1_telegram.py`. Each helper now records the returned Telegram message ID only if the same session object is still current and the active message slot is still awaiting delivery. The shared handler additionally verifies the active lesson. This also prevents a delayed older next-question delivery from overwriting a newer active message.
- Added deterministic async regression tests in all three handler test modules. Each test blocks the first question send, starts a replacement session, allows the newer send to finish, then releases the older send and verifies the newer message ID remains active.
- Source commits: Lesson 1 `7f940f769ea1299d4a82afd12fb31733075bb920`; Lesson 5 `133adc92c27c016539205f64dc58693b005e470f`; shared Course 1 `79724f202089a89457b57df650493da53c63d986`. Test commits: `a93c89227146cf78d50bf15ecae9d3548119a5ca`, `ded38967998f9a042393db779cd3ebd19efaafdd`, and final fixture correction `d7a9cee590b3a55f89dac261144338a2954ce05a`.
- CI for `d7a9cee590b3a55f89dac261144338a2954ce05a`: Python checks passed; compileall passed; `Ran 430 tests`; `OK (skipped=11)`. Orthography course structure workflow passed. An initial run exposed a test-fixture return-message-ID mismatch in the shared-handler test; the fixture was corrected before the passing run. No production-code rollback was needed.
- Backup before source/test edits: `backup/course1-duplicate-start-race-20261106`, created from `4497116fae28d869d01ed6ca8cf75915c2e1b8fa`. Backup before the test-fixture correction: `backup/course1-duplicate-start-test-fixture-20261106`, created from `8d8c80ffe70006911f37bf576755268d3ad9db02`. Backup before this audit-log update: `backup/course1-duplicate-start-ci-log-20261106`, created from `d7a9cee590b3a55f89dac261144338a2954ce05a`.
- Scope: deterministic mocked Telegram callback interleaving and repository CI only. This does not verify live Telegram delivery, multiple bot processes, Botkeep runtime, production DB, or deployment. No `main` changes; PR #118 remains Draft/open/unmerged.


## Course 1 delayed selection acknowledgement versus submit callback — 2026-11-06

- Deterministic interleaving review identified a stale-keyboard race in all three Course 1 quiz handlers. A `pick:` callback commits `selected_index` before awaiting Telegram callback acknowledgement. If a `submit` callback is processed while that acknowledgement is pending, submit advances the question and edits the message with feedback; the delayed pick callback could then resume and restore the previous question's answer keyboard.
- Added a post-acknowledgement state check before the selection-keyboard edit in `arami_lesson1_telegram.py`, `arami_lesson5_telegram.py`, and `arami_course1_telegram.py`. The edit now proceeds only while the same session and active message remain current, the question index has not advanced, and the selected option still matches the callback. Lesson 5 and the shared handler now snapshot the question before awaiting acknowledgement, matching the dedicated Lesson 1 flow.
- Added one deterministic async regression test to each of `tests/test_arami_lesson1_telegram.py`, `tests/test_arami_lesson5_telegram.py`, and `tests/test_arami_course1_telegram.py`. Each delays the pick callback acknowledgement, processes submit against the same message, then releases the delayed acknowledgement and verifies that the stale selection callback does not edit the answer keyboard after submit has advanced the session.
- Source commits: Lesson 1 `a54a2bdc8361e5e608fa6b781a0d8197d5735ecc`; Lesson 5 `e8640872f1875f3c7eb426af2e79e6638cd93861`; shared Course 1 `67ab046917dafa837321755b3b37ff023a401cdd`. Test commits: `8f2481747913d4dcaa4e12cbfb6a64b08c8db2c3`, `89ab2026bd047ce893846d510cf132d9d1b80835`, and final `50df6bd40c1238d8e885fb385ff4edd5d46d76c3`.
- CI for `50df6bd40c1238d8e885fb385ff4edd5d46d76c3`: Python checks passed; compileall passed; `Ran 433 tests`; `OK (skipped=11)`. Orthography course structure workflow passed.
- Backup before handler/test edits: `backup/course1-pick-submit-interleave-20261106`, created from `338bca02307d3e52bd4787fb80b0eb3504bbdf28`. Backup before this audit-log update: `backup/course1-stale-pick-keyboard-ci-log-20261106`, created from `50df6bd40c1238d8e885fb385ff4edd5d46d76c3`.
- Scope: deterministic mocked callback interleaving and repository CI only. This covers the delay between state selection and callback acknowledgement; it does not establish ordering guarantees for Telegram API edits already in flight, live Telegram behavior, multi-process callback coordination, Botkeep runtime, production DB, or deployment. No `main` changes; PR #118 remains Draft/open/unmerged.


## Course 1 assessment reward identity and idempotency audit — 2026-11-06

- Compared the dedicated Lesson 1 and Lesson 5 result handlers, the shared Course 1 result handler, and the production reward adapter in `bot.py`. All three handler paths pass the canonical lesson ID to `award_arami_assessment`; that adapter consistently namespaces the database ledger key as `arami_assessment:{lesson_id}` and requests exactly 20 points. Thus the dedicated and shared paths for the same lesson converge on the same reward identity, while distinct lesson IDs remain separate.
- Reviewed `database.complete_quiz_with_rewards`: it uses `BEGIN IMMEDIATE`, reads the user's `completed_quizzes` ledger, and updates the ledger, test count, score, XP, and level in one transaction. A repeated key for the same user returns `False` without a second grant. Existing database tests already cover concurrent same-key claims and independent Lesson 1 / Lesson 5 keys.
- No production defect was found in the reward-key composition or the transaction-level duplicate guard. Added `test_assessment_reward_uses_one_stable_user_and_lesson_scoped_key` in `tests/test_bot_quiz_callbacks.py` to pin the adapter contract: same user + same lesson repeats the same key; a different lesson gets a distinct key; all calls request 20 points.
- Test commit: `545c038297c8876ef9264d55060b7d9b8d2e7c28`. CI: Python checks passed, compileall passed, `Ran 434 tests`, `OK (skipped=11)`; orthography course structure workflow passed.
- Backup before the test change: `backup/course1-reward-namespace-identity-20261106`, created from `fc8b6c85e3d91ef4b129e40123d522bcbacc823b`. Backup before this audit-log update: `backup/course1-reward-identity-audit-log-20261106`, created from `545c038297c8876ef9264d55060b7d9b8d2e7c28`.
- Scope: source inspection, deterministic unit tests, and repository CI. This does not validate an actual production database file, live Telegram behavior, multi-process deployment behavior, Botkeep storage, or recovery. No production reward data was changed. No `main` changes; PR #118 remains Draft/open/unmerged.


## فهرستی یەکگرتووی پاراستنی کارە ئەنجامدراوەکان — 2026-11-06

ئەم بەشە پوختە و فهرستی ڕێنیشاندەری تۆمارە پێشووەکانە؛ هیچ تۆمارێکی پێشوو ناسڕێتەوە و جێگایان ناگرێتەوە. وردەکاریی هەر کارێک لە بەشی تایبەتی خۆیدا لە هەمان بەڵگەنامەدا پارێزراوە. تۆماری ناوەڕۆکی کۆرسی ٣ بە جیاوازی لە `course_data/UNIFIED_ORTHOGRAPHY_COURSE3_AUDIT.md` دەمێنێتەوە.

### A) کارەکانی کۆرسی ١ و کویز/تاقیکردنەوە
- گەڕاندنەوەی دۆخی کویز دوای هەڵەی ناردنی feedback، پرسیاری داهاتوو، ئەنجامی کۆتایی و تۆمارکردنی خەڵات؛ بە پشتبەستن بە ledgerی idempotency بۆ نەبوونی خەڵاتی دووبارە.
- retryی ناردنی وانەی ئۆتۆماتیکی کۆرسی ٣ی ئارامی و پیشاندانی پڕۆفایلی پێشکەوتنی فێرخواز.
- پاراستنی زنجیرەی کردنەوەی وانەکان و پێداویستی تەواوکردنی وانە پێش دەستگەیشتن بە تاقیکردنەوەی کۆرسی ١؛ ڕاهێنان لە وانەی کراوەدا بەردەوامە.
- چاکسازیی retry بۆ ئەنجامی تاقیکردنەوە و پاشەکەوتکردنی خەڵات لە هاندڵەرە تایبەتەکانی وانەی ١ و ٥ و هاندڵەری هاوبەش.
- پشکنینی callback ـە هاوکاتەکان: submitی دووبارە، دەستپێکردنی دووبارەی وانە، acknowledgementی دواکەوتووی هەڵبژاردنی وەڵام، و نەهێشتنی keyboardی کۆن دوای گواستنەوە بۆ پرسیاری داهاتوو.
- پشکنینی callbackی هەڵە و ژمارەی هەڵبژاردنی نادروست؛ callback دەبێت acknowledge بکرێت و stateی هەڵە نەگیرێت.
- پشکنینی ناسنامەی خەڵات: هەمان user و هەمان lesson بە هەمان کلیلی `arami_assessment:{lesson_id}` دەگەن؛ وانە جیاوازەکان کلیلی جیاوازیان هەیە؛ transactionی `BEGIN IMMEDIATE` و ledger دووبارەخەڵاتکردن ڕادەگرن.
- تاقیکردنەوەی نوێی ناسنامەی خەڵات زیاد کرا: `test_assessment_reward_uses_one_stable_user_and_lesson_scoped_key`.

### B) سنووری CI و بەڵگە
- لە کۆمیتی `545c038297c8876ef9264d55060b7d9b8d2e7c28`: `compileall` سەرکەوتوو؛ ٤٣٤ تاقیکردنەوە، `OK (skipped=11)`؛ پشکنینی پێکهاتەی کۆرسی ڕێنووس سەرکەوتوو.
- کۆمیتی دواتری تۆماری ئەم پوختەیە تەنیا بەڵگەنامەی audit زیاد دەکات؛ CIی سەرچاوە و تاقیکردنەوە بۆ کۆمیتی پێشووی کۆد جێبەجێ کراوە. دۆخی CIی کۆمیتی audit-log لە کاتی نووسینی ئەم تۆمارەدا هێشتا پشتڕاست نەکراوەتەوە.
- تاقیکردنەوەکان unit/mock ـن؛ بەڵگەی کارکردنی Telegramی ڕاستەقینە، داتابەیسی بەرهەمهێنان، runtimeی Botkeep یان deployment نین.

### C) پشکنینی مانەوەی داتا و سنووری deployment
- PTB persistence backend دانەمەزراوە؛ assessment session ـەکان لە `context.user_data` ـی ناو پرۆسەدا هەڵدەگیرێن و لە restartدا لەدەست دەچن. ledgerی خەڵات دەتوانێت دووبارەخەڵاتکردن ڕابگرێت، بەڵام پرسیار/وەڵام/ئەنجامی sessionی لەدەستچوو ناگەڕێنێتەوە.
- پێشنیاری چارەسەری persistenceی بەردەوام پێویستی بە expiry/cleanup، گواستنەوەی atomicی session و خەڵات، پاراستنی دەرئەنجامی خەڵات، ڕەتکردنەوەی message IDی کۆن و بیرکردنەوە لە هاوکاتیی چەند پرۆسە هەیە. تا دڵنیایی لە backup و storageی بەردەوام نەبێت، ئەم گۆڕانکارییە جێبەجێ ناکرێت.
- کێشەی backupی Botkeep هێشتا چارەسەرنەکراوە و چاوەڕوانی وەڵامی تیمی پشتگیرییە. تا دڵنیایی لە recovery point و پاراستنی `kejyar.db` و فایلەکان نەدرێت، restore، reset، restart، سڕینەوەی backup یان نووسینەوەی فایلەکانی Botkeep قەدەغەیە.
- هیچ live Telegram، production DB migration، Botkeep runtime test یان deployment لەم کارانەدا ئەنجام نەدراوە.

### D) پاراستن و دۆخی ڕیپۆزیتۆری
- هەموو تۆمارە وردەکانی پشکنین و CI لە بەڵگەنامەی runtime audit و تۆماری جیاوازی کۆرسی ٣دا هەڵگیراون؛ backup branch ـەکانی پێش هەر دەستکارییەکیش بە ناوی خۆیان لە GitHubدا پارێزراون.
- backupی پێش زیادکردنی ئەم پوختەیە: `backup/work-preservation-index-20261106`، لەسەر HEADی `0cbd3f737ec1a143c4008c9cf7b310a90d8fdcd0`.
- لقەی کار: `audit/course3-lessons-31-40`. PR #118 کراوە و Draft ـە و merge نەکراوە. `main` لە `bde4b44ddf5127e6c9762d014fd7d2cde2dc0423` ماوەتەوە؛ هیچ گۆڕانکارییەکی لەسەر نەکراوە.
- ئەم پوختەیە تۆماری پاراستن و ڕێنیشاندەرە، نە پەسەندکردنی بەرهەمهێنان. هەر کاری داهاتوو دەبێت بە backupی نوێ، بەڵگەی تاقیکردنەوە و زیادکردنی تۆمار بەبێ سڕینەوەی مێژووی پێشوو بەردەوام بێت.


## پەیوەستکردنی فهرستی ناوەندیی پاراستن — 2026-11-06

- فهرستی ناوەندیی شوێنکەوتن و backup refs لە `docs/WORK_PRESERVATION_INDEX_2026-11-06.md` زیاد کرا. ئەو فایلە ٩٥ backup branchی دۆزراوە لە GitHub، SHAی هەر یەک، کۆمیتە گرنگەکانی کار، شوێنی audit ـەکان و سنووری CI/runtime تۆمار دەکات.
- کۆمیتی دروستکردنی فهرست: `8c8de73391871e427975b3d7cfd51db92de3cb57`.
- Backup پێش پەیوەستکردنی ئەم تۆمارە: `backup/preservation-index-crosslink-20261106`، لە HEADی `8c8de73391871e427975b3d7cfd51db92de3cb57`.
- فهرستەکە لە هەمان لقی کارە و بە تەنیا backupی سەربەخۆی دەرەکی نییە؛ بۆ پاراستنی زیاتر، mirrorێکی سەربەخۆ پێویستە. کێشەی Botkeep هێشتا چارەسەر نەکراوە.

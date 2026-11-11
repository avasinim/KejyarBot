# Main-Based Release Validation and Runtime Readiness Checkpoint — 2026-11-11

## Release candidate
- Repository: `avasinim/KejyarBot`
- Isolated branch: `release/main-based-review-gates-2026-11-11`
- Verified branch snapshot: `aecd59ea` (GitHub Actions head SHA)
- Main base: `7db20f242087e3eb9149e2e788f6c20529870f32`
- Compare to main: 76 commits ahead, 0 behind; 32 changed paths; 10 added, 22 modified, 0 removed.
- No merge or main-branch update was performed.

## Scope of the 32 changed paths
- Runtime: `bot.py`, `course_runtime.py`, three Arami callback modules.
- Course 4: 50-lesson source data, 50 quiz override records, 50-lesson curriculum plan, course manifest.
- Provenance: original source drafts for Lessons 47–50 and the capstone appendix.
- Tests: academic review/reward gates, Arami callback routes, Course 4 beta and quiz overrides, menu/search behavior, database migration regression.
- CI workflows: Python checks, Course 4 beta safety, Course 4 50-lesson validation, quiz override validation, review-gate regression, orthography structure.
- No files were removed. In particular, no PDFs or original lesson sources were deleted in this release branch.

## Verified Course 4 source state
- 50 lesson records; 50 plan entries; 50 manifest lesson IDs.
- 248 original quiz questions remain in the authored lesson source.
- Review status counts: 30 `scientific_review_complete_with_qualified_notes`; Lesson 13 is `internal_cross_lesson_synthesis_no_external_source_mapping`; 19 lessons (32–50) are `owner_review_pending_expanded_draft`.
- Lessons 32–50 have empty quiz arrays and remain Beta/read-only for official assessment/rewards.
- Lesson 13 retains the main-side internal source-map review status and remains Beta-only; its source map and terminology crosswalk are preserved in the archive.
- 50 quiz overrides are in a separate append-only file. Every original snapshot matches its exact source question; 44 target Lessons 1–30 and 6 target Lesson 31. The original 248 question records are not rewritten by the override loader.
- The override loader validates course ID, duplicate keys, exact source snapshots, question text, four unique options, answer index, and explanation before applying in-memory replacements.

## Verified cross-course gates
- Every active course requires an explicit status in the academic approval allowlist before official quizzes/rewards/badges.
- Arami Course 1 uses its own manifest status gate; source receipt/preservation is not academic approval.
- Global assessment menus omit unapproved Arami lessons. Shared, dedicated Lesson 1, and dedicated Lesson 5 callback routes require an explicit permission callback; absence of the callback fails closed.
- Arami reward helper independently checks course membership and review status before writing.
- Quiz answer callbacks revalidate the lesson status before accepting an answer and again before official reward ledger writes. An already-open draft Latin quiz may finish only as unscored Beta practice; it cannot reveal the answer key, increment score, or grant rewards.
- Beta lesson completion writes only the separate Beta-progress ledger. Official XP, coins, chests, badges, lesson completion and quiz completion remain blocked for review lessons.
- Badge generation stops before Beta lessons; stale legacy completion rows cannot promote a Beta lesson to official status.

## CI on the exact release snapshot
All six workflows completed successfully on `aecd59ea`:
1. Python checks — `510 tests`, 11 skipped; compileall passed.
2. Course 4 beta review safety — `510 tests`, 11 skipped.
3. Course 4 50-lesson beta validation — `510 tests`, 11 skipped.
4. Course 4 quiz override validation — `510 tests`, 11 skipped.
5. Review-gate regression validation — `510 tests`, 11 skipped.
6. Orthography course structure — 4 dedicated tests passed.

Run links:
- https://github.com/avasinim/KejyarBot/actions/runs/43014288490
- https://github.com/avasinim/KejyarBot/actions/runs/43014288509
- https://github.com/avasinim/KejyarBot/actions/runs/43014288651
- https://github.com/avasinim/KejyarBot/actions/runs/43014288645
- https://github.com/avasinim/KejyarBot/actions/runs/43014288627
- https://github.com/avasinim/KejyarBot/actions/runs/43014288575

## Database and deployment boundary
- `database.py` has the same Git blob SHA as main: `812df0aeb6dba9b8cf33e7582ec677e509f9462d`; no database code change is part of this release.
- The additive Beta-ledger migration and idempotency behavior were previously rehearsed on a disposable copy of the KejyarBot-Test backup. No live DB write occurred.
- Main branch remains unchanged at `7db20f242087e3eb9149e2e788f6c20529870f32`.
- No Botkeep import, restore, restart, Railway deployment, live database write, or main-bot deployment occurred.
- Botkeep Node17 import remains blocked until written support clearance. The earlier import failure was in infrastructure staging before application file movement; bypassing the support hold would risk the test runtime and is not acceptable.
- A GitHub release branch and green CI do not prove Botkeep runtime activation. Runtime activation still requires an approved import, fresh Botkeep runtime confirmation, Telegram smoke tests, and post-import DB integrity verification.

## Next operational sequence
1. Keep this exact release snapshot frozen while Botkeep support reviews Node17.
2. Once written clearance arrives, import only the verified release SHA into the test bot, never the main bot.
3. Verify startup, course menus, reading access, Beta progress, assessment denial, reward ledger, quiz override behavior, Arami dedicated routes, and Telegram getUpdates/webhook behavior.
4. Back up and verify the test DB before and after import; compare learner rows and progress values.
5. Only after test-bot runtime verification should a separate file-scoped main release be considered.

This checkpoint is a source/CI release-readiness record, not a runtime deployment or a claim that the bot is already available to learners.

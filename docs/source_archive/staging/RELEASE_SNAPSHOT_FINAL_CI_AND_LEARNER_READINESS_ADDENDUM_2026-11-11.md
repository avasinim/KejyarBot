# Release Snapshot Addendum — Final CI and Learner-Readiness Reconciliation — 2026-11-11

## Exact snapshot
- Release branch: `release/main-based-review-gates-2026-11-11`
- Latest validated SHA: `03e2efb2a40838cb71fdcb02b3692a1203c2b22d`
- Main SHA remains: `7db20f242087e3eb9149e2e788f6c20529870f32`
- Compare: release is 84 commits ahead, 0 behind main; 35 changed paths (13 added, 22 modified, 0 removed).
- No `.env`, token, secret, or `database.py` change is included. `database.py` has the same blob SHA as main: `812df0aeb6dba9b8cf33e7582ec677e509f9462d`.
- No PDF or original lesson source was deleted.

## Final CI on exact SHA `03e2efb2`
All six workflows passed:
- Python checks: 513 tests, 11 skipped.
- Review gate regression validation: 513 tests, 11 skipped.
- Course 4 beta review safety: 513 tests, 11 skipped.
- Course 4 50-lesson beta validation: 513 tests, 11 skipped.
- Course 4 quiz override validation: 513 tests, 11 skipped.
- Orthography course structure: 4 dedicated tests passed.

The 11 skips are explicitly retired legacy 22-lesson Course 1 tests; the Arami 21-lesson replacement is covered by current interaction tests. Three new regression tests explicitly verify that missing permission callbacks fail closed for shared Arami, dedicated Lesson 1, and dedicated Lesson 5 assessment routes.

## Active learner readiness
- Active courses: 203 lesson records total.
- Explicitly approved: 30 Course 4 lessons.
- Review-gated: 173 lessons (all 21 Arami, all 42 Course 2, all 66 Course 3, all 24 Latin-course lessons, plus Course 4 Lesson 13 and Lessons 32–50).
- Course 4: 50 lesson records, 50 plan entries, 50 manifest IDs, 248 original authored quiz questions, 50 source-verified append-only overrides.
- Lesson 13 remains `internal_cross_lesson_synthesis_no_external_source_mapping` and Beta-only; its internal map/crosswalk does not assert external source verification.
- Course 4 Lessons 32–50 remain Beta/read-only and have no quiz bank.

## Clarification: Beta quiz behavior
The practice menu and new quiz-start route do not expose or start unapproved Latin/Course 2/Course 3 quizzes. If a draft interactive quiz session was already open before the review gate changed, the session may finish only as unscored Beta practice: responses are accepted, answer keys are not revealed, score is not incremented, and no official reward/completion ledger is written. All new starts remain blocked until explicit academic approval.

Arami lessons retain reading and restricted practice routes. Official Arami assessment menus and all three callback routes are hidden/blocked unless an explicit permission callback confirms academic approval. Missing permission callbacks fail closed; dedicated Lesson 1 and Lesson 5 menu builders now hide assessment by default.

## Deployment boundary
This exact release SHA is source- and CI-validated, not runtime-validated. No Botkeep import, restore, replace, restart, live DB write, Railway deployment, or main-bot deployment has occurred. Botkeep Node17 written support clearance remains outstanding in the available conversation context; the earlier staging file-access failure must not be bypassed. The Telegram token previously visible in a screenshot should be rotated before any live smoke test.

A limited learner pilot cannot be declared live until the exact SHA is imported into `KejyarBot-Test` through the supported route, the applied revision is confirmed, database integrity/progress are compared, and the smoke-test runbook passes. No academic approval is inferred from CI.

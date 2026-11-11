# KejyarBot-Test Runtime Smoke-Test Runbook — 2026-11-11

## Release snapshot to test
- Repository: `avasinim/KejyarBot`
- Branch: `release/main-based-review-gates-2026-11-11`
- Exact source SHA: `aecd59ea5af7371bd1139e85d1279001f320e2ab`
- Main base: `7db20f242087e3eb9149e2e788f6c20529870f32`
- CI: six workflows green; Python suite 510 tests, 11 skipped; Orthography structure 4 tests.
- Target: `KejyarBot-Test` only. Never import this snapshot into the main learner bot.

## Preflight — hard stop conditions
1. Obtain written Botkeep support clearance for Node17 and the earlier staging file-access failure. Do not use restore/import/replace workarounds to bypass this.
2. Rotate the Telegram bot token previously visible in a screenshot before running any Telegram smoke test. Use the newly rotated token only in Botkeep's secret environment; never paste it into chat, GitHub, logs, or screenshots.
3. Take a fresh Botkeep-Test database backup and verify its SHA-256, archive listing, SQLite `integrity_check`, and row counts. Do not use a main-bot database.
4. Record the current Botkeep applied revision and confirm the current runtime is stable before importing.
5. Confirm Node17 resource/space health with support. If any preflight check fails, stop and preserve the current runtime.

## Import and startup
1. Import the exact SHA above into `KejyarBot-Test` only.
2. Do not import from `main`; do not select a moving branch head when the exact SHA is available.
3. Confirm the import operation reports completion and the applied revision equals the exact SHA.
4. Start the test bot once only after the import is confirmed. Do not repeat a failed import or restart while the runtime state is uncertain.
5. Confirm the application starts without syntax, missing-file, manifest, or quiz-override validation errors.
6. Confirm Telegram polling/webhook behavior is stable and there is only one active polling process.

## Learner-facing smoke tests
### Global navigation and courses
- `/start` returns the expected Kurdish welcome and course menu.
- Course 1 Arami lists all 21 lessons; Course 2 lists 42; Course 3 lists 66; each Kurmanji Latin course lists 12; Course 4 lists 50.
- Course menus paginate and edit the existing message rather than duplicating menu messages.
- Lesson search starts clean, paginates results, and selecting a menu item exits search mode.

### Reading and Beta progress
- A learner can read a pending lesson and sees the Beta/review notice without loss of source text.
- Completing a pending lesson records only `beta_completed_lessons`; it must not change XP, score, coins, chests, badges, official completed lessons, or official completed quizzes.
- A repeated Beta completion is idempotent.
- Beta progress unlocks only the next still-pending lesson in that course; it does not count as official completion after approval status changes.

### Academic assessment and rewards
- A pending Course 2, Course 3, Latin, or Course 4 lesson cannot start an official quiz.
- A pending lesson cannot enter the official assessment menu.
- A stale quiz callback for a lesson that has become pending is cleared or can finish only as unscored Beta practice; no correct answer key, score, XP, or official quiz ledger is written.
- Course 4 Lessons 32–50 have no quizzes and remain Beta-only.
- Course 4 Lesson 13 remains Beta-only with status `internal_cross_lesson_synthesis_no_external_source_mapping`.
- Course 4 Lesson 31 uses the validated replacement questions; the 248 authored source questions remain unchanged.

### Arami Course 1
- Reading and practice routes work for Lessons 1 and 5 dedicated handlers and shared Lessons 2–4 and 6–21.
- Official assessment menus do not show unapproved Arami lessons.
- Direct callback attempts for `arami1:assessment`, `arami5:assessment`, and `aramiC:assessment` fail closed.
- Omitting the permission callback in any dedicated handler must not activate assessment.
- Direct calls to the Arami award helper for unapproved/non-Arami lesson IDs must not change the reward ledger.

## Database verification
- Run `PRAGMA integrity_check` after startup and after smoke tests.
- Confirm the additive `beta_completed_lessons` column exists and defaults to an empty value for existing learners.
- Compare user count, completed lesson arrays, quiz ledger, score, XP, coins, chests, and badges with the pre-import backup; only intentional test-user Beta progress may differ.
- Do not run a migration against main-bot data.

## Rollback and incident handling
- If import or startup state is ambiguous, do not issue another import, restore, replace, or restart. Capture the current revision/status and return to Botkeep support.
- If SQLite integrity or learner-progress comparison fails, stop learner access and preserve both before/after backups for support diagnosis.
- Do not deploy to Railway or merge to `main` during this test.
- Only after every smoke test passes should the exact tested SHA be considered for a separate main-bot promotion plan.

## Current status
This is a prepared runbook, not evidence of a completed Botkeep import. Node17 support clearance has not been confirmed in the available conversation context. No runtime import, restart, live database write, Railway deployment, or main-bot deployment has occurred.

# KejyarBot-Test Runtime Smoke-Test Runbook — Release SHA 03e2efb2 — 2026-11-11

## Exact release to test
- Repository: `avasinim/KejyarBot`
- Branch: `release/main-based-review-gates-2026-11-11`
- Exact SHA: `03e2efb2a40838cb71fdcb02b3692a1203c2b22d`
- Main base: `7db20f242087e3eb9149e2e788f6c20529870f32`
- CI on this SHA: six workflows passed; 513 tests, 11 retired legacy tests skipped; orthography workflow passed 4 dedicated tests.
- Target: `KejyarBot-Test` only. Never import this SHA into the main learner bot.

## Hard preflight stops
1. Obtain written Botkeep support clearance for Node17 and the earlier staging file-access failure. Do not use restore/import/replace workarounds to bypass this.
2. Rotate the Telegram bot token previously visible in a screenshot before any Telegram smoke test. Store the new token only in Botkeep's secret environment; never paste it into chat, GitHub, logs, or screenshots.
3. Take a fresh Botkeep-Test database backup. Verify archive listing, SHA-256, SQLite `integrity_check`, and row counts. Never use main-bot data.
4. Record current Botkeep applied revision and confirm the existing runtime is stable.
5. Confirm Node17 resource/space health with support. If any preflight fails, stop.

## Import and startup
1. Import exact SHA `03e2efb2a40838cb71fdcb02b3692a1203c2b22d` into `KejyarBot-Test` only.
2. Do not import from `main` or a moving branch head.
3. Confirm import completion and exact applied revision.
4. Start the test bot once only after import is confirmed.
5. Confirm no syntax, missing-file, manifest, or quiz-override validation errors at startup.
6. Confirm Telegram polling/webhook behavior is stable and only one polling process is active.

## Learner-facing smoke tests
### Navigation
- `/start` returns the expected Kurdish welcome and course menu.
- Course 1 Arami: 21 lessons; Course 2: 42; Course 3: 66; two Latin courses: 12 each; Course 4: 50.
- Course menus paginate and edit the existing message rather than duplicating it.
- Lesson search starts clean, paginates, and exits search mode when a menu item is selected.

### Reading and Beta progress
- A pending lesson is readable and displays its Beta/review notice without losing source text.
- Completing a pending lesson writes only the separate Beta progress ledger; XP, score, coins, chests, badges, official lesson completion, and official quiz completion must not change.
- Repeated Beta completion is idempotent.
- Beta progress unlocks only the next pending lesson; stale Beta rows do not become official completion after approval status changes.

### Assessments and rewards
- Pending Course 2, Course 3, Latin, and Course 4 lessons cannot start new official quizzes.
- Pending lessons do not appear in official assessment menus.
- A stale interactive quiz that was already open before the gate changed may finish only as unscored Beta practice: accept responses, hide the answer key, do not increment score, and do not write reward/completion ledgers.
- Course 4 Lessons 32–50 are Beta-only with empty quiz banks.
- Course 4 Lesson 13 remains Beta-only with status `internal_cross_lesson_synthesis_no_external_source_mapping`.
- Course 4 Lesson 31 uses the source-validated replacement questions; all 248 authored quiz questions remain unchanged.

### Arami
- Reading and restricted practice work through shared Lessons 2–4 and 6–21 and dedicated Lesson 1 / Lesson 5 routes.
- Official assessment menus omit unapproved Arami lessons.
- Direct callback attempts for `arami1:assessment`, `arami5:assessment`, and `aramiC:assessment` fail closed.
- Missing permission callbacks in dedicated Lesson 1 and Lesson 5 routes do not expose assessment.
- Direct calls to the Arami reward helper for unapproved or non-Arami IDs do not change the reward ledger.

## Database verification
- Run `PRAGMA integrity_check` after startup and after smoke tests.
- Confirm additive `beta_completed_lessons` column exists and defaults empty for existing learners.
- Compare user count, official completed lesson arrays, completed quiz ledger, score, XP, coins, chests, and badges with the pre-import backup; only intentional test-user Beta progress may differ.
- No migration or test is to touch main-bot data.

## Rollback / incident handling
- If import or startup state is ambiguous, do not issue another import, restore, replace, or restart. Capture current revision/status and return to Botkeep support.
- If SQLite integrity or learner-progress comparison fails, stop learner access and preserve before/after backups for support diagnosis.
- Do not deploy to Railway or merge to `main` during this test.
- After all smoke tests pass, freeze the exact tested SHA and prepare a separate main-bot promotion plan; do not auto-promote.

## Current status
This is a prepared runbook, not evidence of a completed Botkeep import. Node17 written support clearance is not confirmed in the available conversation context. No runtime import, restart, live DB write, Railway deployment, or main-bot deployment has occurred.

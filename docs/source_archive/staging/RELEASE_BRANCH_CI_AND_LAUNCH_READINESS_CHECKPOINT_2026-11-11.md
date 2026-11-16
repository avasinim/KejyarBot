# Main-based release branch — CI and launch-readiness checkpoint
Date: 2026-11-11
Branch: `release/main-based-review-gates-2026-11-11`
Base main SHA: `7db20f242087e3eb9149e2e788f6c20529870f32`
Validated branch head: `ae67a9245af7371bd1139e85d1279001f320e2ab`

## Scope and preservation

- This is an isolated release branch. `main` was not changed, no pull request was opened, and no deployment/import/restart was performed.
- Course 4 lesson records 1–46 are restored from the current main branch without wholesale candidate replacement. Lessons 47–50 alone were appended from the preserved V2 draft records.
- Course 4 now has 50 ordered lesson IDs in source data, curriculum plan, and course manifest.
- The 248 original quiz questions remain in Lessons 1–31. Lessons 32–50 have no quiz bank and remain review drafts.
- Lesson 13 retains `internal_cross_lesson_synthesis_no_external_source_mapping`; it is Beta-only pending reconciliation. No external page/source mapping is claimed.
- The 50 quiz override records use exact original snapshots; all 50 snapshots match the main source records. Overrides are validated before in-memory replacement; original lesson JSON and original quiz records remain intact.
- The four new lesson source drafts and related provenance are preserved under `docs/source_archive/staging/drafts/`.

## Runtime safety changes

- Active courses require an explicit academic approval status; missing, draft, and unrecognized statuses fail closed.
- Unapproved Arami lessons remain readable/practice-only; official assessment callbacks and direct reward helper are gated.
- Main quiz callbacks re-check academic availability before official reward writes and reject malformed Unicode numeric callbacks safely.
- Latin draft interactive practice can collect responses without exposing answer keys, calculating official scores, or writing official rewards. Official assessment remains disabled.
- Beta lesson completion uses the separate Beta progress ledger; it grants no XP, coins, chests, badges, or official course completion.
- Course menus, practice/assessment menus, and pagination remain covered by regression tests.

## CI evidence — all successful at the validated head

- Python checks: run [43014495808](https://github.com/avasinim/KejyarBot/actions/runs/43014495808) — 511 tests, 11 skipped, all remaining tests passed.
- Review gate regression validation: [43014495898](https://github.com/avasinim/KejyarBot/actions/runs/43014495898).
- Course 4 quiz override validation: [43014495916](https://github.com/avasinim/KejyarBot/actions/runs/43014495916).
- Course 4 Beta review safety: [43014495856](https://github.com/avasinim/KejyarBot/actions/runs/43014495856).
- Course 4 50-lesson Beta validation: [43014495810](https://github.com/avasinim/KejyarBot/actions/runs/43014495810).
- Orthography course structure tests: [43014495977](https://github.com/avasinim/KejyarBot/actions/runs/43014495977).

## Deployment boundary and remaining launch work

- The Botkeep test bot remains blocked by the previously reported Node17 infrastructure/resource incident. Support has not yet provided the written Node17 clearance in the available conversation context.
- Do not import, restore, replace files, restart, or redeploy Botkeep until that written clearance is received. The failed prior import did not apply files; the database and environment were left unchanged.
- No Railway deployment and no production/main bot deployment were performed.
- CI success validates the branch code and tests; it does not prove that the live Botkeep runtime has loaded this commit or that Telegram end-to-end smoke tests have passed.
- Remaining launch gate: obtain Node17 clearance, apply the validated release to the test bot using the supported route, verify runtime revision and run Telegram smoke tests (start/menu, Course 4 lessons 1–31 quizzes, Beta lessons 32–50 reading/progress, Arami practice/assessment gates, rewards/DB idempotency), then decide whether the main bot can be promoted.

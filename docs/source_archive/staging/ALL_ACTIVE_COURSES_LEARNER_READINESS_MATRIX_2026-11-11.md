# Cross-course learner readiness and release gate — 2026-11-11

Branch: `release/main-based-reconciled-2026-11-11`
Repository base: `main` at `7db20f242087e3eb9149e2e788f6c20529870f32`
Pull request: [#152](https://github.com/avasinim/KejyarBot/pull/152)

## Verified catalogue inventory

The six active course catalogues contain 203 registered lessons:

| Course | Registered lessons | Academic readiness |
|---|---:|---|
| Course 1 — Arami orthography foundations | 21 | 0 explicitly approved; manifest source/review records remain incomplete or pending |
| Course 2 — Daily conversation | 42 | 42 `draft_editorial_review` |
| Course 3 — Unified orthography | 66 | 66 `draft_editorial_review` |
| Course 4 — Kurdish grammar | 50 | 30 approved with qualified notes; Lesson 13 remains internal synthesis/review-only; 19 expanded drafts await owner review |
| Latin orthography | 12 | Draft course; lessons remain `draft_editorial_review` |
| Latin grammar | 12 | Draft course; lessons remain `draft_editorial_review` |
| **Total** | **203** | **30 approved; 173 review-only** |

This is an inventory of current source metadata, not a claim that all 203 lessons have received human academic approval. The 173 review-only lessons can be presented through the explicitly marked Beta/read-only or practice-only paths permitted by the runtime. They must not receive official quiz eligibility, XP, coins, chests, badges, or official completion.

## Runtime safeguards checked

- Academic approval is explicit and fail-closed: missing, unknown, source-received, or draft statuses do not imply approval.
- Beta completion is separate from official completion and reward ledgers.
- Official quiz start and answer callbacks re-check review eligibility; stale sessions are cleared before reward writes.
- Arami assessment buttons and callback routes are disabled unless an explicit approved status is present.
- Course 4 Lesson 13 remains `internal_cross_lesson_synthesis_no_external_source_mapping`; no external source mapping or approval is invented.
- Fifty Course 4 quiz overrides retain exact source snapshots; authored source questions remain unchanged.
- Search pagination and search-mode exit have regression coverage.

## CI evidence at PR head

Validated PR head: `90a2a15e05dd594441b7717b993c5423af93f870`.

- Python checks: 547 tests passed; 11 intentionally skipped; compileall passed.
- Course 4 Beta review safety: passed.
- Orthography course structure: 4/4 passed.
- The four `ERROR` log lines in Python output are expected exception logs inside tests that simulate Telegram delivery failures; the suite concluded `OK (skipped=11)`.

A new cross-course readiness regression test is added in this commit. Its result must be checked in the subsequent CI run before this updated head is considered validated.

## Launch decision

**Not yet approved for a full public launch.** The source branch and tests are healthy, but only 30 of 203 lessons are explicitly academically approved. A controlled learner pilot can expose the approved content and clearly marked Beta reading/practice material, provided the actual deployed runtime is verified first.

The external Botkeep Node17 support blocker remains unresolved in the available record. Do not import, restart, or deploy to Botkeep until the platform's written compatibility/clearance response is received. After clearance, perform a test-bot import using the supported runtime, verify the loaded commit/revision, and complete Telegram end-to-end smoke tests for menus, lesson reading, search, Beta labels/progress, quiz eligibility, reward idempotency, and database persistence. No production database or live Telegram bot was changed by this work.

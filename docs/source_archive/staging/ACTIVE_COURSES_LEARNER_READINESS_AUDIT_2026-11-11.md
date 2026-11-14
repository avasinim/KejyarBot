# Active courses — learner-readiness and academic approval audit
Date: 2026-11-11
Release branch: `release/main-based-review-gates-2026-11-11`
Audited branch head before this note: `f09d828f50d8c19185d8492663a4bf962d483906`

## Scope

This audit reads the active course manifest and the lesson metadata currently loaded by the release branch. It distinguishes:
- content that can be exposed for reading or restricted practice;
- explicit academic approval for official assessments and rewards;
- deployment/runtime readiness, which is a separate infrastructure gate.

## Active course inventory

| Course | Lessons | Explicit academic approval | Current review state |
|---|---:|---:|---|
| Course 1 — Arami orthography foundations | 21 | 0 | All 21 fail closed: 16 source-review pending, 2 source received/preserved, 1 source received with Lesson 5 identity note, 1 user-supplied source preserved, 1 record has no status |
| Course 2 — Daily conversation | 42 | 0 | 42 draft_editorial_review |
| Course 3 — Unified orthography | 66 | 0 | 66 draft_editorial_review |
| Course 4 — Grammar | 50 | 30 | 30 scientific_review_complete_with_qualified_notes; 1 internal_cross_lesson_synthesis_no_external_source_mapping; 19 owner_review_pending_expanded_draft |
| Latin orthography + grammar | 24 | 0 | 24 draft_editorial_review |

Total active lessons: 203.
Explicitly academically approved: 30.
Not explicitly approved and therefore restricted from official assessment/reward: 173.

## Runtime interpretation

- The 30 approved Course 4 lessons may use the normal official assessment/reward path subject to ordinary progression and quiz validation.
- Course 4 Lesson 13 remains Beta-only; its internal cross-lesson source map is not external source reconciliation.
- Course 4 Lessons 32–50 remain Beta review drafts; no quiz bank is fabricated for them.
- All 21 Arami lessons remain without explicit approval in the manifest. They may be made available for reading/restricted practice according to progression, but official assessment and XP rewards remain disabled.
- Courses 2 and 3 and both Latin courses remain editorial-review drafts. Their official assessments/rewards remain gated; any permitted Beta practice must not expose answer keys, award XP/coins/badges, or write official completion.
- Unknown, missing, or non-approved review metadata must continue to fail closed.

## Release and deployment boundary

- The isolated release branch passed all six CI workflows at code head `ae67a924f2f084bfbce48d17791744c79920a451`; Python checks ran 511 tests (11 skipped), all remaining tests passed.
- The current branch head `f09d828f50d8c19185d8492663a4bf962d483906` adds only the previous CI/launch checkpoint note; no runtime source changed after the validated code head.
- This is not a claim that all 203 lessons have received academic approval. The safe learner-facing posture is staged access with the review gates enforced.
- Botkeep remains blocked pending written Node17 infrastructure clearance. Do not import/restore/replace files or restart the test bot before that clearance. No live bot deployment or Telegram end-to-end smoke test is claimed here.

## Launch decision

A safe limited learner pilot can only be considered after Botkeep clearance and verified test-bot smoke tests. A claim of a fully academically approved six-course launch is not supported by current lesson metadata: 173 of 203 active lessons remain review-gated. Academic approval must come from source review, not from bypassing the runtime gate.


## Append-only runtime revalidation — Arami Course 1 (2026-11-12)

Re-read the current branch manifest, shared Course 1 Telegram adapter, dedicated Lesson 1 and Lesson 5 adapters, and their tests after the academic approval gate was added.

### Manifest status and learner-facing behavior
- The 21 lesson records still contain **zero explicitly approved lessons** under the allowlist `scientific_review_complete`, `scientific_review_complete_with_qualified_notes`, or `approved`.
- The 16 `source_review_pending` records, Lesson 5's `source_received_preserved; lesson_identity_confirmed_as_5`, Lessons 14–15 `source_received_preserved`, Lesson 16 `user_supplied_source_received_and_preserved`, and Lesson 1's missing `status` all fail closed for official assessment/reward. Receipt/preservation is not academic approval; a missing status is not approval.
- The catalogue labels non-approved lessons with the Beta/review marker. The shared selector exposes reading and practice, but hides the official assessment button unless explicit approval is present.
- The shared reader displays a Beta-only notice and records Beta completion rather than official completion for lessons without approved status.
- The dedicated Lesson 1 and Lesson 5 adapters also derive assessment-button visibility from `can_take_arami_assessment`; their assessment callbacks fail closed when the permission callback is missing or returns false. Active assessment sessions recheck approval and unlock status before accepting further answers.
- `can_take_arami_assessment` verifies course identity, rejects Beta-review lessons, reads the manifest, and fails closed on missing records or load errors. `award_arami_assessment` rechecks this permission before awarding XP.

### Tests and remaining semantic caution
- The four PR workflows on head `f105a36661bee013d93e169fdc3f4faa0c6f5e81` completed successfully: Python checks, Kurdish months tests, Course 4 beta review safety, and Orthography course structure tests.
- The Arami tests include review-only assessment blocking, missing permission/unlock callback behavior, session revalidation, and no XP award for unapproved assessments. The workflow result is CI evidence, not a live Telegram end-to-end smoke test.
- Manifest records currently label the activation mode as `reader_practice_assessment_enabled_text_only`; that label can be misread as unconditional official assessment availability. Runtime code correctly gates official assessment and rewards by explicit academic approval, but the activation label should be clarified in a future manifest-only, append-only metadata change after confirming every consumer of this field.
- No academic status was promoted, no lesson source or question bank was changed, and no Telegram/Botkeep deployment or live-user data was touched.

### Result
Arami Course 1's current runtime gate is internally consistent with the fail-closed policy: reading and practice can remain available, while official assessments and rewards remain disabled until explicit academic approval. The activation-status wording is a documentation/metadata clarity issue, not evidence that the runtime gate has been bypassed.

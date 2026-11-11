# Cross-Course Callback and Reward Gate Audit — 2026-11-11

## Scope and evidence

Read-only source inspection of branch `botkeep-menu-clean-2026-11-09` in `avasinim/KejyarBot`.
Inspected `bot.py`, `course_lesson_adapters.py`, `latin_course_runtime.py`, and `course_quiz_review.py`. No runtime files, learner records, or deployment settings were changed.

## Confirmed callback path

- `lesson_is_pending_review()` in `bot.py` returns true only for the exact status `owner_review_pending_expanded_draft`.
- `lesson_quiz_is_available()` blocks only Course 4 beta lessons plus lesson keys in the legacy Course 1 allowlist in `course_quiz_review.py`.
- `lesson_keyboard()` suppresses the completion button only for owner-pending non-beta lessons.
- `finish_lesson()` validates lesson identity and ordered access, then sends every non-beta lesson through `complete_lesson_with_rewards()`. Therefore a lesson carrying `draft_editorial_review` is not blocked by its review status and can reach the ordinary completion/reward path.
- `start_quiz()` validates the lesson and ordered access, and the general quiz availability check does not treat `draft_editorial_review` as a block.
- On successful quiz completion, the common path calls `complete_quiz_with_rewards()` after the availability check.
- `open_next_lesson()` and `open_selected_lesson()` validate ordered access with `can_open()`; that protects sequence order but does not itself certify editorial approval.
- The Latin loader assigns `draft_editorial_review` to all 24 loaded Latin lessons. Course 2 Daily Conversation (42) and Course 3 Unified Orthography (66) also carry `draft_editorial_review` in their source records and adapters preserve that status. Their status is not currently a fail-closed completion/quiz/reward gate.
- Course 4 has a separate explicit beta gate for lessons 32–50, but the previously recorded Lesson 13 status/helper mismatch remains a separate release blocker.

## Risk

A draft lesson may be visible in an active course and can pass the normal completion and quiz reward paths even though its editorial status has not been approved. This is a release-policy mismatch, not merely a menu-label issue. A forged or stale callback does not bypass the ordered lesson sequence, but sequence validation is not a substitute for review-status authorization.

## Required release policy decision

Before promoting the candidate, the project owner/editor must choose and document one of these policies for each course:
1. **Approved release:** explicitly mark only source-reviewed lessons approved, then allow official completion, quizzes, and rewards; or
2. **Read-only / beta without rewards:** permit reading or explicitly approved beta progress, but block official quiz scoring and all XP/coins/chests/badges until approval.

Do not infer approval from structural quiz validation, answer-key consistency, or the fact that a course is marked `active` in `courses.json`.

## Required implementation and regression coverage

Apply one centralized, fail-closed eligibility policy and enforce it at every trust boundary:
- lesson open/display and direct callback entry;
- completion callback, including stale/forged callback payloads;
- quiz start, answer selection/submission, and final scoring;
- all completion/reward issuance call sites, including dedicated Arami assessment handlers where relevant;
- next-lesson progression and course/menu visibility where policy requires it.

Add regression tests proving that a `draft_editorial_review` lesson cannot receive official completion, quiz score, XP, coins, chest, or badge rewards; approved lessons retain normal behavior; explicit Course 4 beta lessons retain only their documented beta progress behavior; duplicate callbacks remain idempotent; and direct/stale callback attempts cannot bypass the gate.

## Deployment and data safety

This is an archive-only audit record. It does not change runtime behavior, merge a pull request, deploy to Botkeep/Railway, restart a bot, or modify the SQLite database. Do not retry Botkeep import/restore while the Node17 support incident remains uncleared. Keep test and main bot credentials/databases isolated. Rotate any Telegram token previously exposed in a screenshot before user-facing tests.

## Conclusion

The current candidate is not safe for blanket promotion merely because structural tests pass. First resolve editorial approval policy and close every completion/quiz/reward callback path, then run regression tests against a disposable copy of the test database and obtain fresh Botkeep support clearance before any import.

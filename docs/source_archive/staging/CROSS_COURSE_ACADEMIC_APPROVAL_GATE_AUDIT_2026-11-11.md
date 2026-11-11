# Cross-Course Academic Approval Gate Audit — 2026-11-11

## Scope
Read-only audit of candidate branch `botkeep-menu-clean-2026-11-09` after PR #145 and PR #146. No runtime files were modified by this audit and no deployment/import was attempted.

## Finding
The candidate already implements a centralized, fail-closed approval check in `bot.py`:

- `ACADEMIC_REVIEW_REQUIRED_COURSE_IDS` is derived from every course whose manifest status is `active`.
- `_lesson_requires_academic_approval()` requires a loaded lesson record and an exact `review_status` member of `ACADEMIC_APPROVAL_STATUSES`; missing, empty, or unrecognized review states are therefore not approved.
- Arami Course 1 is checked against its own manifest `status` field through `lesson_is_academically_approved()`; missing status and source-received/source-review-pending states are not approved.
- `finish_lesson()` sends unapproved lessons to the separate beta-progress ledger and does not grant XP, coins, chests, or badges.
- `start_quiz()` and `quiz_answer()` re-check quiz availability, including immediately before the reward write, preventing a stale quiz session from paying out after a lesson becomes pending.
- Badge visibility and badge creation stop at lessons classified as beta review.
- Course 4 lessons 32–50 retain the explicit beta-review classification; Course 4 Lesson 13 remains approved under its existing `scientific_review_complete_with_qualified_notes` status.

## Source status inventory
Candidate source files were read directly from the candidate branch:

- Daily Conversation: 42/42 lessons have `draft_editorial_review`.
- Unified Orthography: 66/66 lessons have `draft_editorial_review`.
- Course 4 Grammar: 31 lessons have `scientific_review_complete_with_qualified_notes`; 19 have `owner_review_pending_expanded_draft`.
- Arami Course 1: 21 lessons use a separate manifest status field; Lesson 1 has no academic status and the remaining lessons are source-review-pending, source-received-preserved, or user-supplied-source-received-and-preserved. None are in the academic approval allowlist.
- Both Kurmanji Latin courses are assigned `draft_editorial_review` by the runtime loader for all 24 lessons.

## Callback/reward path review
The standard Telegram lesson completion handler checks the review gate before choosing either the beta ledger or official reward ledger. The standard quiz start and answer handlers check the same quiz-availability helper. Arami dedicated and shared callbacks receive the same review-gate callback, and their award helper independently checks the gate before calling the quiz reward ledger.

## Conclusion
The earlier concern that absent or unknown review statuses might be treated as approved is not supported by the candidate code: for lessons mapped to active courses, those states fail closed. No additional runtime patch is justified by this audit. The prior partial progress note suggesting a remaining fail-open issue is corrected by this source inspection.

## Safety boundary
This is a source-level audit only. No Botkeep import, runtime restart, live database write, Railway deployment, or main-bot deployment occurred. Botkeep Node17 support clearance is still required before any import/restore attempt.

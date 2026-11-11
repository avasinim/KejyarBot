# Course 2–3 regression-test coverage addendum
## 2026-11-11 | Append-only

Candidate: `botkeep-menu-clean-2026-11-09`

Inspection of `tests/test_activated_courses.py` found a test named `test_lesson_editorial_review_notes_do_not_deactivate_courses`. It asserts that Daily Conversation and Unified Orthography remain catalogue-active while their first lesson has `review_status=draft_editorial_review`. This test does not assert that quiz, completion, XP, coins, chests, or badges are blocked for those draft lessons.

The test suite contains Course 2 and Course 3 progression/pagination tests, but the inspected review-status assertions do not exercise reward enforcement for `draft_editorial_review`. The existing Course 1 quiz-review allowlist is not a substitute for course-wide status enforcement.

Required tests before release:
- draft-editorial lesson cannot start or submit an official quiz;
- draft-editorial lesson cannot complete via direct callback even if a forged callback is sent;
- no XP, coins, chest, official completion, or badge is granted;
- approved lessons still use the normal quiz/reward path;
- beta/read-only lessons preserve their intended progress semantics;
- Course 2 and Course 3 progress remains isolated and contiguous.

No test or runtime source was changed in this audit.

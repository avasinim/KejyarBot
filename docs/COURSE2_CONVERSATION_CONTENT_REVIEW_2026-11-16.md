# Course 2 conversational content review — 2026-11-16

Branch: `fix/course1-menu-label-2026-11-16`

## Scope and structural checks

Inspected all four active Course 2 data files:
- `course_data/daily_conversation_lessons_01_06.json`
- `course_data/daily_conversation_lessons_07_30.json`
- `course_data/daily_conversation_lessons_31_36.json`
- `course_data/daily_conversation_lessons_37_42.json`

Read-only structural validation returned:
- 42 lessons, numbered sequentially 1–42, with no missing or duplicate lesson numbers.
- 306 dialogue turns; every turn has a non-empty speaker and utterance.
- Every lesson has vocabulary, exercises, comprehension prompts, and a role-play activity.
- 87 multiple-choice questions; every question has at least two options, a valid integer answer index, and an explanation.
- All 42 lessons remain `draft_editorial_review`; this review does not approve them scientifically or editorially.

## Confirmed content correction

Lesson 2 asks for a person's origin with `تۆ لە کوێوەیت؟` but the reply is `منیش دانیشتوی ئەم شارەم.`, which states residence rather than origin. The question was corrected to:

`تۆ لە کوێ نیشتەجێیت؟`

This now matches the residence answer without changing the owner-requested reply. A focused regression test was added to `tests/test_daily_conversation_content.py`.

Files changed:
- `course_data/daily_conversation_lessons_01_06.json`
- `tests/test_daily_conversation_content.py`

Commits:
- Content correction: `945b7036d5c6343478efc85257be8738a7514e8c`
- Regression test: `b35f44ca8e2a922092c75fbc5db28b6c4c1cc44b`

## Verification boundary

The preceding branch head `dc13490e35d6686fe2d1da6d2fcb4d1d758c61d3` had a completed successful Python checks workflow. At the time of this record, no workflow run was yet returned for the new head `b35f44ca8e2a922092c75fbc5db28b6c4c1cc44b`; therefore the new content correction and regression test are pending CI verification.

No production runtime, database, token, deployment, course order, or image routing was changed. No image work was performed in this pass.

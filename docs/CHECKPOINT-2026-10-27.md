# KejyarBot — checkpoint before project wrap-up

Date: 2026-10-27

## Safety
- This is a backup/checkpoint branch only.
- Do not merge to main, deploy, activate draft courses, change production bot/token/database, or enable dynamic speech without explicit user permission.
- Keep KEJYAR_ENABLE_DYNAMIC_SPEECH=false.

## Branches
- Working branch: fix/four-course-structure-2026-10-27
- Backup branch: backup/kejy-arbot-before-wrapup-2026-10-27
- Backup branch was created from the working branch head before adding this checkpoint file.

## Work preserved
- Four-course structure in courses.json: Course 1 orthography (22 lessons active), Course 2 daily conversation (12 planned lessons), Course 3 unified orthography (planned), Course 4 grammar (planned).
- Course 1 source and curriculum artifacts:
  - course_data/orthography_original_lessons.json
  - course_data/orthography_foundations.json
  - course_data/orthography_foundations_quiz_draft.json
- Course 2 draft plan and lessons:
  - course_data/daily_conversation_plan.json
  - course_data/daily_conversation_lessons_01_06.json
  - course_data/daily_conversation_lessons_07_12.json
- Structural tests and audit notes are in the working branch, including tests/test_courses_catalog.py and docs/ORTHOGRAPHY_QUIZ_AUDIT.md.
- Recent conversation draft changes include vocabulary/exercise expansion for lesson 7, and prior fixes to sibling counts (lesson 4), date consistency (lesson 9), shopping total/price (lesson 8), direction phrasing (lesson 10), and course vocabulary conventions (ڕێکەوت, سپاس).

## Resume checklist for 2026-10-28
1. Fetch both branches and compare their heads; keep all work on the working branch.
2. Verify lesson 7 typo is corrected to "چایم خواردووەتەوە" (not "چاوم خواردووەتەوە").
3. Verify lesson 12 phrase is "بە پێ دەڕۆین؛ کتێبخانەکە نزیکە." If stale wording remains, correct only the intended draft.
4. Run/review CI for the latest commits; do not claim success without a completed successful run.
5. Continue natural Kurdish-language review of Course 2 drafts, then update tests if needed.
6. Keep Courses 2–4 planned and unactivated until reviewed/approved by the user.
7. No infographic work until source/content intake and review are complete.

## Current known limitations
- Course 2 lesson files are drafts for review, not approved/published curriculum.
- Latest content update to lesson 7 is commit 0abaed9e6c6769e6e49034313c2e7f9467575c33 on the working branch; verify branch head before resuming.

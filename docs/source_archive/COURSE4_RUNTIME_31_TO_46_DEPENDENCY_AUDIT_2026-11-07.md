# Runtime integration dependency map — Course 4 (31 → 46)
**Date:** 2026-11-07  
**Branch:** `feat/course4-clean-port-main-20261106`  
**Scope:** static source inspection only; no runtime or production changes.

## Verified runtime structure
1. `course_data/grammar_course4_lessons.json` contains 31 lesson records, IDs `grammar_01`–`grammar_31`, and a top-level `lesson_count` of 31.
2. `curriculum/grammar_course4_plan.json` declares `lesson_count: 31` and its lesson list ends at lesson 31. Its current state is `active_owner_review_beta`, with replacement state describing owner lessons 1–25 and researched lessons 26–31.
3. `courses.json` registers Course 4 lesson IDs through `grammar_31`.
4. `bot.py` builds `COURSE_LESSON_ORDER` dynamically from the registered course catalogue via `visible_course_lessons(...)`; no separate hard-coded 31-item list was found in the inspected section.
5. `tests/test_course4_grammar_runtime.py` explicitly asserts exactly 31 lesson records, IDs 01–31, a plan count of 31, catalog alignment, and the current fixed per-lesson content schema (3 activities, 5 exercises, 10 comprehension entries, 8 quiz questions).
6. `tests/test_activated_courses.py` also asserts that Course 4 order equals `grammar_01`–`grammar_31` and that the count is 31.

## What this means for safe expansion
A 46-lesson integration cannot be completed by appending lesson records to the runtime JSON alone. The same change set must reconcile:
- lesson data and top-level count in `course_data/grammar_course4_lessons.json`;
- curriculum plan and lesson count in `curriculum/grammar_course4_plan.json`;
- registered `lesson_ids` and course status in `courses.json`;
- exact-count and ID-range expectations in both Course 4 runtime/activation tests;
- any per-lesson content-shape expectations, only where the real lesson content supports them.

The current tests enforce an identical 3/5/10/8 content shape for all 31 existing lessons. New lessons must not be filled with copied, empty, or invented content just to satisfy that schema. If the verified source lessons have a different valid structure, the adapter/schema and tests should be updated deliberately and tested.

## Activation safety
- PR #119 remains open, Draft and unmerged at the time of this inspection.
- The 46-lesson source archive is not a 46-lesson runtime dataset.
- No Botkeep deployment, live database migration, learner-progress write, or production activation was performed.
- Do not change the production course status to active until all 46 lesson records and the corresponding catalog, plan, adapters, tests, backup and deployment checks are ready.

## Next safe sequence
1. Recover or obtain the owner's full source texts for lessons 33–38.
2. Extract and validate 39–45 without losing original text, exercises or answers.
3. Resolve and obtain owner approval for the final lesson 46 version.
4. Prepare the 46-lesson data/plan/catalog/test change together on a test branch.
5. Run the repository test suite and inspect the rendered/runtime lesson sequence.
6. Back up and only then request explicit approval for deployment/activation.

# Latin Course 2 Runtime and Quiz-Handler Linkage Audit — 2026-11-10

**Scope:** Static repository inspection of the Course 2 content loader, manifest linkage, Telegram callback routing, quiz state machine, answer-key parser, tests, and CI workflow. No runtime files, active manifests, databases, Botkeep configuration, or Telegram deployment were changed.

## 1. Runtime content path confirmed

The repository's current runtime path is:

1. `bot.py` imports `load_latin_courses` from `latin_course_runtime.py`.
2. `latin_course_runtime.py` reads:
   - `course_data/latin_course_1_source_aligned_lessons_01_12.md`
   - `course_data/latin_course_2_source_aligned_lessons_01_12.md`
   - `course_data/latin_course_1_quiz_answer_key_draft.md`
   - `course_data/latin_course_2_quiz_answer_key_draft.md`
3. The loader parses 12 lessons per course and creates namespaced IDs `kurmanji_latin_grammar_01` through `_12`.
4. `bot.py` checks the parsed course IDs and lesson IDs against `latin_courses_manifest_draft.json` and the active entries in `courses.json`, then merges the lesson and quiz dictionaries into `LESSON_DATA` and `QUIZ_DATA`.
5. `COURSE_LESSON_ORDER` is derived from the registered course lesson IDs. The progress gate checks the same course-specific sequence.

## 2. Telegram callback chain structurally connected

Static inspection confirms the following path exists:

- Course selection: `course_<course_id>` → `open_course` → `send_course_page`.
- Lesson paging: `coursepage:<course_id>:<page>` → `open_course_page`.
- Lesson opening and completion use namespaced lesson IDs and the shared course-progress map.
- Quiz menu/start: `quiz_<namespaced_lesson_id>_start` → `start_quiz`.
- Both Latin courses are included in `LATIN_COURSE_IDS`; `quiz_requires_submission` therefore selects the select-then-submit interaction.
- Answer selection: `select_answer_<index>` → `select_quiz_answer`; submission: `submit_answer` → `submit_quiz_answer` → `quiz_answer`.
- The question state stores the selected option index and the answer text; the option-shuffle helper preserves the correct answer by text and does not mutate the source bank.
- The handler registrations in `main()` include the corresponding course, page, quiz-start, select, submit, and answer callback patterns.

This establishes source-code linkage only. It does not establish that a deployed Telegram process is running this revision or that a live callback has succeeded.

## 3. Critical staging mismatch: the newly reviewed 62-question draft is not the runtime source

The latest reviewed editorial files are:
- `course_data/latin_course_2_reviewed_draft_2026-11-10.md`
- `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`

They contain 62 questions/answer-key rows: Lesson 8 has 7 questions; each of the other 11 lessons has 5.

The runtime loader does **not** read those reviewed files. It still reads the separate source-aligned document and the older runtime key:
- `course_data/latin_course_2_source_aligned_lessons_01_12.md`
- `course_data/latin_course_2_quiz_answer_key_draft.md`

Those runtime files and their tests are still structured for 60 questions: exactly 5 questions per lesson and 60 answer-key rows.

This is an intentional staging boundary at present, not evidence that the current loader is broken. However, the 62-question reviewed draft cannot simply replace the runtime source/key pair: `latin_course_runtime.py` currently enforces exactly five questions in `_parse_quiz` and exactly 60 key rows in `load_latin_courses`. The test suite independently enforces 60 rows and five questions per lesson. Promoting only the reviewed text/key would therefore fail loader/test validation or leave the edited questions absent from the bot.

**Severity: release/promotion blocker.** Before any future activation, an explicitly approved integration step must decide whether to keep the current 60-question runtime version or intentionally migrate the runtime parser, source paths, answer-key path, tests, and count assertions together to the 62-question reviewed version. Do not mix the reviewed lesson body with the older 60-row key.

## 4. Existing safeguards and coverage

- Loader checks: 12 ordered lessons per course, unique namespaced IDs, valid question/option structure, contiguous A/B/C(/D) option labels, unique options, answer-key row presence, exact answer-text match, and one occurrence of the correct answer.
- Course/manifest checks: separate source parts, manifest lesson IDs, registered active course IDs, and no lesson-ID collision.
- Quiz-state checks: completed-lesson gate, course-order gate, stale message rejection, malformed callback handling, duplicate-answer guard, and safe option randomization.
- Relevant test files include `tests/test_latin_course_runtime.py`, `tests/test_latin_course_2_quiz_keys.py`, `tests/test_latin_courses_manifest.py`, `tests/test_bot_quiz_callbacks.py`, and `tests/test_activated_courses.py`.
- `.github/workflows/python-checks.yml` defines compileall and unittest discovery on supported push/pull-request events.

The tests and workflow were inspected as source; they were **not executed** during this audit. No green CI result is claimed.

## 5. Main-vs-archive comparison

The following runtime-related files have identical Git blob SHAs on `main` and `archive/preservation-audit-2026-11-10` at the time of inspection:
- `bot.py`
- `latin_course_runtime.py`
- `course_data/latin_course_2_source_aligned_lessons_01_12.md`
- `course_data/latin_course_2_quiz_answer_key_draft.md`
- `tests/test_latin_course_2_quiz_keys.py`
- `tests/test_latin_course_runtime.py`

Therefore this audit added no runtime/code changes and did not alter the active main-branch implementation.

## 6. Required next steps before activation

1. Keep the reviewed 62-question draft and key as editorial staging artifacts.
2. Decide explicitly whether the runtime should remain at 60 or move to 62 questions.
3. If 62 is approved, update the loader's exact-count assumptions, parser/test expectations, runtime source/key selection, and answer-key consistency checks as one coordinated change on a review branch.
4. Add a regression test proving that Lesson 8's seventh question reaches the runtime quiz and that all 62 key entries match the runtime options.
5. Run the full test suite and CI, inspect the resulting diff, and obtain explicit authorization before any live deployment.

**Conclusion:** The existing 60-question Latin Course 2 callback/handler path is structurally wired in repository code. The recently reviewed 62-question content is not wired into that path. Preserve this separation until an approved, fully tested integration is made.

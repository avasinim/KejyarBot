# Latin Course 2 — 62-Question Runtime Migration Plan (2026-11-10)

**Status:** Proposal only — not implemented or activated.
**Target branch:** a future dedicated integration branch created only after explicit approval.
**Current review branch:** `archive/preservation-audit-2026-11-10`.

## 1. Immutable baseline

The current runtime remains the 60-question version. Keep these active paths unchanged until an approved integration:
- `latin_course_runtime.py`
- `bot.py`
- `course_data/latin_course_2_source_aligned_lessons_01_12.md`
- `course_data/latin_course_2_quiz_answer_key_draft.md`
- `courses.json`, `course_data/latin_courses_manifest_draft.json`
- Existing runtime and callback tests.

Reviewed 62-question artifacts remain editorial staging files:
- `course_data/latin_course_2_reviewed_draft_2026-11-10.md`
- `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`

Do not replace the runtime source/key with either reviewed artifact in isolation.

## 2. Target count contract

Course 1 remains unchanged: 12 lessons × 5 = 60 quiz items.

Course 2 target:
| Lesson | Expected questions |
|---:|---:|
| 1–7 | 5 each |
| 8 | 7 |
| 9–12 | 5 each |
| **Total** | **62** |

Both Latin courses together therefore contain 122 quiz items, while the total number of lessons remains 24. Lesson IDs, course IDs, manifest order, and progression sequence do not change.

## 3. Required coordinated code changes

### A. Make expected question counts explicit per course

Add a per-course expected-count tuple/map to the loader configuration, rather than globally changing every lesson to seven questions. Example:

```python
COURSE1_QUESTION_COUNTS = (5,) * 12
COURSE2_QUESTION_COUNTS = (5, 5, 5, 5, 5, 5, 5, 7, 5, 5, 5, 5)
```

Attach the correct tuple to each course record in `COURSES`. Pass the expected count for the current lesson into `_parse_quiz(..., expected_count=...)`; replace the hard-coded `len(questions) != 5` check with a comparison to that explicit value. Keep the default forbidden: missing count metadata should raise an error, not silently assume five.

### B. Validate exact answer-key coverage, not only total row count

For each course, construct the exact expected key set:
`{(lesson_number, question_number) for each lesson and question in its configured count}`.

Compare it to the parsed key's key set and report missing and unexpected rows. Also check the expected total (60 for Course 1; 62 for Course 2). Keep the existing checks for:
- duplicate key rows;
- valid option letters;
- key letter points to an existing option;
- key answer text equals that option text;
- exactly one occurrence of the correct answer.

### C. Switch Course 2 source and key as one atomic integration

Only after the candidate source is fully verified, copy the reviewed lesson document into the canonical runtime source path (preserving the previous source file as a separate immutable archive artifact), and copy the reviewed key into the canonical runtime key path (preserving the old key). Do both in the same integration commit as the loader and tests. Never promote the reviewed source without its matching 62-row key.

Course 1 source and key paths must not change.

### D. Update the dedicated answer-key test parser

The current `tests/test_latin_course_2_quiz_keys.py` assumes:
- quiz header exactly `Kuis — 5 pirs`;
- 5 questions per lesson;
- 60 key rows;
- option letters only `A/B/C`.

For the target Course 2 test:
- recognize a numeric quiz count in the heading (e.g. `Kuis — 5 pirs` and `Kuis — 7 pirs`), while retaining the legacy `10. Testa Kejyar` form;
- parse all supported option letters consistently with the runtime parser;
- derive the expected question-key set from the explicit 12-item count tuple;
- assert 62 embedded questions and 62 key rows;
- retain exact answer-letter/text matching for all 62 questions;
- add a specific assertion that Lesson 8 Q7 is present and matches its key row.

### E. Update aggregate runtime tests

In `tests/test_latin_course_runtime.py`:
- change the aggregate quiz total from 120 to 122 (Course 1 60 + Course 2 62);
- assert Course 1 remains five questions per lesson;
- assert Course 2 uses the exact count tuple above, including seven for Lesson 8;
- retain all existing 24-lesson, unique-ID, no-collision, source separation, and progression assertions.

In `tests/test_activated_courses.py` and any other test that assumes every Latin lesson has five questions, replace the global five-question assumption with course-aware counts. Keep submission-mode checks for both Latin courses unchanged.

### F. Keep Telegram handlers stable

No callback format or handler redesign is required for this count-only migration. The existing select-then-submit handlers should receive the seven-question list from `QUIZ_DATA` naturally. Add a handler-level regression test for Course 2 Lesson 8 that verifies:
1. the seventh question is reachable after six submissions;
2. the correct answer is checked against the correct shuffled option mapping;
3. the quiz completes after question seven, not after question five;
4. stale/duplicate submission protection remains intact.

Do not change callback names or course/lesson IDs unless a test reveals a separate defect.

## 4. Validation sequence required before merge

1. Confirm reviewed lesson source has 12 unique, ordered headings and exactly the target quiz counts.
2. Parse all 62 options and confirm each question has unique option text and contiguous labels.
3. Compare every one of the 62 key rows to its exact option text and letter.
4. Confirm Lesson 8 Q7 is parsed by both the loader parser and dedicated test parser.
5. Run focused tests:
   - `python -m unittest tests.test_latin_course_2_quiz_keys`
   - `python -m unittest tests.test_latin_course_runtime`
   - focused callback tests for Latin quiz selection/submission.
6. Run full suite:
   - `python -m unittest discover -s tests`
   - `python -m compileall -q .`
7. Review test output, diff, and CI result; do not infer success from test definitions.
8. Confirm Course 1 still loads exactly 60 questions and all other course IDs/progression are unchanged.
9. Obtain explicit user authorization before any Botkeep/Telegram deployment or active manifest change.

## 5. Rollback

Keep the pre-migration source/key and loader/test revisions intact on the integration branch history. If any parser, key, callback, or progression regression appears, revert the entire coordinated integration commit—not only one of the source/key files. Since no database schema or callback ID migration is planned, rollback should be a code/content revert, but deployment rollback must still be explicitly authorized.


## 7. Test-surface precision notes (2026-11-10)

A follow-up source inspection refined the test inventory above:

- `tests/test_latin_course_2_quiz_keys.py` parses only option labels `A/B/C` and asserts exactly those three labels for every Course 2 question. The runtime parser accepts contiguous labels through `D`. The integration must make the dedicated parser use the same option-label contract as runtime, while retaining per-question validation of the actual option count; do not assume every question must have four options.
- The dedicated key test currently recognizes only `Kuis — 5 pirs` or the legacy `10. Testa Kejyar` heading, constructs a 12×5 expected key set, and asserts 60 rows. These are separate changes from broadening the option-letter parser.
- `tests/test_latin_course_runtime.py` contains the aggregate total 120, the per-lesson five-question assertion, and a bot-loaded per-lesson five-question assertion. Those need course-aware expected counts.
- The inspected `tests/test_activated_courses.py` does not contain a five-question-per-Latin-lesson assertion; it checks other course/assessment behavior. Do not modify it solely for this migration unless a subsequent focused search identifies a concrete Latin-count dependency.
- `tests/test_bot_quiz_callbacks.py` already verifies that a Latin quiz starts with the same question count as `QUIZ_DATA`, but it does not specifically drive Course 2 Lesson 8 through seven select-and-submit cycles. Add that explicit end-to-end handler regression.

This precision note supersedes any broader suggestion in the preceding plan/audit that `test_activated_courses.py` necessarily needs a five-to-seven count update. No code or test file was changed and no test was executed.

## 6. Current blockers and boundaries

- The reviewed 62-question files are not yet runtime inputs.
- The loader's exact-five check and exact-60 key check must be changed together.
- The dedicated key test's quiz-heading parser currently recognizes only `Kuis — 5 pirs`; it will miss the seven-question heading unless generalized.
- Aggregate runtime tests and at least one activated-course test hard-code five questions per Latin lesson.
- The tests and CI have been inspected, not executed in this audit.
- This plan creates no runtime change, no manifest activation, no database change, no Botkeep operation, and no Telegram deployment.

**Recommendation:** Approve a separate, isolated 62-question integration branch only after the reviewed content/key are frozen and the full coordinated test plan above is ready. Until then, preserve the current 60-question runtime and the reviewed 62-question editorial draft as separate versions.

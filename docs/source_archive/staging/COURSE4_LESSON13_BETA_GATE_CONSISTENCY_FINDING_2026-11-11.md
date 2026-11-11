# Course 4 Lesson 13 runtime gate — source/data/test consistency finding
## 2026-11-11 | Append-only audit finding

### Finding
The PR #125 runtime candidate contains a special beta-gate branch for Course 4 Lesson 13, but the actual lesson record in the same candidate does not carry the status that activates that branch.

### Exact evidence
- `course_runtime.py` defines `is_beta_review_lesson()` to return true for `grammar_13` only when:
  - `source_number == 13`
  - `lesson_id == "grammar_13"`
  - `review_status == "internal_cross_lesson_synthesis_no_external_source_mapping"`
- The actual `course_data/grammar_course4_lessons.json` record for `grammar_13` has:
  - `number == 13`
  - `id == "grammar_13"`
  - `review_status == "scientific_review_complete_with_qualified_notes"`
  - 8 structured quiz questions.
- `tests/test_course4_beta_review.py` tests the helper with a synthetic record containing the special internal-synthesis status, but does not load the actual Course 4 JSON and assert the real lesson-13 gate.
- `tests/test_course4_grammar_runtime.py` explicitly expects the actual Lesson 13 status to be `scientific_review_complete_with_qualified_notes` and expects 8 quiz questions.
- In `bot.py`, `lesson_quiz_is_available()` blocks quizzes only when `lesson_is_beta_review()` returns true. `finish_lesson()` records beta progress without rewards only when that same helper returns true. Therefore, for the actual source record currently in PR #125, Lesson 13 is not classified as beta and can follow the ordinary quiz/completion/reward path.
- The curriculum plan's lesson list also labels Lesson 13 as `scientific_review_complete_with_qualified_notes`, while a note in the plan and the helper's special branch refer to an internal cross-lesson synthesis/no-external-source-mapping status. This is a source-of-truth inconsistency.

### Risk / interpretation
This is not proof that Lesson 13 is scientifically wrong. It is proof that the runtime gate, source lesson metadata, curriculum notes, and tests do not express one consistent policy. If the project owner's intended rule is that Lesson 13 remains beta-only until external source mapping is complete, the current actual JSON does not enforce that rule. If the lesson has since been approved for normal quiz/reward progression, the stale special gate and synthetic-only test should be reconciled instead.

### Required resolution before release
1. Confirm the intended Lesson 13 policy from the project owner/source decision record; do not infer it from the helper alone.
2. Make the canonical lesson record, curriculum plan, helper, and tests agree on the same status.
3. Add an integration regression test that loads the real Course 4 JSON and asserts Lesson 13's quiz availability, completion classification, and reward eligibility.
4. Re-run the full test suite on the exact release commit after the policy is reconciled.
5. Do not silently change Lesson 13's status, remove its quiz, or grant/withhold rewards during this audit. Preserve its existing 8 quiz questions and source record until the policy is resolved.

### Non-actions
This is a read-only finding. No runtime source, lesson data, quiz, database, Botkeep instance, or production bot was changed. No PR was merged and no deployment was performed.

# Daily Conversation Course — 48-Lesson Structural Audit

Date: 2026-10-28

## Scope and safety

- Reviewed the five lesson-data files and `daily_conversation_plan.json` on branch `feature/expand-lesson-catalog-2026-10-28`.
- This is a structural/editorial triage, not approval of Kurdish language accuracy.
- All 48 lessons remain marked `draft_editorial_review`. Do not activate the course based on this audit alone.
- No lesson text was changed by this audit.

## Structural checks

- Lesson numbers cover exactly 1–48, with no missing or duplicate numbers.
- All 48 lessons have non-empty titles, objectives, dialogue, vocabulary, exercises, quiz, and role-play prompt.
- The plan's 48 working titles match the lesson-record titles.
- The lessons contain 99 quiz questions in total.
- Every quiz question has a non-empty prompt and explanation, at least three options, no normalized duplicate options within that question, and a valid integer answer index.
- No exact normalized duplicate vocabulary entries or dialogue lines were found within individual lessons.
- No structural errors were detected by these checks.

## Editorial review candidates

These are possible topic overlaps, not confirmed errors. An editor should compare the actual dialogues, vocabulary, exercises, and learning outcomes before deciding whether to merge, differentiate, or retain them as spaced practice.

| Lessons | Shared theme | Review question |
|---|---|---|
| 8, 25, 38 | Shopping / market | Do later lessons add clear progression (e.g. comparison, size, negotiation) rather than repeating the same basic transaction? |
| 10, 29, 43 | Places, directions, neighborhood | Are spatial language and navigation skills developed step by step? |
| 11, 19, 32 | Travel and transport | Are these distinct outcomes (transport vocabulary, asking directions/arrival, planning a trip)? |
| 13, 45 | Health and doctor appointments | Does lesson 45 extend the earlier health lesson into scheduling and appointment language? |
| 22, 40 | Library/reading versus books/films | Are the contexts and language functions sufficiently distinct? |
| 28, 47 | Emergency / asking for help | Is lesson 47 a deliberate practice/review lesson with a distinct scenario? |
| 6, 20, 39 | Daily routine, household tasks, preparing food | Are the dialogues and target expressions clearly differentiated? |
| 12, 18, 30, 36, 42, 48 | Review / integrated conversation | Does each review lesson have a defined cumulative target and a meaningfully different task? |

## Recommended next steps

1. Keep the course gated as `draft_for_review`.
2. Review each candidate cluster for progression and meaningful differentiation; preserve deliberate recycling where it supports learning.
3. Perform a Kurdish-language and orthography review against the project's chosen beginner-level conventions.
4. Test dialogues and quizzes with learners or a reviewer before considering activation.
5. Re-run structural tests after any editorial changes.

## Conclusion

The current data passed the listed structural checks. That does not establish linguistic correctness, pedagogical quality, or production readiness. The topic overlaps above should be reviewed by a human editor before the course is activated.


## Cross-lesson repetition scan (follow-up)

A second scan compared normalized dialogue lines, role-play prompts, quiz questions, and vocabulary terms across all 48 lessons.

- No exact duplicate role-play prompts were found across lessons.
- No exact duplicate quiz-question prompts were found across lessons.
- Two dialogue lines repeat exactly across different lessons:
  - Lessons 1 and 12: `سڵاو ئاڕگەش چۆنی`
  - Lessons 13 and 43: `زۆر سپاس بۆ ڕێنماییەکەت`
- 28 vocabulary terms appear in more than one lesson. Reuse is expected for core language, so this is not automatically a defect. Review topic overlaps to ensure that repeated terms are revisited in a useful new context.

The two repeated dialogue lines should be checked by the editor. They may be intentional reinforcement, but if not, revise one instance so the dialogue feels specific to its lesson. No lesson text was changed by this scan.


## Integration verification (2026-10-29)

- The integration branch retains the Course 1 source lesson file from the four-course safety base; the separate PR #5 edit to that original source was not copied, so this integration does not silently rewrite user-provided lesson text.
- The adapter regression test now loads all five conversation data files and verifies namespaced keys for lessons 1–48. Existing malformed-question, blank-option, duplicate-option, duplicate-number, and non-contiguous-number checks are preserved.
- Runtime integrity tests verify all 82 manifest lessons load without ID collisions, all 48 conversation lessons remain locked even when fake completion rows exist, and progress/quiz listings stay scoped to active courses.
- GitHub Actions run #40827126187 passed on commit `0d2c8ec9302dc1a89ef06d4254dd2f46768eb6f3`: compile check and 236 Python tests passed.
- This is integration evidence only. The PR remains Draft; no merge, deployment, bot activation, production data change, or dynamic-speech enablement occurred.

### Follow-up regression coverage (2026-10-29)

- Added two database regression tests that were present on the separate course-expansion branch but missing from the integration branch:
  - `test_namespaced_course_rewards_do_not_collide_with_legacy_course_one`
  - `test_namespaced_quiz_rewards_do_not_collide_with_legacy_course_one`
- These tests verify that a legacy Course 1 lesson key (`وانە_1`) and a namespaced conversation key (`daily_conversation_01`) retain separate completion/reward records, and that repeating the legacy key does not award twice.
- GitHub Actions run #40827536324 passed on commit `63063b7aa488403e26e59cd6f13acfffe0e702eb`: `compileall` and all 238 Python tests passed.
- The test suite logs one expected error-level message from the test that deliberately simulates failed voice delivery and checks quota refund behavior; the workflow and test suite still completed successfully.
- Current PR #6 remains open and Draft, with no merge or deployment. All 48 conversation lessons remain review-gated; dynamic speech remains disabled.
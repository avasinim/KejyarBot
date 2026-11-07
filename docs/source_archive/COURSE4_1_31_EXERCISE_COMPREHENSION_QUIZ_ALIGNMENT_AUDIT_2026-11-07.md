# Course 4 — Lessons 1–31: Exercise, comprehension, and quiz alignment audit
Date: 2026-11-07
Branch: `feat/course4-clean-port-main-20261106`
Runtime source: `course_data/grammar_course4_lessons.json`
Runtime blob SHA inspected: `4789a3c969786acd144cea528db2c4c57d9353ac`
Latest previously recorded CI head: `d11f323ddc95d62f1947e7afa5e5b2cff05947b3`

## Scope and method
This is an append-only audit record. The source lesson text and current runtime arrays were inspected without modifying lesson content, exercise prompts, comprehension prompts, quiz items, answer indices, curriculum plan, manifest, learner data, or production configuration.

The pass covered:
- per-lesson assessment structure and counts;
- quiz question/options/answer-index/explanation integrity;
- distribution of correct-answer positions;
- exact prompt duplication between comprehension questions and quiz questions;
- targeted semantic alignment of exercise and quiz prompts against lesson objectives, key points, examples, and stated evidence limits.

This report distinguishes confirmed defects from editorial refinements and intentional reinforcement.

## Verified inventory
All 31 lessons use the same assessment counts:

| Assessment component | Per lesson | Course total |
|---|---:|---:|
| Exercises | 5 | 155 |
| Comprehension questions | 8 | 248 |
| Quiz questions | 8 | 248 |
| Comprehension array entries including summary and closing line | 10 | 310 |

The comprehension array contains a lesson summary, eight numbered questions, and a closing line. The eight numbered comprehension questions are present in every lesson; they are not absent from the runtime.

## Structural quiz validation
Across 248 quiz items:
- every question has exactly four options;
- every answer index is an integer in the valid range 0–3;
- every question and explanation is non-empty;
- no quiz item has duplicate option text;
- no structural defect was found in the quiz answer-index fields.

Correct-answer position distribution:
- option 1: 62;
- option 2: 62;
- option 3: 62;
- option 4: 62.

Each lesson has two correct answers at each position. The balanced distribution recorded in the prior quiz audit remains present in the inspected runtime.

## Confirmed semantic alignment issue

### Lesson 31 — Exercise 4 overstates the evidence
Current prompt:
> بە نموونە ڕوون بکەرەوە چۆن گروپی ناوکردراو دەتوانێت لە شوێنی بابەت، بەرکار یان تەواوکەری پێشبەنددا بێت.

Why this is a mismatch:
- Lesson 31's key points explicitly treat the subject role as source-supported.
- The same key points say object and prepositional-complement roles are only pedagogical possibilities pending corpus/speaker evidence, and must not be presented as established Sorani rules.
- The exercise nevertheless asks the learner to demonstrate all three roles as if each were established.

Recommended correction (proposal only; not applied):
> لە نموونەی «کوشتنی ئاژەڵەکە خراپ بوو»دا ڕۆڵی بابەتی گروپی ناوکردراو دیاری بکە. پاشان ڕوون بکەرەوە بۆچی بەرکار و تەواوکەری پێشبەند لەم وانەیەدا تەنها وەک ئەگەری فێرکاری هاتوون و پێویستیان بە بەڵگەی زیاتر هەیە.

This correction preserves the lesson's evidence boundary and does not invent Sorani examples for unverified roles.

## Exact repetition between comprehension and quiz
Four exact or near-exact question repetitions were found within the same lesson:
1. Lesson 12: the question about the role of `ـیان` in «ئەوان کتێبەکەیان خوێند».
2. Lesson 15: the question identifying «خوێند» as a past-tense form.
3. Lesson 16: the question identifying the present stem in «دەخۆم».
4. Lesson 21: the question about what matters when analyzing a multi-part construction.

These repetitions are not answer-key errors. They may be intentional retrieval practice, but if the goal is broader assessment coverage, one instance in each pair can be replaced by an application or contrast question drawn from the same lesson. No replacement has been made.

## Minor precision note
Lesson 22, Quiz 2 asks what relation «بە» expresses in «من بە قەڵەم نووسیم»; the correct option is «ئامراز». The answer is compatible with the lesson, but a more explicit wording such as «ئامراز/کەرەستەی نووسین» would reduce ambiguity. This is an editorial refinement, not a factual error, and has not been applied.

## Source-qualified item retained
Lesson 24's treatment of «ا» in «خوایا» is explicitly attributed to the supplied material and is tested as the position of the form after the vocative noun. It remains source-qualified; this audit does not generalize it into a universal Sorani vocative rule.

## Change and verification status
- No runtime or assessment content was changed in this audit.
- No exercise answer key was invented. The exercise field contains prompts, not keyed answers.
- Comprehension items are prompts; their answers are not stored as a separate structured answer key in this lesson schema.
- No database, Botkeep, production deployment, or Courses 1–3 operation was performed.
- The prior PR record reports successful CI on head `d11f323ddc95d62f1947e7afa5e5b2cff05947b3` (455 passed, 11 skipped). This documentation-only audit did not run a new CI job.

## Next controlled step
Prepare a separate proposed patch for Lesson 31 Exercise 4 and decide whether to retain or diversify the four repeated comprehension/quiz prompts. Do not alter the runtime JSON until the proposed wording has been reviewed; preserve the existing assessment content in the audit trail.

# Course 1 beginner quiz review

## Audience and editorial rule

Course 1 is an introductory orthography course for beginner learners. Quiz questions must check the lesson's basic learning goal in plain, direct Kurdish. They should not require learners to reason about source criticism, linguistic research methodology, or specialist phonetic analysis unless that material has first been taught explicitly and is genuinely necessary for the beginner course.

Preferred question progression:
1. Recognize a letter or written form.
2. Match a familiar example to the lesson's rule.
3. Apply that rule to one short, familiar example.

Avoid:
- asking the same fact twice with only small wording changes;
- making a broad spelling/phonology claim an absolute rule without clear support;
- testing technical notation or a research claim that the lesson has not taught;
- using implausible distractors that make the answer obvious without checking understanding;
- using a quiz question to explain that a source needs review. Editorial review belongs in project notes, not in the learner-facing quiz.

## Findings from the current draft

The following items are already marked for editorial/source review by `course_quiz_review.py`. A flag means the quiz should remain unavailable until reviewed; it does not disable the lesson itself or activate/deactivate a course.

- Lesson 2: the claims that vowels are always written after non-vowels and that two vowels never occur consecutively are broad absolutes. Verify against the intended beginner orthography source and rewrite as scoped rules if appropriate.
- Lesson 4: questions 1 and 2 both ask which helper letter is used at the beginning of a word; question 3 tests the same rule through the example `ئیمان`. Reduce repetition and use a simple application item only if supported by the lesson.
- Lesson 5: questions 1 and 2 repeat the same fact about `و` and `ی`.
- Lesson 6: questions 1 and 2 both test recognition of `کو`; diversify the learning objective rather than repeating the same example.
- Lesson 7: questions 1 and 2 repeat the same position rule for `و` and `ی`.
- Lessons 8 and 12: both have the title `سێ دەنگی گرینگ`. Confirm the intended distinction and titles before renaming either one. Lesson 8 also tests the same three-way mapping across three questions; consider reducing repetition.
- Lessons 9, 10 and 11: each set includes multiple example-recognition questions. Keep one recognition item and use other questions for simple comparisons or rule application only where the lesson text supports it.
- Lesson 12: do not make the learner resolve the duplicate-title editorial issue; clarify the lesson content and title first.
- Lesson 13: the question about the symbol `ٚ` asks learners to reason about source verification and editorial evidence. That is not an appropriate beginner learning objective unless the lesson explicitly teaches it; replace it with a direct, taught skill after the symbol's function is verified.
- Lesson 14: the claim that `ڵ` does not occur at the beginning of a word should be checked against the intended source before it is taught as an absolute rule.
- Lesson 16: distinguish the written sequence `وو` from the linguistic claim that it counts as one letter; the latter needs a clear definition in the beginner lesson.
- Lessons 18 and 19: both are titled `پیتی (ی)`, but the examples concern syllabification and require editorial/source review. Confirm the intended lesson titles and the correctness of the divisions before revising them.
- Lesson 20: questions 1 and 3 both ask about the short vowel `/i/` and the burzoka. The source text did not clearly support the claim at the time of the audit; confirm it from the intended reference and remove the duplicate question.
- Lesson 21: the question about a named metrical research analysis is too specialized for an introductory orthography quiz unless the course explicitly teaches it. Confirm the source and replace it with a basic, taught syllabification task if appropriate.

## Guardrails

- Do not silently rewrite Kurdish language facts, examples, dialect claims, or lesson titles without evidence.
- Keep Course 1 separate from the later unified-orthography and daily-conversation courses.
- Do not put citations or source discussions inside learner-facing lessons or quiz questions unless the project owner specifically asks for them.
- Do not change `main`, merge the draft PR, deploy, or alter the production bot/database as part of this audit.
- Run the relevant Python tests before claiming the review gate is verified at runtime.

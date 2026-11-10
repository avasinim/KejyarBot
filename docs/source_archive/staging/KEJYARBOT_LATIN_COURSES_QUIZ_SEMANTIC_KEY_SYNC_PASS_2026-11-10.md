# Latin Courses 1–2 — quiz semantic and answer-key synchronization pass
Date: 2026-11-10
Branch: `archive/preservation-audit-2026-11-10`

## Scope
Reviewed the 12 × 5 quiz items in each of the two Latin-script courses against their corresponding reviewed lesson and answer-key files. This pass checks answer wording, the selected option letter's presence, and obvious conceptual ambiguity in the item wording. It is a source/editorial review, not a runtime test.

## Verified structure
- Course 1: 12 lessons, 60 quiz-key rows.
- Course 2: 12 lessons, 60 quiz-key rows.
- Every key row refers to a lesson/question pair within the 12 × 5 structure.
- Every stored answer letter (A/B/C/D) exists among the options for its corresponding question.
- Every stored answer-text string appears in the corresponding reviewed lesson.
- The review did not execute the repository test suite or a Telegram/Botkeep runtime.

## Corrections made

### Course 1 — Lesson 9, Question 5
The question's correct option is `A) Dengdar e`. The reviewed key had the correct letter A but stored an explanatory sentence (`Y di koma 23 herfên dengdar de tê hesibandin`) instead of the actual option text. The reviewed key was synchronized to `Dengdar e`; the question, choices, and correct letter were not changed.

Reviewed key SHA after verification: `f540deb973903d5a173cdd8584075d537f053080`.

### Course 2 — Lesson 5, Question 3
The reviewed lesson asks for `mehînê`, but the older answer-key draft still stored `mehinê`. A separate reviewed key copy was created and synchronized to `mehînê`. The original answer-key draft remains untouched.

Reviewed key path: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`
Reviewed key SHA after verification: `a7813c09b2259e35c7e07bfe057f2cc5d38c1102`.

## Conceptual checks sampled across all 120 questions
- Course 1: alphabet inventory (31 letters, 8 vowels, 23 consonant letters), short/long vowel sets as presented by the source, I/Î and U/Û contrasts, V/W letter examples, source's Y classification, raw frequency counts, and dialect distribution.
- Course 2: the four language elements and `tîp`; noun classes and grammatical gender; number versus oblique inflection; noun modifiers; definite versus indefinite suffix patterns; personal pronoun forms; direct-object pronouns and role alternation; demonstrative/relative/interrogative forms; adjective classes and numeral categories.
- No additional definite wrong answer or two-correct-answer defect was confirmed in this pass. This is not a claim that every distractor is optimally discriminating; weak distractors remain editorial opportunities and should be strengthened only after a focused review.

## Preservation boundary
Only reviewed draft/key artifacts and this append-only note are in scope. No original lesson, source file, original key draft, `main`, active manifest, runtime, database, Botkeep, Telegram or deployment was changed. No test-suite pass, live-runtime state or production backup is claimed.

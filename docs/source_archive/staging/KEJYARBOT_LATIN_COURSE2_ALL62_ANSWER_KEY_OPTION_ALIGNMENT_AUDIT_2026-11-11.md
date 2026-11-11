# Course 2 — Full 62-item answer-key to quiz-option alignment audit

**Date:** 2026-11-11  
**Status:** Structural and text-alignment audit; not an independent linguistic correctness ruling.  
**Branch:** `archive/preservation-audit-2026-11-10`

## Re-fetched inputs

- Quiz/lesson draft: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`, SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.

## Method

Parsed all quiz blocks by lesson and question number, extracted options A/B/C, and compared each answer-key row's keyed letter and answer text with the corresponding option. Text comparison normalized case, whitespace, Markdown backticks/emphasis and ordinary punctuation; no semantic equivalence was inferred where the text did not align.

## Results

| Check | Result |
|---|---:|
| Quiz items parsed | 62 |
| Answer-key rows parsed | 62 |
| Expected lesson/question coordinates present | 62/62 |
| Duplicate answer-key coordinates | 0 |
| Missing quiz-to-key coordinates | 0 |
| Keyed option letters missing from quiz item | 0 |
| Answer text mismatches | 0 |

All 62 answer-key letters point to an option present in the corresponding quiz item, and all 62 answer-text entries align with the text of that keyed option under the normalization described above.

## Interpretation and limitations

This verifies the *mapping* between quiz question, option letter and answer-key answer text. It does **not** prove that the keyed answer is linguistically correct, that distractors are psychometrically effective, or that the quiz runs correctly in the bot. Those require separate source/linguistic review, native-speaker adjudication where relevant, and runtime testing.

Existing editorial holds remain unchanged: L1 Q4, L6 Q3/Q4, L8 Q3, L10 Q1/Q2, L12 Q1/Q3.

## Preservation boundary

- New audit artifact only.
- No quiz, answer key, lesson, rationale, runtime, parser, manifest, database, Botkeep, Telegram or deployment file changed.
- No tests, CI, runtime checks or deployment were run.
- `main` remains read-only.
- Archive branch is not an independent ZIP/offsite backup; none is claimed.

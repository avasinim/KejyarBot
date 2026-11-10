# Latin Courses — learning objective, sequence, and quiz alignment pass
**Date:** 2026-11-10  
**Branch:** `archive/preservation-audit-2026-11-10`

## Scope and method
Reviewed all 12 lesson blocks in each reviewed Latin course, their stated learning aims/content sequence, all 120 quiz questions, and both separate reviewed answer keys. Compared each keyed answer to the option bearing its answer letter. This was a source-file review; no bot/runtime execution or automated test suite is claimed.

## Structural and key alignment
- Course 1: 12 lessons, 60 quiz questions, 60 answer-key rows; four options per question.
- Course 2: 12 lessons, 60 quiz questions, 60 answer-key rows; three options per question, matching the current course format.
- Before the correction below, the option/key comparisons had no mismatches. After the correction, the changed Course 1 Lesson 1 Q3 and its answer-key row were fetched again and verified. The answer letter remains B.
- Lesson sequence remains 1–12 in both courses.

## Correction made — Course 1, Lesson 1
The original Q3 tested the short-vowel set `E, I, U`, although short/long vowel classification is not taught until Course 1, Lessons 4–5. This violated the prerequisite sequence.

The question now asks which group contains only consonant letters:
- Correct option: B) `B, M, R`.
- The answer-key row remains letter B and its answer text was synchronized to `B, M, R`.
- Both the reviewed lesson draft and reviewed answer key were fetched before updating, changed using their fetched SHAs, and fetched again to verify.

## Remaining alignment observations — no unapproved scope expansion
1. **Course 1, Lesson 2:** one stated aim says learners identify letters also found in other alphabets. The lesson presents the Kurdish alphabet and marked letters but does not explicitly compare another alphabet, and the quiz does not assess that aim. This needs either a short supported comparison in the lesson or a narrower, accurately scoped aim in a future reviewed revision.
2. **Course 2, Lesson 10:** the aim names object, reciprocal, compound, reflexive pronouns, and the neuter `ê`. The lesson content and practice include these, but the five-question quiz directly assesses object and reciprocal pronouns; compound/reflexive forms and neuter `ê` are not directly sampled.
3. **Course 2, Lesson 11:** the aim includes demonstrative, relative, interrogative, indefinite, and possessive pronouns. The quiz samples demonstrative, relative, and interrogative forms, but not indefinite or possessive forms.
4. **Course 2, Lesson 12:** the lesson teaches six adjective classes and adjective degrees, alongside numerals. The five-question quiz samples adjective definition, qualitative adjective, numeral adjective, the separate numeral category, and `nîv`; it does not directly sample all six adjective classes or adjective degrees.
5. **Course 1, Lesson 7:** its learning aims are present as a plain bold heading rather than a Markdown heading. The content and quiz are present; this is a formatting inconsistency, not a missing lesson objective.

## Recommended next review
Create a small supplementary assessment pass for Course 2 Lessons 10–12 (and decide whether Lesson 2's Course 1 objective should be expanded or narrowed). Preserve the existing five questions and key rows; add only clearly identified supplementary questions/rows if approved. Do not silently replace or remove original questions.

## Preservation
All work remains on `archive/preservation-audit-2026-11-10`. No baseline/original course content, `main`, active manifest, runtime, database, Botkeep bot, Telegram bot, or deployment was modified. No runtime status or live backup is claimed.

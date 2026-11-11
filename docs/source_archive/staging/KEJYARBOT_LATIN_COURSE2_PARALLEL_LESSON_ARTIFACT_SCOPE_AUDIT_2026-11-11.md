# Course 2 — Parallel lesson-artifact scope and quiz-count audit

**Date:** 2026-11-11  
**Status:** Read-only artifact-scope audit; no files edited.  
**Branch:** `archive/preservation-audit-2026-11-10`

## Files compared

1. `course_data/latin_course_2_source_aligned_lessons_01_12.md`
   - SHA: `19090077a11dc9d7211987e958e560b328fcd3d6`
   - 600 lines.
2. `course_data/latin_course_2_reviewed_draft_2026-11-10.md`
   - SHA: `abc88219e2a0e249883e8d62c5117a9b3aaa3108`
   - 651 lines.
3. `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`
   - SHA: `879e1525e720bdc25b8f6e896de3e388801238d0`

## Parsed quiz inventory

| Lesson | Source-aligned artifact | Reviewed draft |
|---|---:|---:|
| 1 | 5 | 5 |
| 2 | 5 | 5 |
| 3 | 5 | 5 |
| 4 | 5 | 5 |
| 5 | 5 | 5 |
| 6 | 5 | 5 |
| 7 | 5 | 5 |
| 8 | 5 | 7 |
| 9 | 5 | 5 |
| 10 | 5 | 5 |
| 11 | 5 | 5 |
| 12 | 5 | 5 |
| **Total** | **60** | **62** |

The 62-row reviewed answer key maps to the 62-question reviewed draft, not to the 60-question source-aligned artifact.

## Material differences confirmed

The files are not byte-for-byte or quiz-content-equivalent versions of one master:
- Lesson 8 has seven quiz items in the reviewed draft, but five in the source-aligned artifact. The two additional reviewed-draft items are L8 Q6 and L8 Q7 (the pre-adjective forms and oblique determiner forms).
- Several stems and distractors were refined between the artifacts. Examples include L1 Q1/Q3/Q4, L5 Q2–Q4, L6 Q1, L7 Q2–Q4, L8 Q2–Q4, L9 Q1–Q4, L10 Q4, and L12 Q1.
- Some technical explanations also differ, including Lesson 6's explicit full-term distinction `bireserê navdêrê` vs clause `bireser`, and Lesson 8's more explicit distinction between §66 and §67 conditions.

## Operational interpretation

- For the active 62-question quiz/key review, the reviewed draft dated 2026-11-10 and its matching 62-row answer key are the internally aligned pair.
- The 60-question `source_aligned_lessons_01_12.md` remains a separate source-aligned lesson artifact. Do not silently treat its older embedded quiz snippets as the current 62-item quiz or copy them over the reviewed draft.
- This audit does not declare either file universally canonical for every downstream use. Repository maintainers should explicitly identify artifact roles in any future manifest/index.
- The two files must remain preserved as separate artifacts; do not merge, overwrite or delete one on the assumption that they are duplicate copies.

## Preservation boundary

- New audit artifact only.
- No lesson, quiz, answer-key, source-aligned, runtime, parser, manifest, database, Botkeep, Telegram or deployment file changed.
- No tests, CI, runtime checks or learner-response analysis were run.
- `main` remains read-only.
- Archive branch is not an independent ZIP/offsite backup; none is claimed.

# Course 2 — 62-question to 45-rationale coverage audit

**Date:** 2026-11-11  
**Status:** Append-only structural coverage audit.  
**Branch:** `archive/preservation-audit-2026-11-10`

## Re-fetched inputs

- Quiz/lesson draft: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`, SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.
- Consolidated rationale pack: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_CONSOLIDATED_45_RATIONALE_EDITORIAL_REVIEW_PACK_2026-11-11.md`, SHA `177faaaa5260879bf4b2211474dede013f8d002c`.

## Structural comparison

Expected quiz population: 62 items (Lessons 1–7 and 9–12 have 5 each; Lesson 8 has 7).

Parsed rationale proposal population:
- 45 rows found.
- 45 unique lesson/question coordinates.
- 0 duplicate coordinates.
- Every included rationale row has a lesson/question coordinate within the 62-item quiz.
- All 45 rows carry a key letter in the pack; this audit does not independently revalidate their linguistic rationale or key correctness.

## Items not represented in the 45-row proposal pack

The following 17 quiz items are absent from the consolidated rationale proposal tables:

| Lesson | Missing question rows |
|---:|---|
| 1 | Q4 |
| 5 | Q2, Q3, Q4 |
| 7 | Q2, Q3, Q4 |
| 8 | Q4, Q6, Q7 |
| 9 | Q1, Q2, Q3, Q4 |
| 11 | Q4 |
| 12 | Q1, Q3 |

Important distinction:
- L1 Q4, L12 Q1 and L12 Q3 are explicitly held or withheld for separate editorial ruling in the rationale pack / audit records.
- The other 14 items are simply not included in this 45-row rewrite proposal. Their absence is not evidence that they are defective, nor does it mean the answer key has no rationale text for them. The answer-key file itself contains a rationale cell for every quiz row.
- Do not silently expand “45 proposed rewrites” into “45 of 62 items approved” or “17 items have no rationale”. These are different statuses.

## Reconciliation with the answer key

The answer-key table contains 62 rows and includes a rationale field for each. The consolidated pack is a selective editorial rewrite set of 45 rows, not a full replacement answer key. Any future attempt to produce a complete 62-item rationale edition must preserve this distinction and separately decide whether the 14 unrepresented items need revision or should retain their current answer-key explanations.

## Disposition

- Structural result: 45/45 included rows are unique; 17/62 quiz coordinates are not represented in the proposal pack.
- No key letters or rationale wording were changed.
- No lesson, quiz, answer key, runtime, parser, manifest, database, Botkeep, Telegram or deployment file changed.
- No tests, CI, runtime checks or deployment were run.
- `main` remains read-only.
- Archive branch is not an independent ZIP/offsite backup; no such backup is claimed.

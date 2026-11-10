# Course 2 — 62-question answer-key structural verification

**Date:** 2026-11-10  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Scope:** Structural comparison of the reviewed Course 2 quiz draft and its reviewed answer-key draft.  
**Source draft SHA:** `abc88219e2a0e249883e8d62c5117a9b3aaa3108`  
**Answer-key draft SHA:** `879e1525e720bdc25b8f6e896de3e388801238d0`

## Method
A read-only parser inspected each of the 12 lesson blocks, recognized both heading conventions used in the reviewed file (`Kuis — N pirs` and Lesson 12's legacy `10. Testa Kejyar`), extracted numbered questions and their A–D options, and compared every answer-key row by lesson/question number, option letter, and normalized answer text. Normalization removed Markdown code delimiters, the recurring bot signature/separator, and inconsequential whitespace/case only. No source content was rewritten.

## Results
- Lessons found: **12**.
- Question counts by lesson: **5, 5, 5, 5, 5, 5, 5, 7, 5, 5, 5, 5**.
- Parsed quiz questions: **62**.
- Answer-key rows: **62**.
- Missing key rows: **0**.
- Orphan key rows: **0**.
- Duplicate key rows: **0**.
- Answer-letter references to absent options: **0**.
- Answer-text mismatches after normalization: **0**.
- Quiz question numbering gaps or repeats: **0**.
- Questions with fewer than 3 or more than 4 options: **0**.
- Duplicate option texts within a question: **0**.

**Structural outcome:** all 62 answer-key entries point to an existing option in the corresponding reviewed quiz question, and the stored answer text matches that option exactly after the stated normalization.

## Limits
This is a structural consistency check, not an independent linguistic adjudication that every keyed answer is pedagogically or scientifically correct. It does not validate distractor quality, source interpretation, or the correctness of every lesson claim. It does not execute the runtime parser, Telegram handlers, unit tests, or CI. The reviewed draft uses two quiz heading formats; the runtime migration and test parser must explicitly support both or normalize them in a separately reviewed source change.

No runtime, original source file, answer-key source file, active manifest, database, Botkeep, Telegram, or deployment state was changed.

# Course 4 — Quiz-Level Basten Patch Review (Round 58)
Date: 2026-11-10
Source branch: `botkeep-menu-clean-2026-11-09`
Source blob SHA: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
Reviewed proposal: `COURSE4_BASTEN_TERM_REVERSIBLE_PATCH_PROPOSAL_ROUND57_2026-11-10.md`

## Scope and counts
- Reviewed every structured quiz item touched by the Round 57 replacement map, including its full question, all options, answer field and explanation.
- **16 quiz items** affected across lessons 7, 8, 10, 11, 12, 13, 15, 16, 27, 30 and 31.
- **18 exact occurrences** in **17 quiz string paths** (Lesson 30 has two occurrences in one option).
- The Round 57 ledger's count of 17 quiz strings is correct; the number of quiz items is 16.

## Quiz integrity result
- All answer values/indices remain unchanged in the temporary-copy transformation.
- No option order or option text outside the target terminology changed.
- No question's intended grammatical target changed merely by substituting the context term.
- Lesson 12's contrast between possessive reading and transitive-past subject marking remains intact.
- Lessons 13 and 16 retain the point that `دەـ` is not future-only; the temporal adverb and broader linguistic context remain distinct.
- Lesson 27 retains the requirement for natural-speech examples/data before assigning uncertain interjection functions.
- Lesson 30 retains the distinction between a light-verb use and a lexical/main-verb use.
- Lesson 31 retains the restriction that an infinitive is not a noun in every environment.

## Occurrence-level disposition
The touched quiz locations are:
- Lesson 7: `quiz[1].q`
- Lesson 8: `quiz[4].options[0]`, `quiz[4].options[1]`
- Lesson 10: `quiz[3].explanation`, `quiz[7].explanation`
- Lesson 11: `quiz[3].options[1]`, `quiz[6].options[2]`, `quiz[7].q`
- Lesson 12: `quiz[3].explanation`
- Lesson 13: `quiz[6].q`
- Lesson 15: `quiz[4].options[3]`
- Lesson 16: `quiz[2].options[0]`, `quiz[2].explanation`, `quiz[3].explanation`, `quiz[5].q`, `quiz[5].explanation`
- Lesson 27: `quiz[7].options[0]`
- Lesson 30: `quiz[4].options[2]` (two occurrences)
- Lesson 31: `quiz[5].options[2]`

## Editorial cautions before any actual patch
1. Review naturalness of every inflected form in its full sentence; in particular, distinguish `بەستێنی ...` as ezafe construction from `لە بەستێندا` as a locative construction.
2. Lesson 27's `بەستێنی/داتای قسەی سروشتی` is a slash-list in an option. It may be edited to a smoother coordinated phrase in a later copy-edit, but do not alter the pedagogical meaning or answer.
3. The terminology replacement does not certify the factual correctness of the underlying grammar item; existing scientific review gates remain in force.

## Decision
All 16 quiz items pass the *answer-integrity* check for the mechanical candidate transformation. The linguistic naturalness review remains pending; no quiz edit is approved by this report.

## Change-control
Append-only review record. No source JSON, quiz, answer key, runtime, database, Botkeep, Telegram, deployment or merge change.

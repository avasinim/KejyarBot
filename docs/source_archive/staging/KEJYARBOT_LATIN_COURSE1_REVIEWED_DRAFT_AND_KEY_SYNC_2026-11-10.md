# Latin Course 1 — Reviewed draft and answer-key synchronization

Date: 2026-11-10
Repository: avasinim/KejyarBot
Source branch: main (read-only)
Output branch: archive/preservation-audit-2026-11-10

## Authorized work performed
Following the user's instruction to proceed autonomously with the Latin-course review, created two separate reviewed-draft artifacts on the preservation branch. The original files on main were not modified.

1. `course_data/latin_course_1_reviewed_draft_2026-11-10.md`
   - Based on the complete 12-lesson source-aligned draft.
   - Lesson 2: removed the exact duplicate note and standardized the label to “herfên nîşankirî”.
   - Lesson 5: lowercased `Aşxane` to `aşxane`; removed the unverified `avis` example rather than inventing a replacement.
   - Lesson 6: replaced the semantically incorrect exercise label `Kêşeyeke biçûk` (“a small problem”) with `Xebateke biçûk` (“a small exercise”).
   - Lesson 9: normalized `yêk` to `yek` and `çîya` to `çiya` in all occurrences; rewrote Q5 to ask explicitly for Y's alphabetic class.
   - Lesson 10: rewrote the sentence about hearing sounds for grammatical clarity.
   - Lesson 11: renamed the lesson/section headings to describe the displayed raw counts; clarified that the numbers are not percentages or normalized ratios; revised Q5 wording accordingly.
   - All 12 lesson bodies remain present.

2. `course_data/latin_course_1_quiz_answer_key_reviewed_draft_2026-11-10.md`
   - Copied the 60-row answer key.
   - Updated Lesson 9 Q5 explanation to match its clearer wording; correct option remains A.
   - Updated Lesson 11 Q5 explanation to match the revised raw-count / distribution wording; correct option remains D.
   - All 60 keyed rows remain present.

## Verification performed
- Both new files were fetched again from the preservation branch and their blob SHAs verified.
- Reviewed lesson draft contains 12 lesson headings.
- Reviewed answer key contains 60 keyed rows.
- Searches over the reviewed lesson draft found no remaining `yêk`, `çîya`, or `avis` example; the duplicated Lesson 2 note now occurs once.
- No lesson or answer-key source file on main was overwritten.
- No runtime files, active manifests, course activation settings, database, Botkeep server, or deployment were changed.

## Important limits
- The exact lexical status of the removed `avis` item and all source examples still needs a page-image/source collation against the physical edition; it was removed from the teaching example list pending verification, not declared impossible as a word.
- The source's Part I frequency-table heading may itself use “Nisbet”; the lesson's own title is made more precise because its displayed values are raw counts. Keep the original source heading in provenance, and do not misrepresent counts as percentages.
- The alphabetic classification of Y follows the cited source's 23-letter inventory; detailed phonetic behavior requires a separate phonetics explanation.
- This reviewed draft is not activated or deployed. It is staged for review; main remains unchanged.
- Next work: inspect Course 2 (Part II grammar) separately, starting from its source-aligned lessons and answer key, preserving source separation.

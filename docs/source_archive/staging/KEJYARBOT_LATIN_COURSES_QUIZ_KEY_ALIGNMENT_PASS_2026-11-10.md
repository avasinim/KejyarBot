# Latin Courses 1–2 — quiz and answer-key alignment pass
**Date:** 2026-11-10  
**Branch:** `archive/preservation-audit-2026-11-10`

## Scope
Compared all 12 lessons and 60 quiz questions in each reviewed course draft against the corresponding separate reviewed answer-key file.

## Results
- **Course 1:** 12 lessons, 60 questions, 60 answer-key rows. All 60 answer letters selected the option whose text is recorded in the reviewed answer key. All 60 questions had the expected option set in the quiz text.
- **Course 2:** 12 lessons, 60 questions, 60 answer-key rows. The check found one answer-letter mismatch in Lesson 1, Question 3. The question asks what a `tîp` is; option A describes a spoken sound, while option B says `nîşana nivîskî`. The answer text in the key was already correct, but its letter was incorrectly recorded as A. The reviewed key was corrected to **B**. Lesson 12's five multiline questions were also checked directly against their options and key rows.
- After the correction, all 120 questions align with their answer-key answer text and option letters.

## Specific correction
File: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`  
Row changed: `| 1 | 3 | A | nîşana nivîskî |` → `| 1 | 3 | B | nîşana nivîskî |`

The reviewed lesson question itself was not changed; option B is already the correct written-symbol definition. The original/master answer key remains untouched.

## Preservation and validation limits
The reviewed key was fetched before editing, updated using its fetched SHA, then fetched again to verify the corrected row. No lesson text, quiz options, original source file, baseline file, `main`, active manifest, runtime, database, Botkeep, Telegram, or deployment was modified. No original content was deleted. This was a text-level key-to-option alignment check; it is not a runtime test and does not claim that the full automated test suite was executed.

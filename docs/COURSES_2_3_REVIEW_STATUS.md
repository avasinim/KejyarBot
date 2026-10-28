# Courses 2–3 Editorial Review Status

Date: 2026-10-28  
Branch: `fix/four-course-structure-2026-10-27`  
Scope: test branch only. No production files, bot token, database, or deployment changed.

## Current state

- Course 2, `daily_conversation`: 12 ordered lessons. Each lesson has an objective, dialogue, vocabulary, exercises, comprehension prompts, role-play guidance, and valid multiple-choice quiz data.
- Course 3, `unified_orthography`: 12 ordered lessons. Each lesson has an objective, key points, examples, exercises, comprehension prompts, practical work, and valid multiple-choice quiz data.
- Both courses intentionally remain `draft_for_review`. Structural validity is not linguistic approval; do not activate either course solely because the bot can load it.
- Course 4 remains planned and out of scope.

## Course 2 — required editorial pass

1. Read every dialogue aloud and review naturalness, register, case/verb forms, and consistency of speaker turns.
2. Confirm each vocabulary gloss matches the exact expression as used in the dialogue.
3. Check each comprehension prompt against its dialogue and each quiz answer/explanation against the same lesson.
4. Check progression from greetings and self-introduction through family, home, routines, food, shopping, time, directions, travel, and final practice.
5. After editorial corrections, test opening lessons in order, completion/unlock behavior, quiz callbacks, and returning to the course menu on the isolated Telegram test bot.

## Course 3 — issues to resolve before activation

1. **Lesson 7, `ک/ك، ھ/ه و ە`:** The lesson mixes practical Kurdish spelling with Unicode look-alike/code-point discussion. Keep the distinction between the Kurdish letter `ه` and the visually similar `ھ` explicit; do not present `ھ` as a normal replacement for `ه`. Decide whether the technical-code-point material belongs in this beginner course.
2. **Lesson 9, `ئامرازەکان و پێکەوەنووسین`:** The examples test spacing in specific phrases, while the lesson itself correctly notes that the general joining/separation rule has not yet been confirmed. Verify every example against the course's chosen orthographic authority before stating a general rule.
3. **Lesson 10, `وشەی لێکدراو و داڕێژراو`:** The example `کتێب‌خانە` uses a non-breaking/zero-width joiner-like separator in the displayed text. Decide and document the intended visible spelling/spacing convention, then use it consistently in lesson text, examples, and quiz options.
4. **Lesson 11, `هاوەڵکار، وشەی بیانی و ژمارەی لێکدراو`:** The exercises identify `زۆر` in an adverbial phrase, locate `تەلەفۆن` in a sentence, and compare number spellings. Add a clear beginner-level explanation of the borrowed-word concept or narrow the objective/title to what is actually taught. Verify number-spacing rules before generalizing from the two examples.
5. **Lesson 12:** The three correction questions align with the three displayed examples (`ك/ک`, `ي/ی`, `ر/ڕ`), but this is a limited practice set. Do not describe it as a comprehensive assessment of all unified spelling rules.
6. **Lessons 1–8 overall:** Verify every linguistic claim, syllable split, and example against the selected source/course standard. In particular, lesson 3's syllable divisions and lesson 4's definition/examples of consonant clusters need a final language-editor pass.

## Release gate

Before changing either course status to `active`:

- Resolve the items above and record which authority/standard governs the examples.
- Re-check all 24 lessons and quiz keys against the final edited lesson text.
- Run the repository test suite in a clean checkout and confirm the test results.
- Test the complete learner journey on the isolated Telegram test bot.
- Keep the production bot, production token, production database, `main`, and PR merge untouched unless separately and explicitly authorized.
- Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false` and preserve the existing approved voice.

## Separate confirmed typo fix

Commit `63b3ba1565ac69c0f3f5222970b27858a48e41a3` changes the Course 1 lesson header and Lesson 1 infographic caption from `کەویار` to `کەژیار`. It does not change the original lesson prose where `کەویار` is deliberately shown as a contrasting example. This commit is on the test branch only and is not automatically deployed to Botkeep.

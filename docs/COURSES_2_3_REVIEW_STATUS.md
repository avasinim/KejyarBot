# Courses 2–3 Editorial Review Status

Date: 2026-10-29  
Branch: `fix/integration-daily-conversation-48-2026-10-29`  
Scope: integration branch only. No production files, bot token, database, or deployment changed.

> **Current status:** By the owner's explicit request, Course 2 (48 lessons) and Course 3 (12 lessons) are technically `active` in the integration manifest. Lesson-level editorial review remains incomplete; this is not final language approval or a production release. The full local suite passed 244 tests on commit `d4af297` (7.238 seconds). Dynamic speech remains disabled.

## Current state

- Course 2, `daily_conversation`: 48 ordered lessons. Each lesson has an objective, dialogue, vocabulary, exercises, comprehension prompts, role-play guidance, and valid multiple-choice quiz data. The detailed lesson-by-lesson review notes below were written for lessons 1–12; lessons 13–48 are tracked in `docs/DAILY_CONVERSATION_48_LESSON_AUDIT.md`.
- Course 3, `unified_orthography`: 12 ordered lessons. Each lesson has an objective, key points, examples, exercises, comprehension prompts, practical work, and valid multiple-choice quiz data.
- Both courses are technically active in the integration manifest by explicit owner request. Structural validity is not linguistic approval; retain `draft_editorial_review` metadata until practical language review is complete and do not infer production release.
- Course 4 remains planned and out of scope.

## Course 2 — required editorial pass

1. Read every dialogue aloud and review naturalness, register, case/verb forms, and consistency of speaker turns.
2. Confirm each vocabulary gloss matches the exact expression as used in the dialogue.
3. Check each comprehension prompt against its dialogue and each quiz answer/explanation against the same lesson.
4. Check progression from greetings and self-introduction through family, home, routines, food, shopping, time, directions, travel, and final practice.
5. After editorial corrections, test opening lessons in order, completion/unlock behavior, quiz callbacks, and returning to the course menu on the isolated Telegram test bot.

## Course 3 — editorial issues to resolve before production release

1. **Lesson 7, `ک/ك، ھ/ه و ە`:** The lesson mixes practical Kurdish spelling with Unicode look-alike/code-point discussion. Keep the distinction between the Kurdish letter `ه` and the visually similar `ھ` explicit; do not present `ھ` as a normal replacement for `ه`. Decide whether the technical-code-point material belongs in this beginner course.
2. **Lesson 9, `ئامرازەکان و پێکەوەنووسین`:** The examples test spacing in specific phrases, while the lesson itself correctly notes that the general joining/separation rule has not yet been confirmed. Verify every example against the course's chosen orthographic authority before stating a general rule.
3. **Lesson 10, `وشەی لێکدراو و داڕێژراو`:** The example `کتێب‌خانە` uses a non-breaking/zero-width joiner-like separator in the displayed text. Decide and document the intended visible spelling/spacing convention, then use it consistently in lesson text, examples, and quiz options.
4. **Lesson 11, `هاوەڵکار، وشەی بیانی و ژمارەی لێکدراو`:** The exercises identify `زۆر` in an adverbial phrase, locate `تەلەفۆن` in a sentence, and compare number spellings. Add a clear beginner-level explanation of the borrowed-word concept or narrow the objective/title to what is actually taught. Verify number-spacing rules before generalizing from the two examples.
5. **Lesson 12:** The three correction questions align with the three displayed examples (`ك/ک`, `ي/ی`, `ر/ڕ`), but this is a limited practice set. Do not describe it as a comprehensive assessment of all unified spelling rules.
6. **Lessons 1–8 overall:** Verify every linguistic claim, syllable split, and example against the selected source/course standard. In particular, lesson 3's syllable divisions and lesson 4's definition/examples of consonant clusters need a final language-editor pass.

## Release gate

Before any production release:

- Resolve the items above and record which authority/standard governs the examples.
- Re-check all 24 lessons and quiz keys against the final edited lesson text.
- Run the repository test suite in a clean checkout and confirm the test results.
- Test the complete learner journey on the isolated Telegram test bot.
- Keep the production bot, production token, production database, and `main` untouched unless separately and explicitly authorized. PR #6 was merged only into `fix/four-course-structure-2026-10-27`; this integration branch's subsequent commits are separate.
- Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false` and preserve the existing approved voice.

## Automated checks (2026-10-28)

- Latest GitHub Actions run for commit `1b2fda8a7dd80efaa599b2f9c9ddaf6a54bce48c` passed: `python -m compileall -q .` and all 187 tests passed.
- The first run after adding callback/branding regression tests exposed stale Course 1 quiz-review test expectations. The tests were updated to match the explicit source-review gate; quizzes were not re-enabled to make the tests pass.
- Added a regression test that checks 188 generated course/lesson callback payloads against Telegram's 64-byte limit, ensures course callback IDs are unique, and protects the `کەژیار` spelling in the generated lesson header/caption.
- These are automated structural/runtime checks only. They do not constitute manual Telegram testing or linguistic approval of Courses 2–3.

## Separate confirmed typo fix

Commit `63b3ba1565ac69c0f3f5222970b27858a48e41a3` changes the Course 1 lesson header and Lesson 1 infographic caption from `کەویار` to `کەژیار`. It does not change the original lesson prose where `کەویار` is deliberately shown as a contrasting example. This commit is on the test branch only and is not automatically deployed to Botkeep.



## Focused content pass — additional findings (2026-10-28)

This is a review log, not a blanket rewrite. Course JSON was inspected directly; lesson files remain unchanged pending deliberate content decisions.

### Course 2 — daily conversation

1. **Lesson 1, objective vs dialogue:** The objective is greetings and farewells, but the dialogue also introduces an invitation and a plan to go to the library. Broaden the objective or simplify the dialogue.
2. **Lesson 2, naturalness/level:** “ئێستا یەکترمان ناسیوە” sounds like a formal summary after a short introduction. A Kurdish-language reviewer should consider a more natural everyday closing. Check “خەڵکی ئەم شارەم” and “لە گوندێکی نزیک ئەم شارەوەم” for the intended dialect/register.
3. **Lesson 3, sequencing:** The lesson teaches question words, but also uses several verb forms and the time expression “نزیکەی کاتژمێر دە دەگەمە کتێبخانە”. Verify naturalness and whether that time pattern is appropriate for the beginner stage.
4. **Lesson 4, vocabulary glosses:** The glosses for “دایک” and “باوک” are asymmetrical and too definitional for beginners. Use concise, parallel definitions after language review. The dialogue and quiz agree on family counts.
5. **Lesson 5, productive practice:** The exercise asks learners to repeat location/room-count information already supplied. Add a productive task that makes them use the vocabulary in a new description.
6. **Lesson 6, time expression:** Confirm the preferred spoken form for telling time and keep it consistent across lessons 6, 9, 11 and 12.
7. **Lesson 7, vocabulary precision:** The gloss for “مریشک” says it means chicken as food in this dialogue, which can confuse the animal and meat senses. Give a simpler context-sensitive gloss. Also verify that past/perfect forms such as “خواردووە” fit the intended beginner progression.
8. **Lesson 8, currency/context:** The arithmetic is internally correct: two kilograms of apples at 3,000 dinars plus one kilogram of oranges at 3,000 dinars equals 9,000 dinars. The current dialogue consistently uses dinar; confirm that the prices are clear for beginners.
9. **Lesson 9, date convention:** “بیست و حەوتی مانگی بەفرانبار” assumes a particular calendar/month convention. Confirm it fits the intended audience and standardize clock-time notation throughout.
10. **Lesson 10, directions:** The dialogue combines straight ahead, turning right, beside, opposite and behind. The quiz keys match the dialogue, but learners need a simple route-sequence exercise before being assessed on all relations together.
11. **Lesson 11, travel plan:** The dialogue appropriately marks the one-hour trip duration as an estimate to be checked; preserve that uncertainty. Review whether “کاتژمێر چەند دەڕۆین؟” is the most natural phrasing for the intended register.
12. **Lesson 12, final review:** The dialogue revisits many vocabulary areas, but the exercises do not define measurable role-play requirements. Specify a minimum number of turns or required functions (greeting, price, directions, time and farewell).

### Course 3 — unified orthography

1. **Lesson 1, scope:** It combines the definition of orthography with Unicode look-alikes (ک/ك, ی/ي). Decide whether these digital-text distinctions belong in the opening lesson or the later letter-shape lesson.
2. **Lesson 2, missing alphabet inventory:** The title promises alphabet and letter order, but the content mainly discusses letter vs sound and the roles of و and ی. It supplies no alphabet list/order. Add the promised inventory or narrow the title/objective.
3. **Lesson 3, examples need source check:** The syllable divisions “کۆ-مار” and “هێ-لا-نە” need confirmation against the chosen pronunciation/dialect and accepted syllabification method.
4. **Lesson 4, terminology:** Confirm that “هێشوو” is the intended term for consonant clusters in this course standard, and that its definition is not confused with written digraphs or syllable boundaries.
5. **Lesson 5, scope mismatch:** The title promises “هەمزە و پیتی ئـ”, but the content only identifies ئ at the beginning of three words. Add the promised explanation or narrow the title.
6. **Lesson 7, objective conflict:** The objective says learners should recognize Kurdish ک, ھ and ە, but the examples/exercises explicitly warn that ھ should not replace ordinary Kurdish ه. This is a direct internal contradiction. The target should say that ه is the ordinary spelling and ھ is only a technical look-alike if that topic remains in scope.
7. **Lesson 8, objective coverage:** The title/objective lists و، وو، ی، ێ, but the examples mostly identify written shapes and do not systematically teach/test sound distinctions. Decide whether this is a spelling-recognition lesson or a sound/letter lesson and align the objective and exercises.
8. **Lesson 9, terminology/content gap:** The title mentions particles and joining/separation, but the examples mostly show separated phrases (لە ماڵ، بە خێرایی، بە کوردی). No verified general joining/separation rule is established. Keep these as examples until the governing standard is confirmed.
9. **Lesson 10, separator rendering:** “کتێب‌خانە” contains a special invisible/nonbreaking separator. Ensure Telegram displays the chosen convention clearly and does not require learners to type an invisible character. Confirm the morphological classification of examples before teaching it as a general rule.
10. **Lesson 11, title vs content:** The title includes “وشەی بیانی”, but the lesson does not define or teach how to identify borrowed words; it only locates “تەلەفۆن” in a sentence. Add a simple explanation/examples or narrow the title/objective. Keep number examples provisional until spacing rules are verified.
11. **Lesson 12, assessment scope:** The three questions test only ک/ك, ی/ي and ر/ڕ. This is useful focused practice, not a comprehensive final assessment. Label it accordingly or add coverage for the approved course objectives.

### Review boundary

This focused pass was a historical editorial log and did not change lesson content. Course activation was subsequently requested and applied in the integration manifest. The remaining findings need editorial decisions and, where a rule is disputed, confirmation against the chosen Kurdish orthographic source before changes are made.

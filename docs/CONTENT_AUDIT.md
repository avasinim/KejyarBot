# KejyarBot lesson and quiz content audit

Branch reviewed: `fix/kejyarbot-stability-2026-10-25`

> **Current-state note (26 October 2026):** The current branch contains ten lessons and quiz sets for all ten. Sections below are dated audit history; references there to six lessons, four questions per lesson, or earlier CI checkpoints describe the state at that earlier point in time and are not the current inventory. Use the **Current checks**, **Latest verification**, and later dated sections to determine the present state.

## Current checks

- `lessons.json` contains ten non-empty lesson records, numbered 1–10, and `learning_path.json` matches their titles and intended order.
- `quiz.json` contains quiz sets for all ten lessons; every question has non-empty text, unique options, and an answer present among those options.
- The bot's lesson navigation, unlocking sequence, completion badges, and final-lesson quiz path are covered by regression tests for ten lessons.
- All ten lesson SVGs are checked for well-formed XML, RTL direction, bidi handling, and the chosen Arabic-script font stack.
- Lesson 2 now presents 34 practice entries with five words per entry (170 examples in total). Its infographic is tested against the lesson text so every listed example must appear in both places.
- The inventory intentionally calls these “practice entries” rather than asserting that every entry is an independent alphabet letter: some orthographic combinations and vowel signs may need a separate academic classification review.
- The currently observed CI runs for commit `3e91a6b7679c41951461ff39f8310acccd132eaf` passed:
  - https://github.com/avasinim/KejyarBot/actions/runs/40195442921
  - https://github.com/avasinim/KejyarBot/actions/runs/40195446238

## Latest verification

- The infographic-example regression test was added in commit `a9d870d63397454e7e387f9aa8a38ac8dd5514b5` and re-read from the branch.
- CI run #244 passed for that commit: https://github.com/avasinim/KejyarBot/actions/runs/40195984360 . This confirms the automated checks passed; it does not establish source-level orthographic correctness.
- The documentation update itself was also checked by CI runs #246 and #247; both passed for commit `6ddd91e3cbef61b71d5f08575bf807b06e92703c`: https://github.com/avasinim/KejyarBot/actions/runs/40196071449 and https://github.com/avasinim/KejyarBot/actions/runs/40196074868.

## Expanded vocabulary and example policy

- The Diako Hashemi book is a reference for orthography and punctuation, not the exclusive source or limit for lesson vocabulary, example sentences, dialogues, or exercises.
- Expand teaching examples using appropriate Kurdish dictionaries, other Kurdish-language textbooks and linguistic references, literature, and natural everyday dialogue where suitable.
- New illustrative sentences and practice items may be authored directly when pedagogically useful; do not present invented examples as quotations or attribute them to a source.
- Keep source-sensitive claims (such as alphabet inventory/order or prescriptive spelling rules) distinct from ordinary illustrative examples. Verify claims against suitable references, and record source details when a factual linguistic claim depends on them.
- Prioritize varied examples, clear meaning, natural usage, gradual difficulty, and useful repetition without duplicating quiz question text within the same lesson.
- Keep KejyarBot spelling policy separate from Avasin Code.

## Lesson-example expansion (25 October 2026)

- Added further original illustrative material to lessons 1–6: greetings and introductions; additional letter/word examples; everyday polite expressions; number sentences and dialogue; color descriptions; and home/school vocabulary with a short dialogue.
- These additions are authored teaching examples, not quotations attributed to any book. They broaden practice beyond the single orthography reference.
- Re-fetched and parsed `lessons.json` after the update: JSON is valid and all six lesson records remain present.
- CI run #254 passed for commit `1f7e2c427d6ab324585f8dc761e689e5805f7915`: https://github.com/avasinim/KejyarBot/actions/runs/40196506760 .
- This structural CI result does not certify every new sentence's regional naturalness or settle source-sensitive spelling rules; those remain separate editorial review items.

## Regression coverage for expanded examples (25 October 2026)

- Added `test_recent_example_expansion_remains_in_all_six_lessons` in `tests/test_content.py` to guard representative new phrases in every lesson.
- Re-read the test file after commit `6300187b7f59ac292ea0481ac0234e4dcf0be3c7`.
- CI runs #258 and #259 passed for that commit:
  - https://github.com/avasinim/KejyarBot/actions/runs/40196636041
  - https://github.com/avasinim/KejyarBot/actions/runs/40196640104

## Speech-quota failure-path test correction (25 October 2026)

- Corrected `test_failed_generation_does_not_consume_daily_quota`: removed a pre-existing reservation that obscured the intended assertion, and now verify a failed generation leaves usage at zero.
- Re-read the updated test file; CI run #262 passed for commit `f06d810f7f878e030044d22c54f2e8bf1dfa67ae`: https://github.com/avasinim/KejyarBot/actions/runs/40196876297 .

## Quiz callback regression coverage (25 October 2026)

- Added `tests/test_bot_quiz_callbacks.py` to cover malformed answer callback data, out-of-range option indexes, and stale buttons from a previous question. Each case verifies the active quiz index, score, and current question ID remain unchanged.
- Re-read the new test file on the working branch. CI runs #266 and #267 passed for commit `0e894482d52b77bf738500ff923e1d9fc5307b73`:
  - https://github.com/avasinim/KejyarBot/actions/runs/40197094742
  - https://github.com/avasinim/KejyarBot/actions/runs/40197098114

## Daily-chat and menu transition regression coverage (25 October 2026)

- Extended `tests/test_bot_quiz_callbacks.py` to verify a quiz is blocked until its lesson is completed and starts correctly after completion, including recording the first question message ID. These are mocked handler tests, not live Telegram tests.


- Added `tests/test_bot_message_mode.py` to check that ordinary text remains in daily-chat mode and that choosing a lesson button exits daily-chat mode and routes into the lesson handler.
- These tests exercise the message-handler integration with mocked Telegram objects; they do not replace a live Telegram test.
- Test commit: `2e478b996573e0b6adbe6074b009e1143697f639`.

## Additional quiz callback regression coverage (25 October 2026)

- Added tests for a valid final answer completing the quiz and claiming the reward once, and for a valid answer advancing to the next question with the updated message ID and score.
- These complement the malformed callback, out-of-range option, and stale-question tests. They are mocked unit tests; they do not replace a live Telegram test.
- Test file: `tests/test_bot_quiz_callbacks.py`; commit: `8d6de4a465949a625e3d84b7b65e056878c79ba2`.

## Manual Telegram test preparation (25 October 2026)

- Added `docs/TEST_RUNBOOK.md` with a test-bot-only setup, token/production-data safety boundaries, and a step-by-step checklist for lessons, reward idempotency, quiz callbacks, daily-chat exit behavior, persistence across restart, and speech safety.
- Re-read the runbook after commit `48814bbd9a69fde620a351514e04e7a205a9ece4`. This is preparation only: **no live Telegram test was executed**, because a separately authorized test bot/token and isolated environment have not been provided in this workflow.
- CI triggered for the runbook commit: https://github.com/avasinim/KejyarBot/actions/runs/40197282682 .

## Items deliberately not changed

- Lesson 2 states that the Sorani Kurdish alphabet has 34 letters, while the lesson presents a sample of letters rather than a complete alphabet table. The claim and the exact inventory/order should be checked against the selected edition of Diako Hashemi's `پوختەی ڕێنووس و خاڵبەندی` before changing either the number or the examples.
- Some spellings in lesson and quiz text need source-based orthographic review. The exact edition and relevant pages have not yet been verified, so no speculative global replacement or application of Avasin Code was made.
- Quiz coverage is introductory and checks basic recall; passing structural tests does not prove the linguistic accuracy or completeness of the teaching material.

## Source edition selected for the next pass

- The working reference is now the **third updated edition dated 16 August 2024**, linked from the preparer's website: https://diyako.yageyziman.com/wp-content/uploads/2024/08/Puxtey_Renus_U_Xallbendi_Weshani_3_New.pdf .
- Kurdipedia's record lists several editions, including 90-page PDF versions from 2022 and 2024: https://www.kurdipedia.org/default.aspx?lng=1&q=20211004184500395359 .
- The PDF's title page identifies it as the third updated edition. Its relevant rule pages still need to be read and compared before changing any lesson, quiz, or infographic wording.

## Next review steps

1. Inspect the selected edition's relevant pages for alphabet inventory/order and spelling rules.
2. Compare lesson text, quiz wording, and infographic labels against those pages.
3. Make only evidence-backed corrections and add regression tests for confirmed rules.

## Safety boundary

This audit is documentation only. It does not change `main`, production bot settings, production databases, migrations, or prerecorded audio assets. KejyarBot's orthography remains separate from Avasin Code.

## Legacy quiz-data file note (25 October 2026)

- Runtime code in `bot.py` loads `quiz.json` as `QUIZ_DATA`; the separate `quizzes.json` file is not referenced by the reviewed runtime entry point and contains an older, partial `lesson_3` schema.
- Kept `quizzes.json` untouched in this stability pass to avoid deleting potentially user-retained material without confirmation. Treat `quiz.json` as the active quiz source unless a repository-wide reference check establishes a different intended use; before any future removal, search all scripts, tests, documentation, and deployment configuration for references.

## Stability verification checkpoint (25 October 2026)

- The stability branch head for this checkpoint is `106188d95a4ef7e2a904459e56c21b22addc4e36` (`docs: record latest stability verification checkpoint`). It includes `277f6cd24434612d597bf5451d28aa4a881c5cc0` (`Fix SQLite connection cleanup and quota transactions`) as its parent, so the SQLite cleanup and quota fixes are present at the reviewed head.
- GitHub Actions run #40210284689 completed successfully for the current branch head. Its `checks` job completed dependency installation, `python -m compileall -q .`, and `python -m unittest discover -s tests -v` successfully:
  - https://github.com/avasinim/KejyarBot/actions/runs/40210284689
- Earlier runs #40209804446 and #40209801402 also passed for the parent code commit `277f6cd24434612d597bf5451d28aa4a881c5cc0`.
- This checkpoint verifies automated code and regression tests only. It does not verify live Telegram behavior, regional naturalness of every Kurdish example, or source-based orthographic correctness.
- Lesson 2 remains intentionally described as a sample rather than a complete alphabet inventory until the selected 2024 reference edition and relevant pages are checked. Do not treat the infographic's six examples as a full alphabet table.
- Manual Telegram testing remains blocked on an authorized separate test bot/token and isolated test environment. No production token should be requested or exposed.



## Source-verified lesson 2 orthography correction (25 October 2026)

- The selected third updated edition of Diyako Hashemi's *Puxtey Renus u Xallbendi* is indexed with its alphabet section on page 3. The extract explicitly gives the spelling **«ئەلفبێ»**, rejects **«ئەلفوبێ»** and **«ئەلف بێ»**, and states a 34-letter inventory. Source: https://diyako.yageyziman.com/wp-content/uploads/2024/08/Puxtey_Renus_U_Xallbendi_Weshani_3_New.pdf
- Based on that source, corrected the lesson 2 heading/term, learning-path label, quiz prompt, and infographic title from «ئەلفوبێ» to «ئەلفبێ». Updated the corresponding content-consistency test to lock in the corrected term.
- The 34-letter statement remains in the lesson, while the displayed letter examples and infographic remain explicitly a sample, not a full inventory. No alphabet ordering or list was invented.
- Re-read the changed files after updates and run CI to confirm consistency. Source extract is searchable/indexed; this note does not claim visual inspection of the PDF page image.


## Alphabet spelling regression guard (25 October 2026)

- The searchable extract of the selected third updated edition (16 August 2024), page 3, uses «ئەلفبێ» and explicitly rejects «ئەلفوبێ» and «ئەلف بێ»; it also states a 34-letter inventory. Source: https://diyako.yageyziman.com/wp-content/uploads/2024/08/Puxtey_Renus_U_Xallbendi_Weshani_3_New.pdf
- Added `test_alphabet_spelling_matches_selected_reference` to check that the lesson-2 title/content, learning-path labels, quiz prompts/options, and lesson-2 infographic contain the approved term and do not reintroduce either rejected spelling.
- This is a focused spelling regression check, not a complete audit of alphabet inventory/order or every orthographic rule. The infographic remains a sample, not a full alphabet chart.
- CI run #40210996888 passed before this new test was added; the new test requires a fresh CI run after commit.


## Review of lessons 1–6 after alphabet spelling guard (25 October 2026)

- Re-read all six lesson records and their quiz records on `fix/kejyarbot-stability-2026-10-25`.
- Confirmed the six lesson keys/titles align with the learning-path catalog, and each lesson has quiz items; existing regression tests already require nonempty unique quiz questions, distinct options, and an answer present among the options.
- Lesson 2 correctly presents a selection of letters as examples and explicitly warns that it is not a complete alphabet inventory. No full alphabet chart or letter-order claim was added.
- No further content edits were made in this pass: possible wording/spacing choices in the Kurdish examples need page-level evidence from the selected orthography reference before changing them.
- The spelling regression test's newline separators were corrected in commit `ae4d3df`. Although the status-check endpoint returned no individual statuses, GitHub Actions subsequently confirmed successful Python checks for commit `18e5314` and for the follow-up audit-document commit `df8335a` (run `40216024376`). No live Telegram test was performed. Production, `main`, and PR merge state remain untouched.


## CI verification for content audit update (25 October 2026)

- GitHub Actions workflow run `40215980145` for commit `18e53144620a55ceef51f91ae506018e64eef6ba` completed with conclusion `success`.
- The `checks` job completed successfully, including dependency installation, `python -m compileall -q .`, and `python -m unittest discover -s tests -v`.
- This confirms the automated suite at that commit; it does not replace manual Telegram testing or expert/source-based review of every Kurdish phrase.
- Manual Telegram test remains blocked until an authorized test bot/token and isolated test environment are available. No production token or database was accessed.


## Latest audit-document commit CI (25 October 2026)

- Commit `df8335a01c88237c285e76fc20f7cbc57cfed58b` passed GitHub Actions run `40216024376`.
- The `checks` job succeeded for dependency installation, Python compilation, and the full unittest discovery command.
- This is automated repository validation only; Telegram integration remains untested in a separate authorized test environment.


## Quiz coverage and regression check (25 October 2026)

- Re-read `lessons.json` and `quiz.json` from the protected work branch after the lesson-one quiz addition.
- All six beginner lessons now have four quiz questions each (24 total). Every question has non-empty text, distinct options, and an answer that appears among its options; no structural quiz issues were found in this pass.
- Added a regression assertion in `tests/test_content.py` requiring at least four questions for each beginner lesson, so future edits cannot silently reduce a lesson back to fewer than four.
- GitHub Actions run `40216155708` for commit `03b70e98d0811ac6d06f8813e99a6a5d266b9705` completed successfully. The `checks` job passed dependency installation, `python -m compileall -q .`, and `python -m unittest discover -s tests -v`.
- This verifies automated structural checks only. It does not certify every Kurdish phrase against the selected book or count as a live Telegram test.


## Verification of quiz-coverage regression commit (25 October 2026)

- The follow-up audit-document commit `419fdfb8a8ec1b9b912ef7162c9f5f6d6f6e994f` passed GitHub Actions run `40216215362`.
- The `checks` job completed successfully: dependency installation, `python -m compileall -q .`, and `python -m unittest discover -s tests -v`.
- Re-read all six lesson records and their quizzes. Each lesson has four questions; the structural check found no empty question text, repeated options within a question, or answer missing from its options.
- A direct attempt to access the selected 2024 third-edition PDF for page-level verification was not accessible in this audit session. Therefore no uncertain spelling or wording was changed on guesswork. Manual Telegram integration testing is still pending in a separate authorized test environment.


## Online source cross-check for lesson 2 (25 October 2026)

- Checked the author's publicly accessible online page “زمانی کوردی: ڕێنووس”: https://chawg.org/zimani-kurdi-renus/ .
- The page's alphabet section explicitly recommends “ئەلفبێ” and rejects “ئەلف بێ”, “ئەلف و بێ”, and “ئەلفوبێ”; it also states that the Central Kurdish alphabet has 34 letters. This corroborates two claims already represented in the lesson and its automated test.
- The online page is not the selected 2024 third-edition PDF, and its content may be updated. It does not validate every spelling or the complete alphabet order in the book. Lesson 2 remains clearly labeled as a selection of examples rather than a complete chart; no content was changed just to match an unverified source version.
- The selected PDF remains inaccessible through the current audit reader. Continue using page-level citations before changing other prescriptive spellings.


## Expanded letter examples and infographic refresh (25 October 2026)

- Expanded lessons 1, 3, 4, 5, and 6 with additional everyday dialogues, contextual examples, location phrases, number practice, color descriptions, and role-play prompts.
- Rebuilt lesson 2 as a letter-by-letter practice lesson with 34 entries and three example words per entry. Added four quiz questions, bringing lesson 2 to eight questions.
- Redesigned all six SVG infographics in a consistent forest-green, warm-cream, and copper/gold palette. The alphabet infographic now shows all 34 practice entries and three words for each entry; the other five use six text-led teaching cards each.
- SVG text uses explicit RTL direction, plaintext bidi handling, and the Noto Naskh Arabic / Noto Sans Arabic font stack to preserve Kurdish text as editable text rather than rasterized lettering.
- Source cross-check: Kurdish Academy of Language publishes a comparative Kurdish alphabet table and a Kurdish phonetic alphabet table: https://kurdishacademy.org/?page_id=284 and https://kurdishacademy.org/?page_id=357 . These are useful references for checking the writing systems, but they do not constitute a formal endorsement of these particular teaching graphics.
- The examples are authored for practice and are not presented as quotations. The lesson explicitly cautions that alphabet inventories and ordering can vary by writing-system convention; the selected PDF edition has still not been verified page by page.
- Added a regression test requiring 34 lesson/infographic example pairs to remain present. Structural and source-level spelling review remain separate; automated tests cannot establish that every example is the most natural regional choice.
- The changes remain on fix/kejyarbot-stability-2026-10-25. No production bot, database, migrations, main, or PR merge was touched.

- CI run #359 passed for commit `5a09bddbbceb08467971150ba2192e93c03e7899` (compileall and the full unittest suite): https://github.com/avasinim/KejyarBot/actions/runs/40217026467 .


## Expansion to ten beginner lessons (25 October 2026)

- Added lessons 7–10: family and close relations; food and drink; days of the week and time; simple sentences and question words.
- Added four distinct quiz questions for each new lesson. The full beginner path now contains ten lessons, each with a corresponding SVG infographic.
- Updated lesson navigation, sequential unlocking, completion badges, final-lesson quiz callback, and regression tests to use the ten lesson records. Lesson order is now derived from the ordered lesson data rather than fixed at six.
- The new material uses original practice examples, not quotations. Regional vocabulary and spelling still require human review before public release.
- CI run #389 passed for commit `58e02d8d8c5eedc971decef803b83517f3973b2e`: dependency installation, `python -m compileall -q .`, and the full unittest suite all succeeded. Run: https://github.com/avasinim/KejyarBot/actions/runs/40217276132 . This verifies automated structure and behavior, not every regional spelling or a live Telegram test.


## Expanded alphabet examples and infographic (25 October 2026)

- Expanded lesson 2 from three examples per practice entry to five, for 34 entries and 170 total word examples.
- Rebuilt `assets/infographics/lesson-02-letters-sample.svg` in a four-column, right-to-left layout. Each entry has its own card, five examples, and a consistent forest-green / warm-cream / copper-gold visual style.
- Added a regression test that parses the lesson's example section and checks all 34 entries have exactly five examples and that every word appears in both the lesson and SVG.
- This is an authored teaching aid, not an official alphabet chart. Some items (including combinations such as `وو`) should be classified carefully before claiming a definitive alphabet inventory. The examples need human review for regional naturalness and source-sensitive spelling.
- This change does not use Avasin Code and does not alter `main`, production credentials, or any database.
- CI run #403 passed for commit `d6908a7ba97e87225800d7c6e405cc79cc0a3b55`: https://github.com/avasinim/KejyarBot/actions/runs/40217641807 . The Python compile and unit-test workflow passed, including the 170-example lesson/infographic consistency check. This does not certify every example as a formal academic spelling or confirm live Telegram rendering.


## Further expansion of lessons 7–10 (25 October 2026)

- Added ten additional sentence examples to each of lessons 7, 8, 9, and 10 (40 new practice sentences total), covering family descriptions, food requests and preferences, weekdays and schedules, and question formation.
- Reviewed several phrases for clearer grammar and naturalness, including the verb agreement in the food lesson and more idiomatic wording for meeting friends.
- Expanded each of the four quizzes from four to six questions. The new questions reinforce polite requests, food/drink verbs, weekday sequencing, time references, question words, and sentence order.
- Updated the four corresponding SVG infographics to show four example lines per card, using RTL text, bidi handling, and the shared Kurdish-Arabic font stack.
- Added regression coverage for ten extra example lines per lesson, six quiz questions per lesson, XML validity, and exact text shared between each lesson and its infographic.
- The first CI attempt exposed a mismatched expected phrase in the new test (the content itself was present with a longer sentence). The assertion was corrected to match the exact lesson wording. CI run #428 then passed: https://github.com/avasinim/KejyarBot/actions/runs/40217899262 .
- These are original beginner-level practice examples. Automated tests validate structure and consistency, not official academic endorsement or every regional wording; human Kurdish-language review and manual Telegram rendering tests remain pending.
- No production credentials, database, migrations, or `main` changes were made. Work remains on `fix/kejyarbot-stability-2026-10-25`.


## Test-name consistency cleanup (25 October 2026)

- Renamed the message-mode regression test from `test_lesson_catalog_lists_all_six_lessons_even_when_locked` to `test_lesson_catalog_lists_all_ten_lessons_even_when_locked`. Its assertion already verified ten lessons; only the stale test name was wrong.
- CI run #432 passed after the rename: https://github.com/avasinim/KejyarBot/actions/runs/40218025405 .
- This is a test-maintenance change only; lesson behavior and runtime code were not changed.


## Quiz coverage balanced across all ten lessons (25 October 2026)

- Added two new quiz questions to each of lessons 1, 3, 4, 5, and 6 (10 questions total), bringing every lesson to at least six questions. Lesson 2 retains eight questions; lessons 7–10 retain six each.
- New questions cover introductions and responses to thanks, requesting help, agreement, number sequencing and addition, color recognition, and classroom/home objects and position.
- Strengthened `tests/test_content.py` so all ten lessons must have at least six quiz questions. Existing checks still validate non-empty question text, distinct options, and that every answer appears among its options.
- CI run #438 passed after the quiz-coverage test update: https://github.com/avasinim/KejyarBot/actions/runs/40218153690 . Automated CI validates structure and consistency; the new language examples have not been formally certified against the selected orthography book. Human Kurdish-language review and manual Telegram testing remain pending.
- No production bot, production database, migrations, or `main` branch changes.


## Quiz alignment check (25 October 2026)

- Two newly added questions were refined to match phrases explicitly taught in their lessons: lesson 1 now tests the exchange asking and stating a name; lesson 3 tests the taught use of the word meaning an affirmative answer.
- Added a regression test for these two lesson-to-quiz links.
- This focused check does not replace human linguistic review of all 62 quiz questions. Manual Telegram testing remains pending.


## Alphabet quiz answer clarity (25 October 2026)

- Refined three lesson 2 quiz answers so they follow the lesson's own definitions more closely: alphabet as a set of written signs, a letter as a written sign, and the contrast between «ر» and «ڕ».
- Added a regression test tying those answers to the relevant explanatory statements in the lesson.
- This is a consistency improvement, not a claim of page-by-page validation against the selected 2024 orthography book. Broader human review and manual Telegram testing remain pending.


## Lesson-to-quiz answer alignment follow-up (25 October 2026)

- A broader comparison of all 62 quiz answers against their lesson text found three answers whose wording or example was not directly aligned with the lesson.
- Updated the alphabet definition answer to use the lesson's own definition, added an explicit «کتێبەکە لەژێر مێزەکەیە» example for the location question, and matched the fictional-family answer to the lesson's instruction.
- Updated the alphabet-definition regression assertion to compare against the lesson wording. This is a text-alignment check; it does not establish that every language example is independently validated by a human editor or by page-level evidence from the selected 2024 reference book.
- Manual Telegram rendering and end-to-end interaction tests remain pending.

- Continued the same alignment pass by making the food/drink and location quiz choices quote the exact sentences used in their lessons, including the contrast «نەک لە ژێرەوەی» in the location example.

- CI caught two answer/options mismatches introduced during this wording alignment. The correct options are now synchronized with the answers; a fresh CI run is required to confirm the repair.


## Documentation consistency check (25 October 2026)

- Corrected a stale count in `docs/ORTHOGRAPHY_POLICY.md`: lesson 2 contains 34 practice entries with five examples each (170 total), not three examples per entry.
- Kept the important qualification that these are practice entries, not a definitive official alphabet inventory. The selected 2024 reference PDF has not been verified page by page, and human review remains necessary.


## Natural phrasing review — lesson 8 (25 October 2026)

- Replaced the awkward example `من چای حەز دەکەم.` with `من چای بەبێ شەکر حەز لێ دەکەم.`. The replacement reuses a fuller example already present in the same lesson and avoids introducing a new unverified spelling rule.
- This is a pedagogical phrasing correction, not a claim of page-level verification against the selected 2024 orthography handbook. Human Kurdish-language review and manual Telegram rendering checks remain pending.


## Quiz coverage review — lessons 9 and 10 (25 October 2026)

- Reduced repeated quiz concepts: lesson 9 now checks identifying a daily routine sentence, and lesson 10 now checks a causal question using `بۆچی؟`, instead of repeating a previously tested day-order or location-word question.
- Added `test_lesson_nine_and_ten_quizzes_cover_distinct_skills` to guard the intended question coverage and verify the answers remain in both the options and lesson text.
- This is a pedagogical assessment adjustment, not a change to orthography policy. Full human review and manual Telegram testing remain pending.


## Quiz skill-coverage review — lessons 1 and 5 (25 October 2026)

- Re-read beginner lessons 1–6 and their quiz items, focusing on repeated assessment skills rather than changing uncertain orthography.
- Lesson 1 had two questions testing nearly the same basic name-introduction response. Replaced one with a polite request to repeat a name, using the exact phrase already taught in the lesson.
- Lesson 5 had a question repeating the green-leaf recognition skill. Replaced it with a contrast question using the exact taught example contrasting a yellow page and a white page.
- Added `test_lessons_one_and_five_quizzes_cover_distinct_skills` to check that both answers are present in the lesson and the correct options.
- No spelling-policy decisions or source-sensitive vocabulary were changed. This is a pedagogical coverage improvement, not page-level verification against Diyako Hashemi's handbook.
- Re-read the modified quiz and test files after the edits; full CI verification is required for these commits. Live Telegram testing remains pending in a separate authorized test environment. No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 4 scope and example review (25 October 2026)

- The lesson objective introduces numbers 0–10, but two supplementary examples introduced the number twelve and weekday names before those topics are taught in the learning path.
- Replaced those examples with simple classroom/object-counting sentences using numbers already within the lesson scope. This reduces premature vocabulary and keeps the lesson focused on beginner counting.
- Added `test_lesson_four_examples_stay_within_beginner_number_scope` to protect the intended examples and flag the removed scope drift.
- This is a pedagogical sequencing change only; no orthography rule or source-sensitive spelling was inferred. Manual language review and Telegram testing remain pending.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 4 quiz skill diversity follow-up (25 October 2026)

- Replaced the lesson 4 question asking which number lies between 4 and 6; this overlapped with the existing question asking which number follows 5.
- The replacement asks the learner to identify a correctly formed sentence connecting a number with an object, using the exact taught example `دوو پێنووسم هەیە.`.
- Added `test_lesson_four_quiz_assesses_number_in_context` to verify the answer is taught in the lesson and appears among the options.
- This broadens assessment from sequence recall to using number vocabulary in context. It does not assert independent source-level validation of spelling or regional phrasing.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 6 quiz vocabulary alignment (25 October 2026)

- The lesson teaches `پێنووس` as the school writing tool, while one quiz answer used `قەڵەم`. Although both terms can be used in Kurdish contexts, switching terms without explaining the relationship adds avoidable uncertainty for beginners.
- Updated the quiz answer to the exact term taught in the lesson (`پێنووس`) and added a regression test to keep the assessment aligned with lesson vocabulary.
- This is a consistency/pedagogy change, not a claim that the alternate term is universally incorrect. Regional and source-based terminology still needs human review against the selected handbook where relevant.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 1 quiz coverage follow-up (25 October 2026)

- Reviewed the six beginner questions for repeated assessment targets. Two questions focused on introducing or responding with a person’s name, while the lesson also teaches a distinct morning greeting.
- Replaced one repeated name-introduction item with a question about choosing the appropriate morning greeting (`بەیانی باش`). The answer is present in the lesson text and among the options.
- Added a regression test to protect this coverage and answer-to-lesson alignment. This is an assessment-design adjustment, not an orthography correction.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 3 contextual quiz coverage (25 October 2026)

- Reviewed the lesson 3 quiz for whether it tested only definitions or also practical use. The standalone item asking which word is polite for a request overlapped with the lesson’s direct vocabulary list.
- Replaced it with a market scenario asking which expression is suitable for asking a price (`تکایە، ئەمە چەندە؟`), already present in the lesson. This tests context-sensitive application while retaining the lesson’s polite-request objective.
- Added a regression test to ensure the scenario and answer remain grounded in the lesson text. No source-sensitive orthography was changed.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 2 alphabet practice inventory regression check (25 October 2026)

- Reviewed the alphabet practice list without treating it as a definitive official alphabet inventory; the lesson itself correctly flags that a source-verified formal inventory requires a named academic reference.
- Added a regression test confirming the current teaching list contains 34 practice entries and exactly five non-empty example words per entry. This protects the documented practice format and catches accidental truncation or malformed rows.
- No alphabet order, letter classification, Kurdish spelling, or example word was changed because those changes would require stronger source-level evidence.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lessons 4–5 applied-skill quiz regression checks (25 October 2026)

- Reviewed the beginner-number and color quizzes against their lesson objectives. Lesson 4 already includes a simple addition-in-context item (three apples plus two more); Lesson 5 already includes a sentence comparing two colors.
- Added regression tests that protect these applied-skill items and confirm their correct answers remain present in the lesson text and quiz options.
- No lesson wording, answer, or spelling was changed; this update protects existing coverage rather than claiming a new curriculum change.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 8 quiz variety and breakfast vocabulary (25 October 2026)

- The lesson 8 quiz had two items assessing polite food/drink requests, while the lesson also teaches breakfast vocabulary in a concrete sentence.
- Replaced one repeated request item with a question about what is eaten for breakfast, using the existing lesson phrase `هێلکە و نان دەخۆم` and distractors from unrelated vocabulary.
- Added a regression test to keep the new assessment tied to the lesson text and its answer options. No lesson content or orthography was changed.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Lesson 9 clock-time comprehension (25 October 2026)

- Replaced a broad time-of-day vocabulary quiz item with a question that checks whether learners can retrieve the specific class start time stated in the lesson dialogue/example.
- The answer `کاتژمێر نۆ` is directly grounded in the lesson sentence `وانەکە کاتژمێر نۆ دەست پێ دەکات`; added a regression test to preserve this alignment.
- Lesson 10 questions were reviewed for variety; the existing quiz already checks complete sentences, question words for place/object/reason, and word order, so its content was left unchanged.
- No `main`, production bot/database, migrations, or PR merge was touched.


## Final automated content-integrity sweep (25 October 2026)

- Re-read `lessons.json`, `quiz.json`, `tests/test_content.py`, and this audit log on the protected work branch after the lesson 9 update.
- Integrity checks: 10 lesson records, quiz records for all 10 lessons, 62 questions total; no repeated question text within a lesson, no duplicate options, no answer missing from its options, and no answer missing from its own lesson text.
- The existing test suite already enforces unique question text and unique options, so no redundant test was added.
- This is structural/content-alignment evidence only. It does not establish page-by-page compliance with the 2024 third edition of Diyako Hashemi’s handbook or prove that every sentence is idiomatic. No spelling was changed without source-page evidence.
- Next release blockers remain: page-level orthography review against the selected handbook edition, browser/mobile visual review of the SVG infographics, and manual Telegram testing in a separate test environment.
- No `main`, production bot/database, migrations, or PR merge was touched.

## Dynamic-speech approval guard regression test (25 October 2026)

- Added a focused test for `speech.py`: dynamic generation remains disabled when the enable flag is absent, remains blocked when the configured voice ID differs from the explicitly approved ID, and is considered configured only when the enable flag, API key, voice ID, and matching approved voice ID are all present.
- The test calls the local guard directly with mocked environment variables and does not send a request to the speech provider or use real credentials.
- This protects the existing safety gate; it does not enable dynamic speech or establish that generated Kurdish audio is linguistically acceptable.
- No runtime bot logic, voice configuration, `main`, production bot/database, migrations, or PR merge was changed.


## Daily-conversation exit-priority regression (25 October 2026)

- Review found that a message combining a greeting and an explicit goodbye (for example, “سڵاو، خواحافیز”) was handled by the earlier greeting branch, leaving daily-chat mode active despite the goodbye.
- Moved recognized goodbye phrases into the early exit branch so explicit exit intent takes priority over greeting and role-play matching; the exit still clears role-play state.
- Added a regression test for the combined greeting/goodbye case and verifies that chat mode and role-play state are cleared.
- This is a narrow conversation-flow fix; it does not alter lesson text, quiz answers, the KejyarBot orthography policy, speech settings, main, production data, or PR merge status.


## Quiz option minimum consistency check (26 October 2026)

- Rechecked all ten quiz sets: 62 questions total, and every question currently has at least three distinct options; lesson 4 includes one four-option item.
- The general content regression test had drifted to accepting two options, which was weaker than the project’s documented minimum. Updated the assertion to require at least three options so future two-choice regressions fail.
- This change validates quiz structure only; it does not certify every Kurdish example against the selected reference book or replace manual Telegram testing.
- Change is limited to `tests/test_content.py` and this audit record on `fix/kejyarbot-stability-2026-10-25`. No `main`, production bot/database, migrations, voice assets, or pull-request merge was changed.

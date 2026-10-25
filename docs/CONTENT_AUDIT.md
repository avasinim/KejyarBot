# KejyarBot lesson and quiz content audit

Branch reviewed: `fix/kejyarbot-stability-2026-10-25`

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
- The first CI attempt exposed a mismatched expected phrase in the new test (the content itself was present with a longer sentence). The assertion was corrected to match the exact lesson wording; verification for the corrected test commit is pending.
- These are original beginner-level practice examples. Automated tests validate structure and consistency, not official academic endorsement or every regional wording; human Kurdish-language review and manual Telegram rendering tests remain pending.
- No production credentials, database, migrations, or `main` changes were made. Work remains on `fix/kejyarbot-stability-2026-10-25`.

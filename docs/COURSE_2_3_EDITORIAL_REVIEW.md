# Course 2–3 Editorial Review Queue
Updated: 2026-10-28
Branch: `fix/four-course-structure-2026-10-27`

## Scope and safety

**Editorial principle clarified on 2026-10-28:** These are beginner-friendly educational bot courses. Learner-facing lessons should not contain source lists, citations, page numbers, or bibliographic discussion. Do not hold simple teaching material to a publication-level evidence standard. Focus review on clear Kurdish, useful examples, beginner accessibility, internal consistency, and quiz answers matching the lesson. Use external references privately only if a concrete factual uncertainty needs resolving; do not require a source for every lesson or example.


This queue is for Course 2 (daily conversation) and Course 3 (unified orthography). Course 1 is out of scope unless a regression blocks integration. Course 4 remains planned and empty. This document is a review tracker, not a claim that the courses are linguistically or bibliographically approved.

Do not activate either draft course until the checks below are completed. Do not merge the draft PR, deploy, modify the production bot/token/database, or enable dynamic speech without explicit user approval. Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`.

## Course 2 — Daily conversation (12 lessons)

### Completed in this pass
- Rechecked the dialogue against the quiz keys for lessons 4, 5, 10, and 11.
- Confirmed the key answers against their corresponding dialogue lines:
  - Lesson 4: Kêjyar says he has five sisters and no brothers; Argesh says he has two sisters and two brothers.
  - Lesson 5: Argesh asks Kêjyar to call before visiting; Kêjyar agrees.
  - Lesson 10: the library is beside the school and opposite the park.
  - Lesson 11: the pair agree to meet at 8 a.m. at the bus station.
- Rewrote the four quiz explanations to state the relevant dialogue evidence and cleared only those four lessons' dialogue-answer findings.
- CI passed after a test assertion was adjusted to check that review status is rendered independently of whether a lesson still has findings.

### Targeted Course 2 review queue

These are editorial checks to perform, not claims that the wording is necessarily wrong:

| Lesson | Focus for review |
|---|---|
| 1 | Clarified the farewell to «تا دواتر لە بەردەم کتێبخانەکە یەکتر دەبینینەوە»; broader naturalness review across the course remains. |
| 2 | Review the naturalness of the self-introduction and the question/answer about where someone is from. |
| 3 | Polished the question «تۆ بۆچی دێیتە ئەوێ؟» to «تۆ بۆچی دەچیتە ئەوێ؟» so the verb matches the speaker asking why the other person is going to the library. The full dialogue still needs a final naturalness pass. |
| 4 | Quiz keys were checked against the dialogue; review family vocabulary definitions and consistency of singular/plural forms. |
| 5 | Corrected the home-location sentence to «ماڵمان لە گەڕەکێکی ئارامدایە، نزیک پارکەکە» and made the first exercise explicitly cover location, rooms, and home features. The invitation and pre-visit phone-call phrasing still need a broader naturalness review. |
| 6 | Changed the fragment «نیوەڕۆ چۆن؟» to the direct beginner-friendly question «نیوەڕۆ چی دەکەیت؟» to match the lesson's daily-routine topic. Continue the overall naturalness and tense-consistency review. |
| 7 | Aligned the objective with the actual dialogue: breakfast, food preferences, and drinks. The dialogue does not teach ordering food, so that claim was removed from the objective. Continue checking repeated expressions and colloquial naturalness. |
| 8 | Arithmetic is internally consistent: 2 kg apples at 3,000 toman/kg plus 1 kg oranges at 3,000 toman/kg totals 9,000 toman. The lesson's currency wording has been changed from dinar to toman. Check the pricing exchange remains clear for learners. |
| 9 | Smoothed the opening reply to «سڵاو کەژیار، بەڵێ. ئێستا کاتژمێر چەندە؟» so the question about the current time flows directly into the answer. The today/tomorrow timeline remains clear; final date/locale convention review is still needed. |
| 10 | Quiz keys were checked against the dialogue; review the distinction between “beside,” “opposite,” and “behind” with a simple spatial diagram/example if needed. |
| 11 | Quiz key was checked against the dialogue; clarified that the 8 AM meeting at the bus station is also the departure point. Review travel-planning phrasing and consistency of transport terms. |
| 12 | The closing line was polished to “یەکتر دەبینینەوە”; the three quiz keys were structurally checked and remain aligned with the taught phrases. Clarified the meeting question to «کاتژمێر چەند لە بەردەم دوکانەکە کۆببینەوە؟» so the question matches the reply's exact meeting point. |

### Remaining release gates
1. Complete the targeted editorial checks above for all 12 dialogues, including natural Kurdish, consistent names/terms, useful real-life phrasing, and spelling.
2. Recheck every quiz key against the dialogue or lesson text; do not rely on explanations alone.
3. Keep dialogue natural, useful, and understandable for beginners; source citations are not a lesson requirement.
4. Keep each lesson in draft until its practical editorial review and quiz-key checks are complete. Do not require page citations or bibliographic proof as a release gate.

## Course 3 — Unified orthography (12 lessons)

All 12 lessons remain drafts for practical editorial review, not bibliography review. Learner-facing lessons do not need source notes, citations, page numbers, or bibliographies. Focus on whether the explanations are simple, examples are familiar and clear, the Kurdish spelling is consistent with the intended course, and the quiz checks what the lesson actually teaches. The following are the remaining beginner-usability tasks recorded in the lesson data:

| Lesson | Topic | Practical improvement |
|---|---|---|
| 1 | Unicode and unified spelling | Added whole-word comparisons «کورد / كورد» and «یاری / ياری»; final check that the explanation is beginner-friendly remains. |
| 2 | Alphabet and letter/sound distinction | Removed a repeated key point, made the examples concrete (written/seen vs. heard), and changed the quiz to test that distinction directly. The broad claim about letter and sound counts still needs a precise example before release. |
| 3 | Vowels and syllables | Reworked the quiz to ask learners to read aloud and identify syllables; added explicit segmentation «کۆ-مار» and «هێ-لا-نە» plus a syllable-marking exercise. Confirm pronunciation/dialect consistency in final review. |
| 4 | Consonant clusters and syllables | Quiz now asks learners to identify «س» and «ت» in «مەست», directly checking the concrete cluster taught in the lesson; final language review remains. |
| 6 | Difference between ڕ and ر | Quiz asks which familiar word begins with «ڕ»; exercises now directly mark and compare «ڕ»/«ر» in «ڕۆژ», «ڕەنگ» and «باران» rather than using imaginary color marking. Final course spelling review remains. |
| 7 | ک/ك, ھ/ه and ە | Clarified that «هەوا / ھەوا» is only a digital code-point comparison and that «ھەوا» is not an interchangeable ordinary spelling. Replaced generic practice with concrete tasks on «کورد / كورد», the position of «ە» in «کەس», and writing «هەوا» with Kurdish «ه». The quiz now tests the location of «ە» directly; final check against the course spelling convention remains. |
| 5 | Hamza / «ئ» | Replaced the abstract quiz question with direct recognition of «ئاو» and aligned comprehension/role-play tasks with finding and writing «ئ» in the lesson examples. |
| 8 | و، وو، ی و ێ | Replaced the single «وو» sound claim quiz with direct letter recognition: the quiz identifies «ێ» in «شێر», and exercises now mark «و» in «وانە», «وو» in «دوور», «ی» in «یاری», and «ێ» in «شێر». Final review of the course's pronunciation/spelling conventions remains. |
| 9 | Particles and joined spelling | Kept the «لە» recognition example and added concrete spacing practice with «لە ماڵ», «بە خێرایی», and «بە کوردی». The quiz tests the exact two-word form «بە خێرایی» and explicitly avoids presenting that one example as a universal spacing rule; verify general join/separation conventions before release. |
| 10 | Compound and derived words | Expanded the lesson to contrast «کتێب‌خانە» (compound) with «بەهێز» (prefix + base), added a direct comparison exercise, and split the quiz into two checks—one for each category. The lesson cautions against classifying every word by visual splitting alone; final linguistic review against the course convention remains necessary. |
| 11 | Adverbs, loanwords and compound numerals | Replaced the numeral-only quiz with a direct question on «زۆر» in «زۆر خێرا», aligning the check with the lesson's adverb example; loanword and numeral coverage still need review. |
| 11 | Adverbs, loanwords and compound numerals | Reworked exercises and quiz to cover all three parts: «زۆر» modifying «خێرا», «تەلەفۆن» in a sentence, and the exact displayed forms «بیست و یەک» / «سی و دوو». Quiz explanations avoid claiming a universal numeral or loanword rule before the course convention is verified. |
| 12 | Final review | Quiz now asks learners to correct «رۆژ» to «ڕۆژ», directly testing one of the explicit corrections in the practice passage; final consistency check remains. |
| 12 | Final review | Aligned the passage, answer key, exercises, and three quiz items: «كورد» → «کورد», «ياري» → «یاری», and «رۆژ» → «ڕۆژ». Each correction now has its own quiz check. These are lesson-specific examples, not a universal spelling rule; final course-wide convention review remains. |

### Practical review checklist
- Is the explanation easy for a beginner to understand?
- Are examples familiar, correctly written, and sufficient to practice the point?
- Does each exercise teach the stated objective?
- Does every quiz answer match the lesson text, with no ambiguous or duplicate options?
- Keep internal editorial notes out of learner-facing lesson text.
- Do not require citations, page numbers, or a bibliography for these beginner lessons.

## Integration verification

The automated suite checks that all 82 configured lesson IDs across active Courses 1–3 load without collisions, each course keeps its own progression, and Course 4 remains planned and empty. Courses 2–3 are technically active in the integration manifest at the owner's explicit request; lesson-level editorial review metadata remains visible and does not certify language review as complete. Automated checks do not replace practical editorial review or a manual Telegram smoke test.

Manual smoke test must use an authorized isolated test bot/account only. Confirm course navigation, next-lesson unlocking, quiz answer handling, progress isolation, long-message chunking, and optional infographic delivery. Do not use the production bot token for this check.

## Current status

- Runtime/CI: local full suite was run on commit `d4af297a0e54e790ed8e0e31397c775da066bf7c` and passed: 244 tests in 7.238 seconds (`OK`). No GitHub Actions run/status is currently available for that exact head, so CI is not independently verified for this commit.
- Course activation: Courses 2–3 are active in `courses.json` on the integration branch by explicit owner request. Editorial status on lesson records remains `draft_editorial_review`; this is a warning for follow-up review, not a runtime access gate. Course 4 remains planned and unavailable.
- Course 2 quiz pass: structurally checked all 27 quiz items across the two lesson JSON files; answer indices/options are valid and each keyed answer appears in its lesson data. This is a static consistency check, not a live Telegram run.
- Runtime access guard: quiz-answer callbacks now re-check that the lesson belongs to an active course and is completed before accepting further answers; stale quiz state is cleared if either condition fails. Editorial quiz availability is still checked separately.
- Course-menu status label: the menu renders the manifest status; Courses 2–3 appear as active, while editorial review status remains documented on their lesson records. Course 4 remains labelled as planned.
- Course 2: dialogue-to-quiz checks for lessons 4, 5, 10, and 11 remain resolved; lesson 1 farewell wording and lesson 9 date/meeting phrasing plus lesson 12 closing line were clarified. Practical editorial review still pending; lesson 8 now includes the seller's response to the bag request.
- Course 3: concrete examples or clarifications were added in lessons 1, 2, 4, 6, 7, 9, 10, 11, and 12. Lesson 12 now includes a short proofreading passage and answer key. Final language review remains, especially checking examples against the intended course spelling rules.
- Pull request #6 was merged into `fix/four-course-structure-2026-10-27`, not `main`. Subsequent commits on this integration branch still require their own validation; do not infer production deployment from the PR merge.

- Status-map consistency: removed a duplicate `draft_for_review` key in `open_course` and added the same status to the empty-course response map.
- Activation troubleshooting: `bot.py` now checks for a configured Telegram token before initializing SQLite, logs the authenticated test-bot username/ID through `post_init` (never the token), and records startup/polling exceptions with a traceback. This improves diagnosis but is not proof of a successful live Telegram connection; that still requires a separate test-bot token and a local run.

- CI failure triage (2026-10-28): the latest failing workflow exposed a real quiz-callback validation issue in the test path (`query.from_user` was assumed); changed the gate to use `update.effective_user.id`, matching the handler's established identity source. Updated stale regression expectations for the draft lock wording, the corrected Lesson 5 home-location sentence, and the now-expanded comprehension questions in Lessons 10–11. Re-run the full workflow on the final branch head before claiming green; Telegram live smoke testing is still pending.
- CI recheck: workflow run [40679765014](https://github.com/avasinim/KejyarBot/actions/runs/40679765014) passed on commit `7144db2dc5ac1b44a24d0b3691b698d2c0f8866e`: `compileall` passed and all 173 unit tests returned `OK`. Follow-up workflow [40680261689](https://github.com/avasinim/KejyarBot/actions/runs/40680261689) also passed after adding the standalone token/network preflight script and updating the runbooks. Live Telegram smoke testing remains outstanding.
- Activation preflight: added `check_telegram_connection.py`. It reads the local `.env` or process environment, checks Telegram `getMe`, distinguishes missing token, rejected token, timeout and network failure, and never prints the token or raw request exception. It does not start polling or send messages.
- Always-on hosting preparation (2026-10-28): added `railway.toml` with `python bot.py`, `restartPolicyType = "ALWAYS"`, and a single replica; `database.py` now accepts `KEJYAR_DB_PATH` so Railway can store SQLite on a mounted persistent volume. Added `docs/ALWAYS_ON_RAILWAY.md` and linked it from README. This is configuration/runbook preparation only: no Railway service was created or deployed, because the previously used Railway trial was expired and service/volume/billing settings require dashboard access and owner approval. Live Telegram polling and persistence across redeploy still need a smoke test.

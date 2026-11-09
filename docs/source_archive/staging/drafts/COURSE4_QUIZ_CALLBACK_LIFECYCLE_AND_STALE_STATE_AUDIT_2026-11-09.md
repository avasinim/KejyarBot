# کۆرسی ٤ — پشکنینی lifecycleی کویز، callback و stale state

**بەروار:** 2026-11-09  
**Base:** `main`  
**Scope:** `bot.py`، `database.py`، `course_quiz_review.py` و test filesی callback/runtime  
**دۆخ:** static source audit؛ هیچ test run یان code change ئەنجام نەدراوە.

## ١. پوختە

ڕێڕەوی کویز لە runtimeدا چەند پاراستنێکی باشی هەیە:
- duplicate launch callback لە هەمان start message دووبارە quiz دروست ناکات.
- question callbackی stale بە message_id دەناسێتەوە و ڕەتی دەکاتەوە.
- duplicate answer لە کاتی processing بە `answer_in_progress` قەدەغە دەکرێت.
- callbackی malformed/out-of-range ناتوانێت indexی پرسیار بگۆڕێت.
- failureی delivery لە ناو answer flowدا stateی کویز پاک دەکاتەوە.
- database ledger خەڵاتی کویز بە یەکجار تۆمار دەکات.

بەڵام lifecycleی کویز بە review statusی وانە بە تەواوی نەبەستراوەتەوە. ئەمە لە quiz start، global menu و finalizationدا کەلێنی policy دروست دەکات.

## ٢. ڕێڕەوی start

لە `start_quiz`:
1. lesson ID دەناسێتەوە.
2. active-course status پشکنین دەکات.
3. `quiz_is_available(lesson)` پشکنین دەکات.
4. quiz bank پشکنین دەکات.
5. completion و sequence پشکنین دەکات.
6. duplicate start لە هەمان message ID ڕەت دەکاتەوە.
7. quiz state دروست دەکات و پرسیاری یەکەم دەنێرێت.

**کەلێن:** `lesson_is_pending_review(lesson)` لە start flowدا بە ڕاستەوخۆ بانگ ناکرێت. لە دۆخی ئێستادا وانەکانی ٣٢–٤٦ quiz bankیان بەتاڵە، بۆیە empty-bank check ڕێگری دەکات؛ بەڵام ئەمە قفڵی review نییە. ئەگەر bankێک بە هەڵە بۆ pending lesson زیاد بکرێت، قفڵەکە دەتوانێت بشکێت.

## ٣. Global quiz menu

`quiz_menu_items` ئەمانە پشکنین دەکات:
- quiz bank هەبێت؛
- `quiz_is_available` true بێت؛
- وانەکە completed بێت؛
- `can_open` true بێت.

**کەلێن:** helperی review status بە ڕاستەوخۆ پشکنین ناکرێت. `quiz_is_available` لە `course_quiz_review.py` بە لیستی legacyی Course1 بەستراوە و policyی گشتی بۆ statusی Course4 نییە. تاقیکردنەوەی menu بۆ pending source review هەیە، بەڵام لەو testەدا `quiz_is_available=False` mock کراوە؛ ئەمە ناتوانێت بەڵگەی قفڵی pending status بە خۆی بێت.

## ٤. Question و answer callback safety

### ٤.١ Selection و submission
- `select_quiz_answer` question message ID و option index پشکنین دەکات.
- هەڵبژاردنی وەڵام پێش await لە stateدا هەڵدەگیرێت.
- `submit_quiz_answer` تەنها selected integer دەگوازێتەوە بۆ `quiz_answer`.
- `quiz_answer` question message ID، index، options، answer، score و callback data پشکنین دەکات.

### ٤.٢ Duplicate/stale callbacks
- `answer_in_progress` duplicate callback لە processingدا ڕەت دەکاتەوە.
- `question_message_id` بۆ questionی کۆن ڕێگری دەکات.
- پێش await، handler claim دەکات و question_message_id پاک دەکاتەوە؛ ئەمە raceی duplicate answer کەم دەکاتەوە.

### ٤.٣ Delivery failure
- هەڵەی reply، next question یان final result باعثی پاککردنەوەی quiz state دەبێت.
- final result failure دوای database reward claim ڕوودەدات؛ ledgerی database ڕێگری لە rewardی دووبارە دەکاتەوە، بەڵام user دەتوانێت result message نەبینێت. ئەمە لە testدا بە mock پشکنراوە.

**کەلێنی ماوە:** هیچ پشکنینی review status لە ناو `quiz_answer`دا پێش scoring و بە تایبەتی پێش final reward دیار نییە.

## ٥. Review status helper

`lesson_is_pending_review` تەنها ئەم stringە بە یەکسانی دەناسێتەوە:
`owner_review_pending_expanded_draft`

لە startup validationدا `startswith("owner_review_pending")` بەکاردێت، بەڵام ئەو یاسایە لە helperی runtimeی completion/quizدا بەکارنەهاتووە. ئەم دوو شێوازە لە یەک policyدا هاوتا نین.

## ٦. Test coverageی ئێستا

### بەڵگەی هەبوو
لە `tests/test_bot_quiz_callbacks.py`:
- menu hides quiz when `quiz_is_available=False`.
- menu shows approved completed quiz.
- malformed answer callback.
- out-of-range answer.
- stale question callback by message ID.
- duplicate callback while answer processing.
- feedback delivery failure clears state.
- next question delivery failure clears state.
- final result delivery failure clears state after idempotent reward claim.
- valid final answer claims reward once.
- repeated click after completion does not claim reward twice.
- non-final correct answer advances once.

لە `tests/test_database.py`:
- concurrent quiz completion has one winner.
- concurrent quiz reward has one winner.
- quiz reward idempotency.

لە `tests/test_course4_grammar_runtime.py` و `tests/test_activated_courses.py`:
- Course4 has 46 lesson IDs.
- lessons 32–46 are pending review and their structured quizzes are empty.
- Course4 lesson catalog callbacks are reachable.
- quizzes 1–31 have expected schema and availability.

### Coverage gaps
- No explicit integration test: pending review + non-empty mock quiz bank → start must reject.
- No explicit test: pending review + completed lesson + non-empty quiz bank → global quiz menu must omit.
- No explicit test: quiz starts while approved, then review status changes to pending before final answer → no reward.
- No explicit test: review status is checked again on every answer or at least at finalization.
- No explicit test for unknown future `owner_review_pending_*` statuses through the same helper.
- No explicit test for stale quiz state from a previous review version/approval cycle.
- No Course4-specific start/finalization test that combines review policy, sequence, database ledger and callback flow.

## ٧. تاقیکردنەوە نوێیە پێشنیارکراوەکان

1. `test_start_quiz_rejects_pending_lesson_even_when_mock_quiz_bank_exists`
   - mock a Course4 lesson with `owner_review_pending_source_check` and a valid quiz bank.
   - verify no quiz state is created and no question is sent.

2. `test_quiz_menu_omits_pending_lesson_even_when_completed_and_quiz_available`
   - mock completion, contiguous progress and quiz availability.
   - pending status must still omit the item.

3. `test_final_quiz_answer_rechecks_review_status_before_reward`
   - start approved; change lesson status to pending before final answer.
   - reward helper must not be called; quiz state must be cleared or safely invalidated.

4. `test_unknown_pending_review_status_fails_closed`
   - ensure every `owner_review_pending_*` status is pending.

5. `test_review_status_change_invalidates_existing_quiz_state`
   - status changes during quiz; next answer callback must be rejected.

6. `test_approved_status_restoration_does_not_reuse_old_quiz_state`
   - if a lesson is re-approved, require a fresh quiz start rather than reuse stale state.

7. `test_course4_quiz_callback_sequence_and_reward_end_to_end`
   - integrate start, question answer, final answer, database ledger and review policy with isolated DB.

## ٨. بڕیاری معماریی پێشنیارکراو

- یەک helperی گشتی بۆ review policy بەکاربهێنرێت؛ startup، lesson completion، quiz menu، quiz start و finalization هەموویان هەمان helper بەکاربهێنن.
- Fail-closed policy بۆ statusی ناشناو دیاری بکرێت؛ statusی ناشناو نابێت بە پەسەندکراو دابنرێت.
- لە کاتی finalization، review status دووبارە پشکنین بکرێت.
- ئەگەر approval دەتوانێت لە هاوکاتی transactionدا بگۆڕدرێت، application-layer check تەنها raceی تەواو چارەسەر ناکات؛ approval version/ledgerی transaction-safe پێویستی بە دیزاینی جیاواز هەیە.
- هیچ migrationێک پێش بڕیاری خاوەن پڕۆژە و دیاریکردنی source of truth بۆ approval status نەکرێت.

## ٩. کردار و سنوور

- فایلەکان لە `main` خوێندرانەوە.
- هیچ pytest/unittest/CI run لەم قۆناغەدا نەکرا.
- هیچ test/code/source/DBیەک دەستکاری نەکرا.
- هیچ commitێک بۆ `main` نەکرا.
- هیچ Telegram/Botkeep deployment یان activation نەکرا.

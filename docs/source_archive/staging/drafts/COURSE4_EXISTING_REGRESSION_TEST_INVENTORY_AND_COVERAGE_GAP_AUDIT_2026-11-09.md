# کۆرسی ٤ — لیستی regression testsی ئێستا و پشکنینی کەلێنی coverage

**بەروار:** 2026-11-09  
**Base:** `main`  
**دۆخ:** پشکنینی staticی source/test files؛ تاقیکردنەوەکان لەم قۆناغەدا نەجێبەجێ کراون. هیچ فایلێکی runtime/test دەستکاری نەکراوە.

## ١. چاککردنەوەی تێبینیی ڕاپۆرتی پێشوو

ڕاپۆرتی remediation plan پێشنیاری زیادکردنی تاقیکردنەوەی Course4 کردبوو. پشکنینی وردی ئێستای `main` پیشانی دا کە بنەمای regression coverage هەیە و پێویستە لە هەر پێشنیارێکی نوێدا ئەو تاقیکردنەوانە بپارێزرێن و تەنها کەلێنە ڕاستەقینەکان زیاد بکرێن. ئەمە پێداچوونەوەی وردترە، نەک ڕەتکردنەوەی هەموو پێشنیارەکانی ڕاپۆرتی پێشوو.

## ٢. فایلە تاقیکردنەوە سەرەکییەکان

### ٢.١ `tests/test_course4_grammar_runtime.py`

بەڵگەی تاقیکردنەوەی هەیە بۆ:
- هەبوونی ٤٦ وانە و ڕیزبەندیی `grammar_01` تا `grammar_46`.
- هاوتاییی JSON، curriculum plan و `courses.json`.
- پاراستنی schema و learning componentsی وانەکانی ١–٣١.
- بەتاڵبوونی quiz و هەبوونی `source_markdown` بۆ وانەکانی ٣٢–٤٦.
- پشکنینی review statusی وانە pending.
- خوێندنەوەی وانەی pending بە ئاگاداری و بەبێ completion button.
- ڕێگریکردن لە تەواوکردن و reward بۆ `grammar_32`.
- بەردەوامبوونی completion button بۆ وانەی پەسەندکراو.
- جیاکردنەوەی terminology و هەڵسەنگاندنی زانستی لە وانەکانی پێشوو.

### ٢.٢ `tests/test_activated_courses.py`

بەڵگەی تاقیکردنەوە هەیە بۆ:
- پەڕەبەندی و گەیشتن بە هەموو ٤٦ callbackی وانە.
- نمایشکردنی هەموو وانەکان بە chunkی Telegram-safe.
- هەبوونی ٨ پرسیاری کویز بۆ وانەکانی ١–٣١.
- بەتاڵبوونی کویز و pending status بۆ وانەکانی ٣٢–٤٦.

### ٢.٣ `tests/test_bot_quiz_callbacks.py`

تاقیکردنەوەی گشتی هەیە بۆ:
- پەنهانکردنی کویزی source-review لە منووی کویز.
- stale question callback و duplicate callback.
- پاککردنەوەی state لە کاتی هەڵەی گەیاندنی پرسیار/وەڵام.
- خەڵاتدانی idempotent.
- ڕێگریکردن لە کویز پێش تەواوکردنی وانە.
- پشکنینی progression و callbackە کۆنەکان.

### ٢.٤ تاقیکردنەوەی adapter و quiz quality

- `tests/test_orthography_quiz_adapter.py`: validationی quiz schema، answer index، duplicate options و missing prompt/explanation.
- `tests/test_quiz_bank_quality.py`: جیاوازیی پرسیارەکان، answer index و ڕاستیی quiz banksی کۆرسەکانی تر.

## ٣. کەلێنە پشتڕاستکراوەکان

### P0 — قفڵی review لە کویز

لە `bot.py`:
- `lesson_is_pending_review(lesson)` تەنها یەک statusی دیاریکراو بە یەکسانی دەناسێتەوە.
- `start_quiz` پشکنینی `quiz_is_available(lesson)` دەکات، بەڵام `lesson_is_pending_review(lesson)` بە ڕاستەوخۆ پشکنین ناکات.
- `quiz_menu_items` هەمان شێوە `quiz_is_available` و completion پشکنین دەکات، بەڵام pending status بە ڕاستەوخۆ ناگرێتەوە.
- `course_quiz_review.py` لیستی `COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED` تەنها بۆ کلیلە کۆنەکانی Course1 ـە؛ یاسای گشتیی Course4 نییە.

**مەترسیی دۆخی ئێستا:** کویزی وانەکانی ٣٢–٤٦ بەتاڵە، بۆیە بە داتای ئێستا کویز دەست پێ ناکرێت. بەڵام ئەگەر کویز بۆ وانەی pending بە هەڵە زیاد بکرێت، یان تۆماری completionی کۆن هەبێت، قفڵی status لە `start_quiz` و منووی کویزدا بە تەنها بە quiz availability پشتگیری ناکرێت.

### P0 — status لە کۆتایی کویز

لە `quiz_answer`دا دوای پرسیاری کۆتایی:
- `lesson = quiz["lesson"]` و score وەردەگیرێن.
- `complete_quiz_with_rewards(update.effective_user.id, lesson)` بانگ دەکرێت.
- لەو خاڵەیەدا پشکنینی دووبارەی review statusی وانەکە لە کۆدی خوێندراودا دیار نییە.

ئەگەر statusی وانە لە ماوەی کویزدا بگۆڕدرێت بۆ pending، stateی کویز دەتوانێت هێشتا بە کۆتایی بگات و reward بانگ بکات. ئەمە کەلێنی regressionی گرنگە؛ پێویستە testی stale review status لە کۆتایی کویز زیاد بکرێت.

### P1 — status taxonomyی گشتی

- testەکان statusی ئێستا بە وردی پشکنین دەکەن؛ ئەمە بۆ baseline باشە.
- بەڵام helper تەنها stringی `owner_review_pending_expanded_draft` دەناسێتەوە.
- هیچ testێک بۆ statusی pendingی داهاتوو، وەک `owner_review_pending_source_check`، دیار نییە.
- policyی statusی نەناسراو بۆ completion/reward بە ڕوونی تاقی نەکراوەتەوە.

### P1 — Course4 quiz lifecycle tests

تاقیکردنەوەی Course4 assessment لە `tests/test_activated_courses.py` تەنها بۆ وانەکانی ١–٣١ هەبوونی question bank و standard quiz schema پشکنین دەکات. لە تاقیکردنەوەکانی callbackدا، lifecycleی کویزی Course4 بە تایبەتی بۆ pending status و stale status لە کۆتایی کویز تاقی نەکراوەتەوە.

### P2 — source_markdown precedence و preservation

تاقیکردنەوەکان contentی وانەکان و renderکردنی chunkەکان پشکنین دەکەن، بەڵام ماتریسی diffی هەموو structured fields لەگەڵ `source_markdown` بۆ ٤٦ وانە نییە. پێویستە هەر migrationێک پێش و دوای خۆی semantic-preservation test هەبێت؛ بەڵام هیچ auto-merge/auto-parseێک لە ئێستادا پێشنیار ناکرێت.

## ٤. تاقیکردنەوە نوێیە پێشنیارکراوەکان

1. `test_pending_review_status_prefix_is_fail_closed_for_rewards`: هەموو statusەکانی `owner_review_pending*` completion و reward ڕەت بکەنەوە.
2. `test_pending_course4_lesson_cannot_start_quiz_even_with_question_bank`: `grammar_32` بە quiz bankی mock پڕ بێت؛ `start_quiz` نابێت state دروست بکات.
3. `test_pending_course4_lesson_is_hidden_from_global_quiz_menu_even_if_completed`: completionی mock و quiz bankی mock هەبێت؛ منووی کویز نابێت بیخاتەڕوو.
4. `test_course4_quiz_finalization_rechecks_current_review_status`: کویز بە statusی پەسەندکراو دەست پێ بکات، پێش وەڵامی کۆتایی status بگۆڕدرێت بۆ pending؛ هیچ reward و completion نەبێت.
5. `test_stale_course4_quiz_callback_after_review_status_change_is_rejected`: callbackی کویزی پێشووتر دوای گۆڕانی status ڕەت بکرێتەوە و state پاک بکرێتەوە.
6. `test_unknown_review_status_does_not_award_rewards`: policyی fail-closed بۆ statusی نەناسراو.
7. `test_course4_source_markdown_and_structured_content_semantically_preserved`: هەموو ٤٦ وانە، بەبێ حذف و بەبێ overwriteی ناوەڕۆک.

## ٥. پێشنیاری شوێنی زیادکردنی tests

- `tests/test_course4_grammar_runtime.py`: زیادکردنی testی status-prefix و review-only behavior.
- `tests/test_bot_quiz_callbacks.py`: زیادکردنی pending quiz start، global quiz menu و stale finalization.
- `tests/test_activated_courses.py`: دڵنیایی لەوەی active course بوونی وانەی pending بە مانای approved نییە.
- `tests/test_course_review_policy.py` (فایلی نوێ): تاقیکردنەوەی pure policy/helper، ئەگەر helper بگوازرێتەوە بۆ مۆدیولی جیاواز.

## ٦. سنوور و دۆخی کردار

- ئەم audit ـە لەسەر sourceی `main` و فایلەکانی tests خوێندراوە.
- هیچ `pytest`، `unittest`، CI یان runtime execution لەم قۆناغەدا ئەنجام نەدراوە؛ ئەوەی باس کراوە تەنها هەبوونی test و static coverage ـە.
- هیچ test یان source code دەستکاری نەکراوە.
- هیچ status، quiz، lesson، completion، DB، Botkeep، Telegram، main branch یان deployment گۆڕانکاریی بەسەردا نەهاتووە.
- هەموو چاکسازییەکان پێشنیارن و پێویستیان بە تاقیکردنەوە و ڕێگەپێدانی خاوەن پرۆژە هەیە.

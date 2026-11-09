# کۆرسی ٤ — پشکنینی database، atomicity و قفڵی review بۆ completion/reward

**بەروار:** 2026-11-09  
**Source:** `main`  
**دۆخ:** static code audit؛ هیچ تاقیکردنەوەیەک لەم قۆناغەدا نەجێبەجێ کراوە. هیچ کۆدێک نەگۆڕدراوە.

## ١. پوختەی بڕیار

Database layerی ئێستا بۆ **idempotency و atomicityی reward** بنەمای بەهێزی هەیە: SQLite بە `BEGIN IMMEDIATE` کار دەکات، completion/quiz ledger پشکنین دەکات و تاقیکردنەوەی concurrency لە `tests/test_database.py` هەیە.

بەڵام database layer **هیچ زانیارییەکی review_statusی وانەکان نازانێت**. لە schemaدا تەنها user progress ـەکان وەک `completed_lessons` و `completed_quizzes` هەڵدەگیرێن. بۆیە atomicity بە تەنها ناتوانێت بزانێت کویزێک لە ڕووی policy ـەوە مۆڵەتی خەڵاتدان هەیە یان نا.

کەلێنی سەرەکی لە نێوان:
1. **Idempotency:** خەڵات دووجار نەدرێت.
2. **Authorization/policy:** خەڵات تەنها بۆ وانە/کویزی پەسەندکراو بدرێت.

یەکەم لە databaseدا بە باشی پارێزراوە؛ دووەم لە لایەنی botدا پێویستی بە قفڵی reviewی گشتی و پشکنینی دووبارەی کاتی کۆتایی هەیە.

## ٢. Schema و پاشەکەوت

فایلی `database.py`:
- `users.user_id` primary key ـە.
- `completed_lessons` و `completed_quizzes` وەک stringی comma-separated لە تۆماری userدا هەڵدەگیرێن.
- `completed_quizzes` بە migrationی `ALTER TABLE` زیاد دەکرێت، ئەگەر لە DBی کۆندا نەبێت.
- هیچ table یان fieldێک بۆ `lesson_review_status`، `quiz_approval`، `review_version` یان `reward_authorization` لە schemaی خوێندراودا نییە.

**تێبینی:** ئەمە بە مانای خراپیی schema بۆ ئەرکی ئێستای progress نییە؛ بەڵام DB بە خۆی ناتوانێت قەدەغەی خەڵاتدان بۆ draft/pending جێبەجێ بکات.

## ٣. Atomicityی completion و reward

### ٣.١ Lesson completion

`complete_lesson_with_rewards`:
- transaction بە `BEGIN IMMEDIATE` دەست پێ دەکات.
- تۆماری completed_lessons دەخوێنێتەوە.
- ئەگەر lesson_id پێشتر هەبێت، `False` دەگەڕێنێتەوە و rewardی نوێ نادات.
- ئەگەر نەبێت، completion و score/xp/coins/chests لە یەک UPDATEدا زیاد دەکات.
- commit/rollback و close هەیە.

### ٣.٢ Quiz completion

`complete_quiz_with_rewards`:
- transaction بە `BEGIN IMMEDIATE` دەست پێ دەکات.
- `completed_quizzes` دەخوێنێتەوە.
- quiz_idی دووبارە ڕەت دەکاتەوە.
- completion ledger، tests، score، xp و level لە یەک UPDATEدا دەگۆڕێت.
- commit/rollback و close هەیە.

### ٣.٣ تاقیکردنەوەی DBی ئێستا

`tests/test_database.py` هەیە بۆ:
- یەکجارەیی lesson completion و reward.
- concurrent lesson reward و یەک winner.
- concurrent lesson completion و یەک winner.
- concurrent quiz completion و یەک winner.
- یەکجارەیی quiz reward.
- concurrent quiz reward و یەک winner.
- migrationی schema و parallel first access.
- chest/badge و reward helpers.

ئەم تاقیکردنەوانە پشتگیری لە atomicity/idempotency دەکەن؛ بەڵام review policy تاقی ناکەنەوە.

## ٤. کەلێنی policy لە bot ↔ database

### ٤.١ Lesson completion

لە `bot.py`، `finish_lesson` پێش بانگکردنی `complete_lesson_with_rewards`:
- lesson_id لە courseدا هەبوونی پشکنین دەکات.
- `lesson_is_pending_review(lesson)` پشکنین دەکات.
- `can_open` پشکنین دەکات.

ئەمە قفڵێکی لایەنی bot ـە، نە قفڵێکی database. هەروەها helperی pending تەنها statusی یەکسان بە `owner_review_pending_expanded_draft` دەناسێتەوە.

### ٤.٢ Quiz start

لە `start_quiz`:
- course active، `quiz_is_available`، quiz bank، completion و sequence پشکنین دەکرێن.
- بەڵام `lesson_is_pending_review` بە ڕاستەوخۆ پشکنین ناکرێت.
- `quiz_is_available` لە `course_quiz_review.py` تەنها لیستی کۆنی Course1 ـە.

بۆیە ئەم availability helper ـە policyی گشتیی review statusی Course4 نییە.

### ٤.٣ Quiz finalization

لە `quiz_answer` دوای وەڵامی کۆتایی:
- lesson و score لە in-memory quiz state وەردەگیرێن.
- بەبێ پشکنینی نوێی review status، `complete_quiz_with_rewards(user_id, lesson)` بانگ دەکرێت.

ئەگەر statusی وانە لە ماوەی کویزدا بگۆڕدرێت بۆ pending، DB هۆکاری policy بۆ ڕەتکردنەوەی reward نییە؛ چونکە DB statusی وانە نازانێت.

## ٥. سنووری پێویستی بە atomic guard

زیادکردنی پشکنینی review status تەنها لە `bot.py` مەترسیی race conditionی تەواو لاناچێت: status دەتوانێت دوای پشکنین و پێش transactionی reward بگۆڕدرێت. بۆ قفڵی بەهێزتر دوو ڕێگا هەیە:

1. **ساده و کەم‌گۆڕانکاری:** helperی گشتیی review + پشکنینی لە quiz start، لە هەر وەڵام/کۆتایی کویز و پێش reward. ئەمە risk کەم دەکاتەوە، بەڵام transactionی DB لەگەڵ source status هاوکات ناکات.
2. **Atomic authorization:** policyی پەسەندکردن لە storageدا version/approval recordێکی جێگیر هەبێت و DB لە هەمان transactionدا approval/version بخوێنێتەوە و reward تەنها ئەگەر هێشتا approved بوو زیاد بکات. ئەمە گۆڕانکاریی معمارییە و پێویستی بە دیزاین و migration و testی تایبەت هەیە؛ ئێستا جێبەجێ نەکراوە.

بۆ ئەم قۆناغەدا، هیچ schema migrationێک پێشنیار ناکرێت تا policyی خاوەن پڕۆژە و سەرچاوەی ڕاستیی review status دیاری نەکرێت.

## ٦. Test casesی پێشنیارکراو

### Bot integration
1. pending status + quiz bankی mock → `start_quiz` نابێت quiz state دروست بکات.
2. pending status + completed lesson + quiz bank → لە quiz menuدا نابێت دەرکەوێت.
3. approved status لە start، pending status پێش final answer → quiz state پاک بکرێتەوە و reward function بانگ نەکرێت.
4. stale callbackی quiz دوای pending status → ڕەت بکرێتەوە.
5. statusی ناشناو → لە policyی fail-closedدا reward ڕەت بکرێتەوە.

### Database unit/integration
6. database reward API بە approval guard ـەوە، pending/revoked approval → هیچ ledger، score، xp یان tests زیاد نەبێت.
7. approved version لە transactionدا → تەنها یەک reward.
8. revoke/approval race لە دوو connectionدا → یەک بڕیاری transactionی دیاریکراو، نە دوو reward.
9. دووبارەکردنەوەی migrationی approval schema، ئەگەر دواتر هەڵبژێردرا → data preservation.
10. هەڵە لە transaction → rollbackی ledger و هەموو reward fields.

## ٧. بڕیاری ئێستا

- **پشتڕاستکراو:** SQLite transaction و idempotent ledger هەن؛ concurrent reward testsیش هەن.
- **پشتڕاستکراو:** DBی ئێستا review_statusی وانە ناپارێزێت و لە reward APIدا policy gate نییە.
- **مەترسیی bot:** quiz finalization لە کۆتایی status دووبارە ناپشکنێت.
- **نەکراو:** هیچ test run، code change، DB migration، deployment یان Telegram/Botkeep action.
- **پێویستی بە بڕیاری خاوەن پڕۆژە:** ئایا داهاتوودا review approval دەبێت لە DBدا بە version/ledger هەڵبگیرێت، یان قفڵی application-layer بۆ ئێستا بەسە؟

## ٨. فایلە پشکنراوەکان

- `database.py`
- `tests/test_database.py`
- `bot.py`
- `course_quiz_review.py`
- `tests/test_course4_grammar_runtime.py`
- `tests/test_activated_courses.py`
- `tests/test_bot_quiz_callbacks.py`

ئەم ڕاپۆرتە تەنها لەسەر خوێندنەوەی فایلەکانی `main` دامەزراوە؛ هیچ لابراتوار/DBی بەرهەمهێنان یان Telegram sessionێک نەکراوەتەوە.

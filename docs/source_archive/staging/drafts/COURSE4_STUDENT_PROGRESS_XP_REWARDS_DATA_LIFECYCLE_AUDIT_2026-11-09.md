# کۆرسی ٤ — پشکنینی lifecycleی داتای قوتابی، پێشکەوتن و خەڵات

**بەروار:** 2026-11-09  
**Base:** main  
**Scope:** database.py، bot.py، course_runtime.py، tests/test_database.py  
**دۆخ:** static source audit؛ هیچ داتای بەرهەمهێنان نەخوێندرایەوە و هیچ testی نوێ نەکرا.

## ١. پوختە

داتای قوتابی لە یەک rowی SQLite بە user_idی Telegram کۆدەکرێتەوە. فیلدە سەرەکییەکان:
- score و xp؛
- level؛
- correct_answers؛
- completed_lessons؛
- completed_quizzes؛
- badges؛
- tests؛
- coins و chests.

پێشکەوتنی وانە و کویز بە stringی comma-separated ID لە users rowدا هەڵدەگیرێت. completion/reward helperەکان transaction و idempotency بەکار دەهێنن. بەڵام schemaی ئێستا event history، timestamp، course/lesson version، review approval version، یان audit ledgerی وردی خەڵات نییە.

## ٢. ناسنامە و دروستکردنی user row

- users.user_id integer primary key ـە.
- get_user(user_id) بە INSERT OR IGNORE rowی نوێ دروست دەکات و SELECT * دەکات.
- get_user connectionی SQLite دەکاتەوە و لە finallyدا داخڵی دەکات.
- testی parallel first access هەیە کە rowی تاک لە accessی هاوکاتدا پشتڕاست دەکاتەوە.

**تێبینی:** هیچ profile table، Telegram username/display name، email، یان external identity mapping لە schemaی پشکنراودا نییە. ناسنامەی بنەڕەتی user_id ـە.

## ٣. پێشکەوتنی وانە

- completed_lessons لە users rowدا بە comma-separated string هەڵدەگیرێت.
- get_completed_lessons() ئەو stringە split دەکات.
- complete_lesson_with_rewards() بە BEGIN IMMEDIATE وانەی نوێ تۆمار دەکات؛ ئەگەر ID پێشتر هەبێت False دەگەڕێنێتەوە و خەڵات دووبارە نادات.
- لە یەک transactionدا score، XP، coins، chests و level نوێ دەکرێنەوە.
- bot.py پێش finish lesson review status، course active و sequenceی وانەکان پشکنین دەکات.
- course_runtime.can_open_lesson() ڕێگری لە پەڕین بەسەر وانەی پێشوو دەکات.

### سنوور
- completed_lessons timestamp، completion source، quiz score، یاخود versionی وانە لەگەڵ خۆیدا نییە.
- comma-separated ID لەسەر scaleی زۆر و queryی تحلیلی، migration و referential integrity بە قەبارەی normalized table نییە.
- لە schemaدا foreign key بۆ lesson/course registry نییە؛ validity لە application layer ـە.

## ٤. پێشکەوتنی کویز

- completed_quizzes بە comma-separated string لە users rowدا هەڵدەگیرێت.
- لە DBی کۆندا init_db() ئەم columnە زیاد دەکات.
- complete_quiz_with_rewards() بە transactionی BEGIN IMMEDIATE تەنها یەکجار quiz ID تۆمار دەکات و tests، score، XP و level نوێ دەکاتەوە.
- bot.py لە کۆتایی کویزدا ئەم helperە بانگ دەکات؛ duplicate completion خەڵاتی دووبارە نادات.

### کەلێن
- completed_quizzes لە schemaدا تەنها completion ID ـە؛ نمرە، هەوڵ، کاتی دەستپێک/کۆتایی، versionی quiz bank، review status لە کاتی attempt، یان answer history نییە.
- quiz ID لە current flowدا lesson IDی کویزە؛ ئەمە ledgerی یەک completion بۆ هەر lessonە، نە هەموو attemptەکان.
- ئەگەر لە داهاتوودا quiz bank بگۆڕدرێت، ledgerی ئێستا ناتوانێت دیاری بکات خەڵاتی قوتابی لە کام version و کام پرسیارانەوە هاتووە.

## ٥. XP، Score، Level و پاداشت

### Lesson reward
complete_lesson_with_rewards():
- default +10 points/XP؛
- +5 coins؛
- +1 chest؛
- level لە XPی نوێوە هەژمار دەکرێت؛
- هەموو updateەکان لە transactionێکدان.

### Quiz reward
complete_quiz_with_rewards():
- default +20 points/XP؛
- tests +1؛
- level نوێ دەکرێتەوە؛
- coins/chests زیاد ناکات.

### Chest و badge
- open_chest() بە BEGIN IMMEDIATE تەنها ئەگەر chests>0 بێت یەک chest کەم دەکات و coins زیاد دەکات.
- badge update بە transaction و duplicate check پارێزراوە.
- current_progress_badges() لە completed lesson IDs و course order نیشانەی پیشان دەدات؛ stored badges لە legacy ledgerدا جیاوازن.

### Test coverageی دیار
- lesson/quiz rewards one-time؛
- concurrent reward claims؛
- XP level thresholds؛
- chest inventory cannot go negative؛
- concurrent badge updates و duplicate badge prevention؛
- XP reward coin bonus زیاد ناکات.

## ٦. مەترسییەکانی data lifecycle

1. **No event ledger:** تەنها snapshotی کۆتایی هەیە؛ ناتوانرێت بە وردی بزانرێت کێ/کەی/لە کام versionدا completion و reward ڕوویداوە.
2. **No version binding:** lesson/quiz ID بە content version یان review approval revision نەبەستراوە.
3. **No attempt history:** نمرە و هەوڵەکانی کویز بۆ analytics یان dispute resolution نەپارێزراون.
4. **String list storage:** completed IDs لە comma-separated stringدا query و constraintی وردیان قورسە.
5. **Application-layer review policy:** DB helper خۆی نازانێت lesson pending review ـە یان نا؛ قفڵ لە bot.py ـە.
6. **No DB audit trail:** change historyی XP/coins/chests/badges نییە؛ لەبەر ئەوە reconciliationی خەڵات لە دواوە سنووردارە.
7. **User privacy/retention:** schema policyی retention، export، deletion یان anonymization لە codeی پشکنراودا دیار نییە؛ ئەمە پێویستی بە بڕیاری خاوەن پڕۆژە و policyی privacy هەیە.

## ٧. Test gap matrix

| Testی پێویست | مەبەست |
|---|---|
| User row round-trip all fields | دڵنیایی لە خوێندنەوە/نووسینەوەی هەموو فیلدەکان |
| Lesson completion persistence across restart | progress ون نەبێت |
| Quiz completion persistence across restart | quiz ledger بمێنێتەوە |
| Full reward invariants | score/XP/coins/chests/level لە یەک transactionدا دروست بن |
| Failure injection during reward update | هیچ rewardی نیوەچڵ نەماوێت |
| Legacy DB fixture with populated data | migration هەموو valueکانی کۆن بپارێزێت |
| Backup/restore round-trip | DBی گەڕێندراوەوە بە row counts و fields هاوتا بێت |
| Course4 namespaced ID collision test | IDی کۆرسەکان لە ledgerدا تێکەڵ نەبن |
| Review status + reward integration | pending lesson هیچ completion/rewardێک وەرنەگرێت |
| Quiz version/attempt audit | version و هەوڵەکان بە جیاوازی تۆمار بکرێن، ئەگەر داواکرا |

## ٨. ڕێکخستنی معماریی پێشنیارکراو — بێ دەستکاری

- users table وەک current balance/progress snapshot بمێنێتەوە بۆ runtimeی خێرا.
- لە قۆناغێکی جیاوازدا lesson_completions، quiz_attempts و reward_ledger بە normalized tables زیاد بکرێن؛ unique constraints بۆ (user_id, course_id, lesson_id, content_version) و idempotency key.
- reward_ledger هەر rewardێک بە reason، amount، timestamp، source version و unique claim key تۆمار بکات.
- quiz_attempts score، started_at، completed_at، quiz_version و status هەڵبگرێت؛ answer history تەنها ئەگەر پێویستی privacy/analytics ڕوون بێت.
- approval/review state بە versionی lesson content پەیوەست بکرێت، نە تەنها stringێکی mutable.
- migrationی نوێ additive بێت، backupی verified و restore drill پێش deploy؛ old columns تا کاتی migrationی دڵنیابوون لابنەبرێن.
- privacy retention/export/delete policy پێش زیادکردنی event history دیاری بکرێت.

## ٩. سنووری کار

- database.py، bot.py، course_runtime.py و tests/test_database.py لە main خوێندرایەوە.
- هیچ داتای userی بەرهەمهێنان نەخوێندرایەوە.
- هیچ DB query لە environmentی بەرهەمهێنان نەکرا.
- هیچ schema، migration، test، code، backup، server، Telegram یان Botkeep دەستکاری نەکرا.
- هیچ commitێک بۆ main نەکرا.

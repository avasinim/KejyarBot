# کۆرسی ٤ — پشکنینی backup، migration، rollback و پاراستنی داتای SQLite

**بەروار:** 2026-11-09  
**Base:** main  
**دۆخ:** static source/test audit؛ هیچ DBی بەرهەمهێنان نەخوێندرایەوە یان نەگۆڕدرا.

## ١. پوختە

- لە repositoryدا backup/restore utility، schedule، script، workflow یان runbookی DB نەدۆزرایەوە.
- bot_backup.py backup utility نییە؛ فایلێکی کۆنی Telegram bot ـە کە هەمان database.py بەکاردەهێنێت و polling دەکات.
- database.py تەنها migrationی schemaی دیاریکراوی completed_quizzes ئەنجام دەدات؛ migration framework/version table نییە.
- migration لە transactionدا دەکرێت و rollback/close لە exceptionدا هەیە.
- testی schema migration idempotency هەیە، بەڵام preservationی هەموو field/dataی userی کۆن بە شێوەی exhaustive ناپشکنێت.
- SQLite DB لە pathی ثابت لە directoryی database.py دروست دەبێت؛ persistent volume و backup خارج لە repository پێویستیان بە پشتڕاستکردنەوەی host هەیە.

## ٢. پشکنینی backup و restore

لە treeی mainدا ناوی فایلەکانی پەیوەندیدار بە backup/restore پشکنرا:
- bot_backup.py
- database.py
- tests/test_database.py

هیچ scriptێکی backup/restore، SQLite online backup API، cron/scheduler، GitHub Actions backup workflow، object-storage integration یان restore runbook نەدۆزرایەوە.

**تێبینی گرنگ:** ناوی bot_backup.py نابێت بەڵگەی backupی database وەربگیرێت. ناوەڕۆکەکە Telegram botێکی جیاوازە، LESSON_DATA لە lessons.json دەخوێنێتەوە، database.init_db() بانگ دەکات و app.run_polling() جێبەجێ دەکات. هیچ backup، dump یان restore functionی تێدا نییە.

## ٣. Schema migrationی ئێستا

لە database.py:
1. SQLite file بە DB_NAME دەکرێتەوە.
2. CREATE TABLE IF NOT EXISTS بۆ users جێبەجێ دەکرێت.
3. PRAGMA table_info(users) بۆ ناسینی columnەکان بەکاردێت.
4. ئەگەر completed_quizzes نەبێت، ALTER TABLE ADD COLUMN completed_quizzes TEXT DEFAULT '' جێبەجێ دەکرێت.
5. commit لە successدا؛ rollback لە exceptionدا؛ connection لە finallyدا داخراوە.

### خاڵە باشەکان
- Migrationی columnی نوێ dataی columnە کۆنەکان ناگۆڕێت.
- Checkی column name migration دووبارە لە init_dbدا ڕێگری لە ALTER TABLEی دووبارە دەکات.
- Exception path rollback و close دەکات.
- DBی نوێ و DBی کۆن لە یەک init functionدا پشتگیری دەکرێن.

### سنوورەکان
- migration version table نییە؛ schema evolution لە if/column checkی تاکەیی پێکهاتووە.
- migration order و dependencyی schema لە versioned migration historyدا تۆمار ناکرێت.
- backupی پێش migration لە خودی init_dbدا نییە.
- migrationی پیچیده‌تر یان rollbackی schema لە codeدا دیزاین نەکراوە.
- SQLite ALTER TABLEی ئەم columnە سادەیە؛ ئەمە نابێت بە توانای rollbackی هەموو migrationەکانی داهاتوو تێبگەین.

## ٤. Test coverageی migration

لە tests/test_database.py:
- test_existing_database_schema_is_migrated_idempotently دوو جار init_db() بانگ دەکات و userی پێشتر هەبوو دەدۆزێتەوە.
- test_init_db_rolls_back_and_closes_when_schema_setup_fails rollback و close پشکنین دەکات.
- setUp DBی کاتی دروست دەکات و tearDown پاکی دەکاتەوە.
- testەکانی completion/reward concurrency و idempotency هەن.

### کەلێنەکان
- testی schemaی legacy بە شێوەی ڕوون DBی کۆن بە هەموو columnەکانی پێش migration دروست ناکات و پاش migration هەموو valueکانی score/xp/completed_lessons/badges/coins/chests پشکنین ناکات.
- testی migration failure لە ناو ALTER TABLEی completed_quizzes بە ڕوونی دیاری نەکراوە؛ mockی ئێستا schema setup failure بە گشتی پشکنێت.
- testی backup snapshot → restore → equality نییە.
- testی corrupt/incomplete backup و rejectionی restore نییە.
- testی disk-full/permission failure و rollbackی operational نییە.
- testی version upgrade/downgrade و compatibilityی DB لەگەڵ codeی کۆن/نوێ نییە.

## ٥. پاراستنی داتا و مەترسیی rollback

- DBی SQLite لە BASE_DIR/kejyar.db ـە.
- .gitignore فایلەکانی DB و WAL/SHM لە Git دور دەخاتەوە؛ ئەمە خۆی backup نییە.
- لە filesystemی ephemeralدا restart/redeploy دەتوانێت DBی local لەدەست بدات.
- لە multi-instance deploymentدا هەر instanceێک دەتوانێت DBی جیاواز هەبێت؛ لە repoدا shared DBی ڕاستەقینە پشتڕاست نەکراوەتەوە.
- rollbackی کۆدی بۆ versionی کۆن دوای migrationی schema پێویستی بە compatibility check هەیە؛ ئەگەر کۆدی کۆن columnی زیادکراو پشتگوێ بخات، لەوانەیە کار بکات، بەڵام لەسەر schemaی گەورەتر ئەمە guarantee نییە.
- rollbackی deployment نابێت بە restoreکردنی backupی کۆن بێت، مەگەر قەبارە و ماوەی داتای لەدەستچوو بە ئاگاداری قبوڵ بکرێت.

## ٦. Runbookی پێشنیارکراو — تەنها دیزاین، نە جێبەجێکردن

### پێش migration
1. نووسینی بۆت لە کاتی backupدا بۆ ماوەی کورت بوەستێنرێت یان SQLite online backup API بە شێوەی دروست بەکاربهێنرێت.
2. backup لە pathێکی جیاواز لە live DBدا دروست بکرێت.
3. integrity_check لەسەر copyی backup جێبەجێ بکرێت.
4. checksum، timestamp، schema version و row counts تۆمار بکرێن.
5. backup بە encryption و access control بپارێزرێت؛ token/secret لەگەڵ DB package نەخرێت.
6. restore drill لە stagingدا بکرێت و user row counts و key fields بەراورد بکرێن.

### لە کاتی migration
1. snapshotی backup پشتڕاستکراو پێش migration هەبێت.
2. migration بە single process جێبەجێ بکرێت.
3. schema و data invariants پاش migration پشکنرێن.
4. testی smoke بۆ user lookup، lesson progress، quiz ledger و reward totals بکرێت.

### Rollback
1. لە failureدا polling process و نووسینی نوێ بوەستێنرێت.
2. بڕیار بدرێت rollbackی code بە schemaی گۆڕاوەوە سازگارە یان نا.
3. ئەگەر restore پێویست بوو، live DB لە شوێنی خۆی لاببرێت بە rename و backupی verified بە pathی live بگەڕێندرێتەوە؛ overwriteی بێ backup قەدەغە.
4. integrity_check و row-count reconciliation پێش restart.
5. دوای restore، تۆماری داتای نوێ لە نێوان snapshot و rollback هەڵبسەنگێنرێت؛ داتای لەدەستچوو بە خاوەن پڕۆژە ڕوون بکرێتەوە.

## ٧. پێشنیاری schema evolution

- زیادکردنی schema_migrations(version, applied_at) یان mechanismێکی یەکسان.
- migrationەکان بە ژمارە و checksum و rollback note تۆمار بکرێن.
- migrationی destructive بە دوو قۆناغ (expand → migrate → contract) و پاش backupی verified.
- testی legacy fixture و restore integration لە CI.
- backup policyی ڕۆژانە/هەفتانە، retention، encryption و restore drill لە hostی ڕاستەقینەدا دیاری بکرێت؛ cadence بە خاوەن پڕۆژە و data criticality دیاری بکرێت.

## ٨. کردار و سنوور

- main: database.py، tests/test_database.py، bot_backup.py و treeی فایلەکان خوێندرایەوە.
- هیچ DBی ڕاستەقینە، user data، production host یان backupی بەرهەمهێنان نەخوێندرایەوە.
- هیچ backup/restore/migration/rollback جێبەجێ نەکرا.
- هیچ test run، code change، workflow trigger، main commit، Botkeep/Telegram deployment یان server restart نەکرا.

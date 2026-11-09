# پشکنینی یەکپارچەیی ناسنامەی کۆرس و کلیلی پێشکەوتنی قوتابی
**بەروار:** 2026-11-09  
**قۆناغ:** پشکنینی source-only؛ بێ گۆڕانکاریی کۆد یان DB  
**کۆگا:** `avasinim/KejyarBot`  
**بنەمای پشکنین:** `main`؛ فایلە سەرەکییەکان بە fetch خوێندرانەوە.

## 1. فایل و SHAی پشکنراو
- `courses.json`: `6eb7056cfceb9626993979cf73f4c2efd00424c2`
- `course_runtime.py`: `df6f6ca77946fad185edf8e8ceadbc5db7599907`
- `database.py`: `656b5d8e8a06fb61329890fa79723438e72c6f80`
- `bot.py`: `08dd6a9e8b0b21470f5b6e094ccbf48560312339`
- `tests/test_database.py`: `9d0239f6d16ec82e1826e0a5a71f068735f84ef7`
- `tests/test_course4_grammar_runtime.py`: `7437d63769e68fc4af01c5a829be13bb5cc7111a`

## 2. دەرئەنجامی یەکپارچەیی manifest
- کۆرسی ڕێزمان `grammar` بە 46 ناسنامەی `grammar_01` تا `grammar_46` تۆمارکراوە.
- `tests/test_course4_grammar_runtime.py` بە ڕوونی یەکسانی IDی 46 وانە لە JSON، curriculum plan و `courses.json` دەپشکنێت.
- کۆرسەکانی نوێتر IDی namespaceدار بەکاردەهێنن؛ وەک `daily_conversation_01`، `unified_orthography_01` و `grammar_01`.
- `course_runtime.lesson_key()` بۆ کۆرسی legacyی `orthography_basic` کلیلە کۆنەکەی `وانە_N` دەپارێزێت؛ بۆ کۆرسەکانی تر slug + ژمارەی دووڕەقەم دروست دەکات.
- `LESSON_COURSE` لەسەر بنەمای IDی وانەکان دروست دەکرێت و runtime لە duplicate ID لە نێوان داتاکانی وانەکاندا هەڵە دەدات.

## 3. پێشکەوتنی قوتابی و پاراستنی legacy
- `users.completed_lessons` و `users.completed_quizzes` وەک stringی comma-separated هەڵدەگیرێن.
- `complete_lesson_with_rewards` و `complete_quiz_with_rewards` بە `BEGIN IMMEDIATE` و checkی IDی پێشتر تۆمارکراو، خەڵات دووبارە نادەن.
- `get_completed_lessons` هەمان کلیلەکان دەگەڕێنێتەوە؛ `can_open` بۆ کۆرسێکی دیاریکراو تەنها ئەو IDیانەی لە ڕیزی هەمان کۆرسدا پێویستن بەراورد دەکات.
- بۆیە تێکەڵبوونی پێشکەوتنی کۆرسە namespaceدارەکان لەسەر ئاستی ID کەمکراوەتەوە، بەڵام کلیلی legacyی `وانە_N` تایبەت بە کۆرسی کۆنە و نابێت بۆ کۆرسێکی نوێ بەکاربهێنرێت.
- هیچ migrationێک بۆ گۆڕینی IDی وانەکان پێویست نییە لە دۆخی ئێستادا؛ گۆڕینی IDی پێشتر بەکارهاتوو دەتوانێت پێشکەوتنی قوتابی بە IDی کۆن لەگەڵ IDی نوێ جیا بکاتەوە و وانەکە وەک تەواونەکراو پیشان بدات.

## 4. مەترسییەکان و خاڵە ناتەواوەکان
1. **گۆڕینی ID مەترسیی داتایە:** هەر گۆڕانکارییەک لە `grammar_XX` یان namespaceی کۆرسەکان دەبێت بە migrationی پارێزەری پێشکەوتن، mappingی کۆن→نوێ، و reconciliationی پێش/دوای migration بێت؛ نابێت ID بە سادەیی rename بکرێت.
2. **جیاوازی key function و IDی manifest:** `lesson_key(course_id, number)` هەمان شێوەی IDی manifest دروست دەکات بۆ کۆرسە namespaceدارەکان؛ بەڵام legacy `orthography_basic` استثنایەکی تایبەتی هەیە. هەر callerێک دەبێت کۆرسی دروست بنێرێت.
3. **CSVی comma-separated:** ئەم شێوازە لەگەڵ IDی ئێستادا کار دەکات چونکە IDکان commaیان تێدا نییە؛ بەڵام ئەگەر IDی داهاتوو commaی تێدا بێت، parsing دەشکێت. schemaی نۆرماڵکراو یان JSON array لە migrationێکی داهاتوودا چارەسەرێکی باشترە.
4. **تاقیکردنەوەی یەکپارچەیی runtime بەردەوام پێویستە:** testی Course4 manifest و database test هەن؛ بەڵام ئەم پشکنینە test suiteی نوێ نەخستە کار و هیچ DBی بەرهەمهێنان نەخوێندراوەتەوە.
5. **ناساندنی کۆرس و دۆخی چالاکی:** active بوونی `grammar` لە `courses.json` بە مانای پەسەندبوونی هەموو وانەکان نییە؛ review_statusی وانەکان دەبێت لە جێگای خۆیدا بپارێزرێت.

## 5. تاقیکردنەوەی پێشنیارکراو پێش هەر migration
- snapshotی ژمارەی قوتابی، completed lesson IDs، completed quiz IDs، XP، score، coins، chests و badges پێش migration.
- duplicate scan بۆ هەموو course IDs و lesson IDs؛ دڵنیایی لە یەکتایی IDی manifest.
- mapی IDی کۆن/نوێ و assertionی ئەوەی هیچ completed IDێک ون نەبووە.
- restoreی backup لە DBی تاقیکردنەوە و بەراوردی snapshot پێش/دوای.
- regressionی legacy `وانە_N` و namespaceی کۆرسە نوێکان.
- rollbackی migration بە شێوەیەک کە پێشکەوتن و خەڵات دووبارە نەدرێنەوە.

## 6. سنووری ئەم کارە
- تەنها sourceی GitHub لە `main` خوێندرایەوە.
- هیچ کۆدێک، manifestێک، IDێک، DBێک یان پێشکەوتنی قوتابی دەستکاری نەکرا.
- هیچ test suiteێک نەجێبەجێکرا؛ ئەم ڕاپۆرتە static audit ـە.
- هیچ deployment، Botkeep یان Telegram action ئەنجام نەدرا.

## 7. حوکمی کۆتایی
**دۆخی ئێستا:** ناسنامەی 46 وانەی کۆرسی ڕێزمان لە manifest و testدا هاوتایە؛ namespaceی ID بۆ کۆرسە نوێکان بەکاردهێنرێت و legacy key بە تایبەتی پارێزراوە.  
**گرنگترین ڕێنمایی:** IDی وانەی بەکارهاتوو مەگۆڕە، مەگەر mapping و migrationی پارێزەری پێشکەوتن و restore test لەگەڵیدا هەبێت.

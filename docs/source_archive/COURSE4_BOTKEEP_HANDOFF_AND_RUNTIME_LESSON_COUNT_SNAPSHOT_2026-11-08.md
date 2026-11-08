# کۆرسی ٤ — پاشکۆی دۆخی Runtime و ئامادەکاری بۆ پشکنینی Botkeep

**بەروار:** 2026-11-08  
**ڕیپۆزیتۆری:** `avasinim/KejyarBot`  
**Branchی پشکنین:** `feat/course4-clean-port-main-20261106`

## ١. ژمارەی وانەکان لە دوو دۆخی جیاوازدا

### Branchی پەرەپێدان و پاشکۆکان
فایلی `course_data/grammar_course4_lessons.json` لە branchی `feat/course4-clean-port-main-20261106` پشکنرا:
- SHA: `4789a3c969786acd144cea528db2c4c57d9353ac`
- ژمارەی تۆمارەکانی وانە: **٣١**
- ژمارەکان: ١ تا ٣١، بە زنجیرە.
- `curriculum_state`: `owner_supplied_lessons_1_through_25_plus_scholarly_researched_lessons_26_through_31`.

### Branchی Runtimeی پشکنراو
هەمان فایل لە branchی `reset/grammar-course4-content` پشکنرا:
- SHA: `adea714b9752db12b3f498596c595b1186d916a7`
- ژمارەی تۆمارەکانی وانە: **١**
- تەنها `grammar_01` هەیە.
- `curriculum_state`: `new_owner_supplied_curriculum`.

**ئەنجام:** لە فایلەکانی GitHubدا branchی پەرەپێدان ٣١ وانەی تۆمارکراوی هەیە، بەڵام branchی Runtimeی پشکنراو تەنها ١ وانەی تێدایە. ئەم ژمارانە نابێت تێکەڵ بکرێن؛ ٣١ وانەی branchی پەرەپێدان بە مانای ئەوە نییە کە هەموویان لە ڕۆبۆتی کاراکردا پیشان دەدرێن.

## ٢. دۆخی Botkeep

لە تۆماری پێشووی پڕۆژەدا (2026-11-07):
- `KejyarBot-Test` بە دۆخی Offline تۆمار کرابوو.
- Updateی Botkeep وەستێنرابوو.
- پڕۆداکشن بە مەبەستی پاراستنی داتاکان وەستێنرابوو تا پشتڕاستکردنەوەی backupی نوێتر.

لە ئەم پشکنینەدا هیچ بەستەری Botkeep/Browserی کارپێکردن بەردەست نەبوو؛ بۆیە دۆخی ئێستای UI و ژمارەی وانەکانی ناو خودی ڕۆبۆت لەم پاشکۆیەدا بە شێوەی live پشتڕاست نەکراوەتەوە. پێویستە لە داشبۆردی Botkeep خۆی بپشکنرێت.

## ٣. کاری پاراستن و سنووری دەسەڵات

- پاشکۆکانی پشکنینی وانەی ٣٣ و گۆڕانکاریی ناوی نموونەکان لە master index تۆمار کراون.
- ئەم پاشکۆیە تەنها snapshotی ژمارەی وانەکان و دۆخی پێشووی Botkeepە.
- هیچ sync، update، restart، start، deploy، migration، merge یان گۆڕانکاریی runtime ئەنجام نەدراوە.
- هیچ داتایەکی Botkeep نەگۆڕدراوە و هیچ ژمارەیەک لە UIی Botkeep خەمڵێنراو نییە.

## ٤. ڕێنمایی بۆ پشکنینی داهاتوو

لە داشبۆردی Botkeepدا تەنها ئەم خاڵانە بخوێندرێنەوە:
1. ناوی ڕۆبۆت: `KejyarBot-Test`.
2. دۆخی ئێستا: Online/Offline.
3. ناوی courseی ڕێزمان و ژمارەی وانەی پیشاندراو.
4. ئەو branch/نسخەیەی ڕۆبۆتەکە لێی خوێندنەوە دەکات.
5. هیچ دوگمەی Update/Sync/Restart/Deploy مەکەوە؛ ئەم پشکنینە تەنها خوێندنەوەیە.


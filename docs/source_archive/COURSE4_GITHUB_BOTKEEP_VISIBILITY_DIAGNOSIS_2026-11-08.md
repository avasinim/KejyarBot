# کۆرسی ٤ — ڕاپۆرتی دۆخی دەرکەوتن لە GitHub و ڕۆبۆت
**بەروار:** 2026-11-08  
**سنوور:** تەنها کۆرسی ٤: ڕێزمانی کەژیار  
**دۆخ:** پشکنینی ڕاستەوخۆی فایلەکانی GitHub؛ هیچ deployment یان گۆڕینی Botkeep ئەنجام نەدراوە.

## کورتەی دۆزینەوە
کێشەکە تەنها «بوونی وانەکان» نییە؛ زنجیرەی پەیوەندیی نێوان سەرچاوەی Git، مانیفێستی کۆرس، loaderی ڕۆبۆت، و سەرچاوەی بەستراوی Botkeep پێویستە یەکسان بێت.

## بەڵگەی فایل و لق
| شوێن | دۆخی کۆرسی ٤ | بەڵگە |
|---|---|---|
| `main/courses.json` | هیچ تۆمارێکی `id=grammar` نییە | فایل لە main پشکنرا؛ SHA: `0d7b51e969754e56d3158b377171627571455f66` |
| `main/bot.py` | هیچ بارکردنی `course_data/grammar_course4_lessons.json` نییە | کۆدی main پشکنرا؛ SHA: `3223a18e84616998dc8239a58acbeee4c5744b54` |
| `feat/course4-clean-port-main-20261106/courses.json` | `grammar` بە `active` و 31 وانە تۆمارکراوە | SHA: `6cf263138159bcb36e1b28b6a49bded3fbc24608` |
| `feat/course4-clean-port-main-20261106/bot.py` | loaderی فایلەکە هەیە؛ expected count = 31؛ کۆرسی چالاک لە startup پشکنین دەکرێت | SHA: `6c10d152331af03ae275c3773d3819bd1dcf6c11` |
| `feat/course4-clean-port-main-20261106/course_data/grammar_course4_lessons.json` | 31 وانە، `grammar_01` تا `grammar_31` | SHA: `4789a3c969786acd144cea528db2c4c57d9353ac` |
| `deploy/course4-safe-20261108` | هەمان کۆدی loader، manifest و 31 وانەی لقەی feature لە فایلە سەرەکییە پشکنراوەکاندا | پشکنینی فایل بە refی deploy |

## هۆکاری دەرنەکەوتن
1. **GitHub:** ئەگەر بەشی فایلەکان لە default branchی `main` دەبینرێت، Course 4 لەو لقەدا نییە؛ فایلەکان لە feature/deploy branchدان. بۆیە دەرنەکەوتنی لە main بە مانای ونبوونیان لە هەموو GitHub نییە.
2. **ڕۆبۆت:** `bot.py`ی main فایلەکەی Course 4 نالۆدێت و manifestی mainیش کۆرسەکەی تێدا نییە. کۆدی feature/deploy ئەم دوو بەستەرەی هەیە.
3. **ژمارەی وانە:** runtimeی پشکنراو 31 وانەیە. وانەکانی 32–46 لە ئێستادا لە پاشکۆ/ڕەشنووس و تۆماری پشکنین دان؛ لە runtime JSON و manifestدا نیین.
4. **Botkeep:** پێشتر تۆمارکراوە کە سەرچاوەی بەستراوی Botkeep لە `main` بووە. ئەگەر هێشتا هەمان بەستەرە، Botkeep کۆدی feature/deploy بە خۆکار ناگرێت؛ چونکە ئەو لقەیە سەرچاوەی بەستراوی نییە. دۆخی liveی Botkeep لەم پشکنینەدا دووبارە نەخوێندراوەتەوە، بۆیە ئەمە بەڵگەی دۆخی پێشووە، نەک دڵنیایی لە هەموو گۆڕانکارییەکانی دوایین.

## گرنگ: «active» لە manifest واتای دەرکەوتنی لە ڕۆبۆت نییە
بۆ دەرکەوتن، هەموو ئەمانە پێویستن:
- فایلەکانی کۆرس لە هەمان commit/branchی کارپێکراودا بن؛
- `courses.json` کۆرسی `grammar` بە active و lesson IDsی ڕاست تۆمار بکات؛
- `bot.py` loaderی فایلەکە و routeی `course_grammar` هەبێت؛
- startup validation بەبێ هەڵە تەواو بێت؛
- Botkeep بە هەمان branch/commitی تاقیکراوەوە ببەسترێتەوە؛
- دوای backup و تاقیکردنەوە، import/deploy بە ڕێکاری پارێزراو ئەنجام بدرێت.

## ڕێڕەوی پێشنیارکراوی چالاککردن
1. سەرەتا 46 وانەکە لەسەر بنەمای دەقی خاوەنەوە تەواو و پشکنراو بکەین؛ وانەکانی 32–46 هێشتا runtime-ready نین.
2. runtime schema و adapter بۆ وانەکانی نوێ بپشکنین؛ ژمارەی expected count و تاقیکردنەوەکان بە 46 نوێ بکەین، تەنها دوای پەسەندکردنی ناوەڕۆک.
3. PRێکی پاک و دیاریکراو بۆ گواستنەوەی کۆدی پشکنراو بۆ `main` ئامادە بکەین؛ نەک mergeی PRێکی تێکەڵ بە گۆڕانکاریی کۆرسەکانی تر.
4. CI و startup validation بپشکنین؛ پاشان backupی Botkeep و DB/environment بە پێی ڕێنمایی پێشوو.
5. تەنها بە ڕەزامەندیی خاوەن پڕۆژە، سەرچاوەی Botkeep بگۆڕین و import/deploy بکەین؛ Start/Restart لە کاتی importدا ناچالاک بمێنێتەوە تا پشکنینی کۆتایی.

## ئەوەی لەم پشکنینەدا نەکرا
- هیچ فایلێکی runtime یان manifest نەگۆڕدرا.
- هیچ commitێک بۆ `main` نەکرا و هیچ PRێک merge نەکرا.
- هیچ گۆڕانکارییەک لە Botkeep، DB، environment، webhook، deployment، Start/Restart نەکرا.
- دەقی سەرچاوەی وانەکان نەگۆڕدرا.

## کۆتایی
هۆکاری بەڵگەدار: Course 4 لە لقەی feature/deploy هەیە، بەڵام لە `main`دا loader و manifestی نییە. هۆکاری دووەم: وانەکانی 32–46 هێشتا بە runtime نەگەیشتوون؛ بۆیە ژمارەی وانەی چالاکی runtime هێشتا 31ە.

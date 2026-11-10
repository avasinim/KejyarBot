# کۆرسی ٤ — پشکنینی schema و گەیتی JSON بۆ وانەی ٥٠، خولی ١٠٨

**بەروار:** 2026-11-10  
**سەرچاوە:** `course_data/grammar_course4_lessons.json` لە refی `botkeep-menu-clean-2026-11-09`.  
**SHAی سەرچاوە:** `fd8dfbde7e6937841214cacac653ef10d0c6097d`.  
**پەکەیجی پێشوو:** Round 107، structured extraction candidate.  
**دۆخی ئەم پشکنینە:** schema audit؛ هیچ JSONی runtime دروست/نووسراوەتەوە نییە.

## ١. ئەنجامی پشکنینی schemaی وانەکانی ١–٣١

لە ٣١ وانەی پێشتر پشکنین‌کراودا ئەم خانانە بە شێوەی جێگیر هەن:

| خانە | جۆری داتا | بوونی خانە لە ٣١ وانە |
|---|---|---:|
| `number` | integer | 31/31 |
| `id` | string | 31/31 |
| `title` | string | 31/31 |
| `objective` | string | 31/31 |
| `key_points` | array | 31/31 |
| `examples` | array | 31/31 |
| `exercises` | array | 31/31 |
| `comprehension` | array | 31/31 |
| `quiz` | array | 31/31 |
| `appendix` | array | 31/31 |
| `activities` | array | 31/31 |
| `review_status` | string | 31/31 |

کۆی کویزی وانەکانی ١–٣١: **248**. هەر یەک لە 248 پرسیارەکە ئەم چوار خانەیەی هەیە: `q`, `options`, `answer`, `explanation`. هەموو نموونەکانی ئەم ٣١ وانەیە لە شێوەی array ـی دوو-ئەندامی (label/description pair) هاتوون؛ کۆی نموونەکان 221 ـە.

## ٢. بەراوردی وانەی ٥٠ لەگەڵ schema

وانەی ٥٠ لە source JSONدا ئەم خانانەی بنەڕەتییەی هەیە: `number`, `id`, `title`, `objective`, `key_points`, `examples`, `exercises`, `comprehension`, `quiz`, `review_status`, `source_markdown`, `source_path`, `capstone_source_path`.

بەڵام چوار arrayی فێرکارییەکەی `key_points`, `examples`, `exercises`, `comprehension`, `quiz` بەتاڵن؛ هەروەها `appendix` و `activities` کە لە هەموو وانەکانی ١–٣١ هەن، لە وانەی ٥٠دا نیین. لەبەر ئەوە Round 107 پێویستی بە زیادکردنی ئەم دوو خانەیە هەیە بۆ هاوتایی schema، یان دەبێت جیاوازییەکە بە ڕوونی لە validatorدا بەڵگەدار بکرێت. پێشنیاری ئەم پشکنینە: هەردووکیان وەک arrayی هەبوو زیاد بکرێن، بەڵام ناوەڕۆکیان لە پەکەیجی candidate و بە append-only دابنرێت.

## ٣. خاڵەکانی پێویست بە چاکسازی لە Round 107

1. **appendix و activities:** پەکەیجی Round 107 ناوەڕۆکیان بە شێوەی جیاوازی باس دەکات، بەڵام لە پێشنیاری structured field ـەکاندا خانەی تایبەتیان دانەنراوە. دەبێت پێش JSON candidate بۆ هەردووکیان خانەی array دیاری بکرێت.
2. **examples:** شێوەی وانەکانی ١–٣١ array ـی دوو-ئەندامییە. بۆ نموونەی سەرچاوەیی، دەبێت لە پێکهاتەی هەمان خانەدا label/description ـی ڕوون بۆ citation و gloss هەبێت، یان metadata لە appendixدا پارێزراو بێت؛ شێوەی نوێی object نابێت بەبێ validatorی runtime بەکاربهێنرێت.
3. **quiz:** شێوەی پەسەندکراوی وانەکانی ١–٣١ `q/options/answer/explanation` ـە. هەر ٥ پرسیاری Round 107 ئەم چوار خانەیەیان هەیە، بەڵام دەبێت `answer` بە ژمارەی index بێت، نە بە دەقی وەڵام؛ index ـەکەش دەبێت لە مەودای `options` بێت.
4. **exercises/comprehension:** لە وانەکانی ١–٣١ arrayی string بەکاردێت. پەکەیجی Round 107 دەتوانێت هەمان شێوە بپارێزێت و کلیلی وەڵامەکان لە `appendix` یان بەشێکی دیاریکراوی `key_points`دا جیا بکاتەوە؛ نابێت schemaی نوێی nested بەبێ پشکنین زیاد بکرێت.
5. **review_status:** دەبێت لە دۆخی `owner_review_pending_expanded_draft` بمێنێتەوە تا پەسەندی ئەکادیمی و native validation تەواو نەبن.
6. **سەرچاوە و سنووری داتا:** `source_markdown`, `source_path`, `capstone_source_path` خانەی metadata ـن؛ نابێت ناوەڕۆکی ڕەشنووس دووبارە لە خانە فێرکارییەکاندا بە شێوەیەک بگوازرێتەوە کە ڕەچەڵەکی سەرچاوە ون بکات.

## ٤. گەیتی کویز و پشکنینی یەکەم

پێش دروستکردنی JSON candidate، بۆ هەر پرسیارێک ئەم مەرجانە جێبەجێ بکرێن:

- `q` دەقی پرسیاری تەواو و نادیار نەبێت.
- `options` arrayی string بێت و لانیکەم دوو هەڵبژاردەی هەبێت؛ هیچ هەڵبژاردەیەک بەتاڵ نەبێت.
- `answer` integer بێت و `0 <= answer < options.length`.
- `explanation` stringی بەڵگەدار و هاوتای وەڵامی ڕاست بێت.
- هەڵبژاردەکان نابێت دوو وەڵامی ڕاستیان هەبێت یان بەهۆی پێناسەی نادیارەوە دووڕوویی دروست بکەن.
- هیچ پرسیارێک نابێت نموونەی کوردیی پشتڕاست‌نەکراو وەک بەڵگەی یاسای ڕێزمانی بەکاربهێنێت.
- Q3/Q4ی پەکەیجی Round 107 بە سنووری بەشی سۆرانیی Bahar (2023) بمێننەوە؛ نابێت بە یاسای هەموو شێوەزارەکان بڵاو بکرێنەوە.
- duplicate stem و هاوشێوەیی پرسیارەکان لەگەڵ وانەکانی ٣٢–٤٩ بپشکنرێت.

## ٥. بڕیاری پشکنین

**دۆخی Round 107: PASS WITH REQUIRED SCHEMA PATCH — NOT RUNTIME-READY.**

پەکەیجی ناوەڕۆکی وانەی ٥٠ لە ڕووی پێکهاتەی فێرکارییەوە candidate ـێکی بەسوودە؛ بەڵام پێش دروستکردنی JSON candidate دەبێت appendix/activities و شێوەی examples/exercises/comprehension بە schemaی وانەکانی ١–٣١ هاوتا بکرێن. ئەم بڕیارە تەنها پشکنینی schema ـە و مانای پەسەندکردنی زانستیی وانە یان چالاککردنی runtime نییە.

## ٦. قۆناغی داهاتوو

- دروستکردنی Round 109 وەک **schema-normalized JSON candidateی جیاواز**، نەک وەک گۆڕانکاریی source JSON.
- زیادکردنی `appendix` و `activities` بە پێی schema.
- پاراستنی source_path و metadataی سەرچاوە.
- پشکنینی JSON parse، required keys، field types، quiz answer indices، empty strings، duplicate quiz stems و hashی source.
- دووبارە fetchکردنی candidate بۆ پشتڕاستکردنەوەی commit و ناوەڕۆک.

## ٧. پاراستن

هیچ source JSON، source_markdown، runtime، loader، quiz bank، student data یان بۆت دەستکاری نەکراوە. هیچ merge، deployment، sync، restart، Botkeep یان Telegram action ئەنجام نەدراوە. ئەم پاشکۆیە تەنها تۆماری schema audit ـە.

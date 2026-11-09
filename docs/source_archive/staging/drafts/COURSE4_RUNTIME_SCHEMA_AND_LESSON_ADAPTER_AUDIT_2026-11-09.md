# کۆرسی ٤ — پشکنینی schemaی JSON، adapter و ڕێڕەوی runtime

**بەروار:** 2026-11-09  
**Branchی بنەڕەت:** `main`  
**JSON:** `course_data/grammar_course4_lessons.json` — blob `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`  
**Adapter:** `course_lesson_adapters.py` — blob `124cd04e8b1068467982db35faf9f11fdd41a1af`  
**Bot:** `bot.py` — blob `08dd6a9e8b0b21470f5b6e094ccbf48560312339`  
**Quiz review:** `course_quiz_review.py` — blob `a90890f640ed60341b8e8d2e4c8ca04e6264bf2f`  
**Runtime helpers:** `course_runtime.py` — blob `df6f6ca77946fad185edf8e8ceadbc5db7599907`  
**Manifest:** `courses.json` — blob `6eb7056cfceb9626993979cf73f4c2efd00424c2`  
**دۆخ:** پشکنینی خوێندنەوە و شیکاریی کۆد؛ هیچ کۆد یان JSON دەستکاری نەکراوە، هیچ deploymentێک ئەنجام نەدراوە.

## ١. پوختەی داتا

JSONی کۆرسی ٤:
- ٤٦ وانە، `course_id = grammar`.
- ٣٠ وانە: `scientific_review_complete_with_qualified_notes`.
- ١ وانە: `internal_cross_lesson_synthesis_no_external_source_mapping`.
- ١٥ وانەی ٣٢–٤٦: `owner_review_pending_expanded_draft`.
- ٣١ وانە خانەی `examples`یان پڕە؛ ٣١ وانە خانەی `quizیان پڕە؛ ٣٨ وانە خانەی `comprehensionیان پڕە.
- وانەکانی ٣٢–٤٦ هەموویان `source_markdown`یان هەیە؛ خانەکانی `examples` و `quiz`یان بەتاڵن. تەنها وانەکانی ٣٢–٣٨ لە `comprehension`دا پرسیاری ڕێکخراویان هەیە.

## ٢. Adapter و پێکهاتەی داتا

لە `adapt_unified_orthography_lessons`دا:
- `key_points`، `examples`، `appendix`، `activities`، `exercises` و `comprehension` بەپێی بوونی خانەکان دەخرێنە ناو `content`.
- `appendix` و `activities` تەنها کاتێک زیاد دەکرێن کە `include_extended_sections=True`.
- `quiz` لە ناو دەقی وانەدا دانانرێت؛ بە جیاوازی وەک `quizzes_by_id` دروست دەکرێت.
- هەر پرسیاری کویز دەبێت `q`ی دەقی، لیستی `options`ی جیاواز و `answer`ی ژمارەیی لە سنووری هەڵبژاردەکاندا هەبێت؛ ئەگەر نەبێت adapter لە startupدا `ValueError` دەدات.
- `examples` بە شێوەی دوو-توخمەیی list/tuple وەردەگیرێن؛ فۆڕمی دیکەی نموونە بەبێ گۆڕانکاریی adapter لە ڕووی پیشاندانەوە لەدەست دەچێت.

## ٣. پێشینەی `source_markdown` لە Bot

لە `bot.py`:
1. JSON بە adapter و `include_extended_sections=True` دەخوێندرێتەوە.
2. بۆ هەر وانەیەک کە `source_markdown` و `id`ی هاوتای هەیە، ناوەڕۆکی adapter بە `format_lesson_draft(source_markdown)` دەگۆڕدرێت.
3. ئەمە واتە لە وانەکانی ٣٢–٤٦دا ئەو دەقەی لە adapter دروست کراوە، لە کاتی نمایشدا دەکرێت جێگای بە `source_markdown` بگرێتەوە.

ئەنجام: `include_extended_sections=True` لە قۆناغی دروستکردنی ناوەڕۆکدا پاشکۆ و چالاکییەکان زیاد دەکات، بەڵام ئەگەر `source_markdown` هەبێت، ئەو زیادکراوانە لە contentی نمایشکراودا دەمێننەوە تەنها ئەگەر خۆیان لە source_markdownدا هەبن. پێویستە دڵنیایی لە هاوتاییی ئەم دوو سەرچاوەیە بکرێت؛ نابێت بە تەنها بوونی `include_extended_sections=True` بڵێین هەموو پاشکۆکان بە دڵنیایی نمایش دەدرێن.

## ٤. تاقیکردنەوە و ڕێکخستنی کویز

- `QUIZ_DATA` لە adapterەوە تەنها لە خانەی ڕێکخراوی `quiz` دروست دەبێت.
- کویزە نووسراوەکان لە Markdownی `key_points` یان `source_markdown` بە خۆکارانە ناگۆڕدرێن بۆ `QUIZ_DATA`.
- بۆیە کویزەکانی وانەکانی ٣٢–٤٦، کە خانەی `quiz`یان بەتاڵە، لە runtimeدا کویزی کرتەیی نین؛ تەنانەت ئەگەر پرسیار و کلیلی وەڵام لە دەقی نمایشکراودا هەبێت.
- لە startup validationدا کۆرسی `grammar` بۆ وانەی `owner_review_pending...` بەتاڵی کویز وەک missing quiz ڕەت ناکرێتەوە. ئەمە لەگەڵ beta-review model هاوتایە، بەڵام نابێت بە مانای ئامادەبوونی کویز بخوێندرێتەوە.

## ٥. پاراستنی دۆخی پێداچوونەوە — گرنگترین مەترسی

### ٥.١ قفڵی تەواوکردنی وانە

`lesson_is_pending_review` تەنها ئەم یەک string ـە بە یەکسانی پشکنین دەکات:
`owner_review_pending_expanded_draft`.

لە داتای ئێستادا هەموو ١٥ وانەی ٣٢–٤٦ هەمان statusیان هەیە؛ بۆیە قفڵی ئێستا بۆ ئەم داتایە کار دەکات. بەڵام هەر statusی نوێی pending، وەک `owner_review_pending_source_check`، بەبێ نوێکردنەوەی helper دەکرێت بە هەڵە وەک وانەی تەواو-ئامادە مامەڵەی لەگەڵ بکرێت. پێشنیار: یاسای گشتیی `startswith("owner_review_pending")` یان helperی یەکگرتووی status بەکاربهێنرێت، بە تاقیکردنەوەی regression؛ ئەمە تەنها پێشنیاری چاکسازییە و لەم commitدا جێبەجێ نەکراوە.

### ٥.٢ قفڵی کویز

`course_quiz_review.py` تەنها کلیلە کۆنەکانی `وانە_...`ی کۆرسی ١ لە لیستی پێداچوونەوەدا دەگرێت. کلیلە namespaced ـەکانی کۆرسی ٤، وەک `grammar_46`، لەو لیستەدا نین. لە `start_quiz`دا `quiz_is_available(lesson)` پشکنین دەکرێت، بەڵام پشکنینی ڕاستەوخۆی `lesson_is_pending_review(lesson)` لەو ڕێڕەوەدا نییە.

لە داتای ئێستادا کویزی وانەکانی ٣٢–٤٦ بەتاڵە و قفڵی تەواوکردنی وانەش پێشکەوتن ڕادەگرێت؛ بۆیە ئەم مەترسییە ئێستا بە هۆی بەتاڵی کویزەکانەوە ڕووناک نابێتەوە. بەڵام ئەگەر دواتر کویز بۆ وانەی pending زیاد بکرێت، یان تۆماری تەواوکردنی کۆن/هەڵە لە DBدا هەبێت، پشکنینی status لە دەستپێکردنی کویزدا پێویستە.

### ٥.٣ پشکنینی لە کۆتایی کویز

لە `quiz_answer`دا، دوای تەواوبوونی پرسیارەکان، `complete_quiz_with_rewards` بانگ دەکرێت. لە کۆدی خوێندراوەدا پشکنینی دووبارەی `review_status` لە خاڵی خەڵاتداندا دیار نییە. پێشنیار: پێش دەستپێکردن و پێش تۆمارکردنی خەڵات، statusی وانە دووبارە پشکنرێت؛ تاقیکردنەوەی stale quiz state و stale completion record زیاد بکرێت.

## ٦. دۆخی manifest و چالاکی

- `courses.json` کۆرسی `grammar` بە `status: active` تۆمار کردووە و ٤٦ ناسنامەی `grammar_01` تا `grammar_46` لەخۆ دەگرێت.
- ئەمە بە مانای چالاکبوونی ڕێڕەوی کۆرسە لە manifestدا؛ بەڵام وانەکانی pending لە ڕووی completion/quiz قفڵکراون.
- دۆخی کۆرس و دۆخی پەسەندکردنی وانە دوو شتی جیاوازن؛ READMEیش ئەم جیاوازییە ڕوون دەکاتەوە.
- هەر دەستکاریی manifest یان runtime پێویستی بە ڕێگەپێدانی خاوەن پرۆژە و regression test هەیە.

## ٧. پێشنیاری چاکسازییەکان بە ڕیزبەندی

1. **P0 — یەکگرتوویی قفڵی review:** helperێکی یەکگرتوو بۆ هەموو statusەکانی `owner_review_pending*` بەکاربهێنرێت لە completion، quiz launch، quiz finalization و menu.
2. **P0 — stale-state protection:** statusی وانە لە دەستپێکردنی کویز و پێش خەڵاتدان دووبارە پشکنرێت.
3. **P1 — source precedence:** یەک سەرچاوەی ڕوون بۆ content دیاری بکرێت؛ یان adapter بە source_markdown هاوتا بکرێت، یان source_markdown تەنها fallback بێت. هیچ ناوەڕۆکێک نابێت بێ بەراورد لاببرێت.
4. **P1 — structured lesson schema:** examples، exercises، comprehension و quiz لە خانە تایبەتەکاندا بپارێزرێن؛ Markdown تەنها بۆ پیشاندانی دەق بێت.
5. **P1 — quiz answer secrecy:** کلیلی وەڵام لە contentی خوێندکار جیا بکرێتەوە؛ پشکنینی render بکە بۆ ئەوەی لە پێش وەڵامدانەوە ئاشکرا نەبێت.
6. **P2 — example adapter validation:** فۆڕمی نموونە و شیکارییەکان بە schemaی دیاریکراو پشکنرێن، نە تەنها tupleی دوو-توخمەیی.
7. **P2 — regression suite:** ١٥ وانەی pending، هەموو statusە نوێکان، stale completion، stale quiz callback، source_markdown override، quiz key validation و نمایش/نهێنیی کلیلی وەڵام تاقی بکرێنەوە.

## ٨. سنووری پشکنین و کردار

ئەم ڕاپۆرتە لەسەر خوێندنەوەی فایلەکانی `main` دروست کراوە؛ هیچ تاقیکردنەوەی runtime لە سێرڤەری ڕاستەقینە، Telegram، یان DBی بەکارهێنەر ئەنجام نەدراوە. هیچ فایلێک لە `main`، `bot.py`، `course_lesson_adapters.py`، `course_quiz_review.py`، `course_runtime.py`، `courses.json` یان JSONی وانەکان دەستکاری نەکراوە. هیچ deployment، restart، Botkeep یان Telegram operation نەکراوە.

ئەم commit تەنها ئەرشیفی پشکنینە؛ بەڵگەی چاکسازی یان پەسەندکردنی خاوەن کۆرس نییە.

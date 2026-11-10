# کۆرسی ٤ — پشکنینی ڕاستەوخۆی structured data و release gate
## Round 99 — 2026-11-10

### سەرچاوە و commit
- Repository: `avasinim/KejyarBot`
- PR #125: https://github.com/avasinim/KejyarBot/pull/125
- PR headی پشتڕاستکراو لە زانیاریی PR: `6da59ef1ce991bd4452d10c744378a2327fc0bc1`
- فایلی `course_data/grammar_course4_lessons.json` لەو headەدا: blob SHA `b3e8a050d041962dd07403a79cfaac37159b88a9`

### دۆخی ڕاستەوخۆی فایلەکە
- کۆی وانەکان: ٥٠
- وانەی `scientific_review_complete_with_qualified_notes`: ٣١
- وانەی `owner_review_pending_expanded_draft`: ١٩ (٣٢–٥٠)
- کویزی integrated لە JSONی سەرەکی: ٢٤٨، هەموویان لە وانەکانی ١–٣١.
- نموونە لە وانەکانی ١–٥٠: ٢٢١
- ڕاهێنان: ٣٧٤
- comprehension items: ٣٢٥

### دۆخی structured dataی وانەکانی Beta (٣٢–٥٠)
- هەموو ١٩ وانە کویزی integratedیان نییە؛ quiz array = 0.
- هەموو ١٩ وانە examples arrayیان بەتاڵە.
- وانەکانی ٣٢–٤٦ هەندێک exercise dataیان هەیە (کۆی ٢٢١ ڕاهێنان لەم ١٥ وانەیەدا)؛ بەڵام ٤٧–٥٠ exercisesیان بەتاڵە.
- comprehension: وانەکانی ٣٢–٣٧ و ٤٦ هەندێک داتایان هەیە؛ وانەکانی ٣٨–٤٥ و ٤٧–٥٠ بەتاڵن.
- بۆیە ڕاپۆرتی پێشوو کە دەڵێت هەموو ١٩ وانە لە JSONدا examples و quiz arraysیان بەتاڵە، لەو دوو خانەیەدا ڕاستە؛ بەڵام هەموو ڕاهێنان و comprehension بەتاڵ نین. ئەم ڕاپۆرتە جیاوازییەکە ڕوون دەکاتەوە.

### تێبینییەکی گرنگ لەسەر candidateی کویز
PR #125 لە bodyی خۆیدا باس لە ٩٥ کویزی ڕێکخراوی candidate دەکات، بەڵام ئەم ژمارەیە نابێت بە کویزی integratedی runtime هەژمار بکرێت. پشکنینی فایلە سەرەکییەکە پشتڕاستی کردەوە کە کویزی integrated هێشتا ٢٤٨ دانەن و ١٩ وانەی Beta کویزیان نییە. candidate وەک draft/پاشکۆ دەمێنێتەوە تا review، validation و گواستنەوەی ڕێکخراو بە بەڵگە تەواو بکرێت.

### Release gate
- CIی سەر PR head لە bodyی PRدا ٣ workflowی سەرکەوتوو پیشان دراون: Python checks (529 tests: 518 passed, 11 skipped)، Beta safety (529 tests: 518 passed, 11 skipped)، Orthography structure (4 passed). ئەم دۆخە تەنها بۆ headی دیاریکراوی PR و کاتی تۆمارکردنی bodyی PR پشتڕاستە.
- PR #125 هێشتا unmergedە.
- تیکەتی Botkeep staging لە bodyی PRدا unresolved تۆمار کراوە؛ هەروەها ڕێنماییی ڕوون هەیە کە هیچ Resume، Cancel/restore، Replace، Sync یان server restart نەکرێت تا پشتڕاستکردنەوەی backend state و safe recovery لە support وەربگیرێت.
- deployment، import بۆ Botkeep، restart، و گۆڕینی داتای خوێندکاران نەکراون.

### دەرئەنجام و کارەکانی داهاتوو
١. کویزە candidateەکان بە کویزی runtime تێکەڵ نەکرێن؛ پێویستە candidate بە source و schema diff بپشکنرێت.
٢. examplesی ١٩ وانە بەبێ داهێنان و بە بەراورد لەگەڵ ڕەشنووسە پارێزراوەکان پڕ بکرێنەوە.
٣. exercises و comprehensionی بەتاڵی ٣٨–٤٥ و ٤٧–٥٠ بپشکنرێن؛ ئەو خانانەی ناوەڕۆکیان هەیە بە پارێزراوی بمێننەوە.
٤. کلیلی وەڵام و distractorsی هەر کویزێک پێش integration پشکنینی مانایی و سەرچاوەیی وەربگرن.
٥. هیچ وانەی Beta بۆ runtime چالاک نەکرێت تا owner review، source audit، schema validation و release gate تەواو بن.

**پاراستن:** ئەم پاشکۆیە تەنها زیادکراوە. `course_data/grammar_course4_lessons.json` و runtime دەستکاری نەکراون. هیچ merge، deployment، Botkeep staging action یان server restart ئەنجام نەدراوە.

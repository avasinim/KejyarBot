# کۆرسی ٤ — دۆخی پاشکۆی Source Mapی وانەی ١٣
## Round 33 | 2026-11-10 | Append-only

### PR #133
- PR #133: https://github.com/avasinim/KejyarBot/pull/133
- Branch: review/course4-lesson13-source-map-2026-11-10
- Base: botkeep-menu-clean-2026-11-09.
- Head: ad03c74a934984ecfe4d89fd7fe1f599f0947287.
- Draft/Open/Unmerged.
- Diff: تەنها appendix[0]ی وانەی ١٣ لە JSON و فایلێکی پاشکۆی source map؛ ٢ فایل، ٤٣ زیادە، ١ سڕینەوە لە appendix string ـی پێشوو.

### ناوەڕۆکی پاشکۆ
- Mappingی خاڵەکانی وانەی ١٣ بۆ وانەکانی ١٢ و ١٥–١٨.
- Mappingی وشەنامەی Root/Bound Root/Stem و Clitic/Affix بۆ فەرهەنگۆکی کەرەمی، لاپەڕە ٢١٧–٢١٨.
- Mappingی بنجی ئێستا/ڕابردوو بە بەراوردی سنووردار لە لاپەڕەکانی ٨٧–٩٢؛ داتای کرمانجیی ناوەندی بە یاسای سۆرانی گشتگیر ناکرێت.
- Crosswalkی سۆرانیی کۆرس و فەرهەنگۆکی کەرەمی جیا دەکرێتەوە: لە کۆرسدا ڕەگ/بنج بەکاردێت؛ لە فەرهەنگۆکی کەرەمی Root=ڕیشە، Bound Root=ڕەگ، Stem=بنکە.
- Affix=گیرەک؛ Enclitic=پاشنووس؛ Proclitic=پێشنووس؛ Clitic=لکاو.

### پشتڕاستکردنەوەی پاراستن
- JSONی کۆرس: ٥٠ وانە و ٢٤٨ کویز.
- تەنها lesson 13 لە diffsدا دەردەکەوێت و تەنها فیلدی appendix گۆڕاوە.
- هەموو ٤٩ وانەی دیکە و هەموو quiz records پارێزراون.
- review_statusی وانەی ١٣ هێشتا internal_cross_lesson_synthesis_no_external_source_mapping ـە.
- قەفڵی Beta و بێ‌خەڵاتی فەرمی بۆ وانەی ١٣ نەگۆڕدراوە.

### تێبینیی بەڵگەنامەیی
دوو فایلێکی تەنها بەڵگەنامەیی بەبێ دیاریکردنی branch لە main زیاد کران: Round30 quiz count clarification و Lesson13 source map. هیچ کۆد، JSONی وانە، runtime، DB، Botkeep یان Telegram لەو دوو commit ـەدا نەگۆڕدراوە. هەردوو ناوەڕۆکە لە branchی پەیوەندیداری PR #132 و PR #133یش کۆپی کراون بۆ پاراستن و پشکنین.

### دۆخی deployment
PR #125 هێشتا Open/Unmerged ـە و stagingی Botkeep unresolved ـە. PR #133 پەسەندی زانستیی وانەی ١٣ ناکات و deployment ڕێگەپێدراو نییە.

### دۆخی ئەم تۆمارە
ئەم فایلە append-only ـە؛ هیچ ماددەیەک نەسڕدراوەتەوە و هیچ production action ـێک ئەنجام نەدراوە.

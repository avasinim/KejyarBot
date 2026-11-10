# کۆرسی ٤ — یەکخستنی زاراوەی ٥٠ وانە
## Round 39 | 2026-11-10 | Append-only

### PR #137
- PR #137: https://github.com/avasinim/KejyarBot/pull/137
- squash-merge کرا بۆ botkeep-menu-clean-2026-11-09.
- Merge commit: 83e263805727fe0c2df88f1b9e55587acb81d050.
- CIی head: https://github.com/avasinim/KejyarBot/actions/runs/42785855671 — success.
- Python compileall passed؛ ٥٢٩ test ran، ٥١٨ passed، ١١ skipped، ٠ failure.

### زاراوە یەکخراوەکان
- Noun Phrase: گروپی ناوی → گرێی ناوی.
- Verb Phrase: گروپی کرداری → گرێی کرداری.
- Grammatical Subject: نیهاد → بکەر؛ Agent وەک ڕۆڵی واتایی جیا دەمێنێتەوە.
- Subordinate Clause: بەرڕستە → ژێرەڕستە.
- Inflection: لەچۆنایەتی → گەردان.
- Affix: ئەفیکس → گیرەک.
- Enclitic لە glossaryی وانەکانی ١١–١٢: پاشبەستە → پاشنووس؛ بەکارهێنانی گشتیی «پاشبەستە» لە پێناسەکاندا پارێزراوە.

### پشتڕاستکردنەوەی دوای merge
لە branchی botkeep-menu-clean-2026-11-09:
- ٥٠ وانە.
- ٢٤٨ پرسیاری structured.
- ٥٠ quiz override.
- ٠ answer indexی هەڵە.
- زاراوە کۆنەکان لە خانەی نا-quizی وانەکانی ئامانجدا ٠ ماون.
- titleی وانەی ٣٨ لە JSON و curriculum plan هاوتایە.
- هەموو review_status ـەکان و Beta gates وەک خۆیان ماون.
- هیچ quiz array ـێک لە PR #137دا نەگۆڕدرا.

### پاراستنی سەرچاوە
- metadataی خاو «کۆرسی: ١ — بەشی ٤» لە source_markdownدا پارێزراوە.
- ڕەشنووس و source text لە commit historyدا پارێزراون؛ گۆڕانکارییەکان تەنها زاراوەی هەمان چەمک یەکدەخەن.
- Root/Bound Root/Stem crosswalkی وانەی ١٣ بەپێی فەرهەنگۆکی کەرەمی لە PR #133 جیا کراوەتەوە؛ ڕەگ/بنجی سۆرانیی کۆرس بەبێ پێناسە ناگۆڕدرێن.

### دۆخی کۆرس و deployment
- PR #129، #132، #134 و #137 بۆ branchی کاری PR #125 یەکخراون؛ ٥٠ وانەی Beta و ٥٠ overrideی کویزی چاککراو لەو branch ـەدان.
- PR #125 هێشتا open/unmerged ـە؛ کێشەی stagingی Botkeep و پشکنینی backup/DB هێشتا release block ـن.
- PR #128 پاشکۆی پشکنینی زانستییە و open/draft/unmerged دەمێنێتەوە.
- PR #133 پاشکۆی Lesson 13 ـە و یەکخراوە؛ بەڵام review_statusی وانەی ١٣ هێشتا internal_cross_lesson_synthesis_no_external_source_mapping ـە.
- وانەکانی ٣٢–٥٠ هێشتا owner_review_pending_expanded_draft ـن و Beta-only دەمێننەوە.

### دۆخی ئەم تۆمارە
ئەم فایلە append-only ـە؛ هیچ وانە، پرسیار، سەرچاوە، DB، Botkeep یان Telegram نەسڕدراوەتەوە یان دەستکاری نەکراوە.

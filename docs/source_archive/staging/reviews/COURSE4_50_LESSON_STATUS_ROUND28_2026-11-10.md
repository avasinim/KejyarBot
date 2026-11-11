# کۆرسی ٤ — دۆخی یەکگرتووی Round 28
## 2026-11-10 | Append-only checkpoint

### ١. چالاککردنی ٥٠ وانە
- PR #129 بە هەژماری خاوەن ڕیپۆزیتۆری merge کرا بۆ `botkeep-menu-clean-2026-11-09`.
- Merge commit: `acb55ea72b20e50aa4d1b5f45bffcbc8a99c4ae4`.
- ئەم merge ـە ٥٠ وانەی Course 4 لە staging/review branchدا تۆمار دەکات؛ production deployment نییە.
- PR #125 هێشتا Open ـە بۆ `botkeep-runtime-2026-11-09`; نە merge کراوە و نە Botkeep importی بۆ کراوە.
- وانەکانی ٤٧–٥٠ لە دەقی V2ی ئارشیڤکراویان گەڕێنراونەتەوە؛ پاشکۆی Capstoneی وانەی ٥٠ پەیوەستە.

### ٢. دۆخی Beta
- وانەکانی ٣٢–٥٠ بە خوێندنەوە و Beta progression بەردەستن.
- کویز، XP، دراو، سەندوق، نیشانە و تەواوبوونی فەرمی بۆ وانەکانی ٣٢–٥٠ چالاک نەکراوە تا پشکنین و پەسەندکردنی زانستی.
- وانەی ١٣یش تا چارەسەری source mapping لە قەفڵی Beta ـدایە؛ کویز و خەڵاتی فەرمی بۆی نییە.
- لە منوودا ٥٠ وانە بە ٥ پەیج دەردەکەون و ٥٠ callback تاقیکراونەتەوە.

### ٣. کویزی وانەکانی ١–٣٠
- ٢٤٠ پرسیار تاک‌تاک پشکنران.
- ٤٤ پرسیار لە پاشکۆی runtimeدا جێگرەوەیان هەیە؛ فایلە سەرەکییەکە و ٢٤٠ پرسیاری خاو پارێزراون.
- PR #132: https://github.com/avasinim/KejyarBot/pull/132 — Draft/Open/Unmerged؛ پاشکۆی ٤٤ replacement لەگەڵ original snapshot، reason، و source-match fail-closed validation.
- PR #130 بەبێ merge داخرا و PR #132 جێگۆڕکێی بۆ کرا؛ هیچ ناوەڕۆکێکی ئەو PR ـە نەچووەتە production.
- ١٩٦ پرسیاری دیکە لە audit ـی تاک‌تاکدا هیچ خاڵێکی تایبەتیان دەرنەکەوت؛ ئەمە پەسەندی سەرچاوەییی گشتی نییە.

### ٤. تاقیکردنەوە و ڕاستکردنەوەی ژمارە
- PR #132 workflow: https://github.com/avasinim/KejyarBot/actions/runs/42783164342 — success.
- `Ran 525 tests`; `OK (skipped=11)`; واتە ٥١٤ passed و ١١ skipped.
- Python compileall: success.
- لە تۆمارە پێشووترەکاندا «٥٢٤ passed» بە هەڵە نووسراوە؛ ژمارەی ڕاستی runی پێشوو ٥٢٤ total و ١١ skipped (٥١٣ passed) بوو. پاشکۆی ڕاستکردنەوە لە `COURSE4_50_LESSON_MERGE_AND_TEST_COUNT_CORRECTION_2026-11-10.md` هەیە.

### ٥. تۆماری زاراوەیی
- `COURSE4_50_LESSON_TERMINOLOGY_REGISTER_V1_2026-11-10.md` زیاد کرا.
- زاراوەکانی NP/VP، Subject/Agent، Clause، Adverb/Adverbial، Root/Bound Root/Stem/Base، Clitic/Affix، و Compound Verb/Verbal Compound/Incorporation جیا کراونەتەوە.
- occurrence countی runtimeی ٥٠ وانە تۆمار کرا؛ هیچ mass find-and-replace ـێک نەکراوە.

### ٦. کارە ماوەکان بۆ تەواوبوونی کۆرس
1. پەسەندکردن/mergeی PR #132 بۆ جێگیرکردنی ٤٤ replacement لە staging branch؛ پاشان تاقیکردنەوەی integration.
2. پشکنینی زانستیی وانەکانی ٣٢–٥٠ و پەسەندکردنی نموونە و سنووری شێوەزار.
3. چاکسازیی زاراوە بە پاشکۆی وانە بە وانە بەپێی Register V1؛ دەقی خاو پارێزراو بمێنێتەوە.
4. پشکنینی source mappingی وانەی ١٣ و چالاککردنی کویزی فەرمی تەنها دوای پەسەندی زانستی.
5. تاقیکردنەوەی restoreی backup و وەڵامی پشتگیری لە Botkeep staging پێش هەر deployment.

### ٧. سنووری production
- Botkeep staging incident هێشتا بەڵگەی چارەسەرکردنی نییە.
- هیچ Resume/Cancel/Restore/Replace/Restart/Sync لە Botkeep نەکراوە.
- هیچ database، Telegram bot، live menu یان production deployment دەستکاری نەکراوە.
- تا چارەسەری staging و restore-test، PR #125 نابێت بۆ production بگوازرێتەوە.

### دۆخی کۆتایی Round 28
٥٠ وانە لە staging branchدا تۆمارکراون؛ ٢٤٠ کویز پشکنراون و ٤٤ replacement لە PR #132دا تاقیکراونەتەوە؛ تۆماری زاراوەیی V1 هەیە. بەڵام کۆرسی ٤ لە ڕووی پەسەندی زانستیی وانەکانی ٣٢–٥٠ و deploymentی سەلامەت هێشتا تەواو نییە.

# کۆرسی ٤ — دۆخی یەکگرتووی Round 29
## 2026-11-10 | Append-only checkpoint

### ١. دۆخی ٥٠ وانە
- PR #129 بە هەژماری خاوەن ڕیپۆزیتۆری merge کرا بۆ `botkeep-menu-clean-2026-11-09`؛ merge commit: `acb55ea72b20e50aa4d1b5f45bffcbc8a99c4ae4`.
- ئەم staging branch ـە ئێستا ٥٠ وانەی Course 4 لەخۆدەگرێت؛ وانەکانی ٤٧–٥٠ و پاشکۆی Capstoneی وانەی ٥٠یش لەگەڵیانن.
- PR #125 هێشتا Open ـە بۆ `botkeep-runtime-2026-11-09`; production merge و Botkeep import نەکراوە.
- منووی ٥ پەیجی و ٥٠ callback تاقیکراوەتەوە.
- وانەکانی ٣٢–٥٠ Beta-only ـن؛ کویز و خەڵاتی فەرمییان نییە تا پەسەندی زانستی.

### ٢. کویزی ١–٣٠ و ٤٤ override
- ٢٤٠ پرسیار تاک‌تاک پشکنران؛ ٤٤ خاڵی پێویست بە چاکسازی/سنووردارکردن تۆمار کران.
- PR #132: https://github.com/avasinim/KejyarBot/pull/132 — Draft/Open، mergeable clean.
- ٤٤ جێگرەوە لە `course_data/grammar_course4_quiz_overrides.json` دانراون؛ هەر یەک original snapshot، replacement، answer و reasonی هەیە.
- فایلە سەرەکییەکەی ٢٤٠ پرسیار نەگۆڕدراوە؛ runtime تەنها دوای پشتڕاستکردنەوەی snapshot جێگرەوەکان بەکار دەهێنێت.
- تاقیکردنەوەی PR #132 لە headی `be76e28377e418966735ca2c36d723aade93886c` سەرکەوتووە:
  - Run: https://github.com/avasinim/KejyarBot/actions/runs/42783481791
  - ٥٢٥ test ڕاکرا؛ ٥١٤ passed، ١١ skipped.
  - Python compileall success.
- PR #130 بەبێ merge داخرا و بە PR #132 جێگۆڕکێی بۆ کرا.

### ٣. تۆماری زاراوەیی و پشکنینی زانستی
- تۆماری یەکگرتووی زاراوەکان V1 و نەخشەی ٤٤ override لە PR #128 تۆمار کراون.
- occurrence countی زاراوەکان بۆ ٥٠ وانە هەژمار کرا؛ هیچ mass find-and-replace ـێک نەکراوە.
- PR #128: https://github.com/avasinim/KejyarBot/pull/128 — Draft/Open، documentation/review package.
- دەقی خاو و کویزی سەرچاوە پارێزراون؛ هەر چاکسازییەک بە پاشکۆی زیادکراو دەکرێت.

### ٤. کارە ماوەکان
1. PR #132 دوای پشکنینی review merge بکرێت بۆ staging branch؛ پاشان تاقیکردنەوەی integration لەسەر baseی نوێ.
2. پشکنینی زانستیی وانەکانی ٣٢–٥٠ بە سنووری زاری سۆرانی و پشتڕاستکردنەوەی نموونەکان.
3. جێبەجێکردنی تۆماری زاراوەیی لە ناو دەقی هەموو وانەکان بە patchی وانە بە وانە؛ دەقی پێشووی هەر وانەیەک پارێزراو بمێنێتەوە.
4. بڕیاری سەرچاوەدار بۆ وانەی ١٣ و هەر نموونەی دەرەکیی ماوە.
5. دوای پەسەندی زانستی، دروستکردنی کویزی وانەکانی ٣٢–٥٠؛ هیچ پرسیارێک نابێت بە خۆکارانە دابنرێت.
6. وەڵامی Botkeep support، پشکنینی backend staging و restore-testی backup پێش deployment.

### ٥. سنووری production
- هیچ deployment، database change، Telegram change یان Botkeep import لەم round ـەدا نەکراوە.
- کێشەی source stagingی Botkeep هێشتا unresolved ـە؛ هیچ Resume/Cancel/Restore/Replace/Restart/Sync ئەنجام نادرێت.
- PR #125 هێشتا review base ـە، نە بەڵگەی production readiness.

### دۆخی کۆتایی Round 29
٥٠ وانە لە staging branchدا هەن و ٢٤٠ پرسیاری وانەکانی ١–٣٠ پشکنراون؛ ٤٤ replacementی پاشکۆ لە PR #132دا تاقیکراونەتەوە. بەڵام کۆرسی ٤ لە ڕووی پەسەندی زانستیی ٣٢–٥٠، جێبەجێکردنی تەواوی تۆماری زاراوەیی و deploymentی سەلامەت هێشتا تەواو نییە. هیچ کاری نوێی دەرەوەی کۆرسی ٤ دەست پێ نەکراوە.

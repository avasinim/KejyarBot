# کۆرسی ٤ — دۆخی چالاکیی ٥٠ وانە و قەفڵی کویز
## Round 36 | 2026-11-10 | Append-only

### ١. دۆخی چالاکیی کۆرس
- Course catalogue: status = active.
- Lesson IDs: grammar_01 تا grammar_50؛ هەموو ٥٠ وانە لە lesson_idsدان.
- کۆی وانە لە JSON: ٥٠.
- ئەمە چالاکیی کۆرس/ڕێڕەوی خوێندنەوەی Beta ـە؛ بە مانای پەسەندکردنی زانستیی هەموو ٥٠ وانە یان چالاککردنی خەڵاتی فەرمی نییە.

### ٢. دۆخی پشکنینی وانەکان
- ٣٠ وانە: scientific_review_complete_with_qualified_notes.
- ١ وانە (١٣): internal_cross_lesson_synthesis_no_external_source_mapping؛ پێویستی بە source-mapی دەرەکی/پەسەندکراو و قەفڵی Beta هەیە.
- ١٩ وانە (٣٢–٥٠): owner_review_pending_expanded_draft؛ تەنها دەقی Beta و خوێندنەوەی پێش‌پەسەندکردن.
- وانەکانی ٣٢–٥٠ هێشتا کویزی structuredیان نییە؛ هیچ پرسیارێک بە خەمڵاندن دروست نەکراوە.

### ٣. کویز
- کۆی پرسیاری خاو: ٢٤٨ (وانەکانی ١–٣٠ = ٢٤٠؛ وانەی ٣١ = ٨).
- Overrideی پشکنراو: ٥٠ (٤٤ بۆ وانەکانی ١–٣٠ و ٦ بۆ وانەی ٣١).
- ٥٠ snapshot unique و یەکگرتوو لەگەڵ سەرچاوە؛ هیچ duplicate/snapshot mismatch/replacement schema error لە پشکنینی پێکهاتەیی نەدۆزرایەوە.
- PR #132 و PR #135 لە branchی کاری کۆرسدا merge کراون؛ source quiz records بەجێ ماون.
- PR #135 CI: success؛ ٥٢٥ test ran، ٥١٤ passed، ١١ skipped (runی پەیوەندیدار بە PR #132)؛ latest Lesson31 validation workflow success.
- هیچ کویزێک بۆ وانەکانی ٣٢–٥٠ نییە، تا پشکنینی زانستی و پەسەندی خاوەندار.

### ٤. PR ـەکان
- PR #125: Open/Unmerged؛ پەیوەندیدار بە branchی Botkeep/runtime، staging issue هێشتا unresolved.
- PR #128: Open/Draft؛ پاشکۆی پشکنینی زانستی و terminology registry.
- PR #129: merged بۆ branchی کاری؛ ٥٠ وانەی Beta/progression.
- PR #132: merged بۆ branchی کاری؛ ٤٤ overrideی کویز.
- PR #133: Open/Draft؛ source map و crosswalkی وانەی ١٣.
- PR #135: merged بۆ branchی کاری؛ ٦ overrideی وانەی ٣١.
- PR #131: closed/superseded؛ branch و پاشکۆکان پارێزراون.

### ٥. سنووری deployment
- هەموو ٥٠ وانە لە course catalogue چالاک و ناونیشان‌کراون؛ وانەکانی ٣٢–٥٠ بە شێوەی Beta/read-only review gate دەخوێندرێنەوە.
- Quiz/reward/completionی فەرمی بۆ وانەی ١٣ و ٣٢–٥٠ چالاک ناکرێت تا source reconciliation و پەسەندی زانستی تەواو بێت.
- هیچ merge بۆ main، Botkeep import، Telegram restart، DB migration یان production deploy لەم round ـەدا ئەنجام نەدراوە.
- PR #125 نابێت merge/deploy بکرێت تا Botkeep پشتڕاستیی staging و backup/DB recovery بدات.

### ٦. کارە ماوەکان بۆ کۆتایی زانستی
١. پشکنینی source-map و چاکسازیی وانەی ١٣.
٢. پشکنینی زانستی و term/source mappingی وانەکانی ٣٢–٥٠.
٣. تۆماری زاراوەیی یەکگرتووی ٥٠ وانە و چاکسازیی هەموو دووبارەبوونەوەکان.
٤. پشکنینی کۆتایی Capstoneی وانەی ٥٠ و هەموو پەیوەندییەکانی.
٥. پشکنینی runtime و regressionی Beta gates، کویز و progression.
٦. تاقیکردنەوەی restoreی backup و DB و چارەسەری Botkeep staging لەگەڵ پشتگیری.
٧. دوای ئەمانە، تەنها بە پەسەندی جیاواز، main/production deployment.

### دۆخی ئەم تۆمارە
ئەمە تۆماری append-only ـە. ٥٠ وانە لە catalogueدا active ـن، بەڵام کۆرس بە تەواوی پەسەندکراوی زانستی/production-ready نییە. هیچ وانە، کویز، سەرچاوە یان backup ناسڕدراوەتەوە.

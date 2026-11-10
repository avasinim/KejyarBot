# کۆرسی ٤ — دەرچوونی وانەی ١٣ لە Beta و دۆخی ٥٠ وانە
## Round 41 | 2026-11-10 | Append-only

### PR #138
- PR #138: https://github.com/avasinim/KejyarBot/pull/138
- squash-merge کرا بۆ botkeep-menu-clean-2026-11-09.
- Merge commit: a4186cb33184c3149f61a6ba339d15dfc566838d.
- CIی head: https://github.com/avasinim/KejyarBot/actions/runs/42786656164 — success.
- Python compileall passed؛ ٥٢٩ test ran، ٥١٨ passed، ١١ skipped، ٠ failure.

### بڕیاری وانەی ١٣
- review_status: scientific_review_complete_with_qualified_notes.
- Source mapی خاڵ بە خاڵ بۆ وانەکانی ١٢ و ١٥–١٨ زیاد کرا.
- Crosswalkی فەرهەنگۆکی کەرەمی بۆ Root/Bound Root/Stem/Affix/Clitic/Enclitic/Proclitic ڕوون کراوەتەوە.
- بەڵگەی کەرەمی تەنها بۆ crosswalk و بەراوردی کرمانجیی ناوەندی بەکاردێت؛ هیچ یاسای کرمانجی بۆ سۆرانی گشتگیر نەکراوە.
- هەشت پرسیاری کویز پشکنران و Q8 لە ٥٠ overrideی snapshot-guardedدا چاک کراوە.
- وانەی ١٣ لە Beta gate دەرچووە و کویز، progression و rewardی فەرمیی بەپێی یاساکانی گشتیی کۆرس بۆی چالاکە.

### دۆخی گشتیی کۆرس لە branchی کاری PR #125
- ٥٠ وانە.
- ٢٤٨ کویزی structured.
- ٥٠ overrideی یەکتا و snapshot-guarded.
- ٣١ وانە: scientific_review_complete_with_qualified_notes.
- ١٩ وانە: owner_review_pending_expanded_draft (Lessons 32–50) و Beta-only.
- Course catalogue status = active.

### PR ـە پەیوەندیدارەکان
- PR #129: merged — زیادکردنی ٥٠ وانەی Beta.
- PR #132: merged — ٤٤ override بۆ Lessons 1–30.
- PR #133: merged — source map و crosswalkی وانەی ١٣.
- PR #134: merged — ٦ override بۆ Lesson 31.
- PR #137: merged — یەکخستنی زاراوەی ٥٠ وانە.
- PR #138: merged — پەسەندکردنی زانستیی وانەی ١٣ و دەرچوون لە Beta.
- PR #125: open/unmerged؛ Botkeep staging unresolved.
- PR #128: closed؛ پەکەیجی پشکنینی زانستی و پاشکۆکانی branch پارێزراون.
- PR #131 و #136: closed/superseded؛ branch و پاشکۆکان پارێزراون.

### دۆخی deployment
هیچ production merge، Botkeep import، Telegram restart یان DB migration ئەنجام نەدراوە. PR #125 نابێت merge/deploy بکرێت تا staging و backup/DB safety لەلایەن پشتگیریی Botkeep پشتڕاست بکرێنەوە.

### دۆخی ئەم تۆمارە
ئەم فایلە append-only ـە؛ هیچ وانە، کویز، سەرچاوە، DB، Botkeep یان Telegram نەسڕدراوەتەوە یان دەستکاری نەکراوە.

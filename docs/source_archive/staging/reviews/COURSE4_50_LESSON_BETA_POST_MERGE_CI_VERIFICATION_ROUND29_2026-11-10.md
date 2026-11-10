# کۆرسی ٤ — پشتڕاستکردنەوەی CI دوای یەکخستنی ٥٠ وانە
## Round 29 | 2026-11-10 | Append-only

### یەکخستنی PR #129
- PR #129 بۆ branch ـی botkeep-menu-clean-2026-11-09 squash-merge کرا.
- Merge commit: acb55ea72b20e50aa4d1b5f45bffcbc8a99c4ae4.
- ئەم merge ـە تەنها branchی کاری PR #125 نوێ کردەوە؛ main، production، Botkeep و Telegram نەگۆڕدراون.

### ئەنجامی GitHub Actions لەسەر merge commit
| Workflow | Run ID | دۆخ |
|---|---:|---|
| Orthography course structure tests | 42782537847 | success |
| Python checks | 42782537865 | success |
| Course 4 beta review safety | 42782537721 | success |

### پشتڕاستکردنەوەی داتا
- JSONی کۆرسی ٤: ٥٠ وانە، grammar_01 تا grammar_50.
- Curriculum plan: lesson_count = 50.
- Course catalogue: grammar_50 هەیە.
- Structured quiz: ٢٤٨ پرسیار لە وانەکانی ١–٣١؛ وانەکانی ٣٢–٥٠ کویزی structuredیان نییە.
- ٣٠ وانە دۆخی scientific_review_complete_with_qualified_notes؛ وانەی ١٣ internal_cross_lesson_synthesis_no_external_source_mapping؛ وانەکانی ٣٢–٥٠ owner_review_pending_expanded_draft.
- Beta gate بۆ وانەی ١٣ و ٣٢–٥٠ بپارێزرێت؛ هیچ XP/coin/chest/badge/official completion بۆ ماددەی pending نییە.

### دۆخی PR
- PR #129: merged تەنها بۆ branchی PR #125.
- PR #125: هێشتا merge نەکراوە؛ release hold لەبەر کێشەی Botkeep staging.
- PR #128: پاشکۆی زانستییە، open/draft/unmerged؛ هیچ runtime codeی تێدا نییە.

### کارە ماوەکان
1. چاکسازی و دووبارە تاقیکردنەوەی ٤٤ تێبینیی کویزی وانەکانی ١–٣٠ و ٨ پرسیاری وانەی ٣١ بە پاشکۆی ڕوون.
2. تەواوکردنی source mappingی وانەی ١٣.
3. پشکنینی زانستیی وانەکانی ٣٢–٥٠ و پشتڕاستکردنەوەی نموونەکان.
4. یەکخستنی تۆماری زاراوەیی بۆ ٥٠ وانە.
5. چارەسەری staging بە پشتگیری Botkeep و پشکنینی backup/DB؛ پاشان بڕیاری جیاواز بۆ PR #125 و deployment.

### دۆخی جێبەجێکردن
ئەم پاشکۆیە تەنها تۆماری پشتڕاستکردنەوەیە؛ هیچ فایلێکی Botkeep، Telegram، production runtime یان database دەستکاری نەکراوە. هیچ ماددەیەک نەسڕدراوەتەوە.

# کۆرسی ٤ — دۆخی چاکسازیی ٤٤ پرسیاری کویز
## Round 31 | 2026-11-10 | Append-only

### ١. ڕێگای پەسەندکراوی پاشکۆ
- PR #132 ڕێگای سەرەکیی چاکسازیی کویزە: ٤٤ overrideی snapshot-guarded بۆ وانەکانی ١–٣٠.
- فایل: course_data/grammar_course4_quiz_overrides.json.
- هەر override ـێک original_snapshot، replacement، answer index، explanation و reason لەخۆ دەگرێت.
- bot.py تەنها کاتێک override جێبەجێ دەکات کە snapshotی سەرچاوە بە تەواوی یەکسان بێت؛ source drift، duplicate، optionی هەڵە یان answer indexی هەڵە fail-closed دەبن.
- فایلە خاوەی course_data/grammar_course4_lessons.json دەستکاری نەکراوە لە PR #132دا؛ پرسیارە خاوەکان لە snapshot ـەکاندا پارێزراون.

### ٢. ژمارەی ڕاستی کویز
- وانەکانی ١–٣٠: ٢٤٠ پرسیار؛ ٤٤ override (١٩٦ پرسیاری خاو + ٤٤ جێگرەوە لە لایەنی runtime).
- وانەی ٣١: ٨ پرسیاری خاو، بەبێ override.
- کۆی وانەکانی ١–٣١: ٢٤٨ پرسیاری structured.
- وانەکانی ٣٢–٥٠: کویزی structured نییە؛ Beta-only.
- تاقیکردنەوەی runtime ئێستا هەردوو ژمارەی ٢٤٠ و ٢٤٨ بە جیا پشکنین دەکات.

### ٣. پشتڕاستکردنەوەی پێکهاتەیی لە headی PR #132
- وانە: ٥٠.
- کویزی structured: ٢٤٨.
- Override: ٤٤.
- Overrideی دووبارە: ٠.
- Snapshot mismatch: ٠.
- Replacementی هەڵە (هەڵبژاردەی چوارگۆشە، answer index، explanation): ٠.
- Snapshot guard لە bot.py هەیە.
- PR #132 head: 61df5eede9c3318d5417fd088588850285184e05.
- ئەم ئەنجامە پشکنینی داتای branch ـە؛ جێگرەوەی CI نییە.

### ٤. CI
- Runی پێشووی PR #132: https://github.com/avasinim/KejyarBot/actions/runs/42783164342 — success.
- Runی پێشووتر: ٥٢٥ test ran؛ ٥١٤ جێبەجێکراو سەرکەوتوون، ١١ skipped؛ compileall success.
- دوای زیادکردنی assertionی ٢٤٨، head نوێ بووە؛ latest push-workflow result لە ئامرازەکانی پشکنینەوەدا پشتڕاست نەکراوەتەوە. بۆیە PR #132 Draft دەمێنێتەوە تا CIی headی نوێ پشتڕاست بکرێتەوە.

### ٥. PR ـە پەیوەندیدارەکان
- PR #129: merged بۆ branchی کاری PR #125، نە main و نە production.
- PR #125: open/unmerged؛ stagingی Botkeep هێشتا unresolved.
- PR #128: پاشکۆی زانستی، open/draft/unmerged.
- PR #131: داخراو وەک superseded؛ branch و پاشکۆکانی پێشوو پارێزراون.
- PR #132: open/draft/unmerged؛ تەنها overrideی کویز و تاقیکردنەوەی پەیوەندیدار.

### ٦. تێبینییەکی پاشکەوتی ڕێکخستنی فایل
یەک فایلێکی تەنها بەڵگەنامەییی Round 30 بەبێ دیاریکردنی branch لە main زیاد کرا. ئەو فایلە تەنها ڕوونکردنەوەی ژمارەی ٢٤٠/٢٤٨ە؛ هیچ کۆد، JSONی وانە، runtime، DB، Botkeep یان Telegram ناگۆڕێت. هەمان ناوەڕۆک لە branchی PR #132یش زیاد کراوە. هیچ فایلێک لە main نەسڕدراوەتەوە.

### ٧. دۆخی deployment
- ٥٠ وانە لە branchی کاری PR #125دا Beta-readableن.
- هیچ production merge، Botkeep import، Telegram restart یان DB migration ئەنجام نەدراوە.
- stagingی Botkeep و restore-testی backup/DB هێشتا unresolved ـن؛ PR #125 نابێت merge/deploy بکرێت تا پشتگیری و سەلامەتی پشتڕاست بکرێنەوە.

### دۆخی ئەم تۆمارە
ئەم فایلە پاشکۆیەکی زیادکراوە؛ هیچ پرسیار، وانە، سەرچاوە یان داتای خاو ناسڕدراوەتەوە.

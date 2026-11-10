# کۆرسی ٤ — خاڵی پاشەکەوتی یەکخستنی ٥٠ وانەی Beta
## Round 28 | 2026-11-10 | Append-only

### ١. بڕیاری بەکارهێنەر
ئامانجی کۆرسی ٤، ٥٠ وانەیە. سنووری ٤٦ وانەی runtimeی پێشوو کۆتاییی کۆرس نییە. داواکاریی بەکارهێنەر: هەموو ٥٠ وانە چالاک بکرێن، هەر کارێک دەکرێت پاشکۆ بکرێت و هیچ ماددەیەک ون نەبێت.

### ٢. ئەنجامی یەکخستنی Beta
- PR #129 بە شێوەی squash merge سەرکەوتوو بوو: https://github.com/avasinim/KejyarBot/pull/129
- Merge commit: acb55ea72b20e50aa4d1b5f45bffcbc8a99c4ae4
- PR #129 لەسەر base ـی botkeep-menu-clean-2026-11-09 بوو؛ ئەم base ـە branch ـی کار/پشکنینی PR #125 ـە، نە main و نە production.
- بەراوردی branchی PR #129 بە base ـەکە پێش merge: ٢٥ commit پێشەوە، ٠ commit دواوە؛ file diff ـەکە تەنها گۆڕانکارییە پەیوەندیدارەکانی Course 4ی لەخۆ گرتبوو.
- PR #129 پێش merge ready-for-review بوو و CIی کۆتایی سەرکەوتوو بوو: ٥٢٤ passed، ١١ skipped؛ Python compileall success.
- PR #129 لە baseی کاری PR #125 یەکخرا؛ بە مانای mergeکردنی PR #125، mergeکردنی main، deployment، یان چالاکبوونی production نییە.

### ٣. پشتڕاستکردنەوەی فایلەکان دوای merge
لە branch ـی botkeep-menu-clean-2026-11-09:
- course_data/grammar_course4_lessons.json: ٥٠ وانە؛ ID ـەکان grammar_01 تا grammar_50.
- curriculum/grammar_course4_plan.json: lesson_count = 50.
- courses.json: ناسنامەی grammar_50 لە تۆماری کۆرسدا هەیە.
- دۆخی ٥٠ وانە: ٣٠ scientific_review_complete_with_qualified_notes؛ ١ internal_cross_lesson_synthesis_no_external_source_mapping؛ ١٩ owner_review_pending_expanded_draft (وانەکانی ٣٢–٥٠).
- کۆی کویزی structured: ٢٤٨ پرسیار (وانەکانی ١–٣١، هەر وانە ٨ پرسیار).
- وانەکانی ٣٢–٥٠ کویزی structuredیان نییە؛ Beta-only/readable progression، بێ XP، coin، chest، badge، quiz و official completion.
- وانەی ١٣ هێشتا لە قەفڵی Beta ـدایە تا source mapping تەواو بێت.

### ٤. PR و دۆخی deployment
- PR #129: merged تەنها بۆ branch ـی botkeep-menu-clean-2026-11-09.
- PR #125: هێشتا PR ـی جیاوازە بۆ botkeep-runtime-2026-11-09؛ stagingی Botkeep unresolved ـە.
- PR #128: پاشکۆی پشکنینی زانستییە؛ open/draft/unmerged و هیچ runtime codeی تێدا ناگۆڕدرێت.
- هیچ فایلێکی Botkeep، Telegram، production runtime یان database دەستکاری نەکراوە.
- هیچ Resume/Cancel/Restore/Replace/Restart/Sync لە Botkeep ئەنجام نەدراوە.

### ٥. دۆخی زانستیی کۆرس
چالاککردنی Betaی ٥٠ وانە بە مانای تەواوبوونی زانستی نییە. کارە ماوەکان:
1. چاکسازی و دووبارە تاقیکردنەوەی ٤٤ تێبینیی audit ـی کویزی وانەکانی ١–٣٠، بەبێ گۆڕینی دەقی خاو و بە پاشکۆی ڕوون.
2. تەواوکردنی auditی ٢٤٨ پرسیار؛ پشکنینی ١–٣١ بە وردی، بە تایبەتی کلیلی دوودڵ و نموونەی ناپشتڕاستکراو.
3. یەکخستنی تۆماری زاراوەیی ٥٠ وانە؛ جیاکردنەوەی Root/Bound Root/Stem/Base، NP/VP، Subject/Agent، Clause types، Clitic/Affix، Compound Verb/Verbal Compound/Incorporation.
4. تەواوکردنی source mappingی وانەی ١٣.
5. پشکنینی زانستی و پشتڕاستکردنەوەی نموونەکانی وانەکانی ٣٢–٥٠ لە زاری ئامانج.
6. پاش تەواوبوونی ناوەڕۆک، regression و integration tests بۆ هەموو ٥٠ وانە و smoke test لە ژینگەی جیاواز.
7. چاوەڕوانی وەڵامی Botkeep support و پشکنینی سەلامەتیی staging و backup/DB؛ پاشان بڕیاری جیاواز بۆ PR #125 و deployment.

### ٦. پاراستن
- هەموو دەقی خاو، V2 drafts، capstone و quiz banks پارێزراون.
- هیچ پرسیار یان وانەیەک نەسڕدراوەتەوە.
- PR #129 تەنها Beta-readable progressionی ٥٠ وانەی لە branch ـی کاردا یەکخست؛ خەڵات و تەواوبوونی فەرمی بۆ ماددەی pending قەفڵ کراون.
- ئەم فایلە پاشکۆی زیادکراوە و هیچ runtime/DB/Botkeep/Telegram دەستکاری ناکات.

### دۆخی ئەم تۆمارە
٥٠ وانە لە branch ـی کاری PR #125دا لە ڕووی Beta structure و progression یەکخراون؛ production activation هێشتا نەکراوە. کۆرسی ٤ لە ڕووی زانستی هێشتا تەواو نییە.

# کۆرسی ٤ — پاشکۆی دۆخی merge و ڕاستکردنەوەی ژمارەی تاقیکردنەوە
## 2026-11-10 | Append-only correction

### ١. دۆخی PR ـەکان
- PR #129: https://github.com/avasinim/KejyarBot/pull/129
  - بە هەژماری GitHubی خاوەن ڕیپۆزیتۆری `avasinim` لە 2026-11-10T08:25:28Z merge کرا.
  - Base: `botkeep-menu-clean-2026-11-09`.
  - Merge commit: `acb55ea72b20e50aa4d1b5f45bffcbc8a99c4ae4`.
  - ئەمە تەنها گۆڕینی staging/review branch ـە؛ production deployment، Botkeep import یان Telegram restart نییە.
- PR #125 هێشتا Open ـە بۆ `botkeep-runtime-2026-11-09`; نە merge کراوە و نە deploymentی بۆ ئەنجام دراوە.
- PR #130 بەهۆی divergenceی branch دوای mergeی PR #129، بەبێ merge داخرا و بە PR #132 جێگۆڕکێی بۆ کرا.
- PR #132: https://github.com/avasinim/KejyarBot/pull/132 — Draft/Open/Unmerged؛ تەنها patchی ٤٤ پرسیاری کویز و تاقیکردنەوەکانی پەیوەندیدارە.

### ٢. پاشکۆی چاکسازیی ٤٤ پرسیار
- فایل: `course_data/grammar_course4_quiz_overrides.json`.
- ٤٤ override لەگەڵ original snapshotی تەواو، replacement، answer index، explanation و reason هەیە.
- `course_data/grammar_course4_lessons.json` و ٢٤٠ پرسیاری خاو ناسڕدراون و نەنووسراونەوە.
- `bot.py` تەنها ئەگەر original snapshot لەگەڵ دەقی خاو یەکسان بێت override جێبەجێ دەکات؛ source drift، duplicate، هەڵەی option یان answer index fail-closed دەبێت.
- ٢٤٠ پرسیار لە runtimeدا دەمێننەوە: ١٩٦ی پێشوو + ٤٤ replacement.

### ٣. ڕاستکردنەوەی ژمارەی تاقیکردنەوەکان
لە checkpoint ـە پێشووترەکاندا وشەی «٥٢٤ تاقیکردنەوە سەرکەوتوون» بەکار هاتووە. ئەو دەربڕینە ورد نەبوو؛ ژمارەی `Ran N tests` کۆی هەموو تاقیکردنەوەکانە و skipped ـەکانیش لەخۆدەگرێت.
- Runی PR #129: `Ran 524 tests` و `OK (skipped=11)`؛ واتە ٥١٣ تاقیکردنەوە جێبەجێکراو سەرکەوتوون و ١١ skipped بوون.
- Runی PR #132: https://github.com/avasinim/KejyarBot/actions/runs/42783164342
  - `Ran 525 tests`
  - `OK (skipped=11)`
  - واتە ٥١٤ تاقیکردنەوە جێبەجێکراو سەرکەوتوون و ١١ skipped بوون.
  - Python compileall: success.
- هیچ failure ـێک لە runی PR #132دا نییە.

### ٤. سنووری deployment
- ٥٠ وانە لە staging branchی `botkeep-menu-clean-2026-11-09` دانراون؛ لە productionدا هێشتا چالاک نەکراون.
- وانەکانی ٣٢–٥٠ وەک Beta-only دەمێننەوە؛ کویز و خەڵاتی فەرمییان تا پەسەندی زانستی نییە.
- کێشەی Botkeep source staging هێشتا بەڵگەی چارەسەرکردنی نییە؛ هیچ Resume/Cancel/Restore/Replace/Restart/Sync ئەنجام نەدراوە.
- Backupی پێشووی Botkeep restore-test نەکراوە؛ بۆیە production import/restore هێشتا قەدەغەیە.

### دۆخی ئەم پاشکۆیە
ئەم فایلە ڕاستکردنەوەی تۆماری دۆخ و ژمارەی تاقیکردنەوەیە؛ هیچ وانە یان پرسیاری خاو ناسڕێتەوە و هیچ production action ـێک ئەنجام نادات.

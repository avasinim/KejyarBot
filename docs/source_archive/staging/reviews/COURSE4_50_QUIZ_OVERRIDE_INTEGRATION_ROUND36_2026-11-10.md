# کۆرسی ٤ — یەکخستنی ٥٠ overrideی کویز بۆ وانەکانی ١–٣١
## Round 36 | 2026-11-10 | Append-only

### PR #134
- PR #134: https://github.com/avasinim/KejyarBot/pull/134
- Latest CI: https://github.com/avasinim/KejyarBot/actions/runs/42784427793 — success.
- Python compileall: success.
- Full suite: 525 tests ran؛ 514 جێبەجێکراو سەرکەوتوون و 11 skipped؛ هیچ failure نییە.
- PR #134 squash-merge کرا بۆ botkeep-menu-clean-2026-11-09.
- Merge commit: f4441fd346ce32644392e8a5b05fa6a4babfea4d.
- ئەمە تەنها branchی کاری PR #125 نوێ دەکاتەوە؛ main و production ناگۆڕێت.

### ژمارەی چاکسازی
- Lessons 1–30: ٤٤ override.
- Lesson 31: ٦ override.
- کۆی override: ٥٠؛ هەموویان unique و snapshot-guarded ـن.
- Structured quiz source bank: ٢٤٨ پرسیار؛ ٢٤٠ لە Lessons 1–30 و ٨ لە Lesson 31.
- Lessons 32–50: هیچ structured quiz ـێکیان نییە.

### پشتڕاستکردنەوەی دوای merge
لە branchی botkeep-menu-clean-2026-11-09:
- ٥٠ وانە و Course catalogue status=active.
- ٢٤٨ پرسیاری structured.
- ٥٠ override؛ ٥٠ keyی جیاواز؛ ٠ duplicate.
- ٠ snapshot mismatch.
- ٠ replacementی هەڵە لە ڕووی چوار هەڵبژاردە، answer index و explanation.
- Snapshot guard لە bot.py هەیە.
- Test assertions بۆ ٢٤٠ پرسیاری Lessons 1–30 و ٢٤٨ پرسیاری Lessons 1–31 هەیە.

### پاراستنی ماددەی خاو
- هەموو ٢٤٨ پرسیاری خاو لە course_data/grammar_course4_lessons.json پارێزراون؛ هیچ پرسیارێک لە JSONی سەرچاوەدا overwrite نەکراوە.
- ٥٠ replacement لە course_data/grammar_course4_quiz_overrides.json دانراون و تەنها ئەگەر original snapshot یەکسان بێت جێبەجێ دەبن.
- ٦ پرسیاری Lesson 31 ئاماژەی Kareem (2016) و Salavati & Ahmadi (2018) لە answer keyدا لادەبەن؛ ئەو سەرچاوانە لە سنووری source-approvedی کۆرسدا نەبوون.
- هیچ کویزێک بۆ Lessons 32–50 بە خەمڵاندن زیاد نەکراوە.

### دۆخی PR
- PR #129: merged بۆ branchی کاری PR #125؛ ٥٠ وانەی Beta.
- PR #132: merged؛ ٤٤ override بۆ Lessons 1–30.
- PR #134: merged؛ ٦ override بۆ Lesson 31.
- PR #125: open/unmerged؛ Botkeep staging unresolved.
- PR #128: open/draft/unmerged؛ پاشکۆی پشکنینی زانستی.
- PR #133: open/draft/unmerged؛ source map و crosswalkی Lesson 13.
- PR #131: closed/superseded؛ branch و پاشکۆکانی پارێزراون.

### دۆخی deployment
هیچ production merge، Botkeep import، Telegram restart یان DB migration ئەنجام نەدراوە. PR #125 نابێت merge/deploy بکرێت تا staging و backup/DB safety لەلایەن پشتگیریی Botkeep پشتڕاست بکرێنەوە.

### دۆخی ئەم تۆمارە
ئەم فایلە append-only ـە؛ هیچ ماددەیەک نەسڕدراوەتەوە و هیچ production action ـێک ئەنجام نەدراوە.

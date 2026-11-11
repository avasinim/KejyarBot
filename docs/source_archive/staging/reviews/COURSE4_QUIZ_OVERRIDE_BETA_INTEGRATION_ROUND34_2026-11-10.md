# کۆرسی ٤ — یەکخستنی ٤٤ چاکسازیی کویز لە برانچی Beta
## Round 34 | 2026-11-10 | Append-only

### PR #132
- PR #132: https://github.com/avasinim/KejyarBot/pull/132
- Draft بۆ پشکنین ئامادە کرا و CIی کۆتایی سەرکەوتوو بوو.
- Latest PR-head run: https://github.com/avasinim/KejyarBot/actions/runs/42783648382 — success.
- Head: 61df5eede9c3318d5417fd088588850285184e05.
- Python compileall: success.
- Full suite: 525 tests ran؛ 514 جێبەجێکراو سەرکەوتوون و 11 skipped؛ هیچ failure نییە.
- PR #132 بە شێوەی squash merge سەرکەوتوو بوو: 4c8dd79e2b3d9a25e6db6954430afb7b6c6e91c3.
- Base: botkeep-menu-clean-2026-11-09؛ ئەمە branchی کاری PR #125 ـە، نە main و نە production.

### پشتڕاستکردنەوەی دوای merge
لە branchی botkeep-menu-clean-2026-11-09:
- Course4 lesson JSON: ٥٠ وانە.
- Structured quiz: ٢٤٨ پرسیار (وانەکانی ١–٣٠ = ٢٤٠؛ وانەی ٣١ = ٨).
- Override file: ٤٤ دانە؛ هەر ٤٤ snapshot یەکگرتوون و unique ـن.
- Snapshot guard لە bot.py هەیە.
- Regression assertion بۆ ٢٤٠ و ٢٤٨ هەردووکیان هەیە.
- Course catalogue status = active؛ ٥٠ lesson ID لەخۆ دەگرێت.
- وانەکانی ٣٢–٥٠ کویزی structuredیان نییە و Beta-only دەمێننەوە؛ وانەی ١٣یش تا پشکنینی سەرچاوەیی قەفڵی Betaی هەیە.

### پاراستنی سەرچاوە
- ٢٤٠ پرسیاری خاو لە Lessons 1–30 لە JSONی سەرچاوەدا نەگۆڕدراون؛ ٤٤ جێگرەوە بە snapshot-guarded override لە لایەنی runtime جێبەجێ دەکرێن.
- ٨ پرسیاری Lesson 31 لە override bankدا نیین و بەجێ ماون.
- هیچ پرسیارێک نەسڕدراوەتەوە؛ هیچ کویزێک بۆ Lessons 32–50 بە خەمڵاندن زیاد نەکراوە.

### دۆخی PR ـەکان
- PR #129: merged بۆ branchی کاری PR #125؛ ٥٠ وانەی Beta.
- PR #132: merged بۆ هەمان branch؛ ٤٤ overrideی کویز.
- PR #125: open/unmerged؛ stagingی Botkeep unresolved.
- PR #128: open/draft/unmerged؛ پاشکۆی پشکنینی زانستی.
- PR #133: open/draft/unmerged؛ source map و crosswalkی Lesson 13.
- PR #131: closed/superseded؛ branch و پاشکۆکانی پارێزراون.

### دۆخی deployment
هیچ production merge، Botkeep import، Telegram restart یان DB migration ئەنجام نەدراوە. PR #125 نابێت merge/deploy بکرێت تا staging و backup/DB safety لەلایەن پشتگیریی Botkeep پشتڕاست بکرێتەوە.

### دۆخی ئەم تۆمارە
ئەم فایلە append-only ـە؛ هیچ ماددەیەک نەسڕدراوەتەوە و هیچ production action ـێک ئەنجام نەدراوە.

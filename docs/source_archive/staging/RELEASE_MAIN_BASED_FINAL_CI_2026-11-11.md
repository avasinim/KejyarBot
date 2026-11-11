# بەڵگەی کۆتاییی CI بۆ لقەی یەکخراو — 2026-11-11

ئەم تۆمارە بەشێکی append-only ـی ئەرشیفی وەشانی ئامادەکارییە.

## کۆمیت و PR
- Branch: `release/main-based-reconciled-2026-11-11`
- PR: https://github.com/avasinim/KejyarBot/pull/152
- Head commit: `4516c3afb608dd1269db159443761c624c5c94f2`
- PR state: Open، Ready for review، mergeable؛ merged=false.
- بەراورد بە `main`: ahead 103، behind 0؛ دۆخی ahead و هیچ divergence ـێک نییە.
- PR: 39 فایل گۆڕدراو، 4,414 زیادکراو، 343 لابراو.
- لە diffی PRدا هیچ فایلێکی PDF گۆڕدراو یان لابراو نییە.

## ئەنجامی CI لەسەر head commitی سەرەوە

| Workflow | Run ID | ئەنجام |
|---|---:|---|
| Python checks | 43017520307 | 547 تاقیکردنەوە سەرکەوتوو؛ 11 skip |
| Course 4 Beta review safety | 43017510833 | 547 تاقیکردنەوە سەرکەوتوو؛ 11 skip |
| Course 4 Beta review safety (دووبارە) | 43017532820 | 547 تاقیکردنەوە سەرکەوتوو؛ 11 skip |
| Orthography course structure tests | 43017510812 | 4/4 سەرکەوتوو |

- Python compilation: سەرکەوتوو.
- Unit tests: `OK (skipped=11)` لە هەردوو workflowی گشتی و Course 4 Beta.
- هەموو workflowەکان لەسەر کۆمیتی `4516c3a` کۆتایییان بە success هاتووە.

## دۆخی پاراستن
- داتای کۆرسی ٤: ٥٠ وانە؛ ٣٠ پەسەندکراو، ١ ناوخۆیی و پەسەندنەکراو، ١٩ ڕەشنووسی پێداچوونەوە.
- وانەی ١٣ هێشتا review-only/Beta ـە؛ کویز و خەڵاتی فەرمی بۆی چالاک نییە.
- Arami assessment لەبێ پەسەندکردنی ئەکادیمی شاراوە و قفڵکراوە.
- کویزی ڕەشنووسی کۆرسە لاتینییەکان پێش نمرەدان و خەڵاتدان ڕەت دەکرێتەوە.

## سنووری جێبەجێکردن
PR #152 کراوە و نەیەکگرتووەتەوە. هیچ Botkeep import، restart، deploy، Telegram rollout یان دەستکاریی داتابەیسی بەرهەمهێنان نەکراوە. هێشتا پێویستە وەڵامی نووسراوی Botkeep لەسەر Node17 و تاقیکردنەوەی ڕاستەوخۆی Telegram بە تەواوی بپشکنرێن. CIی سەرکەوتوو بە تەنها بەڵگەی runtimeی زیندوو نییە.

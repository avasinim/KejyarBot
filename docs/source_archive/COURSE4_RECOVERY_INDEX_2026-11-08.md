# فهرستی گەڕانەوەی کۆرسی ٤ — 2026-11-08

ئەم فایلە پەڕگە سەرەکییەکانی پاراستن نیشان دەدات؛ لە کاتی گەڕانەوە لە گفتوگۆی نوێدا سەرەتا checkpoint بخوێنەوە.

1. **[خاڵی گەڕانەوە و پاراستنی کۆرسی ٤](COURSE4_RECOVERY_CHECKPOINT_2026-11-08.md)** — شوێنی کار، دۆخی PR/CI، ڕەشنووسەکان، runtime، چاکسازییەکان، خاڵە کراوەکان و هەنگاوە داهاتووەکان.
2. **[بەستەری پاراستنی وانەکانی ١–٤٦](COURSE4_LESSONS_01_46_PRESERVATION_BUNDLE_2026-11-08.json)** — 31 وانەی runtime + 15 ڕەشنووسی فراوانکراوی 32–46.
3. **[لیستی سەرچاوە خاوەکان](COURSE4_RAW_SOURCE_INVENTORY_2026-11-08.md)** — فایلە سەرچاوە و transcriptە پارێزراوەکانی 32–46.
4. **[Structured reviewی وانەکانی 32–46](staging/COURSE4_LESSONS_032_046_STRUCTURED_REVIEW_2026-11-08.json)** — پێکهاتە و ڕاهێنانەکان؛ هەموویان pending owner review ـن.
5. **[ڕاپۆرتی بەراوردی quiz و پشکنینی ناوەڕۆک](COURSE4_QUIZ_MAINLINE_COMPARISON_2026-11-08.md)**.
6. **[ڕاپۆرتی جیاوازیی main و branch](COURSE4_MAINLINE_DIVERGENCE_RECONCILIATION_2026-11-08.md)**.
7. **[پشکنینی تەواوی سەرچاوەکان](COURSE4_LESSONS_032_046_SOURCE_COMPLETENESS_AUDIT_2026-11-08.md)** — پلەی پشتڕاستبوونی سەرچاوەی هەر وانە، جیاوازی master transcript و پارچەدەقەکان، و پاشکۆی WritingBlockی ماوە.
8. **[لیستی چاکسازییە بەڵگەدارەکان](COURSE4_LESSONS_032_046_EVIDENCE_BASED_CORRECTION_QUEUE_2026-11-08.md)** — شوێنی هەڵە و پێشنیاری چاکسازی؛ بڕیارە زاراوەیی و زانستییەکان لە چاکسازیی دڵنیابووەکان جیا کراونەتەوە.
9. **[پێوەری گواستنەوە بۆ runtime](COURSE4_LESSONS_032_046_RUNTIME_SCHEMA_AND_ACTIVATION_GATE_2026-11-08.md)** — مەرجە فنییەکانی پەسەندکردن و چالاککردن.
10. **ڕەشنووسەکان:** لە `staging/drafts/COURSE4_LESSON_032_EXPANDED_DRAFT_2026-11-08.md` تا `COURSE4_LESSON_046_EXPANDED_DRAFT_2026-11-08.md`.
11. **Snapshotەکانی main:** `MAINLINE_COURSE4_LESSONS_01_26_SNAPSHOT_2026-11-08.json`، `MAINLINE_COURSE4_RUNTIME_TESTS_SNAPSHOT_2026-11-08.py`، `MAINLINE_COURSE4_LESSON26_PARTICLES_RESEARCH_SNAPSHOT_2026-11-08.md`.

Repository: `avasinim/KejyarBot`  
Branch: `feat/course4-clean-port-main-20261106`  
PR: [#119](https://github.com/avasinim/KejyarBot/pull/119)

**یادخستنەوە:** دەقی خاو، ڕەشنووس و runtime جیاوازن. هیچ وانەیەک بە پەسەندکراو مەژمێرە تا خاوەن پڕۆژە پەسەندی نەکات؛ هیچ snapshotێک overwrite مەکە.


**نوێکردنەوە:** پشکنینی دواتری وانەکانی 37–38 و دۆخی ئێستای branch/CI لە کۆتایی `COURSE4_RECOVERY_CHECKPOINT_2026-11-08.md` تۆمار کراوە.


**نوێکردنەوە:** یەکسانکردنی زاراوەی وانەی ٤٦ لە ڕەشنووس، structured review و Preservation Bundle تۆمار کراوە؛ وردەکاری لە checkpoint و terminology audit ـە.


**نوێکردنەوە:** پشکنینی زنجیرەی زاراوەکان لە وانەکانی 32–46 و خاڵە کراوەکانی وانەی 39/41 و 42–45 لە کۆتایی ڕاپۆرتی پشکنینی quiz و ناوەڕۆک و خاڵی گەڕانەوە تۆمار کراوە.


**نوێکردنەوە:** ناونانی پێکهاتەی «لەگەڵ مامۆستاکەی» لە وانەی 41 بە «پێکهاتەی هاوبەشی (Comitative phrase)» چاک کرا و ڕەشنووس، structured review و Preservation Bundle هاوتا نوێ کرانەوە؛ دەقی خاو پارێزراوە.


**نوێکردنەوە:** سنووری بەڵگەی نموونەکانی وانەکانی 42–45 (clitic، نموونەی نەکارا و بەرکارپێشخستن) لە ڕاپۆرت و خاڵی گەڕانەوە تۆمار کرا؛ ئەم نموونانە تا پشتڕاستکردنەوەی زاری لە دۆخی پشکنین دەمێننەوە.


**نوێکردنەوە:** ناونانی دوو پێڕستەی سەربەخۆی هاوئاست لە نموونەی لێکدراوی ئاڵۆزدا لە وانەکانی 37، 38 و 46 یەکگرتوو کرا؛ وردەکاری لە checkpoint و terminology audit ـە.


**نوێکردنەوە:** لە وانەی 46 «پێڕستەی سەربەخۆ» لە «سەرڕستە» جیا کراوەتەوە و خشتەی چوار جۆری ڕستە لەگەڵ نموونەی لێکدراوی ئاڵۆز یەکگرتوو کرا؛ وردەکاری لە checkpoint و terminology audit ـە.

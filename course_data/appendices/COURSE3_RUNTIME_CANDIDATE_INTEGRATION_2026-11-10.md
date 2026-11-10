# تۆماری هاوئاهەنگکردنی runtime — کۆرسی ٣، ٦٨ وانە

- بەروار: 2026-11-10
- برانچ: `work/course3-lessons67-68-practice-archive-2026-11-10`
- PR: #140 — Draft
- ئەم تۆمارە بەڵگەی ئامادەکردنی candidate ـە، نە بەڵگەی deployment یان چالاکبوونی production.

## گۆڕانکارییەکانی candidate

1. `bot.py`
   - loader بۆ فایلی `course_data/appendices/unified_orthography_lessons_01_68_candidate_2026-11-10.json` ڕێکخرا.
   - `include_extended_sections=True` بۆ کۆرسی ٣ دانرا تا چالاکییە زیادکراوەکان لە ناوەڕۆکی وانەدا پیشان بدرێن.
   - ژمارەی چاوەڕوانکراوی `unified_orthography` لە ٦٦ بۆ ٦٨ گۆڕدرا.

2. `courses.json`
   - ناسنامەی وانەکانی `unified_orthography_01` تا `unified_orthography_68` تۆمار کرا.
   - دۆخی کۆرس لە candidateدا `active` ـە؛ ئەمە تەنیا لە کۆدی PR ـە و هیچ کاریگەرییەکی لەسەر runtimeی `main` نییە تا PR بە شێوەی پەسەندکراو merge و deploy نەکرێت.

3. `course_lesson_adapters.py`
   - adapter ئێستا چالاکییەکانی شێوەی dictionary بە دوو بەشی ناونیشان و ڕێنمایی دەخوێنێتەوە.
   - شێوەی کۆنی چالاکیی دەقی سادەش هەر پشتگیری دەکرێت؛ ئەمە بۆ نەشکاندنی شێوازی کۆرسی ٤ پارێزراوە.

4. `course_data/appendices/unified_orthography_lessons_01_68_candidate_2026-11-10.json`
   - بۆ وانەکانی ٦٧ و ٦٨ خانەی `source` زیادکرا، بەڵام `source_note`ی ڕوونکەرەوەش پارێزرا.
   - ژمارەی پەڕە بە ڕاستگۆیی وەک پشتڕاست‌نەکراو تۆمارکرا؛ هیچ پەڕەیەک بە گریمانە دانەنرا.

5. `tests/test_course3_lessons_67_68_integration.py`
   - شەش تاقیکاریی یەکخستن زیادکرا بۆ پاراستنی ٦٦ وانە، ژمارەکردنی ٦٨، manifestی runtime، loader، پیشاندانی چالاکی و کویز.

## ئەنجامی پشکنینی داتای ئێستا

- ٦٨ وانە هەن و ژمارەکان ١–٦٨ بەردەوامن.
- هەموو ٦٦ وانەی سەرچاوە لە candidate بە تەواوی هاوتان.
- manifestی runtime ٦٨ ناسنامەی هەیە و کۆتایییەکەی ٦٧ و ٦٨ ـە.
- loaderی candidate فایلی ڕاست دەخوێنێتەوە و extended sections چالاکە.
- ٨ چالاکی لە وانەی ٦٧ و ١٠ چالاکی لە وانەی ٦٨ هەن؛ هەر چالاکییەک ناونیشان و ڕێنماییی دەقی هەیە.
- هەر وانەیەک ١٢ پرسیاری کویزی هەیە؛ لە پشکنینی داتادا answer index و هەڵبژاردەی دووبارەبووەوەی نادروست نەدۆزرایەوە.
- SHAی فایلی سەرچاوەی ٦٦ وانە نەگۆڕاوە: `e865327032b35bfff0980c7ad7e67b98e3e08523`.

## تاقیکاری و release gate

- تاقیکارییەکانی Python زیادکراون، بەڵام لەم ژینگەیەدا جێبەجێ نەکراون؛ نابێت بە سەرکەوتوو تۆمار بکرێن.
- بۆ commitی ئێستا هیچ GitHub Actions workflow run یان combined status ـێک نەگەڕاوەتەوە.
- smoke testی startup لە ژینگەیەکی سەلامەت هێشتا ماوە.
- پشکنینی زانستیی کۆتاییی هەندێک نموونەی «ە» و نەرێکردن هێشتا ماوە.
- کێشەی infrastructureی Botkeep بەربەستی deployment ـە؛ هیچ restart، sync، database mutation، merge یان deployment نەکراوە.

## دەرئەنجام

کۆدی candidate و پەکەیجی وانەکانی ٦٧–٦٨ ئێستا لە یەک PRدا هاوئاهەنگ کراون، بەڵام PR هێشتا Draft ـە. تەنیا دوای تاقیکاریی سەرکەوتوو، پشکنینی زانستیی کۆتایی و پشتڕاستکردنەوەی سەلامەتیی Botkeep دەتوانرێت بڕیار لەسەر merge/deploy بدرێت.

# خاڵی گەڕانەوە و پاراستنی کۆرسی ٤ — 2026-11-08

ئەم پەڕگەیە خاڵی یەکگرتووی گەڕانەوەی پڕۆژەی کۆرسی ٤ ـە. لە گفتوگۆی نوێ یان دوای وەستانی سیستەم، سەرەتا ئەم فایلە بخوێنەوە و پاشان دۆخی branch/PR/CI لە GitHub پشتڕاست بکەرەوە. وانەی پارێزراو بەهۆی نەبوونی لە چاتێکدا بە ونبوو مەژمێرە و داوای دووبارە ناردنی سەرچاوە مەکە، مەگەر پەڕگەکە لە repository و snapshotەکاندا بە وردی نەدۆزرێتەوە.

## شوێنی کار
- فهرستی گەڕانەوە: `docs/source_archive/COURSE4_RECOVERY_INDEX_2026-11-08.md`.
- Repository: `avasinim/KejyarBot`
- Branch: `feat/course4-clean-port-main-20261106`
- PR: [#119 — Course 4 beta reading, 46 lessons](https://github.com/avasinim/KejyarBot/pull/119)
- Headی پشتڕاستکراو لە 2026-11-08: `288a7538dfbf3d58fb2fc78a95aa3149fc48e010`
- Baseی PR لە پشکنینی کۆتاییدا: `400c9ae8b567b565c74afe1e3db7c5274077da8e`
- دۆخی PR: open، Draft، `mergeable=false`. Merge و deployment ڕوویان نەداوە/پشتڕاست نەکراون.
- براند: کەژیار؛ ناو و ناسنامەی براند بپارێزرێت.

## فهرستی سەرچاوەی خاو
- `docs/source_archive/COURSE4_RAW_SOURCE_INVENTORY_2026-11-08.md` — لیستی فایلە خاوەکانی وانەکانی 32–46 و بەڵگەنامەکانی provenance/source.

## بەڵگەی سەرەکیی پاراستن
1. `docs/source_archive/COURSE4_LESSONS_01_46_PRESERVATION_BUNDLE_2026-11-08.json`
   - 31 وانەی runtimeی پێشوو + 15 ڕەشنووسی پارێزراوی وانەکانی 32–46.
   - کۆی وانەکان 46؛ 31 runtime، 15 draft.
   - snapshotە؛ بە JSONی main یان runtime overwrite مەکرێت.
2. `docs/source_archive/staging/COURSE4_LESSONS_032_046_STRUCTURED_REVIEW_2026-11-08.json`
   - 15 وانەی 32–46؛ هەموویان `owner_review_pending_expanded_draft`.
   - لەگەڵ Markdown بەیەکەوە نوێ بکرێتەوە؛ خانەکانی `exercises` و وەڵامەکان بە جیا پشکنین بکرێن.
3. `docs/source_archive/staging/drafts/COURSE4_LESSON_032_EXPANDED_DRAFT_2026-11-08.md` تا `COURSE4_LESSON_046_EXPANDED_DRAFT_2026-11-08.md`
   - 15 ڕەشنووسی فراوانکراو؛ دەقی خاو لەوانە جیاوازە و نابێت بسڕدرێتەوە.
4. `docs/source_archive/COURSE4_QUIZ_MAINLINE_COMPARISON_2026-11-08.md`
5. `docs/source_archive/COURSE4_MAINLINE_DIVERGENCE_RECONCILIATION_2026-11-08.md`
6. Snapshotەکانی main:
   - `docs/source_archive/MAINLINE_COURSE4_LESSONS_01_26_SNAPSHOT_2026-11-08.json`
   - `docs/source_archive/MAINLINE_COURSE4_RUNTIME_TESTS_SNAPSHOT_2026-11-08.py`
   - `docs/source_archive/MAINLINE_COURSE4_LESSON26_PARTICLES_RESEARCH_SNAPSHOT_2026-11-08.md`

## فایلەکانی کۆرس و runtime
- `course_data/grammar_course4_lessons.json`: 46 دانە؛ 1–31 runtime، 32–46 draftی پێداچوونەوە و بێ quiz.
- `courses.json`: manifest.
- `curriculum/grammar_course4_plan.json`: پلانی 46 وانە.
- `bot.py`: ئاگاداریی draft، ڕێگریکردن لە completion/reward بۆ draft، پاراستنی quiz لە شکستەکانی Telegram، پەڕەکردنی دەقی درێژ.
- `tests/`: تاقیکردنەوەکانی ئەم ڕەفتارانە.

## چاکسازییە سەرەکییە پارێزراوەکان
- Draft لە هەموو ڕێگاکانی کردنەوەی وانەدا بە ئاگاداری پیشان دەدرێت؛ completion و rewardی نییە.
- دۆخی quiz ئەگەر ناردنی پرسیاری یەکەم/feedback/پرسیاری داهاتوو/ئەنجامی کۆتایی شکست بهێنێت پاک دەکرێتەوە.
- منووی quiz تەنها quizی بەردەست و پەسەندکراو پیشان دەدات.
- وانەی 34: یەکسانکردنی `بکەر` لە title و objectives.
- وانەکانی 36 و 39: `Adjunct = پێکهاتەی لاوەکی`؛ لە `هاوەڵکار` (Adverb) و `هاوەڵکاری` (Adverbial) جیا.
- وانەی 43: «دەچن» لەگەڵ «ئەوان» کەسی سێیەمی کۆیە؛ لەگەڵ «ئێوە» کەسی دووەمی کۆیە.
- وانەی 44: جیاکردنەوەی نەکارا لە تێنەپەڕ و بکەری ڕێزمانی لە ئەنجامدەری کردار.
- وانەکانی 37–38 و 46: پشکنینی پێڕستەی سەربەخۆ، سەرڕستە، بەرڕستە و نموونەی لێکدراو/لێکدراوی ئاڵۆز.
- لە وانەکانی 38، 39، 43 ناهاوتاییی خانەکانی ڕاهێنان لە structured review چاک کرا.

## دۆخی پشکنینی هاوتایی
لە پشکنینی 2026-11-08:
- هەموو 15 ڕەشنووسی 32–46 لەگەڵ `source_markdown`ی structured review بە تەواوی یەکسانن.
- هەموو دەقەکانی `exercises` لە فایلە هاوتاکانیاندا بوونیان پشتڕاست کراوەتەوە.
- ئەمە یەکسانیی دوو شێوەی ڕەشنووس دەسەلمێنێت، نەک پەسەندکردنی زانستی یان ئامادەبوونی runtime.
- پشکنینی ناوەڕۆکی 39–45 ئەنجام دراوە؛ خاڵە هەستیارەکانی clitic، agent/object، passive و هەندێک نموونەی زاری بە مەرجی پشتڕاستکردنەوە ماونەتەوە.

## CIی پشتڕاستکراو
- Run `42485236438` — head `74caa788`: completed / success.
- Run `42485201985` — head `1119bbd8`: completed / success.
- Run `42485142235` — head `1dd124ef`: completed / success.
- Run `42485087160` — head `ea9cac5d`: completed / success.
- Run `42485079220` — head `56ce481a`: completed / success.

## بڕیاری mainline
main 26 وانەیە؛ branch 46 وانەیە. وەشانی فراوانکراوی branch لە هەندێک وانەدا زانیاری و نموونەی زیاتر هەیە. JSONی main بە blind overwrite/cherry-pick مەگوازرێتەوە؛ snapshot و reconciliation هەیە، بەراوردی ناوەڕۆکی JSON کارێکی جیاوازە.

## کارە ماوەکان — بە ڕیزبەندی
1. پشکنینی وردی وانەکانی 32–38 لەسەر بنەمای دەقی خاو، Markdown و structured review؛ هیچ وانەیەک لەبەر نەبوونی لە چاتێکدا لادەنرێت.
2. دووبارە پشکنینی نموونە، وەڵام، ژمارەی خانە و هەموو خانە structured ـەکان بۆ 32–46.
3. پشکنینی زاراوە/نموونە هەستیارەکان: clitic، agent/object، passive، transitivity، compound/light verbs، Adjunct/Adverb/Adverbial.
4. تەواوکردنی reconciliationی سێ کۆمیتی main بە پشکنینی ناوەڕۆکی JSON؛ نەک overwriteی خۆکار.
5. پشکنینی کۆتاییی هەموو 46 وانە و CI.
6. پەسەندکردنی وانەکان لەلایەن خاوەن پڕۆژە پێش هەر گۆڕانکارییەکی دۆخی approval؛ merge/deployment تەنها دوای پشتڕاستکردنەوە.

## سنوورەکان و پاراستن
- دەقی خاو، ڕەشنووس و runtime جیاوازن؛ یەکێکیان بە یەکێکی تر مەگۆڕەوە.
- هیچ وانەیەک بە پەسەندکراو ناژمێردرێت تا پەسەندی خاوەن پڕۆژە.
- کۆرسی 4 بەراورد بە کتێبی کۆن یان سەرچاوەی دەرەکی مەکرێت؛ دەقی وانەی خاو بنەمای پشکنینە.
- Backupی Botkeepی خاوەن پڕۆژە: `Kejyar recovery point 2026-11-07`، 7.9 MB، backup 1/1 completed؛ backupێکی زیادەیە، جێگرەوەی GitHub snapshots نییە.
- داوای FileZilla/SFTP یان uploadی گشتیی course_data/.env مەکە.

## دەستپێکردنەوە
لە چاتێکی نوێدا ئەم فایلە بخوێنەوە، branch/head/PR/CI پشتڕاست بکەرەوە و لە «کارە ماوەکان» بەردەوام بە. لە خاوەن پڕۆژە مەپرسە وانە یان کارە پێشووەکان دووبارە بنێرێتەوە، مەگەر پەڕگەیەکی دیاریکراو لە repository و snapshotەکاندا بە تەواوی نەدۆزرێتەوە.

**ئەم checkpoint ـە بەڵگەی پاراستنی کارەکانە؛ بە مانای پەسەندکردن، merge یان deployment نییە.**


## زیادەی پاراستن — پشکنینی 32–38 و چاکسازییەکانی 2026-11-08، کۆمیتی `65e427b1`
- وانەی 33: پێناسەی Agent چاک کرا؛ ئەنقەستیبوون بە مەرجی گشتیی Agent نەما، چونکە ڕۆڵی واتایی بە کردار و کۆنتێکستەوە دیاری دەکرێت.
- وانەی 34: `Subject` لە ناونیشان، پێناسە، ئامانج و ڕەشنووسدا بە `بکەر` یەکسان کرا؛ «نیهاد» تەنها لە تێبینیی پاراستنی دەقی خاو ماوەتەوە. ناونیشانی runtime و curriculum planیش هاوتا کران.
- وانەی 36: `Adjunct` بە `پێکهاتەی لاوەکی` ناونرا؛ لە `هاوەڵکار (Adverb)` و `هاوەڵکاری (Adverbial)` جیا کراوەتەوە. بەشی دووبارەی «پەیوەندی بە وانەکانی تر» لابرا و بەشەکان ڕیزبەندی کران.
- Structured review ـی وانەکانی 33، 34 و 36 لەگەڵ Markdown هاوتا کرا؛ exercises ـی 34 و 36یش نوێ کرانەوە.
- پشکنینی کۆتایی: 15/15 وانەی 32–46، `source_markdown`ی هاوتا و هەموو دەقەکانی `exercises` یەکسان و دۆزرایەوەن.
- CI Run `42486020898` بۆ کۆمیتی `65e427b1`: completed / success. Run `42486017385` بۆ کۆمیتی ناوەڕاستی `f1bbf0c4` شکستی هێنا، چونکە لەو کۆمیتەدا ناونیشانی runtime نوێ بوو بەڵام curriculum plan هێشتا ناونیشانی کۆنی هەبوو؛ کۆمیتی دواتری `65e427b1` هەردووکی یەکسان کرد و CIی سەرکەوتوو هەیە.
- خاڵی کراوەی وانەی 38: شیکاریی ڕستەی درێژی دەقی خاو هێشتا بە مەرجە؛ بکەر و پەیوەندیی کردارە هاوئاهەنگەکان پێویستیان بە پشتڕاستکردنەوەی خاوەن دەق هەیە. ئەمە بە شێوەی ڕاستگۆیانە تۆمار کراوە، نەک بە شیکاریی دڵنیای نادروست.


## نوێکردنەوەی پاشکۆی یەکگرتوو — 2026-11-08
- Preservation Bundle نوێ کرایەوە بۆ ئەوەی ناوەڕۆکی هەموو 15 ڕەشنووسی 32–46 لەگەڵ فایلە ئێستاییەکانی Markdown هاوتا بێت؛ 31 وانەی runtimeی ناو bundle وەک snapshot پارێزراون.
- پشتڕاستکردنەوەی دووبارە: 15/15 `content_markdown`ی bundle بە تەواوی لەگەڵ ڕەشنووسی Markdownی هاوتایان یەکسانن.
- پەڕگەی bundle ئێستا ڕێڕەوی checkpoint و recovery index ـیش لە metadataدا تۆمار دەکات.
- CI Run `42486366934` بۆ bundle commit `9786b263`: completed / success؛ Run `42486340464` بۆ کۆمیتی پێشووی bundle `e8a6fe30`: completed / success.
- لە کاتی ئەم نوێکردنەوەیەدا هەموو 15 وانە هێشتا `owner_review_pending_expanded_draft` ـن؛ هیچ approval، merge یان deployment ڕووی نەداوە.


## زیادەی پاراستن — پشتڕاستکردنەوەی bundle و دۆخی نوێی branch، 2026-11-08T17:14+03:30
- Branch headی ئێستا: `38ad800612c1d91e59ae767773eae79c207c0dd3`؛ PR #119 head هەمان SHAیە. Base: `400c9ae8b567b565c74afe1e3db7c5274077da8e`؛ PR open و Draft و `mergeable=false`.
- Preservation Bundle بە JSON خوێندرایەوە و 31 وانەی runtime لە `lessons` و 15 ڕەشنووسی 32–46 لە `preserved_draft_lessons` هەڵگرتووە؛ `lesson_count=46`, `runtime_lesson_count=31`, `draft_lesson_count=15`.
- هەموو 15 `content_markdown` لە Bundle بە وردی بەراورد کرا بە فایلە Markdown ـە سەرەکییەکانی 32–46: 15/15 exact match؛ هیچ ڕەشنووسێک لە پاشکۆدا کۆن نەماوە.
- Runtime JSON: 46 وانە؛ 1–31 وانەی runtime، 32–46 هەموویان `owner_review_pending_expanded_draft` و بێ quiz. Curriculum plan: 46 وانە، لەوانە 15 pending.
- Structured review: 15 وانە، هەموویان `owner_review_pending_expanded_draft`; 15/15 `source_markdown` لەگەڵ فایلە Markdown ـەکان exact match. خانەکانی ڕاهێنان پێشتر بە جیا پشکنراون؛ لە پشکنینی نوێدا هیچ فایلێکی وانە لە repository ون نییە.
- CIی شکستخواردوو Run `42486017385` بۆ commitی ناوەڕاست `f1bbf0c4` تەنها لە `test_all_lesson_titles_and_numbers_match_curriculum_plan` شکستی هێنا: ناونیشانی runtimeی وانەی 34 بە `بکەر` نوێ کرابووەوە، بەڵام plan هێشتا `نیهاد`ی هەبوو. کۆمیتی دواتری `65e427b1` هەردووکی یەکسان کرد؛ CIی `42486020898` و هەموو runەکانی دواتر سەرکەوتوون.
- نوێترین CI: Run `42486450848`, commit `38ad8006`, completed/success. پێش ئەوەش runەکانی `42486366934`, `42486340464`, `42486273591`, `42486243849`, `42486228713`, `42486020898` completed/success.
- تێبینی: ئەم پشتڕاستکردنەوەیە پاراستنی پەڕگە و تاقیکردنەوەی repository دەسەلمێنێت؛ بە مانای پەسەندکردنی وانەکانی 32–46، merge، یان deploymentی Botkeep نییە.

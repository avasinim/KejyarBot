# خاڵی گەڕانەوە و پاراستنی کۆرسی ٤ — 2026-11-08

ئەم پەڕگەیە خاڵی یەکگرتووی گەڕانەوەی پڕۆژەی کۆرسی ٤ ـە. لە گفتوگۆی نوێ یان دوای وەستانی سیستەم، سەرەتا ئەم فایلە بخوێنەوە و پاشان دۆخی branch/PR/CI لە GitHub پشتڕاست بکەرەوە. وانەی پارێزراو بەهۆی نەبوونی لە چاتێکدا بە ونبوو مەژمێرە و داوای دووبارە ناردنی سەرچاوە مەکە، مەگەر پەڕگەکە لە repository و snapshotەکاندا بە وردی نەدۆزرێتەوە.

## شوێنی کار
- فهرستی گەڕانەوە: `docs/source_archive/COURSE4_RECOVERY_INDEX_2026-11-08.md`.
- Repository: `avasinim/KejyarBot`
- Branch: `feat/course4-clean-port-main-20261106`
- PR: [#119 — Course 4 beta reading, 46 lessons](https://github.com/avasinim/KejyarBot/pull/119)
- Headی پشکنینی پێش ئەم نوێکردنەوەی checkpoint: `1d479050fcbfd6864a74d46dc068e00a7f0ef161`
- Baseی PR لە پشکنینی کۆتاییدا: `400c9ae8b567b565c74afe1e3db7c5274077da8e`
- دۆخی PR: open و Draft؛ merge و deployment ڕوویان نەداوە. mergeability لە هەر گەڕانەوەیەکدا نوێ پشتڕاست بکرێتەوە.
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
   - لەگەڵ Markdown بەیەکەوە نوێ بکرێتەوە؛ `key_points`, `exercises`, `comprehension`, `role_play` و خانەکانی تر بە جیا پشکنین بکرێن.
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
- 225 خانەی `key_points`، 15 خانەی `comprehension`، هەموو `exercises` و `role_play` لە 15 structured reviewدا لە `source_markdown`ی هاوتایاندا بە تەواوی دۆزرایەوە؛ mismatch = 0.
- `quiz`ی structured review بە ئەنقەست بەتاڵە؛ کویزی ناو Markdown بۆ پشکنینە و quizی runtime نییە.
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
1. پشکنینی وردی وانەکانی 32–38 لە ئاستی یەکەم تەواو کرا؛ چاکسازییەکانی 34 و 38 جێبەجێ و پاشکۆ کراون. خاڵە کراوەکان: شیکاریی نموونەی درێژی وانەی 38، پشکنینی هاولکیی «یان…یان/نە…نە» لە 37، و پشتڕاستکردنەوەی زاریی نموونە هەستیارەکان.
2. بەراوردی master transcript و 7 segmentی 32–38 تەواوە (7/7 exact substring)؛ بەڵام 33–36 سەرچاوەی سەربەخۆی owner-verifiedیان نییە، هەرچەند segmentەکان لە master transcriptدا پشتڕاست کراون.
3. پشکنینی structured reviewی 32–46 لە ئاستی خانەکان تەواو کرا؛ 225 key_points و هەموو exercises/comprehension/role_play لەگەڵ source_markdown یەکسانن. هەر چاکسازییەکی داهاتوو دەبێت هەمان پشکنینی خانە بە خانە دووبارە بکاتەوە.
4. پشکنینی زاراوە/نموونە هەستیارەکان بەردەوام بێت: clitic، agent/object، passive، transitivity، compound/light verbs، Adjunct/Adverb/Adverbial.
5. تەواوکردنی reconciliationی سێ کۆمیتی main بە پشکنینی ناوەڕۆکی JSON؛ نەک overwriteی خۆکار.
6. پشکنینی کۆتاییی هەموو 46 وانە، Bundle و CI؛ پاشان بڕیاری runtime readiness تەنها دوای پەسەندی خاوەن پڕۆژە.
7. پاشکۆی مێژوویی WritingBlock بۆ 39–45 بە ID/ناونیشانی دیاریکراو بگەڕێنەوە؛ داوای دووبارە ناردنی هەموو وانەکان مەکە.
8. پەسەندکردنی وانەکان لەلایەن خاوەن پڕۆژە پێش هەر گۆڕانکارییەکی دۆخی approval؛ merge/deployment تەنها دوای پشتڕاستکردنەوە.

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


## CI و سەرچاوەکان — پشتڕاستکردنەوەی کۆتاییی ئەم نۆرەی کار
- هەموو فایلە سەرچاوە بنەڕەتییەکانی وانەکانی 32–38 (OWNER_SOURCE_SEGMENT)، 39–45 (DRAFT_TRANSCRIPT_SEGMENT) و 46 (OWNER_SOURCE_TEXT) لە archive ـدا هەن؛ لیستیان لە `COURSE4_RAW_SOURCE_INVENTORY_2026-11-08.md` ـە.
- Preservation Bundle دووبارە پڕکراوەتەوە و 15/15 ڕەشنووسەکەی لەگەڵ Markdownی ئێستا یەکسانن.
- CI Run `42486659208` بۆ کۆمیتی `56a92f8d`: completed / success؛ `compileall` و تاقیکردنەوەکانی repository لە workflowدا بە سەرکەوتوویی تێپەڕیون.
- Recovery Index، Recovery Checkpoint، Raw Source Inventory و Preservation Bundle هەموویان لە repository دانراون؛ ئەمانە ڕێڕەوی گەڕانەوەی سەربەخۆ لە چاتن.


## نوێکاریی یەکگرتوویی وانەی 33
- ئاماژەی وانەی 33 بۆ وانەی 34 لە «نیهاد» بۆ «بکەر» ڕێکخرا؛ Markdown، structured review و Preservation Bundle هەرسێکیان هاوتا کران.
- پشکنینی تایبەتی وانەی 33: Markdown = structured review = bundle، هەرسێکیان یەکسانن.
- دۆخی PR هێشتا open/Draft و mergeable=false ـە؛ CI بۆ زنجیرەی کۆمیتەکانی ئەم چاکسازییە لە کاتی نووسینی ئەم زیادەیەدا لە پشکنین‌دایە.


## چاکسازیی پشکنینی 32–38 — وانەکانی 34 و 38
- وانەی 34: پرسیاری خاڵە کراوەکان لە «بکەر و بکەر» بۆ «بکەر و نیهاد» چاک کرا؛ ئەمە دووبارەبوونی وشەیەکی هەڵە بوو و لەگەڵ ناونیشانی دەقی خاو هاوتا کرا. دەقی خاو پارێزراوە.
- وانەی 38: دوو هەڵبژاردەی کویز نوێ کرانەوە؛ Main Clause بە «بنەمای سەرەکیی ڕستەی ئاڵۆز» و Subordinate Clause بە «پەیوەندیی ڕێزمانی بە سەرڕستە و ئەرکی دیاریکراو» پێناسە کرا، بۆ ئەوەی لەگەڵ Independent/Dependent وەک هاوواتای ڕەها تێکەڵ نەبن.
- Markdown، source_markdownی structured review و content_markdownی Preservation Bundle بۆ هەردوو وانەکە هاوتا کران.
- دەقی خاو، runtime و کویزی چالاک نەگۆڕدراون؛ هەردوو وانەکە هێشتا ڕەشنووسی پێداچوونەوەن.


## پێداچوونەوەی provenanceی سەرچاوەکان — 2026-11-08
- سەرچاوەی یەکگرتووی وانەکانی 32–38: `docs/source_archive/COURSE4_LESSONS_032_038_SOURCE_2026-11-07.md`، 1548 هێڵ، لە فایلێکی ناردراوی بەکارهێنەرەوە پارێزراوە و دەقی ناوەڕۆکی بەبێ دەستکارییە.
- پارچەدەقەکانی 32–38 لە `docs/source_archive/staging/COURSE4_LESSON_0XX_OWNER_SOURCE_SEGMENT...` لە archive هەن؛ بەڵام Source Completeness Audit دەڵێت بۆ وانەکانی 33–36 سەرچاوەی سەربەخۆی خاوەن پڕۆژە بە جیا پشتڕاست نەکراوەتەوە. ئەم segmentانە وەک پارچەدەقی ئەرشیفی/هەڵگرتنەوەی transcript مامەڵەیان لەگەڵ بکرێت، نەک وەک سەرچاوەی سەربەخۆی owner-verified.
- وانەی 37 دەقی زیادەی خاوەن پڕۆژەی هەیە بەڵام partial ـە؛ وانەی 38یش دەقی زیادەی هەیە بەڵام تەواوی ئەوەی نێردراوە پشتڕاست نەکراوەتەوە. master transcript هەردووکیان لەگەڵدا پارێزراوە.
- وانەکانی 39–45 لە master transcriptی 39–45 و segmentەکاندا هەن؛ پاشکۆ مێژووییەکانی WritingBlock بۆ وانەکانی 39 و 45 لە Source Completeness Auditدا وەک بەشی گەڕانەوەی ماوە تۆمار کراون.
- بۆیە هیچ داواکارییەک بۆ دووبارە ناردنەوەی هەموو وانەکان مەکە؛ سەرەتا master transcript، segmentەکان، snapshot و correction queue بخوێنەوە. ئەگەر پاشکۆیەکی دیاریکراوی WritingBlock پێویست بوو، تەنها هەمان پاشکۆ بە ID/ناونیشانی دیاریکراو بدۆزەرەوە.
- چاکسازییەکانی ئەم نۆرە: وانەی 34 و 38 لە Markdown، structured review و Preservation Bundle یەکسان کران؛ 15/15 draft exact match؛ CI runەکانی 42496410825 تا 42496431481 completed/success.


## دۆخی کۆتاییی نۆرەی کار — 2026-11-08
- Branch head پێش ئەم نوێکردنەوەی checkpoint: `a0a2728134a77bb4068e97b76a40b05f4e3c567a`؛ PR #119 open/Draft و `mergeable=false` ـە.
- چاکسازیی وانەی 34 (بکەر/نیهاد) و وانەی 38 (پێناسەی Main/Subordinate Clause) لە Markdown، structured review و Preservation Bundle هەرسێکیان exact match ـن.
- 15 ڕەشنووسی 32–46 لە پشکنینی پێشوو 15/15 یەکسان بوون؛ دوو فایلە گۆڕدراوەکانی 34 و 38 دووبارە لەگەڵ structured review و bundle پشتڕاست کرانەوە؛ هەردووکیان یەکسانن.
- Raw Source Inventory ڕێکخرایەوە: 32–38 master transcriptی 1548 هێڵی هەیە؛ segmentەکانی 33–36 بە سەرچاوەی سەربەخۆی owner-verified ناژمێردرێن، چونکە Source Completeness Audit ئەو پشتڕاستکردنەوەیەی بۆیان نییە. 37 و 38 additional owner sourceی partial/نا تەواو-پشتڕاستکراویان هەیە. ئەمە جیاوازیی provenance ـە، نە ونبوونی فایل.
- Recovery Index نوێ کرایەوە و Source Completeness Audit، Evidence-based Correction Queue و Runtime Activation Gateی تێدا زیاد کران.
- CI Run `42496537350` بۆ commit `a0a2728134`: completed / success؛ Runەکانی `42496516407` و `42496513210`یش success.
- هەموو گۆڕانکارییەکان لە archive/draft/documentation ـدان؛ دەقی خاو، runtime JSON، quizی چالاک، approval، merge و deployment نەگۆڕدراون.


## بەراوردی ڕاستەوخۆی segmentەکانی 32–38 بە master transcript
- فایلەی master: `COURSE4_LESSONS_032_038_SOURCE_2026-11-07.md` (1548 هێڵ).
- bodyی هەموو 7 segmentی 32–38 بە master transcript بەراورد کرا؛ هەموویان substringی ڕاستەوخۆ و exact match بوون (7/7).
- ئەمە پشتڕاست دەکاتەوە کە segmentەکان لە master transcriptەوە پارێزراون؛ بەڵام Source Completeness Audit هێشتا جیاوازیی نێوان دەقی master و owner sourceی سەربەخۆی 33–36 دەپارێزێت.


## پشکنینی خانەی key_points — وانەی 38
- لە دووبارە پشکنینی structured reviewدا دەرکەوت دوو هەڵبژاردەی کویزی کۆنی وانەی 38 لە خانەی `key_points` ـدا ماونەتەوە، هەرچەند `source_markdown` و Bundle نوێ بوون.
- ئەو block ـەی key_points نوێ کرایەوە تا هەردوو پرسیارەکە لەگەڵ Markdown یەکسان بن؛ لە JSONدا `quiz` بە ئەنقەست بەتاڵە، چونکە ئەم وانەیە draft ـە و quizی runtime نییە.
- چاکسازییەکە لە structured review commit `87a92aed` تۆمار کرا. ئەمە هۆشدارییەکە پشتڕاست دەکاتەوە کە پشکنینی `source_markdown` بە تەنها بەس نییە؛ `key_points`، `exercises` و خانەکانی دیکەش دەبێت جیاواز پشکنین بکرێن.


## پشکنینی تەواوی structured review — 2026-11-08
- لە پشکنینی پێشوودا دەرکەوت `key_points`ی هەندێک وانە هێشتا وەشانی کۆنی هەبوو، هەرچەند `source_markdown` نوێ بوو. ئەمە بە تایبەتی لە وانەکانی 32، 33، 34، 36، 37، 38، 39، 42، 43، 44 و 46 دەرکەوت.
- `key_points`ی 11 وانە بە بنەمای بەشەکانی Markdownی ئێستا دووبارە دروست کرایەوە؛ `comprehension`ی 34 و 36یش نوێ کرایەوە. کۆمیت: `980372ee6ef848755a59f08e90a467c18518abd6`.
- پشتڕاستکردنەوە: 15 وانە؛ 225 key_points؛ 15 comprehension؛ هەموو exercises و role_play؛ هەموویان لە source_markdownی هاوتادا substringی تەواون؛ هیچ mismatchێک نەماوە.
- ئەم چاکسازییە تەنها structured review ـی staging نوێ دەکاتەوە؛ دەقی خاو، runtime JSON، manifest، quizی چالاک و approval نەگۆڕدراون.


## نوێکردنەوەی فهرستی گەڕانەوە و CI — 2026-11-08
- Recovery Index دووبارە ڕیزبەندی کرا؛ بەڵگەی Source Completeness، Correction Queue و Runtime Activation Gate لە ژمارە و لینکە ڕاستەکاندا هەن. کۆمیت: `d24883bb491434a4919be1e024b1fda75ccae0c6`.
- CI Run `42496782145` بۆ checkpoint commit `c3795b776258f965aa06b0fcbd77890512ca5554`: completed / success.
- CIی پێشووی structured review Run `42496721235` بۆ commit `980372ee6ef848755a59f08e90a467c18518abd6`: completed / success.
- PR #119 هێشتا open و Draft ـە؛ mergeability لە APIی ئێستادا `null` ـە و دەبێت لە گەڕانەوەی داهاتوودا دووبارە بخوێندرێتەوە. Merge و deployment نەکراون.


## چاکسازیی کویزی وانەکانی 43 و 44 — 2026-11-08
- وانەی 43 Q2: مەبەستی خاوەندارێتیی `ـی` بە کۆنتێکستی «ئەو کتێبەی خۆی خوێندەوە» ڕوون کرایەوە؛ پرسیاری پێشوو دووخوێندنەوەی هەبوو.
- وانەی 44 Q3: پرسیاری «کەژیار هات چییە؟» بە پرسیاری دیاریکراوی تێپەڕبوون گۆڕدرا، بۆ ئەوەی Active/Passive لە Transitive/Intransitive تێکەڵ نەبن.
- Markdown، structured review و Preservation Bundle هەرسێکیان نوێ کرانەوە. کۆمیتەکان: `34eb18dbffa9865a9d5eeb307ee4516335cd6025`, `c15c3ccdb1ef05b7cc8722708f32796f707a45b7`, `481bbb1353ac2bf9219d91b91ebdd27fbe774c7a`, `33316a91769e23eaca268ef85115d749e19683d6`.
- ئەم چاکسازییانە تەنها لە ڕەشنووس/structured review/archive ـدان؛ quizی runtime و دۆخی approval نەگۆڕدراون.


## پشکنینی وانەکانی 39–45 و چاکسازییەکان — 2026-11-08
- وانەکانی 39–45 لە ڕووی نموونە، ئەرکی ڕێزمانی، کویز و خاڵە پێویستەکانی پشکنین خوێندرایەوە.
- دوو ناڕوونیی کویز چاک کران: وانەی 43 Q2 (خاوەندارێتیی ـی بە کۆنتێکست ڕوون کرا) و وانەی 44 Q3 (پرسیاری تێپەڕبوون لە Passive/Intransitive جیا کرا).
- بڕیارە کراوەکان: وانەی 39 وەرگر/تەواوکەر؛ وانەی 41 توخمی ناوی لە کردارە لێکدراوەکان؛ وانەکانی 42–43 زاری بنەڕەتی و clitic؛ وانەی 44 سروشتیبوونی شێوەکانی نەکارا؛ وانەی 45 سروشتیبوونی بەرکارپێشخستن و نیشانەی clitic. هیچ یەکێک بەبێ بەڵگەی زاری/کۆنتێکستی زیاتر بە یاسای گشتی ناگۆڕدرێت.
- هیچ هەڵەیەکی دیکەی answer-key بە دڵنیایی لەم پشکنینەدا نەدۆزرایەوە؛ ئەمە پەسەندکردنی وانەکان نییە.
- CI بۆ چاکسازییەکانی 43 و 44: `42496934419` و `42496931362` هەردوو completed/success.


### پشکنینی زیاتر لە وانەکانی 37–38 — 2026-11-08
- وانەی 37: لە نموونەکانی «یان…یان» و «نە…نە»دا هاوئاهەنگیی دوو پێکهاتە بە خۆی بەڵگەی دوو پێڕستەی سەربەخۆ نییە؛ ڕەشنووس ئاگادارییەکی پێکهاتەیی زیاد کرد تا ئەم نموونانە بەبێ شیکاریی ورد وەک ڕستەی لێکدراو پۆلێن نەکرێن.
- وانەی 38: لە نموونەی «هەرچەندە من ماندوو بووم، دەخوازم بچم بۆ فلیمی سینەمای نیوەشەو»دا پێڕستەی تەواوکەری «بچم بۆ فلیمی سینەمای نیوەشەو» لە ناو سەرڕستەکەدا دیاری کرا؛ شیکاریی پێشوو کە تەنها بەرڕستەی دژایەتی و سەرڕستەی دەستنیشان دەکرد، تەواو نەبوو.
- دەقی خاو و segmentەکان نەگۆڕدراون؛ چاکسازییەکان تەنها لە ڕەشنووسی پشکنین، structured review و Preservation Bundle دان. هیچ وانەیەک پەسەند نەکراوە و runtime نەگۆڕدراوە.

## نوێترین دۆخی پشکنین — 2026-11-08
- Branch head دوای چاکسازیی وانەکانی 37–38: `91572f63bca52a65a2a91f7661d3c83752b10f72`؛ PR #119 هێشتا open و Draft ـە، base `400c9ae8b567b565c74afe1e3db7c5274077da8e`، `mergeable=false`.
- چاکسازیی وانەی 37: ئاگاداریی پێکهاتەیی بۆ «یان…یان» و «نە…نە» زیاد کرا؛ هاوئاهەنگیی پێکهاتەکان بە خۆی بەڵگەی دوو پێڕستەی سەربەخۆ نییە.
- چاکسازیی وانەی 38: پێڕستەی تەواوکەری «بچم بۆ فلیمی سینەمای نیوەشەو» لە نموونەی «هەرچەندە من ماندوو بووم، دەخوازم بچم…»دا دیاری کرا.
- Markdown، `source_markdown` و `key_points`ی structured review، و `content_markdown`ی Preservation Bundle نوێ کرانەوە. پشکنینی 15/15 وانەی 32–46: هیچ mismatchێک لە Markdown/structured review/bundle و خانەکانی `key_points`, `exercises`, `comprehension`, `role_play` نەماوە.
- CIی ئەم زنجیرەیە completed/success: `42497309337`, `42497313376`, `42497317503`, `42497321659`, `42497324504`, `42497327317`.
- دەقی خاو و runtime نەگۆڕدراون؛ هیچ وانەیەک پەسەند نەکراوە، PR merge نەکراوە و Botkeep deployment پشتڕاست نەکراوەتەوە.

### پشکنینی یەکسانیی زاراوەی وانەی ٤٦ — 2026-11-08
- «بکەر/نیهاد» لە پێناسەی پێڕستەدا بۆ «بکەر» یەکگرتوو کرا؛ «نیهاد» لە تێبینیی پاراستنی سەرچاوەی وانەکانی ٣٢ و ٣٤ وەک بەڵگەی دەقی خاو ماوەتەوە و بە گشتی نەسڕاوەتەوە.
- «هاولکی هاوئاست» و «هاولکیی هاوئاست» بە یەک شێوەی «هاولکیی هاوئاست» نووسران؛ «هاولکی بەرخەر» و «بەستەری ژێرکەر/هاولکی بەرخەر» لە پێناسەی سەرەکی بە «هاولکیی بەرخەر» یەکگرتوون. «بەستەری ژێرکەر» تەنها وەسفی ئەرکەکەیە.
- structured review و Preservation Bundle لەگەڵ Markdown نوێ کرانەوە؛ دەقی خاو و runtime نەگۆڕدراون.


## پشکنینی زنجیرەی زاراوەکان لە وانەکانی 32–46 — 2026-11-08
- پشکنینی زنجیرەیی نیشانی دا کە «بکەر/ئەنجامدەری کردار»، «بەرکار/تەواوکەر/پێکهاتەی لاوەکی»، «هاوەڵکار/هاوەڵکاری»، «سەرڕستە/بەرڕستە»، «تێپەڕ/تێنەپەڕ» و «کارا/نەکارا» لە ڕەشنووسەکاندا بە زۆری بە جیاوازی و بە مانای تایبەتی خۆیان بەکارهاتوون.
- وانەکانی 32–34 بنەمای Subject/Agent/Predicate/Copula دادەمەزرێنن؛ وانەکانی 36 و 39–41 جیاوازیی پێکهاتە و ئەرکی ڕێزمانی دەپارێزن؛ وانەکانی 37–38 و 46 پێڕستە و پەیوەندیی سەرڕستە/بەرڕستە دەخەنەڕوو؛ وانەکانی 40 و 44 تێپەڕبوون لە نەکارایی جیا دەکەنەوە؛ وانەکانی 42–43 clitic، خاوەندارێتی و ڕێککەوتن بە جیاوازی دەخەنەڕوو.
- خاڵی کراوەی وانەی 39/41: «پێکهاتەی وەرگر/ئاراستە» و «پێکهاتەی هاوەڵناوی/هاوبەشی» بە خۆکار یەک ناونانەوە؛ دەبێت بڕیاری زاراوەیی و زاری خاوەن کۆرس دیاری بکات.
- وانەی 43 نموونەی جێناوی بەرکاری لکاوی پشتڕاستکراوی نییە؛ لە دۆخی ئێستادا ڕەشنووسی پشکنینە و بۆ وانەی فێرکاریی تەواو/چالاککردنی runtime ئامادە نییە.
- خاڵەکانی وانەکانی 42، 44 و 45 هێشتا پێویستیان بە پشتڕاستکردنەوەی زاری کەژیار هەیە: شێوەی clitic و ڕێککەوتنی کردار؛ سروشتیبوونی نەکاراکردن و «لەلایەن»؛ بەرکارپێشخستن و نموونەی ڕیزبەندی.
- هیچ دەقی خاو، runtime، quizی چالاک یان دۆخی پەسەندکردن نەگۆڕدرا. پشکنینی زاراوەیی بەڵگەی پەسەندکردنی وانەکان نییە.


### چاکسازیی وانەی 41
- «لەگەڵ مامۆستاکەی» لە نموونەی قسەکردندا بە «پێکهاتەی هاوبەشی (Comitative phrase)» ناونرا؛ وشەی «هاوەڵناوی» لابرا بۆ ئەوەی لەگەڵ زاراوەی وەسف/هاوەڵناو تێکەڵ نەبێت.
- فایلەکانی ڕەشنووس، structured review و Preservation Bundle هاوتا نوێ کرانەوە. دەقی خاو و runtime نەگۆڕدراون؛ پەسەندکردن/چالاککردنیش نەکراوە.


### سنووری بەڵگەی نموونەکان لە وانەکانی 42–45
- وانەی 42–43: «من دەمناسێت»، «ئەو دەتناسێت»، «گرتمن»، «وەرم بگرە» و «بم خوازە» بەبێ کۆنتێکست و مۆرفیم‌بەندیی دڵنیا بۆ یاسای گشتی بەکارنایەن؛ وانەی 43 هێشتا وانەی فێرکاریی تەواو نییە.
- وانەی 44: «دزەکە بە دەستی پۆلیس گیرا» بۆ دیاریکردنی agent/instrument پێویستی بە پشتڕاستکردنەوەی زاری هەیە.
- وانەی 45: نموونەکانی بەرکارپێشخراو و clitic لە ترانسکریپتدا هەن، بەڵام سروشتیبوون و مۆرفیم‌بەندییان پشتڕاست نەکراوەتەوە.
- وردەکاریی ئەم سنوورانە لە ڕاپۆرتی پشکنینی Course 4 تۆمار کراون؛ هیچ یەکێک بە خەیاڵ چاک نەکراوە و دەقی خاو پارێزراوە.


### یەکسانکردنی شیکاریی پێڕستەکان لە وانەکانی 37، 38 و 46 — 2026-11-08
- لە نموونەی لێکدراوی ئاڵۆزدا ناونانی دوو پێڕستەی سەربەخۆی هاوئاست بە «پێڕستەی سەربەخۆی هاوئاستی یەکەم/دووەم» یەکگرتوو کرا؛ «سەرڕستە» وەک ئەرکی پێڕستە لە ڕستەی ئاڵۆزدا لە «سەربەخۆ» جیا کراوەتەوە.
- Markdownی وانەکانی 37، 38 و 46، Structured Review و Preservation Bundle نوێ کرانەوە. دەقی خاو و runtime نەگۆڕدراون؛ پەسەندکردن و چالاککردن نەکراوە.


### ڕوونکردنەوەی جیاوازیی «سەربەخۆ» و «سەرڕستە» لە وانەی 46 — 2026-11-08
- لە خشتەی چوار جۆری ڕستەدا «پێڕستەی سەربەخۆ» وەک تایبەتمەندیی پێڕستە و «سەرڕستە» وەک ئەرکی پێڕستە لە ڕستەی ئاڵۆزدا لە یەکتر جیا کرانەوە؛ بەمەش ناونانی دوو پێڕستەی سەربەخۆی هاوئاست لە نموونەی Compound-complex لەگەڵ خشتەی پۆلێنکردندا یەکدەگرێتەوە.
- Markdownی وانەی 46، source_markdownی Structured Review و content_markdownی Preservation Bundle هاوتا نوێ کرانەوە. دەقی خاو و runtime نەگۆڕدراون.


### جیاکردنەوەی Independent و Main Clause لە وانەی ٤٦ — 2026-11-08
- خشتەی چوار جۆری ڕستە نوێ کرایەوە تا «سەربەخۆ» وەک تایبەتمەندیی پێڕستە و «سەرڕستە» وەک ئەرکی پێڕستە لە ڕستەی ئاڵۆزدا جیا بن؛ نموونەکانی Compound و Compound-complex دوو پێڕستەی سەربەخۆی هاوئاست بە یەک شێوە ناودەبن.
- Markdown، Structured Review و Preservation Bundle هاوتا کراون؛ دەقی خاو و runtime نەگۆڕدراون.


### یەکسانکردنی پێناسەی ڕستەی لێکدراوی ئاڵۆز لە وانەی 38 — 2026-11-08
- لە پێناسەی وانەی 38دا «دوو سەرڕستەی سەربەخۆ» بە «دوو پێڕستەی سەربەخۆی هاوئاست» گۆڕدرا؛ چونکە «سەربەخۆ» تایبەتمەندیی پێڕستەیە و «سەرڕستە» ئەرکی ئەو پێڕستەیە لە پەیوەندیی ژێرڕستەیی. ئەمە لەگەڵ وانەی 37 و 46 یەکدەگرێتەوە.
- Markdownی وانەی 38، source_markdownی Structured Review و content_markdownی Preservation Bundle هاوتا نوێ کرانەوە؛ دەقی خاو و runtime نەگۆڕدراون.


### نوێکردنەوەی وانەی 46 — 2026-11-08
- ناونانی «یەکەم سەرڕستە» لە شیکاریی نموونەی لێکدراوی ئاڵۆز بە «پێڕستەی سەربەخۆی هاوئاستی یەکەم» گۆڕدرا؛ `key_points[7]`ی Structured Review لە Markdownی نوێ وەرگیرا و Preservation Bundle لەگەڵ دەقەکە هاوتایە.
- دەقی خاو و runtime نەگۆڕدراون؛ هیچ پەسەندکردن یان چالاککردنێک نەکراوە.


### پشکنینی دووبارەی Structured Review — 2026-11-08
- لە پشکنینی 15 ڕەشنووسی 32–46دا، هەموو 15 `source_markdown` لەگەڵ Markdownی هاوتایان یەکسانن؛ هەموو 225 `key_points` بە تەواوی وەک دەقی هەمان وانە لە Markdownدا هەن.
- سێ خاڵی کۆن لە key_pointsی وانەکانی 37، 38 و 46 نوێ کرانەوە لە بەشی هاوتای Markdown؛ هەموو 15 وانەکە دووبارە پشکنران و هیچ ناهاوتاییەک نەما.
- Preservation Bundle بۆ هەر 15 وانە لەگەڵ Markdownی ڕەشنووسەکان یەکسانە؛ دەقی خاو و runtime نەگۆڕدراون و هەموو وانەکانی 32–46 pending owner review ـن.


### جیاکردنەوەی Independent Clause و Main Clause لە وانەی 46 — 2026-11-08
- «سەربەخۆ» وەک تایبەتمەندیی پێڕستە و «سەرڕستە» وەک ئەرکی پێڕستە لە پەیوەندی بە بەرڕستەوە جیا کرانەوە؛ ڕاهێنانی چوارەمیش بە «دوو پێڕستەی سەربەخۆی هاوئاست + بەرڕستە» ڕوون کرا.
- Markdown، Structured Review و Preservation Bundle نوێ کرانەوە؛ دەقی خاو و runtime نەگۆڕدراون و وانەکە pending owner review ـە.


### دۆخی PR و جیاوازیی main — پشکنینی 2026-11-08 16:xx UTC
- PR #119 هێشتا open و Draft ـە، merged نییە؛ API دۆخی `mergeable=false` و `mergeable_state=dirty` دەگەڕێنێتەوە.
- `main` لە SHAی `4affb750244daebd1d13f886ef3c5a1d1efad79f` و branch لە کۆتایی ئەم پشکنینەدا لە `cad08c6b94cbdd3e9fa3b53305d26e19e3e2c515` بوو؛ بەراوردی main...branch دۆخی diverged و 3 commitی mainی پێش branch نیشان دەدات.
- ئەم دۆخە بەڵگەی conflict/mergeability blocker ـە؛ PR بە خۆکار merge ناکرێت و هیچ deploymentێک پشتڕاست نەکراوەتەوە. چاکسازییەکانی ڕەشنووس لە branch پارێزراون؛ بۆ چارەسەری merge conflict پێویستە فایلە هاوبەشەکانی main و branch بە وردی یەکلا بکرێنەوە، نەک branch overwrite بکرێت.


### چاکسازیی سەرچاوەیی لە وانەی 46 — 2026-11-08
- نموونەی بەرڕستەی تەواوکەر «دەزانم کە تۆ ڕاست دەکەیت» کە لە دەقی خاوەنی وانەی 46دا نەبوو، بە نموونەی خاوەنی «دەزانم کە ئەو ئەمڕۆ دێت» گۆڕدرا.
- Markdownی وانەی 46، Structured Review، Preservation Bundle و Terminology Audit هاوتا نوێ کرانەوە؛ دەقی خاو و runtime نەگۆڕدراون.
- کۆمیتی زنجیرەیی دواهەم: `65b328016a1024fb9b13ede16a778f9a036c181d`. CI بۆ ئەم زنجیرەیە لە کاتی نووسینی ئەم تۆمارەدا هێشتا `in_progress` بوو.
- PR #119 هێشتا Draft و `mergeable_state=dirty` ـە؛ merge و deployment نەکراوە.


### نوێکردنەوەی reconciliationی mainline — 2026-11-08
- پشکنینی ناوی test method ـەکان بە وردی نوێ کرا: main 48 method و branch 65 method هەیە؛ 4 ناوی method (6 occurrence بەهۆی دووبارەبوونەوە)ی تایبەت بە 26 وانە لە branch بە تاقیکردنەوەی هاوتای گونجاو بە 46 وانە گۆڕدراونەوە. ناوی literal هەموویان هاوتا نییە، بەڵام پشکنینەکانی ژمارە، catalog، plan و pagination بۆ 46 نوێ کراونەوە.
- فایلەکەی توێژینەوەی وانەی 26 لە main و branch بە تەواوی هاوتایە؛ JSONی main 26 وانە و JSONی branch 46 وانەیە و overwrite ناکرێت.
- PR #119 هێشتا Draft و dirty/mergeable=false ـە؛ چاکسازیی ناوەڕۆک و CI سەرکەوتوون، بەڵام conflictی Git چارەسەر نەکراوە و deployment پشتڕاست نەکراوەتەوە.


### پشکنینی وردی تاقیکردنەوەی mainline — 2026-11-08
- main: 48 test method declaration؛ branch: 65. چوار ناوی جیاوازی main کە ژمارەی 26یان تێدایە (6 occurrence بەهۆی duplicate declaration) بە assertionی گونجاو بە 46 وانە لە branchدا جێگۆڕکێیان بۆ کراوە.
- تاقیکردنەوەی نوێی main بۆ ژمارەی پێکهاتەکانی وانەکانی 1–26 لە branchدا بە `test_mainline_first_26_lessons_keep_full_learning_component_counts` پارێزراوە؛ تاقیکردنەوەی expansion بۆ 46 وانەش زیادە.
- ناوی literalی تاقیکردنەوەکان هاوتا نییە، بەڵام assertionەکان بەپێی ژمارەی نوێ گونجێنراون. JSONی 26 وانەی main نابێت overwriteی JSONی 46 وانەی branch بکات.
- CIی گۆڕانکارییەکانی پشکنینەکانی دواهەم success ـە؛ PR #119 هێشتا Draft و `mergeable_state=dirty` ـە، merge/deployment نەکراوە.


### دیاریکردنی سەرچاوەی conflict ـی PR #119 — 2026-11-08
- سێ فایل لە main و branch conflict ـی mergeability دروست دەکەن: `course_data/grammar_course4_lessons.json`, `tests/test_course4_grammar_runtime.py`, `docs/COURSE4_LESSON26_PARTICLES_RESEARCH.md`.
- researchی وانەی 26 لە هەردوو branch یەکسانە؛ test assertions بۆ 46 وانە لە branch گونجێنراون؛ JSONی 26 وانەی main و JSONی 46 وانەی branch پێویستیان بە reconciliationی field-by-field هەیە. overwriteکردنی هەر یەکێکیان قەدەغەیە تا ناوەڕۆکەکان بە وردی یەکلا نەکرێنەوە.
- هیچ merge/rebase/overwrite/deploymentێک لەم قۆناغەدا نەکراوە. PR open/Draft و dirty ـە.


### JSON reconciliation detail — 2026-11-08
- 1–26: both versions have 26 lessons and 208 quiz questions; Activities 78, Exercises 130, Comprehension 260 in both. Main vs branch: Examples 170/181, Appendix 189/216, Key points 235/262.
- Quiz comparison: 185 option-order/answer-index permutations, 14 question-text differences, 21 option-set differences, 13 correct-answer-text differences, 17 explanation differences. No lesson lacks its 8 questions. These differences are not automatically errors; keep them in audit queue pending source-grounded review.
- Lesson 3 has 134 differing field paths and branch contains expanded content; do not overwrite. Lesson 2/19/20 term differences mainly Preposition `پریپۆزیشن` vs `پێشبەند`; project register keeps `پێشبەند`. Lesson 16 uses `بنج` in branch consistent with course register.
- Full detail in `COURSE4_MAINLINE_DIVERGENCE_RECONCILIATION_2026-11-08.md`.

# تۆماری جیاوازیی main و برانچی کۆرسی ٤ — 2026-11-08

## مەبەست
ئەم تۆمارە بۆ پاراستنی هەردوو ڕێڕەوی کارە؛ هیچ ناوەڕۆکی runtime بەهۆی ئەم تۆمارەوە لەسەر یەک نانووسرێتەوە.

## بەڵگەی Git
- برانچی کار: `feat/course4-clean-port-main-20261106`
- PR: #119 (Draft؛ merge نەکراوە)
- کۆمیتی کۆتاییی برانچ لە کاتی پشکنین: `1fbfd22d42dd87359177e925adf8deb7ed11fcbe`
- کۆمیتی main لە کاتی پشکنین: `4affb750244daebd1d13f886ef3c5a1d1efad79f`
- بەراوردی Git: `diverged`؛ برانچ 884 کۆمیت لەپێش و 3 کۆمیت لەپاش main بوو.
- فایلە هاوبەشە جیاوازەکان لە کۆمیتە نوێکانی main: `course_data/grammar_course4_lessons.json`، `tests/test_course4_grammar_runtime.py`، `docs/COURSE4_LESSON26_PARTICLES_RESEARCH.md`.

## دۆخی ناوەڕۆکی وانەکان
- main: 26 وانە.
- برانچی کار: 46 وانە (1–31 structured؛ 32–46 ڕەشنووسی خوێندنەوەی تاقیکاری).
- بەراوردی خانەکانی وانەکانی 1–26: ئەم وانانە لە خانەیەک یان زیاتر جیاوازن:
- وانەی 1: quiz
- وانەی 2: key_points، examples، exercises، comprehension، quiz، appendix
- وانەی 3: title، objective، key_points، examples، activities، exercises، comprehension، quiz، appendix
- وانەی 4: quiz
- وانەی 5: quiz، appendix
- وانەی 6: quiz
- وانەی 7: quiz
- وانەی 8: examples، exercises، comprehension، quiz
- وانەی 9: quiz
- وانەی 10: examples، activities، exercises، quiz
- وانەی 11: key_points، quiz، appendix
- وانەی 12: quiz
- وانەی 13: objective، key_points، examples، activities، exercises، comprehension، quiz، appendix
- وانەی 14: examples، comprehension، quiz
- وانەی 15: key_points، examples، quiz، appendix
- وانەی 16: title، objective، key_points، examples، activities، exercises، comprehension، quiz، appendix
- وانەی 17: key_points، quiz
- وانەی 18: quiz
- وانەی 19: key_points، examples، exercises، quiz، appendix
- وانەی 20: objective، key_points، examples، activities، exercises، comprehension، quiz، appendix
- وانەی 21: quiz
- وانەی 22: key_points، examples، exercises، quiz
- وانەی 23: key_points، examples، activities، exercises، comprehension، quiz، appendix
- وانەی 24: activities، quiz
- وانەی 25: key_points، quiz
- وانەی 26: quiz، appendix
- وانەی 3 لە برانچی کاردا فراوانکراوە (15 نموونە و 30 پاشکۆ)؛ وەشانی main ئەو فراوانکردنەی تێدا نییە. بۆیە نابێت بە جێگۆڕکێی خۆکارانە وەشانی main لە شوێنی branch دابنرێت.
- هەندێک جیاوازیی quiz و appendix لە وانەکانی 1–26 هەیە؛ پێویستیان بە reconciliationی خانە بە خانە و پشکنینی ناوەڕۆک هەیە.

## پشکنینی تاقیکردنەوەکان
- فایلەکەی main: 48 test method.
- فایلەکەی برانچ: 64 test method.
- زۆربەی تاقیکردنەوەکانی هاوبەش لە هەردوو لا هەن؛ ناونیشانی تاقیکردنەوەکانی ژمارەی 26 لە برانچدا بۆ 31/46 گۆڕدراون و تاقیکردنەوەی وانەکانی 27–31 و پێشاندانی 46 وانە زیاد کراون.
- تاقیکردنەوەی CI بۆ کۆمیتە نوێکانی برانچ هێشتا نەگەیشتووە؛ هیچ سەرکەوتنی CI پشتڕاست نەکراوەتەوە.

## پاراستنی بەڵگە
وەشانی mainی پەڕگە سەرەکییەکان بە شێوەی snapshot لە تەنیشت ئەم تۆمارەدا پارێزراون:
- `MAINLINE_COURSE4_LESSONS_01_26_SNAPSHOT_2026-11-08.json`
- `MAINLINE_COURSE4_RUNTIME_TESTS_SNAPSHOT_2026-11-08.py`
- `MAINLINE_COURSE4_LESSON26_PARTICLES_RESEARCH_SNAPSHOT_2026-11-08.md`

## بڕیاری پاراستن
- ناوەڕۆکی برانچی 46 وانەیی لە شوێنی خۆی دەمێنێتەوە.
- وەشانی mainی 26 وانەیی و تاقیکردنەوە و توێژینەوەکەی بە snapshot پارێزراون.
- هیچ merge، deployment یان overwriteی runtime ئەنجام نەدراوە.
- هەنگاوی داهاتوو: پشکنینی خانە بە خانەی جیاوازییەکان، بەتایبەتی quiz و appendix؛ پاشان چارەسەرکردنی 3 کۆمیتی دواوەی main بەبێ لەدەستدانی وانەکانی 27–46.


---

## نوێکردنەوەی پشکنین — 2026-11-08، دوای کۆمیتەکانی CI

### دۆخی نوێی Git و CI
- کۆمیتی برانچ لە کاتی ئەم نوێکردنەوەیە: `8a355b75893376f35ffbd5c1c5a39f212c3492dd`.
- کۆمیتی `main`: `4affb750244daebd1d13f886ef3c5a1d1efad79f`.
- برانچ 905 کۆمیت لەپێش و 3 کۆمیت لەپاش `main` ـە؛ دۆخی compare هێشتا `diverged` ـە.
- PR #119 کراوە و Draft ـە؛ merge نەکراوە و `mergeable=false`.
- CI بۆ کۆمیتی نوێ `8a355b7` لە Run `42482096097` سەرکەوتووە؛ `compileall` و `unittest discover` هەردووکیان تەواو بوون.

### پشکنینی وردی سێ کۆمیتەکەی main
1. `b38e707` — زیادکردنی بەڵگەی توێژینەوەی وانەی ٢٦. وەشانی `docs/COURSE4_LESSON26_PARTICLES_RESEARCH.md` لە برانچی کاردا لەگەڵ main هاوتا کراوەتەوە؛ وەشانی پێشووی برانچیش لە snapshot پارێزراوە.
2. `676131a` — پاراستنی شێوازی جێگیری ڕاهێنان و تێگەیشتن. ناوی هەموو 48 تاقیکردنەوەی main بەراورد کرا؛ 6 ناوی کۆنی تایبەت بە 26 وانە لە شێوازی 31/46 وانەدا جێگایان گرتووەتەوە. دوو تاقیکردنەوەی نوێ زیاد کراون بۆ پشتڕاستکردنەوەی ژمارە و پێکهاتەی وانەکانی 1–26 و دۆخی ڕەشنووسی 32–46.
3. `4affb75` — زیادکردنی تاقیکردنەوەی پێکهاتەی وانەکان؛ لە برانچدا بە دوو تاقیکردنەوەی گونجاو بە مۆدێلی 46 وانە جێبەجێ کراوە.

### بڕیاری پاراستنی JSON
- JSONی main تەنها 26 وانەیە؛ JSONی برانچ 46 وانەیە.
- بەراوردی خانە بە خانە نیشانی دا هەموو 26 وانە لە لانیکەم خانەیەکدا جیاوازن؛ جیاوازییەکان تەنها metadata نین و پێویستیان بە پشکنینی ناوەڕۆک هەیە.
- لە وانەی 3دا وەشانی برانچ 15 نموونە و 30 پاشکۆی هەیە، بەرامبەر 4 نموونە و 4 پاشکۆ لە main. بۆیە وەشانی فراوانکراوی برانچ بەبێ بڕیاری خاوەن پڕۆژە نابێت بسڕدرێتەوە یان بە وەشانی main بگۆڕدرێت.
- لە وانەکانی 1–26دا ژمارەی خانەکانی ڕاهێنان و تێگەیشتن بە گشتی هاوشێوەیە؛ بەڵام جیاوازیی quiz و appendix و ناوەڕۆکی هەندێک خانە هەر ماوە.
- بڕیاری ئێستا: سێ کۆمیتەکەی main بە شێوەی blind cherry-pick یان overwrite ناخرێنە ناو برانچ. snapshotەکان و تاقیکردنەوە هاوتاکان بەڵگەی پاراستنن؛ reconciliationی ناوەڕۆکی JSON هێشتا کارێکی جیاوازە.

### زیادەیەکی پاراستنی ڕەفتاری بۆت
- منووی تاقیکردنەوەکان ئێستا تاقیکردنەوەی وانەی تەواوکراو بەڵام هێشتا پەسەندنەکراو نیشان نادات؛ تەنها ئەو تاقیکردنەوانە دەردەکەون کە `quiz_is_available` ڕێگەیان پێدەدات.
- دوو تاقیکردنەوەی نوێ ئەم سنوورە دەپشکنن؛ CIی کۆمیتی `8a355b7` سەرکەوتووە.


## نوێکردنەوەی وردی ناوی تاقیکردنەوەکان و دۆخی merge — 2026-11-08، پشکنینی دواهەم

### ژمارە و ناوی test method ـەکان
- لە وەشانی ئێستای `main`دا 48 `test_...` method هەیە؛ لە branch ـدا 65 method هەیە.
- بەراوردی ناوەکان نیشانی دا 4 ناوی جیاواز هەن کە بە شێوەی کۆن لە main ـدا ماونەتەوە؛ هەندێکیان بە دووبارە لە چەند TestCase ـدا هاتوون، بۆیە ژمارەی occurrence ـی ناهاوتا 6 ـە:
  - `test_course4_is_active_with_twenty_six_lessons` → `test_course4_is_active_with_forty_six_lessons`؛ پشکنینی active بودن، ڕیزبەندی و کویزەکان هێشتا هەیە، بە ژمارەی نوێی 46.
  - `test_course4_catalogs_register_26_lessons_without_changing_other_courses` → `test_course4_catalogs_register_31_lessons_without_changing_other_courses`؛ پشکنینی catalog/plan/source و پاراستنی کۆرسەکانی تر هەیە، بە ڕیزبەندیی 46 وانە.
  - `test_course4_has_26_registered_lessons` (3 occurrence) → `test_course4_has_31_registered_lessons` (3 occurrence)؛ هەمان پشکنینی ID ـەکان و plan/catalog بە ژمارەی گونجاو نوێ کراوەتەوە.
  - `test_course4_has_26_lessons_and_plan_records_lesson_26` → پشکنینی نوێی `test_course4_has_46_lessons_and_plan_records_lesson_28` و `test_course4_has_46_registered_lessons_and_pagination_reaches_lesson_46`؛ پشکنینی count و گەیشتن بە وانەی کۆتایی بۆ مۆدێلی 46.
- بۆیە ناوی method ـەکان هەموویان بە هەمان literal name نەماون؛ بەڵام پشکنینە کۆنەکانی 26 وانە بە پێی مۆدێلی 46 وانە نوێنراونەوە. ئەمە بە مانای کۆپییەکی ناوی تاقیکردنەوە نییە؛ بە مانای گۆڕینی assertion ـی ژمارەی وانەی کۆرسە.

### پشکنینی سێ فایلە جیاوازەکە و mergeability
- `docs/COURSE4_LESSON26_PARTICLES_RESEARCH.md` لە main و branch بە تەواوی هاوتایە (SHA: `872af3a86e90f84fc19bc10bf897b0a108476369`).
- `course_data/grammar_course4_lessons.json` لە main 26 وانە و لە branch 46 وانەیە؛ وەشانەکان جیاوازن و نابێت بە overwrite یەکێک لەناو ببرێت.
- `tests/test_course4_grammar_runtime.py` لە main 48 و لە branch 65 test method ـی هەیە؛ assertion ـەکانی 26 وانە لە branch بۆ مۆدێلی 46 وانە گونجێنراونەوە.
- `main` لە `4affb750244daebd1d13f886ef3c5a1d1efad79f` و branch لە `909ce146e10ffa6ee977022bd9d9f6680edba9c2` بوو لە کاتی پشکنین؛ compare دۆخی diverged و 3 commitی mainی پێش branch نیشان دا.
- PR #119 هێشتا open/Draft و `mergeable=false`, `mergeable_state=dirty` ـە؛ CI بۆ نوێکردنەوەکانی ئەم پشکنینە سەرکەوتووە، بەڵام ئەمە conflictی Git یان deployment چارەسەر ناکات.
- بڕیاری پاراستن: هیچ JSONێک overwrite نەکرێت؛ تا reconciliationی سەرچاوەیی و خانە بە خانە تەواو نەبێت، PR بە خۆکار merge/deploy ناکرێت.


## پشکنینی وردی تاقیکردنەوەکانی main و branch — 2026-11-08
- پشکنینی ناوی test method ـەکان بە regex و خوێندنەوەی body ئەنجام درا: main 48 method declaration و branch 65 هەیە. لە mainدا 4 ناوی جیاواز کە 26 وانەیان چاوەڕوان دەکەن، بە 6 occurrence دووبارەبوونەوەیان هەیە؛ لە branchدا ناوی literal ـەکان نییە، چونکە assertion ـەکانیان بۆ مۆدێلی 46 وانە گونجێنراون.
- `test_course4_is_active_with_twenty_six_lessons` هاوتای گونجاوی `test_course4_is_active_with_forty_six_lessons` هەیە.
- `test_course4_catalogs_register_26_lessons_without_changing_other_courses` و سێ occurrence ـی `test_course4_has_26_registered_lessons` بە تاقیکردنەوەکانی 46 وانە و هەڵنەگۆڕانی کۆرسەکانی تر، لەگەڵ `test_course4_has_46_registered_lessons_and_pagination_reaches_lesson_46`، گونجێنراون.
- `test_course4_has_26_lessons_and_plan_records_lesson_26` بە `test_course4_has_46_lessons_and_plan_records_lesson_28` و تاقیکردنەوەی 46 وانە/plan/catalog هاوتای گونجاوی هەیە؛ تاقیکردنەوەی 46 وانە بە pagination تا وانەی 46یش هەیە.
- تاقیکردنەوەی نوێی main لەسەر `activities=3`, `exercises=5`, `comprehension=10`, `quiz=8` بۆ وانەکانی 1–26 لە branchدا بە `test_mainline_first_26_lessons_keep_full_learning_component_counts` پارێزراوە؛ تاقیکردنەوەی `test_course4_expansion_preserves_first_26_and_marks_only_new_drafts_pending`یش هەڵگری پەیوەندیی 1–46 و review status ـە.
- بڕیار: ناوی method ـەکان بە خۆکار کۆپی نەکرێن، چونکە چەند ناو دووبارەن و assertion ـی 26 لە مۆدێلی 46دا هەڵە دەبێت. لە ئێستادا بەڵگەی تاقیکردنەوەیی بۆ ئەو جیاوازییانە هەیە؛ JSONی 26 وانەی mainیش نابێت بەسەر JSONی 46 وانەی branchدا overwrite بکرێت.
- پشکنینی سێ فایل: researchی وانەی 26 لە main و branch بە تەواوی یەکسانە؛ JSON جیاوازیی 26/46 وانەی هەیە؛ test file جیاوازییەکانی لەسەر ژمارەی کۆرس و پشکنینە تایبەتەکان هەیە. CIی گۆڕانکارییەکانی دواهەم success ـە، بەڵام PR #119 هێشتا Draft و `mergeable_state=dirty` ـە.


## دیاریکردنی فایلە conflict ـدارەکانی PR #119 — 2026-11-08
- لە سێ commitی main، هەر یەک فایلێکی هاوبەشیان زیاد کردووە: `course_data/grammar_course4_lessons.json`، `tests/test_course4_grammar_runtime.py` و `docs/COURSE4_LESSON26_PARTICLES_RESEARCH.md`. چونکە branchیش ئەم فایلانەی لە merge-base ـەوە بە جیاوازی هەیە، PR لە دۆخی `dirty` ـدایە.
- فایلەی researchی وانەی 26 لە main و branch بە تەواوی identical ـە؛ conflict ـی ناوەڕۆکیی ئەم فایلە لە دوو وەشاندا نییە و branch لە commitی پێشوودا sync کراوە.
- فایلەی test لە main بە 48 method declaration و branch بە 65 method declaration هەیە. ناو و assertion ـەکانی ژمارەی 26 لە branch بە مۆدێلی 46 وانە گونجێنراون؛ تاقیکردنەوەی component countsی 1–26 و pagination تا 46 هەیە. ناوی method ـەکان بە خۆکار کۆپی ناکرێن.
- فایلەی JSON conflict ـی سەرەکیی ماوە: main 26 وانە و branch 46 وانەیە. Main commit `676131a619c749eaac5da80e715d2ac0ef161a69` فایلەکەی بە schemaی نوێ زیاد کردووە؛ branchیش پەرەپێدانی تایبەتیی خۆی، وانەی 3ی فراوانکراو و وانەکانی 27–46ی تێدایە. نابێت هیچ‌کام بە overwrite لەناو بچێت. پێویستە پێکهاتەکانی 1–26 بە وردی field-by-field و source-by-source یەکلا بکرێنەوە و 27–46 لە branch بمێننەوە.
- ئەم پشکنینە conflict ـەکان دیاری کردووە، بەڵام هیچ merge/rebase یان overwriteێک نەکراوە. PR #119 هێشتا Draft و `mergeable=false/dirty` ـە؛ deployment نەکراوە.

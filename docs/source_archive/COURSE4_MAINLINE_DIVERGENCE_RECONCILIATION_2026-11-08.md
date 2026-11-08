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

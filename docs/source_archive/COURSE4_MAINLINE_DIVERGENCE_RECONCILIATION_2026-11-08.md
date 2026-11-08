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

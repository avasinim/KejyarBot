# پشکنینی ساختاریی بانکەی کویزی کۆرسی ٤
**بەروار:** 2026-11-09  
**شێواز:** پشکنینی staticی JSON و adapter/test لە `main`.

## سەرچاوە و SHA
- `course_data/grammar_course4_lessons.json`: `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`
- `course_lesson_adapters.py`: `124cd04e8b1068467982db35faf9f11fdd41a1af`
- `bot.py`: `08dd6a9e8b0b21470f5b6e094ccbf48560312339`
- `tests/test_course4_grammar_runtime.py`: `7437d63769e68fc4af01c5a829be13bb5cc7111a`

## ئەنجامی پشکنینی ساختاری
- ژمارەی وانەکان: 46.
- وانەی structured quiz: 31 (وانە 1–31).
- ژمارەی پرسیارە structured ـەکان: 248 (8 بۆ هەر وانەی 1–31).
- وانەی pending review: 15 (وانە 32–46)، هەموویان structured quizیان بەتاڵە.
- هەڵەی schema لە 248 پرسیاردا: 0.
- دووبارەبوونی دەقی پرسیار لە ناو هەمان وانەدا: 0.
- هەر پرسیارێک 4 هەڵبژاردەی جیاواز، answer indexی integer و لە سنووردا، و explanationی بەتاڵنەبووی هەیە.
- تاقیکردنەوەی Course4 لە sourceدا هاوسەنگی answer index دەخوازێت: بۆ هەر وانە 2 وەڵامی دروست لە هەر یەک لە indexەکانی 0–3.

## گرنگ: جیاوازیی ساختار و دروستیی زانستی
ئەم پشکنینە تەنها دروستیی schema و یەکسانیی داتای پرسیار دەسەلمێنێت؛ **دروستیی زانستیی هەموو 248 پرسیار، گونجانی هەر پرسیار بە بابەتی وانە، و پشتگیریی وەڵامی دروست لە دەقی وانە بە شێوەی semantic هێشتا بە وردی پشکنین نەکراوە.** ژمارەی یەکسانی وەڵامەکانیش بە تەنها نیشانەی دروستیی پرسیار نییە.

## پەیوەندی بە runtime
- Adapter، `q`، `options`، answer index و explanation validate دەکات و answer index دەگۆڕێت بۆ دەقی هەڵبژاردەی دروست.
- `bot.py` structured quizەکان بۆ `QUIZ_DATA` بار دەکات.
- بۆ وانە 32–46، `source_markdown` هەیە بەڵام structured quiz نییە؛ runtime quiz بۆیان بەتاڵە. Testی Course4 ئەم دۆخە بە ئاشکرا پشتڕاست دەکات.
- Startup validation بە ئاشکرا quizی ونبوو بۆ وانەی grammar لە دۆخی pending review قبووڵ دەکات؛ ئەمە هۆکاری جیاوازیی 31 وانەی quizدار و 15 وانەی pending ـە، نەک هەڵەی schema.

## پێشنیاری قۆناغی semantic review
1. 248 پرسیار بە وانە و بەش/ئامانجی فێرکارییەوە map بکرێن.
2. بۆ هەر وەڵامێک بەڵگەی ناو دەقی وانە یان سەرچاوەی زانستی دیاری بکرێت.
3. هەڵبژاردە هەڵەکانیش بە هۆکاری زانستی هەڵەبوونیان پشکنین بکرێن؛ distractor نابێت لە ڕووی زمانەوانییەوە ڕاست بێت.
4. پرسیارەکان لە ڕووی ئاست، ambiguity، dialect و orthography پشکنین بکرێن.
5. هیچ quizێک بۆ وانە 32–46 زیاد نەکرێت تا وانەکە پەسەند نەکراوە و content/answer key پشتڕاست نەکراوەتەوە.

## سنووری کار
هیچ test suiteێک جێبەجێ نەکرا؛ ئەنجامە ژمارەییەکان لە parse و static scanی JSON ـەوە هاتوون. هیچ quiz، lesson، database، main branch، Botkeep یان Telegram دەستکاری نەکرا.

# کۆرسی ٤ — کاندیدی تێکخستنی کویزی ١٩ وانەی Beta، خولی ٩٥
**بەروار:** 2026-11-10

## ١. فایل
`docs/source_archive/staging/drafts/COURSE4_LESSONS_QUIZ_INTEGRATED_CANDIDATE_V1_2026-11-10.json`

SHAی blob دوای fetch:
`b9259a914f9a05a936cfe63659fa099ee33af8c1`

## ٢. شێوازی دروستکردن
- وەک بنەما، فایلی سەرەکیی `course_data/grammar_course4_lessons.json` بە SHAی `fd8dfbde7e6937841214cacac653ef10d0c6097d` خوێندرایەوە.
- تەنها فیلدی `quiz` بۆ وانەکانی ٣٢–٥٠ لە پاشکۆی structured quiz V3 وەرگیرا و پڕ کرا.
- هیچ فیلدێکی دیکەی وانە، ئامانج، key_points، examples، exercises، comprehension، source_markdown، review_status یان metadata نەگۆڕدرا.
- فایلی سەرەکی overwrite نەکرا؛ کاندیدەکە لە پاشکۆی stagingدا جیاوازە.

## ٣. ئەنجامی diff و validation
- وانەکان: ٥٠.
- کویزی پێشوو: ٢٤٨.
- کویزی زیادکراو بۆ Beta: ٩٥.
- کۆی کویزی candidate: ٣٤٣.
- وانەی گۆڕانکاری‌پێکراو: تەنها ١٩ وانەی ٣٢–٥٠.
- جیاوازیی هیچ فیلدێکی دیکە: ٠.
- هەڵەی schemaی کویز: ٠.
- هەڵەی answer index: ٠.
- دۆخی ١٩ وانەکە هەر `owner_review_pending_expanded_draft` ماوەتەوە؛ بە پەسەندکراو ناگۆڕدرێن.

## ٤. دەرئەنجام
ئەمە کاندیدی تاقیکردنەوەییە بۆ دڵنیابوون لەوەی ١٩ کویز بە شێوەی schemaی runtime لەگەڵ ٣١ وانەی پێشوو پێکەوە دەگونجێن. بەڵام هێشتا پشکنینی مانایی و distractorەکان، reviewی وانەکان، و تاقیکردنەوەی loader/adapter/runtime پێویستە. هیچ deployment یان activation ئەنجام نەدراوە؛ هیچ source JSON و runtime نەگۆڕدراوە.

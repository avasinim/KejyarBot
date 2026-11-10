# کۆرسی ٤ — تۆماری کۆتاییی پێکهاتە و گەیتەکانی چالاککردن، خولی ٩٢
**بەروار:** 2026-11-10  
**فایلی وانەکان:** course_data/grammar_course4_lessons.json — SHA: fd8dfbde7e6937841214cacac653ef10d0c6097d.  
**فایلی quiz override:** course_data/grammar_course4_quiz_overrides.json — SHA: d1d264a1831de98e8d9bfe7978e94bf462ee33a2.

## ١. دۆخی پشتڕاستکراوی پێکهاتە
- کۆی وانەکان: ٥٠.
- وانەکانی ١–٣١: ٣١ وانە؛ هەر وانە ٨ پرسیاری quizی هەیە؛ کۆی گشتی ٢٤٨ پرسیار.
- ژمارەی examples لە JSON: ٢٢١.
- ژمارەی exercises لە JSON: ٣٧٤.
- ژمارەی comprehension items: ٣٢٥.
- quiz override: ٥٠ دانە لە ٢٣ وانەدا؛ هەر overrideێک original_snapshot و replacementی هەیە.
- وانەکانی ٣٢–٥٠: ١٩ وانە لە دۆخی owner_review_pending_expanded_draft.

## ٢. کێشەی گەیتەکانی وانەکانی ٣٢–٥٠
لە هەموو ١٩ وانەی Betaدا:
- examples array بەتاڵە.
- quiz array بەتاڵە.
- ناوەڕۆکی وانەکان زۆرجار لە source_markdown یان key_pointsی یەک ئەندامدا هەڵگیراوە؛ بۆیە بوونی دەق بە مانای ئامادەبوونی structured lesson data نییە.

لە وانەکانی ٤٧–٥٠دا:
- key_points بەتاڵە.
- examples بەتاڵە.
- exercises بەتاڵە.
- comprehension بەتاڵە.
- quiz بەتاڵە.
- زۆربەی ناوەڕۆک لە source_markdownدا هەڵگیراوە؛ پێویستی بە گواستنەوەی schemaیی و پشکنینی سەربەخۆ هەیە.

لە وانەکانی ٣٢–٤٦دا exercises و هەندێک comprehension هەن، بەڵام examples و quiz arrays بەتاڵن.

## ٣. ئەنجامی گرنگ
٢٤٨ پرسیاری quizی وانەکانی ١–٣١ پارێزراون؛ ئەمە بە مانای ئەوە نییە کە ١٩ وانەی دواتر quizیان ئامادەیە. پێش چالاککردنی تەواوی کۆرسی ٤ دەبێت:
1. ١٩ وانەی Beta پشکنینی زانستی و زاراوەیییان تەواو بکرێت.
2. نموونە و quiz لە source_markdown بگوازرێنەوە بۆ فیلدە structuredەکان؛ هیچ ناوەڕۆکێک نابێت بسڕدرێتەوە.
3. کلیلی ٥٠ quiz override لەگەڵ وەشانی کۆتاییی وانەکان دووبارە پشکنرێتەوە.
4. schema، loader، adapter و runtime safety tests بە فایلی کۆتایی تاقی بکرێنەوە.
5. پاش ئەوە stagingی Botkeep و PR #125 بەڵگەدار بکرێنەوە.

## ٤. دۆخی deployment
هێشتا هیچ deployment، merge، گۆڕانکاریی runtime، Botkeep، Telegram یان DB ئەنجام نەدراوە. هەرسێ CIی پێشووی Course 4 سەرکەوتوون، بەڵام ئەوان بە تەنیا گەیتی پەسەندکردنی ١٩ وانەی Beta و structured quiz data ناپڕێنن.

## ٥. بڕیاری پاراستن
هیچ JSONی سەرچاوە overwrite نەکراوە. هەموو ڕەشنووس و پاشکۆکانی خولی ٨٠–٩١ append-only پارێزراون. ئەم ڕاپۆرتە بنەمای ڕوونی بۆ ماوەی کار و گەیتەکانی چالاککردنە.

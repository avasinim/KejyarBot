# پشکنینی بەردەستبوونی کویز و دروستیی هەڵسەنگاندنی کۆرسی ٤
**بەروار:** 2026-11-09  
**شێواز:** static source audit لە `main`؛ هیچ تاقیکردنەوە یان دەستکاریی runtime نەکرا.

## فایلە پشکنراوەکان
- `bot.py`: `08dd6a9e8b0b21470f5b6e094ccbf48560312339`
- `course_quiz_review.py`: `a90890f640ed60341b8e8d2e4c8ca04e6264bf2f`
- `tests/test_bot_quiz_callbacks.py`: `49a1dcb0581a1fecd1bce0a5373caf32068fed3e`
- `course_data/grammar_course4_lessons.json`: `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`

## دۆزینەوەکان
1. `quiz_is_available()` لە `course_quiz_review.py` تەنها لیستی legacyی Course 1 (`وانە_N`) دەپشکنێت. IDی کۆرسی ٤ وەک `grammar_46` لەو لیستەدا نییە؛ بۆیە ئەم guard ـە بە تەنها پەسەندبوونی کویزی Course 4 پشتڕاست ناکات.
2. `start_quiz()` چالاکیی کۆرس و `quiz_is_available()` و بوونی بانک و ڕێڕەوی وانە دەپشکنێت، بەڵام بە شێوەی ڕاستەوخۆ `lesson_is_pending_review()` بانگ ناکات. لەگەڵ ئەوەی وانەکانی 32–46 دۆخی `owner_review_pending_expanded_draft`یان هەیە، ئەگەر بانکێکی کویز بۆیان هەبێت، guardی review لە start بە تەنها پشتڕاست نییە.
3. `quiz_menu_items()` بەردەستبوون و تەواوبوون و `can_open` دەبینێت؛ بەڵام review-statusی وانە بە شێوەی گشتی لێک ناداتەوە. Testی ئێستا تەنها mockی `quiz_is_available` دەکات، نەک دۆخی ڕاستەقینەی pending لە Course 4.
4. `quiz_answer()` پاراستنی callbackی کۆن، duplicate submission، شێوەی نادروستی داتای پرسیار و وەڵامی هەڵبژێردراو هەیە. بەڵام لە کۆتایی کویزدا completion/reward بە DB دەگات بێ ئەوەی review-statusی ئێستای وانە لە هەمان خاڵدا دووبارە بپشکنرێت؛ ئەمە مەترسیی sessionی کۆنە ئەگەر status لە کاتی کویزدا بگۆڕدرێت.
5. هەڵبژاردەی وەڵام لە sourceدا بە index هەڵدەگیرێت و adapter دەبێت شێوەی answerی source بگۆڕێت بۆ شێوەی runtime. پێویستە testی هەموو بانکەکان بڵاو بکرێتەوە بۆ دڵنیایی لە mappingی answer index و options، چونکە شێوەی source و runtime هەمان نییە.
6. لە Course 4 ـدا 15 وانەی 32–46 pending review ـن و structured quizیان لە JSONدا بەتاڵە؛ ئەمە بە مانای ئەوە نییە هیچ quizیەکی markdown لە sourceدا نییە، بەڵکو runtime adapter تەنها structured `quiz` دەخوێنێتەوە. کەواتە quizی تەنها لە Markdown لە runtimeدا بەردەست نابێت.

## پێشنیاری پاراستن
- یاسای یەکگرتووی review guard بۆ هەموو status ـەکانی `owner_review_pending*` لە menu، start، answer-finalization و reward boundary بەکاربهێنرێت.
- Testی واقعی بۆ `grammar_32` و `grammar_46`: menu، start، status-change-mid-quiz و final reward.
- Quiz bank validation بۆ هەموو کۆرسە چالاکەکان: optionsی یەکتا، answer indexی لە سنووردا، explanationی دروست، IDی یەکتا.
- Markdown quiz بەخۆکار وەک quizی runtime دانەنرێت تا mapping و validationی پارێزراوی answer key هەبێت.
- rewardی کویز تەنها لە دوای validationی نوێی review-status و completion authorization بدەدرێت؛ چارەسەری race condition لە ئاستی transaction/DB جیاوازە لە checkی Python.

## سنوور
هیچ unittest، DB، bot، Telegram یان deployment نەجێبەجێکرا. هیچ source، lesson، quiz، reward یا main branch نەگۆڕدرا. ئەم ڕاپۆرتە تەنها audit ـە.

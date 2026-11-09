# کۆرسی ٤ — نەخشەی چاکسازیی پارێزراوی runtime و ماتریسی regression

**بەروار:** 2026-11-09  
**Base:** `main`، کۆدی خوێندراوەی ئێستا  
**پەیوەندی بە پشکنینی پێشوو:** `COURSE4_RUNTIME_SCHEMA_AND_LESSON_ADAPTER_AUDIT_2026-11-09.md`  
**دۆخ:** Design-only / owner review pending. هیچ کۆدێک دەستکاری نەکراوە.

## A. مەبەست و سنوور

ئامانج ئەوەیە هەموو ٤٦ وانە و ناوەڕۆکیان بپارێزرێت و statusی پێداچوونەوە بە هەمان یاسا لە هەموو خاڵەکانی runtimeدا جێبەجێ بکرێت. ئەم نەخشەیە هیچ وانەیەک پەسەند ناکات، هیچ کویزێک دروست ناکات و هیچ deploymentێک ڕێگەپێ نادات.

یاساکانی پاراستن:
1. هیچ خانە یان دەقی سەرچاوەیی لە JSON/Markdown ناسڕدرێتەوە.
2. هیچ statusێک بێ بڕیاری خاوەن کۆرس بۆ statusی پەسەندکراو ناگۆڕدرێت.
3. هیچ خەڵات، completion، badge یان progression بۆ وانەی pending تۆمار نەکرێت.
4. هیچ کویزێک بۆ وانەی pending لە ڕێڕەوی فێرخوازدا دەستپێ نەکرێت، تەنانەت ئەگەر question bankی هەبێت.
5. هەموو گۆڕانکارییەکان لە برانچی جیاواز و بە تاقیکردنەوەی خۆجێیی؛ نەک لە `main`. Merge/deploy تەنها بە ڕێگەپێدانی ڕوونی خاوەن پرۆژە.

## B. ڕیزبەندیی چاکسازی

### P0 — یەکگرتوویی قفڵی review

**کێشەی پشتڕاستکراو:** `bot.py: lesson_is_pending_review` تەنها بە یەکسانی `owner_review_pending_expanded_draft` دەگەڕێت. `course_quiz_review.py` تەنها کلیلە کۆنەکانی Course 1 لە `COURSE1_QUIZ_SOURCE_REVIEW_REQUIRED` دەگرێت. `start_quiz` بانگی `quiz_is_available` دەکات، بەڵام statusی وانەی کۆرسی ٤ بە ڕاستەوخۆ لەو خاڵەدا ناپشکنێت.

**چارەسەرێکی پێشنیارکراو:**
- helperی pure لە `course_runtime.py` یان مۆدیولی هاوبەش: `is_owner_review_pending(status)`، کە هەموو statusەکانی پێشگری `owner_review_pending` بگرێتەوە.
- helperی `lesson_is_pending_review(lesson_id)` لە bot تەنها statusی `LESSON_DATA` بخوێنێتەوە و یاسای هاوبەش بەکاربهێنێت.
- لە `finish_lesson`، `lesson_keyboard`، `start_quiz`، menuی کویز و کۆتایی کویز هەمان helper بەکاربهێنرێت.
- بۆ وانەی pending، ڕێگریکردن لە completion، XP، Coin، badge، quiz reward و unlock؛ بەڵام خوێندنەوەی وانە بۆ beta inspection بەردەوام بێت.

### P0 — قفڵی کویز لە دەستپێک و کۆتایی

**چارەسەرێکی پێشنیارکراو:**
1. لە `start_quiz`، پێش خوێندنەوەی question bank، `lesson_is_pending_review(lesson)` پشکنە؛ ئەگەر pending بوو، کویز دەستپێ مەکە.
2. دۆخی `review_status` لە stateی کویزدا وەک snapshot هەڵمەگرە بۆ متمانە؛ لە کۆتایی وەڵامی کۆتاییدا لە `LESSON_DATA`ی ئێستا دووبارە بخوێنەوە.
3. پێش `complete_quiz_with_rewards`، status، course active، completion prerequisite و quiz availability دووبارە پشکنە.
4. ئەگەر status لە کاتی کویزدا گۆڕابوو بۆ pending، کویزە چالاکەکە پاک بکەرەوە، هیچ rewardێک مەدە و پەیامی ڕوون بنێرە.
5. بۆ بەڵگەی DB، completionی کۆن نابێت لە تۆماری پێشووەوە قفڵی review لاببات؛ statusی سەرچاوە پێش هەر actionێکی نوێ پێشینەی هەیە.

**تێبینی:** ئەگەر داهاتوودا پێویست بوو هەموو خاڵەکان بە شێوەی atomic بپارێزرێن، دەبێت database transaction/conditional claim لە database layerدا دیزاین بکرێت؛ تەنها پشکنینی Python لەسەر دوو requestی هاوکات دڵنیاییی atomic نادات.

### P1 — یەک سەرچاوەی content بەبێ لەدەستدانی ناوەڕۆک

**دۆخی ئێستا:** adapter لە structured fields ناوەڕۆک دروست دەکات؛ پاشان `bot.py` بۆ وانەکانی `source_markdown`دار content بە دەقی Markdown جێگرەوە دەکات.

**چارەسەری پێشنیارکراو:**
- بڕیار بدرێت `source_markdown` سەرچاوەی نمایشە یان تەنها پاشکۆی review.
- تا بڕیاری خاوەن کۆرس، precedenceی ئێستا مەگۆڕە؛ هیچ fallback/mergeێک لە کۆددا جێبەجێ مەکە.
- پێش هەر گۆڕانکارییەک، بۆ هەر وانە snapshotی هەردوو content دروست بکرێت؛ diffی هەموو ناوەڕۆک، سەردێڕ، نموونە، پاشکۆ، چالاکی و پرسیارەکان بپشکنرێت.
- پێشنیاری درێژخایەن: structured fields و source Markdown بە شێوەی یەک source-of-truth یان دوو representationی بەڵگەدار هەڵبگیرێن؛ renderer نابێت هیچ بەشێک بە بێ ئاگاداری لاببات.
- پێش merge، تاقیکردنەوەی semantic-preservation بۆ هەموو ٤٦ وانە پێویستە.

### P1 — داتای کویز و کلیلی وەڵام

- کلیلی وەڵام و explanation نابێت لە ناو دەقی فێرخوازدا پێش وەڵامدانەوە ئاشکرا بێت.
- بۆ وانەی pending، دەقی review بۆ خاوەن پڕۆژە بەردەست بێت؛ بەڵام ئەگەر ئەم دەقە لە beta learner viewدا نمایش دەکرێت، دەبێت بە ئاشکرا وەک review-only نیشان بدرێت و نابێت وەک assessmentی فەرمی پیشان بدرێت.
- هیچ quizی Markdown بە خۆکارانە مەگوازرێتەوە بۆ JSONی `quiz`؛ پێویستی بە پشکنینی زانستی، پشکنینی کلیلی وەڵام و پەسەندی خاوەن کۆرس هەیە.
- schemaی کویز: `q`ی بەتاڵ نەبوو، لانیکەم دوو هەڵبژاردەی جیاواز، `answer`ی integer لە سنووردا، `explanation`ی پێویست بەپێی policyی کۆرس.

### P2 — schemaی نموونە و بەشە فێرکارییەکان

- بۆ نموونەکان schemaی ڕوون دیاری بکرێت؛ ئەگەر تەنها `[text, explanation]` قبوڵ دەکرێت، adapter نابێت شێوەی نادروست بە بێ ئاگاداری فڕێبدات.
- بۆ زیاتر لە دوو خانە (وەک sentence, gloss, analysis, source, dialect) schemaی objectی ناونراو باشترە، بەڵام migration تەنها لە draft branch و بە پاراستنی فۆڕمی کۆن.
- `examples`, `exercises`, `comprehension`, `appendix`, `activities` و `quiz` لە یەکتر جیا بپارێزرێن؛ هیچ بەشێک لە `key_points[0]` بە شێوەی auto-parse بۆ خانەی نوێ نەگوازرێتەوە.

## C. ماتریسی تاقیکردنەوەی regression

### C1. helper و status
- statusی `owner_review_pending_expanded_draft` → pending.
- statusی داهاتوو `owner_review_pending_source_check` → pending.
- `scientific_review_complete_with_qualified_notes` → pending نییە.
- `internal_cross_lesson_synthesis_no_external_source_mapping` → pending نییە، بەڵام تێبینیی سەرچاوەییی خۆی دەپارێزێت.
- statusی نەناسراو/بەتاڵ: policyی fail-closed دیاری بکرێت؛ پێشنیار: بۆ completion و reward ڕێگە نەدرێت تا statusی ناسراو هەبێت، بەڵام بۆ خوێندنەوەی ناوەڕۆک مەرجی تایبەت دابنرێت.

### C2. lesson routes
- pending lesson: warning هەیە، completion keyboard نییە.
- callbackی کۆنی `finish_grammar_32`: هیچ reward و completion تۆمار ناکات.
- `open_lesson` و `next_lesson`: دەق دەخوێنرێتەوە، warning و review-only state دەپارێزرێت.
- approved lesson: completion keyboard و progressionی ئاسایی دەمێنێتەوە.

### C3. quiz routes
- pending + quiz bankی پڕ: `start_quiz` ڕەت دەکرێتەوە.
- pending + completed DB recordی کۆن: `start_quiz` ڕەت دەکرێتەوە.
- approved + quiz bankی بەتاڵ: پەیامی quiz unavailable.
- approved + completed lesson + prerequisites: کویز دەستپێدەکات.
- status لە نێوان پرسیاری یەکەم و کۆتایی بگۆڕدرێت بۆ pending: هیچ XP/reward نییە؛ state پاک دەکرێتەوە.
- callbackی stale لە کویزی پێشووتر: ناتوانێت خەڵات وەربگرێت.
- کویزی تەواوبوو: idempotent reward وەک پێشوو دەمێنێتەوە.

### C4. content و source
- وانەی source_markdownدار: هەموو سەردێڕ و پاراگراف و نموونە و پاشکۆی سەرچاوەیی دەپارێزرێن.
- renderer هیچ ناوەڕۆکێک لە نێوان structured content و Markdownدا بە بێ diff لەدەست نادات.
- پشکنینی هەموو ٤٦ وانە بۆ title، content، appendix، activities، exercises، comprehension، examples، quiz و status.
- answer key لە viewی فێرخوازدا پێش وەڵامدانەوە دەرناکەوێت.

### C5. adapter و data validation
- duplicate/non-contiguous lesson IDs → fail.
- titleی بەتاڵ → fail.
- exampleی malformed → failی ڕوون، نەک skipی بێدەنگ.
- quiz answer indexی نادروست، optionی دووبارە، یان textی بەتاڵ → fail.
- ٤٦ وانە لە manifest و curriculum plan و JSON هەمان ڕیز و IDیان هەبێت.

## D. فایلەکانی تاقیکردنەوەی پێشنیارکراو

- `tests/test_course4_grammar_runtime.py`: زیادکردنی statusی pendingی نوێ، قفڵی finish و quiz، source-preservation و ٤٦ وانە.
- `tests/test_bot_quiz_callbacks.py`: pending quiz start، stale quiz finalization، duplicate callback و reward suppression.
- `tests/test_activated_courses.py`: دڵنیایی لەوەی active course ≠ approved lesson و review status چالاکیی کۆرس ناگۆڕێت.
- `tests/test_orthography_quiz_adapter.py`: schemaی adapter و validationی options/answer.
- تاقیکردنەوەی نوێی پێشنیارکراو: `tests/test_course_review_policy.py` بۆ pure helper و status taxonomy.

## E. ڕێڕەوی جێبەجێکردن

1. بڕیاری خاوەن کۆرس لەسەر policyی statusی نەناسراو و ئاستی beta learner visibility.
2. زیادکردنی pure helper و unit tests لە برانچی draft.
3. چاککردنی `start_quiz` و finalization guard، لەگەڵ testsی async.
4. پشکنینی source precedence و semantic diff، بەبێ گۆڕینی content.
5. پاشان schemaی examples/quiz و test coverage.
6. اجرای `python -m compileall -q .` و `python -m unittest discover -s tests -v` لە ژینگەی پڕۆژە.
7. پشکنینی diff و commit؛ تەنها پاش ڕێگەپێدانی خاوەن کۆرس بۆ PR/merge/deployment.

## F. دۆخی ئێستا و تۆماری پاراستن

- ئەم فایلە تەنها design/auditە.
- `main`، `bot.py`، `course_lesson_adapters.py`، `course_quiz_review.py`، `course_runtime.py`، JSONی ٤٦ وانە و tests دەستکاری نەکراون.
- هیچ تاقیکردنەوەی CI یان runtime لەم قۆناغەدا جێبەجێ نەکراوە؛ ماتریسی سەرەوە تاقیکردنەوەی پێشنیارکراوە.
- هیچ merge، deployment، Botkeep، Telegram، DB migration یان server restart نەکراوە.
- بڕیاری پەسەندکردنی وانە و کویز بە تەواوی لە دەستی خاوەن کۆرسدا دەمێنێتەوە.

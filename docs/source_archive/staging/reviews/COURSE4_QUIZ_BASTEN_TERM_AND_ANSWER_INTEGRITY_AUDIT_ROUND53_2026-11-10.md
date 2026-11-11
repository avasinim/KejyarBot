# Round 53 — Quiz Terminology Integrity Audit: «سیاق» / «بەستێن»
Date: 2026-11-10
Branch: `botkeep-menu-clean-2026-11-09`
Source JSON blob SHA: `fd8dfbde7e6937841214cacac653ef10d0c6097d`

## Scope and verified counts
- All structured quiz objects across all 50 lesson records.
- Exact occurrences of `سیاق` in quiz question/options/explanation content: **30**.
- Unique occurrence records after deduplication by lesson, quiz index, field path and full string: **29**.
- A duplicate scan hit occurred in the same lesson 30 quiz option string; it is listed once in this ledger.
- Lessons containing hits: 7 (1), 8 (2), 10 (2), 11 (3), 12 (2), 13 (2), 14 (1), 15 (1), 16 (6), 18 (1), 21 (1), 27 (3), 29 (2), 30 (1), 31 (1).
- No occurrence was found in structured `answer` / `correct_answer` fields.
- The structured answer indices were inspected and are not altered by this review.

## Editorial policy for quizzes
1. Preserve question meaning, distractor strength, and the original correct-answer index.
2. Prefer **بەستێن** when the intended concept is linguistic context, interpretation or the contextual evidence needed to disambiguate a form.
3. In expressions like `سیاقی عادەت` or `سیاقی داهاتوو`, assess whether `بارودۆخی عادەت/داهاتوو` is clearer than a literal `بەستێنی عادەت/داهاتوو`. These are not approved substitutions yet.
4. Where the word appears in a quiz stem, option or explanation, check that all linked material uses the same chosen term and that the option remains unambiguous.
5. Do not change any quiz answer, option order, or index solely to accommodate a terminology edit.

## Occurrence-by-occurrence ledger
1. **وانە 7 · پرسیاری 2 · `quiz[1].q`**
   - دەقی ئێستا: کامەیان نموونەی هاوەڵناوی نسبییە لە سیاقی گونجاودا؟
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
2. **وانە 8 · پرسیاری 5 · `quiz[4].options[0]`**
   - دەقی ئێستا: شێوازی جەختکردنەوە/باڵاییە و پێویستی بە پشکنینی سیاق هەیە
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
3. **وانە 8 · پرسیاری 5 · `quiz[4].options[1]`**
   - دەقی ئێستا: هاوەڵکارە لە هەموو سیاقێکدا
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
4. **وانە 10 · پرسیاری 4 · `quiz[3].explanation`**
   - دەقی ئێستا: «ئەو» لەو سیاقەدا جێگرەوەی دەستەواژەی ناوی «کەژیار»ە.
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
5. **وانە 10 · پرسیاری 8 · `quiz[7].explanation`**
   - دەقی ئێستا: جێناو دەتوانێت جێگرەوە بێت یان لە سیاقێکدا جەخت و بەراورد دروست بکات.
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
6. **وانە 11 · پرسیاری 4 · `quiz[3].options[1]`**
   - دەقی ئێستا: هەمان فۆڕم دەتوانێت لە سیاقی جیاوازدا ئەرکی جیاواز هەبێت
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
7. **وانە 11 · پرسیاری 7 · `quiz[6].options[2]`**
   - دەقی ئێستا: سیاق، پێکهاتە و ئەرکی ڕستە بپشکنین
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
8. **وانە 11 · پرسیاری 8 · `quiz[7].q`**
   - دەقی ئێستا: «ـیان» لە «ماڵەکەیان»دا لە سیاقی خاوەنداریدا چییە؟
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
9. **وانە 12 · پرسیاری 4 · `quiz[3].explanation`**
   - دەقی ئێستا: لە خوێندنەوەی مەبەست بە «ئەوان کتێبەکە خوێند»، لکاوەکە بە بکەری ڕابردووی تێپەڕەوە پەیوەستە؛ لە سیاقی خاوەنداریدا ڕستەکە خوێندنەوەیەکی تر هەیە.
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
10. **وانە 12 · پرسیاری 6 · `quiz[5].options[2]`**
   - دەقی ئێستا: ئەرکی ـیان بە پێی پێکهاتە و سیاق دیاری دەکرێت
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
11. **وانە 13 · پرسیاری 3 · `quiz[2].explanation`**
   - دەقی ئێستا: «دەـ» بە پێی سیاق لە ئێستا، عادەت یان داهاتوودا بەکاردێت.
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
12. **وانە 13 · پرسیاری 7 · `quiz[6].q`**
   - دەقی ئێستا: بۆچی ئەرکی «ـیان» دەبێت لە سیاقدا شیکرێتەوە؟
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
13. **وانە 14 · پرسیاری 7 · `quiz[6].explanation`**
   - دەقی ئێستا: واتا و ئەرکی گرووپی پێشگرەدار بە پێی کردار و سیاق دەگۆڕێت.
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
14. **وانە 15 · پرسیاری 5 · `quiz[4].options[3]`**
   - دەقی ئێستا: واتایان بە ڕێباز و سیاقەوە پەیوەستە
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
15. **وانە 16 · پرسیاری 3 · `quiz[2].options[0]`**
   - دەقی ئێستا: نەخێر، واتا بە سیاقەوە پەیوەستە
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
16. **وانە 16 · پرسیاری 3 · `quiz[2].explanation`**
   - دەقی ئێستا: دەـ لە ئێستا، عادەت و داهاتوودا بە پێی سیاق بەکار دێت.
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
17. **وانە 16 · پرسیاری 4 · `quiz[3].explanation`**
   - دەقی ئێستا: هاوەڵکاریی کاتی سیاقی داهاتوو دروست دەکات.
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
18. **وانە 16 · پرسیاری 6 · `quiz[5].q`**
   - دەقی ئێستا: کام ڕستە دەـ لە سیاقی عادەتدا بەکاردەهێنێت؟
   - ئاراستەی چاکسازی: بارودۆخی عادەت / بەستێنی عادەت (هەڵبژاردنی دەقیی)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
19. **وانە 16 · پرسیاری 6 · `quiz[5].explanation`**
   - دەقی ئێستا: «هەموو ڕۆژێک» سیاقی عادەت دروست دەکات.
   - ئاراستەی چاکسازی: بارودۆخی عادەت / بەستێنی عادەت (هەڵبژاردنی دەقیی)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
20. **وانە 16 · پرسیاری 8 · `quiz[7].options[3]`**
   - دەقی ئێستا: پێشگر، بنەما، نیشانەی کەس و سیاق
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
21. **وانە 18 · پرسیاری 3 · `quiz[2].explanation`**
   - دەقی ئێستا: لە ئەم خوێندنەوەیەدا «مامۆستا» ئەنجامدەری کردار و بکەرە؛ «ـی»ی لکێنراو لە «وانەکەی» نیشانەی بکەری سێیەمی تاکە، نە خاوەنداری. بە سیاق خوێندنەوەی خاوەنداری جیا دەکرێتەوە.
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
22. **وانە 21 · پرسیاری 2 · `quiz[1].options[2]`**
   - دەقی ئێستا: پۆل و ئەرک بە پێی سیاق دەگۆڕێت
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
23. **وانە 27 · پرسیاری 7 · `quiz[6].q`**
   - دەقی ئێستا: لە ڕووی زانستییەوە بۆچی «ئەرێ»، «جا»، «خۆ» و «دەی» پێویستیان بە پشکنینی سیاق هەیە؟
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
24. **وانە 27 · پرسیاری 7 · `quiz[6].explanation`**
   - دەقی ئێستا: وانەی ٢٦ ئەم فۆڕمانە لە چوارچێوەی discourse particlesدا دەخاتەڕوو؛ بەبێ نموونە و سیاق نابێت بە خۆکارانە بگوازرێنە ناو پۆلی Interjection.
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
25. **وانە 27 · پرسیاری 8 · `quiz[7].options[0]`**
   - دەقی ئێستا: پاراستنیان و داوای نموونەی سیاقی/داتای قسەی سروشتی پێش دیاریکردنی ئەرکیان
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
26. **وانە 29 · پرسیاری 6 · `quiz[5].options[3]`**
   - دەقی ئێستا: دەتوانێت ئەرکی جیاواز هەبێت و دەبێت بە سیاق شیکرێتەوە
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
27. **وانە 29 · پرسیاری 6 · `quiz[5].explanation`**
   - دەقی ئێستا: «ـەوە» لە کرداردا دەتوانێت واتای گەڕانەوە، دووبارەکردنەوە، ئاراستە یان گۆڕانی واتای لێکسیەمی دروست بکات؛ بۆیە ئەرکەکەی دەبێت بە پێی کردار و سیاق دیاری بکرێت، نەک هەمیشە بە پاشگری داڕێژەیی یان نیشانەی کات دابنرێت.
   - ئاراستەی چاکسازی: بەستێن
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
28. **وانە 30 · پرسیاری 5 · `quiz[4].options[2]`**
   - دەقی ئێستا: دەکرێت هەمان کردار لە سیاقێکدا سووک و لە سیاقێکی دیکەدا سەرەکی بێت
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.
29. **وانە 31 · پرسیاری 6 · `quiz[5].options[2]`**
   - دەقی ئێستا: هەموو چاوگێک لە هەموو سیاقێکدا ناوی ئاساییە
   - ئاراستەی چاکسازی: بەستێن (بە پشکنینی ڕستە و پێکهاتە)
   - کاریگەری لەسەر وەڵامی ڕاست: هیچ؛ خانەی answer نەگۆڕدراوە.

## Critical integrity observations
- Lesson 7, quiz 2: replacing the term must not alter the adjective classification being tested.
- Lesson 8, quiz 5: option A is a qualified claim and option B an absolute claim; retain this contrast.
- Lessons 11–12 and 18: contextual reading is material to distinguishing possessive clitics from transitive past subject marking. Avoid wording that implies context alone replaces morphosyntactic analysis.
- Lessons 13 and 16: `دەـ` is not a future-only marker; the item should preserve the interaction of verb form, temporal adverbial and broader sentence interpretation.
- Lesson 27: retain the evidence requirement for discourse particles/interjections; do not imply every form has one fixed class.
- Lesson 29: retain the distinction between lexical particle/verb construction and inflectional/derivational analysis.
- No answer-key changes are proposed in this round.

## Status
- Append-only audit report.
- No raw lesson text, quiz object, answer key, runtime, database, Botkeep or Telegram content changed.
- No mass replacement or direct quiz edit performed.
- This report is a review gate; occurrence-level approval remains pending.

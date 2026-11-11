# کەژیار — پاشکۆی پاراستنی زیادەی وانەکانی ٤٧–٥٠
**بەروار:** 2026-11-11  
**برانچی پشکنراو:** `release/main-based-reconciled-2026-11-11`  
**کۆمیتی بنەڕەتی:** `3e8c15a612e411c8ab36c176b42ebe06c706baa9`  
**مەبەست:** زیادکردنی فهرستی پاراستنی وانەکانی ٤٧–٥٠ بەبێ دەستکاری یان جێگۆڕکێی ئەرشیفی پێشووی ١–٤٦.

## ١. پەیوەندی بە فهرست و bundleی پێشوو
- فهرستی `docs/COURSE4_LESSONS_01_46_MASTER_PRESERVATION_INDEX_2026-11-08.md` بە ئاشکرا زنجیرەی مێژوویی ١–٤٦ دەگرێتەوە و لە ناوەڕۆکیدا ئاگاداریی جیاوازیی ئەرشیفی مێژوویی و کۆرسی چالاک هەیە.
- `docs/source_archive/COURSE4_LESSONS_01_46_PRESERVATION_BUNDLE_2026-11-08.json` بە پێی metadataی خۆی `lesson_count=46`, `runtime_lesson_count=31`, `draft_lesson_count=15` و `curriculum_state=preservation_bundle_lessons_01_31_runtime_schema_plus_32_46_unapproved_expanded_drafts` ـە. ٣١ snapshotی وانەی ١–٣١ و ١٥ ڕەشنووسی ٣٢–٤٦ لەخۆدەگرێت.
- بۆیە bundleی ١–٤٦ بە خۆی پێویست نییە بە «کەمبوونی وانە» چاک بکرێتەوە؛ بەڵام وانەکانی ٤٧–٥٠ دوای دروستبوونی ئەو bundleە زیادکراون و لە scopeی ناونیشان/metadataی ئەو bundleەدا نین.
- ئەم پاشکۆیە زیادەیە و bundleی ١–٤٦ ناگۆڕێت؛ هیچ مێژوویەک overwrite یان لابردن ناکرێت.

## ٢. فهرستی فایلە پارێزراوەکانی ٤٧–٥٠
| وانە | فایل | Git blob SHA | قەبارەی دەق |
|---|---|---|---:|
| ٤٧ | `docs/source_archive/staging/drafts/COURSE4_LESSON_047_NOUN_PHRASE_EXPANDED_DRAFT_V2_2026-11-09.md` | `24460b064fdd0e32e9fd2cbd49186e6d7f95b633` | 9,741 chars |
| ٤٨ | `docs/source_archive/staging/drafts/COURSE4_LESSON_048_VERB_PHRASE_VALENCY_ARGUMENT_STRUCTURE_DRAFT_V2_2026-11-09.md` | `0cd09db604e9e36f30ffe5939190ebaa6e6163f5` | 9,601 chars |
| ٤٩ | `docs/source_archive/staging/drafts/COURSE4_LESSON_049_SORANI_PERSON_MARKING_CLITICS_ALIGNMENT_DRAFT_V2_2026-11-09.md` | `6db82e2caf3bbab4779a2312ef85f8650cf80b05` | 8,620 chars |
| ٥٠ | `docs/source_archive/staging/drafts/COURSE4_LESSON_050_RELATIVE_CLAUSES_SORANI_DRAFT_V2_2026-11-09.md` | `47c6a6fe88c6252afb51eee9e82d9b352f74dc81` | 11,743 chars |
| ٥٠ — پاشکۆی کۆتایی | `docs/source_archive/staging/drafts/COURSE4_LESSON_050_CAPSTONE_SORANI_GRAMMATICAL_DATA_ANALYSIS_APPENDIX_2026-11-09.md` | `6fc0fb9b179ec3ab8cc70a859740c1ef390d46d5` | 2,964 chars |

*قەبارەکان لە وەشانی خوێندراوەوە ژمێردراون؛ SHA ـەکان Git blob SHA ـی fetchکراون.*

## ٣. دۆخی پاراستن و سنووری هەر ماددەیەک
- وانەکانی ٤٧–٥٠ ڕەشنووسی پەرەپێدراوی پێشنیارکراون؛ هیچ‌کام پەسەندکراوی ئەکادیمی یان runtime نییە.
- لە پشکنینی پێشوو و Appendix 9.37دا بۆ هەموو چوار وانەکە `owner_review_pending_expanded_draft` تۆمار کراوە؛ structured quiz و key_points/examples/exercisesی runtime بەتاڵن. ئەمە دۆخی ڕەشنووسەکانە، نەک کەمبوونی دەقی Markdown.
- وانەی ٥٠ و پاشکۆی capstone دوو فایل و دوو بەڵگەی جیاوازن. Capstone وانەی ٥١ نییە؛ پڕۆژەی ڕاهێنانی پێشنیارکراوە، کویزی structuredی نییە و لە runtimeدا چالاک نییە.
- لە وانەی ٥٠دا ناکۆکیی زاراوەیی `بەرڕستە/ژێرەڕستە` لە cross-referenceی وانەی ٣٨ و لە capstoneدا پێشتر تۆمار کراوە؛ ئەم پاشکۆیە تەنها ناسنامە و شوێنی پاراستن دەپارێزێت و بڕیار لەسەر زاراوە نادات.
- بوونی فایلەکان بە مانای پشتڕاستبوونی سەرچاوە، پەسەندکردنی ناوەڕۆک، یان چوونە ناو کۆرسی چالاک نییە.

## ٤. کاری پێویست بۆ فهرستی داهاتوو
1. ئەم پاشکۆیە وەک supplementی فهرستی ١–٤٦ بەکاربهێنرێت؛ bundleی پێشووی ١–٤٦ بە هەمان شێوەی مێژوویی بپارێزرێت.
2. ئەگەر دواتر bundleی یەکگرتووی ١–٥٠ پێویست بوو، وەشانی نوێی جیاواز دروست بکرێت و وەشانی ١–٤٦ نەگۆڕدرێت.
3. لە هەر گواستنەوەیەکدا دەقی خاو، ڕەشنووس، capstone و runtime بە جیاوازی بناسرێن؛ هیچ ڕەشنووسێک بە خۆکار نەگوازرێتەوە بۆ runtime.

## ٥. سنووری ئەنجام
ئەم پاشکۆیە تەنها indexی پاراستنە. هیچ وانە، source file، JSON، quiz، plan، review_status، runtime، DB یان learner record نەگۆڕدرا. هیچ merge، Botkeep import/restore/restart، deployment یان Telegram production action نەکرا.

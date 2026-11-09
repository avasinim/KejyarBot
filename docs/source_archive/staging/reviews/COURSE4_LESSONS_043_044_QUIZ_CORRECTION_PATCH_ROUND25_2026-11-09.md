# Course 4 — Lessons 43–44
## Append-only quiz correction patch
### Round 25 — 2026-11-09

**Status:** replacement-item proposal for safe beta assessment. Original Markdown quiz items remain preserved. No lesson status is upgraded and no runtime or source JSON is changed.

## Lesson 43 — Clitic function in transitive verbs

### Original item to retain in archive, but not migrate as a scored question
The source quiz asks whether `-ی` in «کتێبەکەی خوێندەوە» expresses possession or the Object of the verb, and keys possession as the answer.

**Reason for replacement:** the form alone is not enough to decide the function. The course's own cross-lesson reviews identify overlap between possessive clitics and person marking in Sorani. Without a full intended context, target dialect, and morphological segmentation, this item risks teaching a false universal rule.

### Replacement question 2 (safe principle)
**پرسیار:** بۆ دیاریکردنی ئەرکی لکاوی «ـی» لە نموونەیەکی ڕابردووی تێپەڕدا، کام زانیارییە پێویستە؟

- أ) تەنها شێوەی نووسینی «ـی»
- ب) تەنها شوێنی لکاوەکە
- ج) ڕستەی تەواو، زار، کۆنتێکست و شیکاریی مۆرفۆلۆژی
- د) تەنها ژمارەی وشەکانی ڕستە

**وەڵامی ڕاست:** ج

**Explanation:** شێوەی نووسراوی هاوشێوە دەتوانێت لە پێکهاتە جیاوازەکاندا ئەرکی جیاواز هەبێت؛ بۆیە پێویستە host، ڕستە، alignment و سیاق بپشکنرێن.

### Migration instruction
Migrate the remaining four original Lesson 43 items only after checking their answer keys against the source. Replace Q2 with the item above. Keep the original Q2 verbatim in the preserved Markdown and record it as retired from scoring, not deleted.

## Lesson 44 — Voice vs Transitivity

### Original item to retain in archive, but not migrate as a scored question
The source quiz asks whether «کەژیار هات» is passive or intransitive and treats the two as alternative answers.

**Reason for replacement:** Passive is a Voice category; intransitive is a Transitivity category. They answer different questions and are not mutually exclusive.

### Replacement question 3A (Transitivity)
**پرسیار:** لە «کەژیار هات»دا کردار لە ڕووی تێپەڕبوونەوە چۆن پۆلێن دەکرێت؟

- أ) تێپەڕ
- ب) تێنەپەڕ
- ج) کاری بەستەر
- د) ناتوانرێت هیچ پۆلێنێک بکرێت

**وەڵامی ڕاست:** ب

**Explanation:** لەم ڕستەیەدا کردار بەرکاری ڕاستەوخۆی داواکراوی نییە؛ بۆیە لە ڕووی تێپەڕبوونەوە تێنەپەڕە. ئەمە بە تەنیا هیچ بڕیارێک لەسەر Voice نادات.

### Replacement question 3B (Voice)
**پرسیار:** بۆ ئەوەی بزانین ڕستەیەک نەکارایە، کام شت دەبێت بپشکنرێت؟

- أ) تەنها ئەوەی بەرکار بە ئاشکرا هەیە یان نا
- ب) تەنها ژمارەی وشەکان
- ج) نیشانە و پێکهاتەی ڕێزمانیی Voice لەگەڵ شیکاریی ڕستە
- د) تەنها شوێنی بکەر

**وەڵامی ڕاست:** ج

**Explanation:** نەکارایی پۆلێنکردنی Voice ـە؛ نابێت بە تەنها لە نەبوونی بەرکاری ئاشکرا یان تێنەپەڕبوونەوە هەڵبهێنجرێت.

### Migration instruction
Migrate the remaining four original Lesson 44 items after checking them. Replace original Q3 with 3A and 3B only if the product design permits six questions for this lesson; otherwise combine the concepts into two separate short sub-items in one assessment screen, or retain five questions by replacing Q3 with 3A and add 3B as a required non-scored comprehension check. Do not conflate the two dimensions.

## Integrity and release notes
- Preserve original Lesson 43 and Lesson 44 source Markdown verbatim.
- These are assessment corrections, not final academic approval of the lessons.
- Target Sorani dialect validation remains necessary for the disputed example forms.
- No JSON quiz migration, source edit, runtime edit, database edit, `main` modification, Botkeep operation, or Telegram deployment was performed.

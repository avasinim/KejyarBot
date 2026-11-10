# Course 4 — Round 61 Quiz-Level Semantic and Editorial Review of Round60 Basten Shortlist
Date: 2026-11-10
Branch: `botkeep-menu-clean-2026-11-09`
Source JSON SHA: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
Round60 shortlist blob SHA: `1316073488bf38f022d7044cb3415c457640ebeb`

## Scope and method
Reviewed all nine quiz string paths listed in the Round60 whole-phrase shortlist. For each item, inspected the complete question, all options, answer index, explanation, and the exact target phrase. This is an editorial/semantic review of the proposed terminology substitutions; it is not a scientific revalidation of the underlying grammar item.

## Findings by quiz path

### 1. Lesson 7 — `quiz[1].q`
- Question: `کامەیان نموونەی هاوەڵناوی نسبییە لە سیاقی گونجاودا؟`
- Proposed: `لە بەستێنی گونجاودا`
- Decision: **Accept the phrase-level substitution as semantically appropriate.**
- Reason: The item asks for a relational adjective in an appropriate linguistic use. The intended qualifier is linguistic/discourse context, not an external real-world circumstance.
- Answer integrity: option 0 (`فەڕەنسی`) remains correct; no option or answer changes.

### 2. Lesson 8 — `quiz[4].options[1]`
- Question: `«هەرە جوان» چۆن مامەڵەی لەگەڵدا دەکرێت؟`
- Option: `هاوەڵکارە لە هەموو سیاقێکدا`
- Proposed: `هاوەڵکارە لە هەموو بەستێنێکدا`
- Decision: **Accept the terminology substitution; retain the option's universal wording unchanged.**
- Reason: The item is testing an overgeneralized grammatical claim. The context term denotes linguistic usage. Do not soften or rewrite the universal quantifier, because that would change the distractor's force.
- Answer integrity: option 0 remains correct; option order and answer index unchanged.

### 3. Lesson 10 — `quiz[3].explanation`
- Question: `لە «کەژیار هات. ئەو ماندوو بوو»دا «ئەو» چی دەکات؟`
- Explanation: `«ئەو» لەو سیاقەدا جێگرەوەی دەستەواژەی ناوی «کەژیار»ە.`
- Proposed: `«ئەو» لەو بەستێنەدا جێگرەوەی دەستەواژەی ناوی «کەژیار»ە.`
- Decision: **Accept, with a precision note.**
- Reason: Antecedent resolution depends on the preceding discourse/textual context. «بەستێن» is suitable as the agreed umbrella term. If this explanation is later expanded, «لەو بەستێنەی دەقەدا» may make the textual/discourse relation more explicit; no such expansion is required for this patch.
- Answer integrity: option 0 remains correct.

### 4. Lesson 10 — `quiz[7].explanation`
- Question: `کام بانگەشە دروستە؟`
- Explanation: `جێناو دەتوانێت جێگرەوە بێت یان لە سیاقێکدا جەخت و بەراورد دروست بکات.`
- Proposed: `جێناو دەتوانێت جێگرەوە بێت یان لە بەستێنێکدا جەخت و بەراورد دروست بکات.`
- Decision: **Accept.**
- Reason: The explanation describes context-dependent pragmatic/discourse functions of pronouns; this is linguistic context, not external circumstance.
- Answer integrity: option 1 remains correct.

### 5. Lesson 13 — `quiz[2].explanation`
- Question: `«دەـ» بە تەنها چی دیاری ناکات؟`
- Explanation: `«دەـ» بە پێی سیاق لە ئێستا، عادەت یان داهاتوودا بەکاردێت.`
- Proposed: `«دەـ» بە پێی بەستێن لە ئێستا، عادەت یان داهاتوودا بەکاردێت.`
- Decision: **Accept.**
- Reason: The explanation correctly keeps the temporal interpretation open and context-dependent. Do not replace «بە پێی بەستێن» with «بە پێی بارودۆخ» here: the teaching point concerns linguistic interpretation of the verbal form, while temporal readings are listed separately.
- Answer integrity: option 1 remains correct; no claim is changed.

### 6. Lesson 16 — `quiz[2].explanation`
- Question: `ئایا «دەـ» بە تەنها داهاتوو نیشان دەدات؟`
- Explanation: `دەـ لە ئێستا، عادەت و داهاتوودا بە پێی سیاق بەکار دێت.`
- Proposed: `دەـ لە ئێستا، عادەت و داهاتوودا بە پێی بەستێن بەکار دێت.`
- Decision: **Accept.**
- Reason: Same distinction as Lesson13. Keep the statement that «دەـ» is not future-only. The term substitution does not alter the aspect/tense interpretation.
- Answer integrity: option 0 remains correct.

### 7. Lesson 21 — `quiz[1].options[2]`
- Question: `بۆچی هەموو توخمی شوێنی هاوەڵکار نییە؟`
- Option: `پۆل و ئەرک بە پێی سیاق دەگۆڕێت`
- Proposed: `پۆل و ئەرک بە پێی بەستێن دەگۆڕێت`
- Decision: **Accept.**
- Reason: Word class and syntactic function are inferred from linguistic distribution and use. «بەستێن» is the appropriate term.
- Answer integrity: option 2 remains correct.

### 8. Lesson 30 — `quiz[4].options[2]`
- Question: `کام بانگەشە لەبارەی کردارە سووکەکان دروستە؟`
- Option: `دەکرێت هەمان کردار لە سیاقێکدا سووک و لە سیاقێکی دیکەدا سەرەکی بێت`
- Proposed: `دەکرێت هەمان کردار لە بەستێنێکدا سووک و لە بەستێنێکی دیکەدا سەرەکی بێت`
- Decision: **Accept.**
- Reason: This is precisely a contrast between two linguistic environments in which the same verb may have different grammatical/lexical status. The parallel locative phrases are grammatical and preserve the contrast.
- Answer integrity: option 2 remains correct.

### 9. Lesson 31 — `quiz[5].options[2]`
- Question: `کام بانگەشە دروستە؟`
- Option: `هەموو چاوگێک لە هەموو سیاقێکدا ناوی ئاساییە`
- Proposed: `هەموو چاوگێک لە هەموو بەستێنێکدا ناوی ئاساییە`
- Decision: **Accept the term substitution; retain the deliberately overgeneralized claim.**
- Reason: The option is a distractor testing whether learners recognize that infinitives/nominalized verb forms do not behave as ordinary nouns in every linguistic environment. The universal quantifier is pedagogically important and must not be weakened.
- Answer integrity: option 1 remains correct.

## Summary
- Quiz paths reviewed: **9/9**
- Phrase substitutions semantically acceptable: **9/9**
- Answer indices changed: **0**
- Correct options changed: **0**
- Option order changed: **0**
- Questions or explanations rewritten beyond the approved term substitution: **0**
- High-priority semantic blocker found: **0**
- Precision note retained for Lesson10 explanation: discourse/textual antecedent relation can be made more explicit in a future substantive edit, but this is not required for the current term patch.

## Decision
The nine quiz-level substitutions in the Round60 shortlist **pass the quiz-specific semantic and answer-integrity review**. This is approval of the wording proposal only, not approval to modify the source JSON or activate/deploy the course.

## Verification and change control
- Source JSON SHA remains `fd8dfbde7e6937841214cacac653ef10d0c6097d`.
- No source JSON or quiz object was edited.
- No answer key, runtime, database, Botkeep, Telegram, deployment, merge, or PR state was changed.
- The Round60 shortlist remains a proposal pending the broader 35-path sentence-level proofreading and explicit authorization before any source edit.

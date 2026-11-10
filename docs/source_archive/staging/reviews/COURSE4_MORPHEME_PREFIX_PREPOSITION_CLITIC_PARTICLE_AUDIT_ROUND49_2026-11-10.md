# Course 4 — Morpheme, Prefix/Preposition, Clitic and Verbal-Particle Boundary Audit (Round 49)
Date: 2026-11-10
Branch: `botkeep-menu-clean-2026-11-09`
Source: `course_data/grammar_course4_lessons.json` on the branch at review time; 50 lessons. Review scope: objective, key_points, examples, exercises, comprehension, appendix, activities, and structured quiz fields where present.
Method: exact-string scan plus contextual inspection of relevant lesson passages. This is a terminology/consistency audit, not a claim of full native-speaker validation.

## Executive finding
The conceptual distinctions are mostly present in the revised material, especially in Lessons 13, 26, 29 and 30. The remaining risks are localized but pedagogically important: older uses of `پێشگر` still appear where the intended concept is Preposition (`پێشبەند)); the same Kurdish string can be read as Prefix, while Prefix is a distinct bound word-forming element. There are also places where the course itself explicitly warns against collapsing verbal particles into prefixes or prepositions; those cautions should be preserved in any later editing.

## Stable terminology for new explanatory prose
- Affix = `گیرەک` (umbrella term)
- Prefix = `پێشگر`
- Suffix = `پاشگر`
- Clitic = `لکاو`
- Enclitic = `پاشنووس` (descriptive gloss: `لکاوی دواوە`)
- Proclitic = `پێشنووس`
- Preposition = `پێشبەند`
- Verbal particle = `پارتیکڵی کردار`
- Inflection = `گەردان`
- Derivation = `داڕشتن`

Do not infer that every clitic is an affix, that every enclitic is a suffix, or that every preverbal particle is a morphological prefix. Affix is the broader morphological category; prefix/suffix are its positional subtypes in the relevant analysis. Clitic status concerns prosodic/syntactic dependence and must be evaluated separately. The category assigned to a Kurdish verbal element such as `هەڵـ`, `داـ`, `ڕاـ` or `وەرـ` depends on the source/framework and the particular construction.

## Contextual findings

### 1. Lesson 11 — clear terminology repair candidate
In key_points the sentence about clitics attached to prepositions uses the phrase `ئەو پێشگرە` after introducing `پێشبەندەکان`. The appendix similarly says that clitic examples with prepositions should be examined by each `پێشگر`. In both contexts the intended category is Preposition, not Prefix.
Proposed text-only patch:
- `بەپێی ئەو پێشگرە` → `بەپێی ئەو پێشبەندە`
- `بەپێی هەر پێشگرێک` → `بەپێی هەر پێشبەندێک`
This is a high-confidence terminology repair because the immediate sentence explicitly names Prepositions. Keep the surrounding caution that clitic behavior must be validated for each preposition/construction; do not turn it into a universal rule.

### 2. Lesson 14 — inspect the legacy phrase in title/terminology
Round45 flagged `تەواوکەری پێشگرەدار` as a possible legacy phrase where the intended relation may be a prepositional complement/phrase. Do not globally replace it. If the phrase describes a complement licensed by a preposition, a candidate wording is `تەواوکەری پێشبەنددار` or, where the constituent itself is meant, `گرێی پێشبەندی`. The correct choice depends on the lesson's syntactic framework and whether it names a function or a phrase. Keep this item pending framework-level review before patching.

### 3. Lesson 13 — preserve the separation of suffix and enclitic
The lesson correctly distinguishes `پاشگر` from `پاشبەستە/پاشنووس`: a suffix is a morphological formative, whereas an enclitic is a clitic positioned after a host. Its appendix uses the normalized labels Affix=`گیرەک`, Prefix=`پێشگر`, Suffix=`پاشگر`, Clitic=`لکاو`, Enclitic=`پاشنووس`, Proclitic=`پێشنووس`.
No mass replacement of legacy `پاشبەستە` is recommended without checking each occurrence and its grammatical function. In particular, don't relabel person/number markers in verbal paradigms solely from their written position.

### 4. Lessons 26, 29 and 30 — verbal particle is not automatically prefix/preposition
- Lesson 26 distinguishes discourse particles from clitics, conjunctions, prepositions and morphological elements. Preserve this separation.
- Lesson 29 treats examples such as `هەڵگرتن` and `داگرتن` as particle-verb constructions in its stated analysis, and distinguishes these from suffixal derivation such as `مراندن`. The lesson also notes that some frameworks may analyze particle verbs differently. Do not flatten the distinction into a single prefix rule.
- Lesson 30 explicitly contrasts prepositional phrase + verb (`لە دەستدان`, `لە دایک بوون`) with particle + verb (`ڕا + کردن`, `هەڵ + کردن`) and notes that framework classifications vary. This is a useful teaching contrast; retain the source/framework qualification.
- The form `پێشگری بەستراو` appears as a framework-specific description in the lesson. It must not silently replace the course's category `پارتیکڵی کردار` in all contexts.

### 5. Lesson 3 and later noun examples — suffix identification must remain contextual
The lesson correctly cautions that strings resembling endings can be plural/definiteness markers, derivational suffixes, inflectional markers, borrowed material or phonological material. Do not classify every final segment as a suffix without a morphological paradigm and evidence of function.

### 6. Lessons 10–12 and 40–43, 49 — clitic form does not identify function
The material appropriately warns that forms such as `ـم، ـت، ـی، ـمان، ـتان، ـیان` can encode different grammatical relations depending on host, clause structure, transitivity, tense/aspect and dialect. Preserve the contrast among independent pronoun, clitic pronoun, possessive marking and verbal person marking. Never use the graphic form alone as the answer key.

## Quiz and runtime caution
The structured quiz field is present for Lessons 1–31; later lessons remain without structured runtime quizzes in the current course data. This round did not modify quiz questions, answer indices, explanations, raw lesson text, or runtime files. Any future quiz that asks students to distinguish prefix, suffix, clitic, preposition and verbal particle must provide a full contextual example and specify the analytical framework/dialect where needed.

## Recommended patch queue
1. Apply only the two clear Lesson 11 wording corrections above in an append-only patch after a separate exact diff review.
2. Keep Lesson 14 phrase unresolved until the lesson's intended syntactic category (function vs constituent) is confirmed.
3. Add a compact contrast table to the relevant lesson appendix only if it can be done without duplicating or deleting existing material.
4. Do not globally replace `پێشگر`, `پاشبەستە`, or `پارتیکڵ`; perform occurrence-specific review.
5. Do not create a new lesson; the course remains capped at 50.

## Safety and preservation
- No raw lesson source changed.
- No structured quiz or answer key changed.
- No runtime/database/Botkeep/Telegram changes.
- No deployment, merge, or production action performed.
- This report is an append-only audit artifact; academic sign-off for dialect-sensitive examples remains separate.

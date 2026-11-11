# Course 4 — terminology register draft (not approved)
Date: 2026-11-11
Repository: avasinim/KejyarBot
Branch at creation: release/main-based-reconciled-2026-11-11
Status: audit artifact only; no academic term is approved by this document.

## Purpose and rules

This is a controlled register for reconciling terms across lesson source drafts, preserved append-only patches, the 2026-11-08 31-lesson Preservation Bundle, and the current 50-lesson Beta runtime. It is not a replacement for lesson text or an instruction to apply patches.

For every term, retain:
- English concept label and scope/definition;
- exact Kurdish form used in each source layer;
- first lesson introducing the concept and later lesson references;
- provenance (source file, patch filename and SHA-256, bundle/runtime blob SHA);
- decision status: unresolved, evidence-reviewed, owner-approved, or superseded (never infer approval from CI);
- cross-reference and aliases without silently treating distinct concepts as synonyms.

Rules:
1. Never overwrite or delete an earlier term form; record changes as dated decisions.
2. Never equate Root and Stem, Affix and Clitic, Subject and Agent, or Object and Patient solely because they overlap in examples.
3. Distinguish morphology, syntax, semantic role, and orthographic representation.
4. A term may be dialect-specific; do not generalize a Sorani example to all Kurdish varieties.
5. Missing baseline/source evidence means fail closed: leave unresolved.
6. Patches remain archival until their schema, baseline, identity, idempotency and terminology crosswalk are validated.

## Candidate register — unresolved entries

| English term | Kurdish form(s) observed | Scope / distinction to preserve | Evidence locations | Status |
|---|---|---|---|---|
| Enclitic | پاشبەستە (patches 11–13); پاشنووس (runtime 11–13) | Must not be collapsed into Suffix; enclitic is attached to a host but its grammatical status differs from an affix. | Patches 11, 12, 13; runtime appendices 11–13; Appendix 9.52 | unresolved |
| Affix | ئەفیکس (patches 13 and 26); گیرەک (runtime 13 and 26) | Must be distinguished from the broader bound-morpheme category and from Clitic/Enclitic; Prefix and Suffix are subtypes in the cited patch terminology. | Patches 13, 26; runtime appendices 13, 26; Appendix 9.52 | unresolved |
| Clitic | لکاو | Broad category in patch 13; do not assume every clitic is enclitic or a suffix. | Patch 13; Lesson 11–12 material | evidence located; mapping not approved |
| Clitic pronoun | جێناوی لکاو | A pronominal clitic; distinguish word class/form from grammatical function such as Subject or Object. | Patch 13; Lesson 11–12 material | evidence located; mapping not approved |
| Prefix | پێشگر | Affixal position/type; distinguish from verbal particle when the theoretical analysis treats particles separately. | Patch 13; patches 29–30 | evidence located; mapping not approved |
| Suffix | پاشگر | Affixal position/type; not synonymous with Enclitic. | Patch 13; patches 11–13 | evidence located; mapping not approved |
| Inflection | لەچۆنایەتی (patch 29); گەردان (runtime 29–30) | Morphological inflection; distinguish from derivation and from conjugation if the course uses a narrower sense. | Patch 29; patch 30; runtime 29–30; Appendix 9.52 | unresolved |
| Noun Phrase | گروپی ناوی (patch 31-v2); گرێی ناوی (runtime 31) | Phrase constituent, not automatically a single word or a word-class label. Preserve source/variant history. | Patch 31-v2; runtime Lesson 31; Appendices 9.48, 9.51, 9.52 | unresolved |
| Root | ڕەگ | Lexical/root base; do not use as a synonym for Stem. | Patches 11, 13, 29; runtime appendix | evidence located; mapping not approved |
| Verb stem | بنج | Inflectional stem form; distinguish from lexical Root and from present/past stems. | Patches 11, 13, 29; runtime appendix | evidence located; mapping not approved |
| Present stem | بنجی ئێستا | A specific stem form; must be supported by the verb paradigm, not mechanically derived from the infinitive. | Patch 13; runtime appendix | evidence located; mapping not approved |
| Past stem | بنجی ڕابردوو | A specific stem form; keep distinct from present stem. | Patch 13; runtime appendix | evidence located; mapping not approved |
| Subject | بکەر (patch/source terminology); بابەت (runtime terminology noted in prior audit) | Grammatical relation; do not conflate with Agent or discourse Topic. Requires source/framework review before choosing a Kurdish label. | Lesson 31 terminology notes; patches 31/33; Appendix 9.50 and prior audits | unresolved |
| Agent | ئەنجامدەری کردار | Semantic role, not necessarily the grammatical Subject; passive examples distinguish them. | Patch 33; patch 44; supplied Lesson 44 addendum | evidence located; mapping not approved |
| Grammatical Subject | بکەری ڕێزمانی | Syntactic function; must be distinguished from Agent and from Topic. | Patch 44; supplied Lesson 44 addendum | evidence located; mapping not approved |
| Object | بەرکار | Syntactic function; distinguish direct object and other complements. | Patches 12, 44; source audits | evidence located; mapping not approved |
| Patient | بەشداربووی کاریگەری‌وەرگر | Semantic role; do not assume every Object is a Patient. | Patch 44 | evidence located; mapping not approved |
| Derivation | داڕێژە / داڕێژەیی | Word-formation process; distinguish from Inflection. Exact preferred form awaits whole-course audit. | Patch 29 | unresolved |
| Verbal particle | پارتیکڵی کردار | Theoretical classification may vary; distinguish from derivational affix and do not classify by spelling alone. | Patches 29–30 | evidence located; mapping not approved |

## Cross-course consistency checks required

- Search every lesson and appendix for each English term and each Kurdish variant, including inflected and compound forms.
- Record first introduction and all later uses; a later use must retain the same sense or explicitly declare a changed sense.
- Compare patch text with source markdown and runtime separately. Similar item counts do not establish textual equivalence.
- Verify every citation and its exact claim. A cited framework does not automatically validate newly authored Sorani examples.
- Test terminology in quiz questions, answer options and explanations; a terminology collision can invalidate a multiple-choice distinction even if the answer index remains unchanged.
- Keep Lesson 13's status `internal_cross_lesson_synthesis_no_external_source_mapping` and review-only eligibility unchanged.
- Keep owner-review-pending lessons out of official assessment/rewards until their approval gate is independently verified.

## Provenance and limitations

- Patch inventory and hashes are preserved in Library README artifacts; patches are not automatically consumed by the production runtime.
- Current runtime and Preservation Bundle are distinct snapshots. Appendix 9.51 documents 24/31 exact lesson matches and seven content differences.
- The exact authoritative source/baseline for every term is not yet mapped. This draft therefore deliberately does not select between competing Kurdish forms.
- No lesson, patch, quiz, runtime, status, database, Botkeep, or Telegram data was changed by creating this register.


## Evidence refinement — 2026-11-11 (append-only)

The following distinctions were confirmed by reading the complete preserved patches for Lessons 12, 13, 26 and 29. They refine the candidate register but do not approve any term.

### Lesson 12 — one surface form, more than one function
- `ـیان` is shown in `دەفتەرەکەیانە` as possessive, while in `ئاڕگەش و فەرزانە نامەکەیان نووسی` the patch gives a possible past-transitive subject-marking reading.
- The patch explicitly asks for context-sensitive interpretation. The register must therefore store form + host + construction + reading, not map the string `ـیان` to one fixed grammatical function.
- The patch also distinguishes word class/form (`جێناوی لکاو`) from grammatical functions such as Subject/Object and the relation of possession.

### Lesson 13 — Root, Stem and clitic boundaries
- The patch explicitly says Root and Stem are not synonyms; present and past stems are to be established through a verb paradigm, not by imagined segmentation.
- It distinguishes Prefix/Suffix as bound affixal morphology from Enclitic attached to a host. This supports keeping the Enclitic/Affix collision unresolved rather than merging them.
- Its examples are declared pedagogical Sorani examples, not direct quotations from Saeed Karimi.

### Lesson 26 — discourse particle vs bound focus clitic
- The lesson is explicitly scoped to narrow discourse particles in Sorani; it warns that not every item called a particle in other sources belongs to this category.
- `ـیش` in `منیش` is described as a bound additive/focus clitic, not an independent discourse particle.
- `خۆ` and `ئەوە` are not classified by form alone; `ئەوە` may be a discourse particle in one context and an independent demonstrative pronoun in another.
- Radnia (2022) is described in the patch as based on author observations because no Kurdish conversational corpus was available; its evidence is characterized as descriptive/preliminary, not representative of all Sorani.

### Lesson 29 — derivation, inflection and verbal particles
- The patch explicitly distinguishes Derivation from Inflection: derivation may create a new lexeme, while inflection changes the grammatical form of the same lexeme.
- It distinguishes verbal particles such as `هەڵـ` from derivational affixes such as `ـاند`; spelling/spacing alone is not a sufficient morphological classification criterion.
- The function of `ـەوە` is context-sensitive and must not automatically be treated as derivational.

### Register implications
- Add contextual fields for host, construction, syntactic/semantic function, dialect scope, evidence type and confidence.
- Preserve alternative analyses when a patch itself identifies ambiguity.
- Do not use a term list as a substitute for full clause-level examples and paradigms.
- Keep every claim tied to its actual source; do not present the pedagogical examples as corpus attestations or quotations from the cited book.


## Lexical first-occurrence scan — current 50-lesson runtime (2026-11-11)

Runtime source: `course_data/grammar_course4_lessons.json`, blob SHA `1dd8abe8a128937c74a18cf04f99878b2e38d962`, 50 lesson records. The scan checks the lesson JSON text fields with Unicode letter-boundary matching; it is a lexical locator, not a semantic determination of where a concept is taught or defined. English and Kurdish forms are listed separately where their first occurrences differ.

| Search concept | Earliest exact lexical hit in runtime | Later lesson hits (same scan) | Limitation / interpretation |
|---|---|---|---|
| Enclitic | Lesson 11: Enclitic, پاشبەستە, پاشنووس | 12, 13 | Both Kurdish forms occur in the runtime; this is a collision, not a settled synonym mapping. |
| Affix | Lesson 13: Affix, گیرەک | 26 | ئەفیکس is present in preserved patch evidence, not in this runtime scan. |
| Clitic | Lesson 3: لکاو | 11, 12, 13, 17, 26, 27, 40, 42, 43, 45, 47, 49, 50 | Earliest token does not prove Lesson 3 formally defines the category. |
| Clitic pronoun | Lesson 11: Clitic pronoun, جێناوی لکاو | 12, 13, 17, 40, 42, 43, 45, 49 | Keep distinct from the broader Clitic category and from grammatical function. |
| Prefix | Lesson 5: پێشگر | 7, 9, 10, 12, 13, 14, 15, 16, 17, 20, 26, 27, 29, 30, 39, 42 | Earliest hit is Kurdish only; English label first appears in Lesson 13/29. |
| Suffix | Lesson 3: پاشگر | 5, 6, 7, 9, 11, 12, 13, 15, 16, 27, 28, 29, 30, 34, 49 | Do not infer equivalence with Enclitic. |
| Inflection | Lesson 28: Inflection | 29, 30, 31 | The Kurdish variants لەچۆنایەتی and گەردان are found in Lessons 29–30; first lexical hit does not resolve preferred form. |
| Noun Phrase | Lesson 3: گرێی ناوی | 22, 23, 24, 25, 31, 32, 33, 34, 47, 49, 50 | Patch 31-v2 also contains گروپی ناوی; runtime scan finds both forms in Lesson 31. |
| Root | Lesson 3: ڕەگ | 13, 15, 16, 17, 29 | Root appears explicitly in English in Lesson 13/29; Kurdish lexical hit in Lesson 3 is not proof of a technical Root definition there. |
| Stem | Lesson 13: Stem, بنج | 16, 28, 29 | Earlier lesson 7 contains بنج only as part of other lexical material; exact-token scan first finds it in 13. |
| Subject | Lesson 1: بابەت; explicit English Subject first appears in Lesson 12; بکەر is not interchangeable by assumption | 3, 6, 8, 10–20, 31–50 (varies by form) | بابەت may denote Topic/subject matter in context; this scan cannot equate it with grammatical Subject. Track بابەت, بکەر and Subject as separate entries until context is reviewed. |
| Agent | Lesson 18: ئەنجامدەری کردار | 32, 33, 34, 39, 42, 43, 44, 45, 48, 49, 50 | Semantic role; not synonymous with grammatical Subject. |
| Object | Lesson 3: بەرکار | 11–14, 18–20, 31–50 (varies by lesson) | Do not infer Patient role from Object label. |
| Patient | No exact lexical hit among the candidate Kurdish/English forms searched | none | Absence from this scan does not prove absence of the concept under another label; source/lesson review remains open. |
| Derivation | Lesson 5: Derivation | 29 | Kurdish داڕێژە has an earlier lexical hit in Lesson 3; definition and scope need context review. |
| Verbal particle | Lesson 29: verbal particle, پارتیکڵی کردار | 30 | General پارتیکڵ appears earlier, but the compound concept first appears in 29. |

### Correction to the candidate register's earlier assumptions
- Noun Phrase has an earlier runtime lexical hit in Lesson 3, not only Lesson 31.
- Prefix has an earlier Kurdish lexical hit in Lesson 5.
- Suffix and Root have earlier Kurdish lexical hits in Lesson 3.
- The earlier register entry that treated Subject/بکەر/بابەت as one mapped set was too compressed. These are now separate unresolved labels; context must determine whether بابەت is Topic, grammatical Subject, or another use in each occurrence.
- Stem's exact-token first hit is Lesson 13; an earlier raw substring match in Lesson 7 was a false positive.
- Patient has no exact hit under the candidate forms searched. It must not be added as if runtime already teaches it.

### Next verification gate
A lexical scan cannot identify pedagogical first introduction. For each candidate, inspect the full lesson context at the earliest hit, identify explicit definition/learning objective/example vs incidental mention, and then check source drafts and patches. Record the first *defined* lesson separately from the first *mentioned* lesson. Do not normalize terms until that review is complete.

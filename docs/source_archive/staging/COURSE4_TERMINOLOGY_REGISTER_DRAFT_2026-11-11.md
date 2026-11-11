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

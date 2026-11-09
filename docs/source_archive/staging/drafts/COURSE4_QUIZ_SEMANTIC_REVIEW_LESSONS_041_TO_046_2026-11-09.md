# COURSE 4 — Final Quiz Semantic Review: Lessons 041–046
Date: 2026-11-09

## Scope
Repository: avasinim/KejyarBot
Source: course_data/grammar_course4_lessons.json
Source branch: main
Lessons: grammar_41–grammar_46
All six lessons currently have status owner_review_pending_expanded_draft.
All six have empty structured quiz arrays; Lessons 41–45 contain quiz text in key_points, and Lesson 46 contains quiz text in key_points/source_markdown.
This is a review and approval-readiness report only. No lesson source, status, quiz JSON, runtime, database, or deployment was modified.

## Executive decision
The six lessons are NOT ready for automatic approval as a group. They contain valuable and largely coherent instructional material, but several owner-level terminology choices, dialect-sensitive analyses, example naturalness checks, and at least one clear quiz-answer conflict must be resolved first.

## Lesson 41 — Simple and compound verbs; relation to objects
Five two-option questions found in key_points; structured quiz empty.
- The distinction between morphological structure (simple/compound) and syntactic transitivity is conceptually sound.
- Q1 correctly treats simple/compound and transitive/intransitive as independent dimensions.
- Q2 «ئەو نانەکەی خوارد» identifies «نانەکە» as object; intended answer aligns.
- Q3 treats «شەڕ» in «ئەو شەڕی کرد» as nominal component of a compound predicate. This is plausible as a teaching analysis but must be verified against the chosen Sorani framework; do not present as universal without source support.
- Q4 correctly rejects that all compound verbs are transitive.
- Q5 correctly treats «نانخۆرەکە» as a noun/subject, not a verb.
Readiness issues:
1. The distinction between lexical compound verb, light-verb construction, and complex predicate must align with Lessons 41–42 and prior L41–45 audits.
2. «قسەی کرد»، «شەڕی کرد»، «سوێندم خوارد» require a stable analysis of the nominal component and person clitics; orthographic spacing alone is not proof.
3. Source text itself flags «نانخواردن» vs «نان خواردن» and several compounds for native-speaker/source verification.
4. Quiz uses only two options; expand plausible distractors after the analyses are approved.

## Lesson 42 — Clitic pronouns and object function
Five two-option questions found; structured quiz empty.
- Q1 «کتێبەکەم»: ـم expresses possession; aligned.
- Q2 in «کتێبەکەم خوێندەوە», the whole NP is object, not ـم alone; aligned.
- Q3 «من ئەو دەناسم»: «ئەو» is object; aligned.
- Q4 correctly rejects clitic position as a standalone test of grammatical function.
- Q5 correctly calls for dialect, context, and morphological segmentation.
Readiness issues:
1. The lesson's central separation of NP function from internal clitic function is valuable and must be retained.
2. The description of clitic as a phonological/grammatical dependent should cite the chosen framework and be consistent across the course.
3. Past-transitive examples require explicit distinction between possessive suffix on a noun and ergative/agent-related person clitic hosted on an object NP.
4. Ensure no blanket list of ـم/ـت/ـی etc. implies each form has one function in every construction.

## Lesson 43 — Clitics in transitive verbs
Five two-option questions found; structured quiz empty.
- Q1 «من ئەو دەناسم»: «ئەو» as object; aligned.
- Q2 «کتێبەکەی خوێندەوە»: quiz marks ـی as possessive; this is a HIGH-RISK inconsistency. In Sorani past-transitive constructions, the suffix hosted by the object NP may mark the agent/person (ergative alignment), not possession. The example is under-specified without full context and dialect analysis. The key must not be approved as written.
- Q3 correctly rejects that every clitic on a verb is an object.
- Q4 appropriately requires full sentence, dialect and context for «گرتمن».
- Q5 identifies the understood second-person subject of the imperative; aligned at introductory level.
Readiness issues:
1. Resolve the Q2 analysis with authoritative Sorani grammar/reference and a fully contextualized example.
2. Align with Lessons 12, 18, 25, 39, 40, 42 and the previous audits of Lessons 43 and 45.
3. Define which clitics are object clitics, agent/person clitics, possessive suffixes, or agreement markers in the adopted framework.
4. Avoid teaching «ـی» as possessive by form alone.

## Lesson 44 — Object in passive clauses; grammatical subject and agent
Five two-option questions found; structured quiz empty.
- Q1 «وانەکە نووسرا»: intended grammatical subject analysis is consistent with passive promotion.
- Q2 «مامۆستا» in the by-phrase is intended as semantic agent, not grammatical subject; conceptually aligned, but the naturalness and exact status of «لەلایەن» in the Sorani example needs dialect/source verification.
- Q3 correctly distinguishes intransitive «کەژیار هات» from passive.
- Q4 correctly says agent need not be overt.
- Q5 correctly tests promotion of the active object to grammatical subject in the standard passive pattern.
Readiness issues:
1. Distinguish passive from middle, anticausative, resultative and impersonal constructions.
2. Verify whether the examples are genuinely passive in the target Sorani dialect and whether «نووسرا» has the intended voice analysis.
3. Keep grammatical Subject distinct from semantic Agent, consistent with Lessons 39–40 and 44.
4. Quiz distractors are binary; add nuanced alternatives only after source validation.

## Lesson 45 — Word order and object fronting
Five two-option questions found; structured quiz empty.
- Q1 fronted «نامەکە» remains object in the intended analysis; aligned, but example punctuation/prosody and naturalness should be verified.
- Q2 correctly rejects initial position as sufficient proof of subjecthood.
- Q3 topic establishes discourse topic; aligned.
- Q4 focus highlights selected information; aligned.
- Q5 in «ئاڕگەش کەژیاری بینی» identifies «ئاڕگەش» as subject; intended basic SOV parse.
Readiness issues:
1. Keep Object Fronting, Topicalization, Left Dislocation and Focus distinct; they are not interchangeable.
2. Verify prosody, punctuation and naturalness of fronted-object examples with native Sorani speaker/source.
3. The source draft itself says word order may affect grammatical function/meaning in some constructions; qualify claims carefully.
4. Binary options make the quiz weak as an assessment. Improve after examples are confirmed.

## Lesson 46 — Simple, compound, complex, compound-complex sentences
Five three-option questions found; structured quiz empty; comprehension items are structured (six).
- Q1 simple sentence example: intended classification as one independent clause; verify embedded clitic morphology is irrelevant to clause count.
- Q2 conditional subordinate clause: aligned.
- Q3 causal subordinate clause: aligned.
- Q4 compound sentence as two or more coordinated independent clauses: aligned.
- Q5 complex sentence as main clause plus at least one subordinate clause: aligned.
Readiness issues:
1. Adopt one taxonomy consistently with Lessons 37–38: simple = one independent clause; compound = 2+ coordinated independent clauses; complex = one main clause plus subordinate clause; compound-complex = 2+ independent clauses plus at least one subordinate clause.
2. Owner decision required on «بەرڕستە» vs «ژێرەڕستە».
3. Normalize «هاولکی هاوئاست» and «بەستەری ژێرکەر/هاولکی بەرخەر» after owner decision.
4. Validate examples «ئاڕگەشیش نووسینی کرد» and compound-complex example for naturalness and clause boundaries.
5. Maintain the distinction between clause count and verb count, and between coordinator and discourse connector.

## Critical cross-course blockers
1. **Clitic ـی:** Lesson 43 Q2's possessive answer conflicts with the distinction required by Sorani past-transitive constructions. Must be resolved before approval.
2. **Compound predicate taxonomy:** lexical compound verb vs light-verb construction vs complex predicate requires one explicit framework and examples.
3. **Passive voice:** validate actual Sorani passive morphology and separate passive from intransitive/middle/anticausative.
4. **Clause terminology:** owner must decide «بەرڕستە» vs «ژێرەڕستە» and the coordinator/subordinator terminology.
5. **Object/Recipient/Complement/Adjunct:** keep grammatical function distinct from semantic role and optional adjunct status.
6. **Dialect/source provenance:** several examples are explicitly draft/preliminary and lack independently verified source/page mapping. Do not describe them as externally validated.

## Approval gates and exact work needed
### Gate A — owner decisions
The following decisions must be explicit and recorded:
- Preferred term for Subordinate Clause: «بەرڕستە» or «ژێرەڕستە».
- Preferred distinction and Kurdish labels for Subject, Agent, Object, Recipient/Indirect Object, Complement and Adjunct.
- Adopted analysis of ـی/ـم in past-transitive Sorani constructions and the dialect to which it applies.
- Taxonomy for compound verb, light-verb construction and complex predicate.
- Approved terminology for coordinating conjunction and subordinating conjunction.

### Gate B — source verification
- Map each key claim and example to a real, inspectable reference with exact page/section when available.
- Verify dialect, morphology, naturalness and punctuation with the target Sorani standard.
- Preserve uncertainty where no source is available; do not fabricate page references.

### Gate C — content correction and quiz QA
- Fix Lesson 43 Q2 only after Gate A/B; audit all related occurrences across Lessons 12, 18, 25, 39, 40, 42 and 43.
- Improve binary distractors in Lessons 41–45.
- Check each quiz answer and explanation against the final lesson text.
- Preserve original draft content append-only; retain a patch/change log and before/after source hashes.

### Gate D — structured runtime readiness
- Convert only approved questions to structured quiz objects (question, options, answer index, explanation).
- Preserve all source Markdown and answer keys; do not make answer keys learner-visible.
- Add schema/semantic validation and regression tests.
- Confirm pending-review guard blocks draft lessons from menu, quiz start and final reward.
- Only after explicit approval should status be changed and a separate deployment authorization considered.

## Approval status
Lessons 41–46 remain owner_review_pending_expanded_draft.
This report does not approve them and does not change their status. The user's request to prepare them for approval is recorded as authorization to carry out review and preparation, not a substitute for unresolved linguistic decisions or source verification.
No tests were run. No code, JSON, DB, runtime, Botkeep, Telegram or main branch changes were made.

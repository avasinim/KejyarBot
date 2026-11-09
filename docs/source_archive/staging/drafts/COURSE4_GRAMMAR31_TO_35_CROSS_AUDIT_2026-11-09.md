# Course 4 — Lessons 31–35 cross-audit
Date: 2026-11-09
Repository: avasinim/KejyarBot
Source: course_data/grammar_course4_lessons.json on main
Scope: grammar_31 to grammar_35; cross-lesson checks against Lessons 11–17 and 28–30. Audit only.

## Critical provenance and release gate
1. Lessons 32–35 are explicitly marked in their own draft text as Course 1, Section 4 materials, with owner-source segment files dated 2026-11-08; their review status is «owner_review_pending_expanded_draft», and their text says runtime false. Do not silently treat them as approved Course 4 curriculum or activate them.
2. Lesson 31 is a developed grammar lesson with named academic sources and explicit scope limits. Keep its source claims distinct from the owner-draft status of Lessons 32–35.
3. The five lessons must be retained as present in the JSON, but the course identity, ordering and activation status require owner confirmation before any runtime migration.

## Lesson 31 — nominalization and infinitive in nominal function
1. Preserve the distinction between infinitive (چاوگ), verbal nominalization (ناوکردنی کردار) and an ordinary lexical noun. A form ending in «ـن» is not automatically a nominalized infinitive.
2. In Kareem (2016), §4.5, pp.112–114, the example «کوشتنی ئاژەڵەکە خراپ بوو» is analyzed as a nominalized verbal form. The ezafe links the nominalized predicate with its Theme participant; it is not literal possession.
3. Salavati & Ahmadi (2018), Figure 1, pp.2–3, gives «ناوەندەکانی دەنگدانمان» as evidence of a non-finite verb inside an NP with a possessive marker. Preserve the source's own analysis and do not generalize every nominalized form to every nominal inflection.
4. The source explicitly rejects an unsupported closed list of «five nominal properties» and «seven syntactic functions». Keep this evidence boundary; do not reintroduce those counts as settled facts.
5. Subject use is supported by the cited examples; object and prepositional-complement uses are presented as pedagogical possibilities pending Sorani corpus/speaker evidence. Label them accordingly.
6. Keep the contrast with Lesson 30: nominalized verb functions within an NP; NV+LV complex predicate is a verbal construction. They are related but not identical.
7. In «ناوەندەکانی دەنگدانمان», the suffix «ـمان» is attached to «دەنگدان» in the cited analysis; do not claim all nominal markers freely attach to every infinitive.

## Lesson 32 — sentence foundations and constituents
1. The draft correctly distinguishes phrase structure (NP/VP) from grammatical functions (Subject/Predicate). Do not equate NP with Subject or VP with Predicate in every sentence.
2. Subject is a grammatical relation, not necessarily an Agent. Cross-reference Lesson 33 and Lesson 12's agent/possessor/object distinctions.
3. The sentence definition must not be reduced to «a set of words with complete meaning»; grammatical relations, clause structure and discourse function matter.
4. Not every sentence has an overt two-word Subject + Verb sequence: imperatives can have an unexpressed subject, and other clause types need separate analysis.
5. Keep the draft's distinction between lexical category, phrase type and syntactic function; these are three different descriptive levels.
6. The draft's source label and status identify it as Course 1, Section 4, owner-review pending, runtime false. It is not approved Course 4 material merely because it appears in the Course 4 JSON.

## Lesson 33 — subject, verb and semantic roles
1. Preserve Subject (بکەر) as a grammatical function and Agent (ئەنجامدەر) as a semantic role. The Subject can be a non-Agent, e.g. the grammatical subject of a passive clause.
2. A subject definition as «the person who performs the action» is invalid as a universal rule.
3. Keep Agent distinct from Theme/Patient, possessor and other participant roles; do not infer semantic role from Subject position alone.
4. In active/passive comparisons, identify grammatical subject separately from the participant that performs or undergoes the event. Check agreement and argument realization in the actual Sorani variety.
5. Examples must be checked for consistency of names, verb form, transitivity and clause interpretation; the source draft itself flags an erroneous name in a later copular example (Lesson 34).
6. This is an owner-review draft marked Course 1, Section 4 and runtime false; preserve that release gate.

## Lesson 34 — subject, predicate and copula
1. Distinguish Subject (نیهاد/بکەر), Predicate (گوزارە) and Copula/Linking Verb (کاری بەستەر). Predicate is the whole constituent that says something about the Subject; copula is only a component of that predicate.
2. The draft's own note leaves unresolved whether «نیهاد» should be treated as a synonym of «بکەر» in the course terminology. Do not standardize the two without an explicit terminology decision and framework definition.
3. Forms «ـە»، «بوو» and «دەبێت» must be analyzed in context. «بوو» can be a lexical verb or copula; «دەبێت» can express necessity or becoming; it is not always a copula.
4. Avoid a blanket division of all verbs into «complete/incomplete». The draft itself notes this is not scientifically adequate as a general classification.
5. Correct the mismatch between the sentence «فەرزانە گەنجێکی ڕۆشنبیرە» and the stray name «ئاڕگەش» in its analysis; preserve the original source separately and record the correction only in the review layer.
6. The draft is Course 1, Section 4, owner-review pending, runtime false. Its terminology remains provisional.

## Lesson 35 — sentence types by communicative purpose
1. The four-way classification (declarative, directive/imperative, interrogative, exclamative) is by communicative purpose, not by syntactic structure. Do not conflate it with later structural clause classifications.
2. Directive sentences include requests, instructions, invitations and commands; not every directive is a forceful command.
3. Interrogatives include open questions and yes/no questions; «ئایا» is one strategy, not a mandatory marker for all questions.
4. Exclamative utterance type is not established solely by punctuation or the presence of an interjection. Intonation, context and communicative purpose matter.
5. Punctuation is a written convention and does not independently determine sentence type. A directive can end with a period or exclamation mark according to tone.
6. Keep interjections (Lesson 27), exclamative sentence type (Lesson 35), and vocatives (Lesson 24) distinct.
7. This is an owner-review draft explicitly marked Course 1, Section 4 and runtime false; do not treat as approved Course 4 content.

## Cross-lesson consistency controls
- Lessons 11–12/33: Subject ≠ Agent ≠ Patient/Theme ≠ Possessor.
- Lessons 28–31: infinitive ≠ past stem ≠ nominalized verbal form ≠ lexical noun.
- Lessons 30–31: complex predicate NV+LV ≠ nominalization.
- Lessons 32–34: phrase type (NP/VP) ≠ grammatical function (Subject/Predicate) ≠ lexical category.
- Lessons 32–34: Subject/نیهاد terminology requires one explicit course-wide decision; do not silently merge or split labels.
- Lessons 24/27/35: vocative ≠ interjection ≠ exclamative sentence type.
- Lessons 18/33: grammatical Subject in passive clauses ≠ Agent.
- Maintain source provenance, dialect scope, owner-review and runtime gates.

## Recommended editorial actions — append/clarify only
1. Preserve Lesson 31's sourced nominalization analysis and its explicit rejection of unsupported property/function counts.
2. Add a diagram to Lesson 32 separating lexical category → phrase type → grammatical function; retain counterexamples to NP=Subject and VP=Predicate.
3. In Lesson 33, add an argument-role table (Subject, Agent, Theme/Patient, Possessor) with active/passive contrasts grounded in Sorani examples.
4. In Lesson 34, resolve «نیهاد» vs «بکەر» only through an explicit owner-approved terminology register; distinguish predicate from copula and contextual readings of «بوو/دەبێت».
5. In Lesson 35, add paired examples where punctuation changes but communicative purpose remains, and vice versa; keep interjection/vocative distinction visible.
6. Keep Lessons 32–35 marked Course 1, owner-review pending and runtime false until explicit owner decision. No silent course reassignment or activation.

## Preservation status
No source JSON modified. No original lesson item or example deleted or overwritten. No main-branch commit, Botkeep deployment or Telegram activation. Audit-only archival note.

# Course 4 — Lesson 40 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of main-branch Course 4 JSON Lesson 40, expanded draft, and the Lessons 39–45 composite source. Append-only audit artifact; not an approved lesson revision.

## 1. Provenance verified
- Main JSON: `course_data/grammar_course4_lessons.json`, main blob `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`.
- Lesson record: `grammar_40`, number 40, title `وانەی 40: کاری تێپەڕ و کاری تێنەپەڕ`, status `owner_review_pending_expanded_draft`.
- Composite source: `docs/source_archive/COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md`, blob `8c2668b3225269fa3ac47db989a4d3db1e1d50c1`, 3125 lines. Its opening section identifies itself as preserved user-supplied source text and explicitly warns that the composite later includes review, planning, and expanded lesson material. The raw material includes the original body-part test, suffix/passive tests, clitic paradigms, lexicalized compound-verb discussion, and the proposed seven-lesson split. Do not call the whole composite a raw transcript.
- Expanded draft: `docs/source_archive/staging/drafts/COURSE4_LESSON_040_EXPANDED_DRAFT_2026-11-08.md`, blob `d5d3abe2b5238b59cc55418f43012d5ae556ae04`, 248 lines / 10616 characters.
- The literal transcript path cited by the draft, `docs/source_archive/staging/drafts/COURSE4_LESSON_040_DRAFT_TRANSCRIPT_SEGMENT_2026-11-08.md`, returned 404. The composite source exists, but the JSON/draft's specific segment reference is stale or misnamed. Provenance should be repaired only in a separately approved patch.

## 2. Current JSON shape and mismatches
- Objectives include transitivity, direct object, lexical capacity vs sentence use, object omission, active/passive, and the independence of lexical compoundhood from transitivity.
- `examples=[]`, `quiz=[]`, `comprehension=[]`, while the Markdown includes worked examples and five multiple-choice questions.
- `key_points[0]` contains the full lesson rather than concise key points.
- The `exercises` array mixes metadata/provenance statements with the actual exercise prompts.
- The expanded draft has a section-numbering gap: section 13 is followed by section 15; the JSON long Markdown includes sections 14–17. The version difference must be reconciled, not silently ignored.
- Metadata says `کۆرسی: ١ — بەشی ٤`, inconsistent with Course 4 repository placement. Treat as metadata requiring owner-approved correction.
- The JSON's `source_path` points to the expanded draft, while the draft itself cites a nonexistent transcript segment. Source lineage is therefore incomplete at the segment-reference level.

## 3. Conceptual findings

### 3.1 Transitivity is about valency/argument structure, not anatomy
The raw source's proposed test—whether all human body parts participate in an action—is not a linguistic diagnostic. Examples such as eating, speaking, seeing, hearing, holding, walking, and going cannot be classified by counting body parts.
Transitivity concerns the verb's argument structure and the syntactic realization of its arguments in a construction. Semantic affectedness is not required: cognition/perception predicates can take objects without physical change. Preserve the expanded draft's rejection of the body-part test.

### 3.2 Lexical transitivity versus construction-level realization
The draft usefully distinguishes a verb's lexical potential to take an object from whether an overt object is expressed in a particular clause. Refine this further:
- distinguish a verb's lexical valency/frame from a construction's realized arguments;
- distinguish an overt object from an implicit, recoverable, generic, or contextually omitted object;
- do not assume that every missing object is a freely omitted object; some predicates/constructions license objectless uses, while others may require a contextually understood complement.
A sentence such as `فەرزانە خوێندەوە` cannot be judged grammatical or ungrammatical without its intended reading, dialect, discourse context, and the verb's construction. The source's asterisked example based on a Chomskyan claim needs a precise bibliographic citation and a clear statement of the analysis; do not attribute the judgment to Chomsky without identifying the work, example, and framework.

### 3.3 Object omission, implicit object, and generic/intransitive use
The draft separates Object Omission/Object Drop from an objectless use, but the distinction is not yet sufficiently operational. It should include contrastive diagnostics:
- recoverable specific object from prior discourse;
- generic object interpretation (e.g. habitual activity such as reading);
- lexical/inherent object incorporated in a compound predicate;
- genuinely intransitive lexical frame.
Do not define omission only as "the object exists in meaning"; discourse recoverability and constructional licensing must be demonstrated. Avoid treating every contextually interpretable activity as a syntactically omitted object.

### 3.4 Alternating transitive/intransitive uses
The examples `ئەو پەنجەرەکەی شکاند` versus `جامەکە شکایەوە` are not necessarily a clean alternation of the same verb: the forms/lexemes and causative/inchoative morphology need checking. A better analysis should distinguish:
- transitive causative construction with an Agent/Causer and an Object/Theme;
- intransitive inchoative or change-of-state construction with a Theme as grammatical Subject;
- lexical alternation versus morphological derivation.
Likewise `کردەوە/کرایەوە` involves voice/morphological structure and must be coordinated with Lesson44; passive formation is not the same as an intransitive lexical use.

### 3.5 Passive formation is a diagnostic, not an absolute test
The draft correctly says active-to-passive transformation is a useful but non-universal diagnostic. Preserve the caveat. Not all transitive predicates passivize equally, and a passive construction's grammatical Subject is not thereby an Agent. Keep the distinction aligned with Lesson44 and avoid claiming passive morphology alone establishes all aspects of transitivity.

### 3.6 Clitic pronouns are not a universal transitivity test
The raw source's rule that transitive verbs generally take `مان، تان، یان` while intransitives cannot take them is overgeneralized. Clitics can encode different relations depending on tense/aspect, person, dialect, and construction. Their role must be parsed in context. The detailed paradigms belong in Lessons42–43; Lesson40 should only state that clitic presence is not a standalone diagnostic.

### 3.7 Lexicalized compound verbs and internal nominal components
The source's central Kurdish-specific observation is important: forms such as `نان خواردن`, `قسەکردن`, `شەڕکردن`, `سوێندخواردن`, and `ئیشکردن` can have lexicalized nominal + light-verb structure, where the nominal component may appear object-like in syntax without necessarily being an independent external object.
The draft includes an extended discussion in sections 11–12, but the agreed lesson plan assigns this topic to Lesson41. Keep only a brief signpost in Lesson40; move the full analysis and examples to Lesson41 through an approved patch. Do not force these constructions into transitive or intransitive categories solely from surface form.

### 3.8 Lexical compoundhood versus transitivity
The draft correctly distinguishes lexical composition (simple/compound) from transitivity (argument structure). This is an important cross-cutting rule and should remain. However, examples must distinguish lexicalized compounds from productive noun + verb phrases and light-verb constructions. The classification of `قسەکردن`, `نان خواردن`, and similar forms requires lexical evidence and construction-level analysis, not orthographic spacing alone.

### 3.9 Terminology and Kurdish examples
- Keep `کاری تێپەڕ / کاری تێنەپەڕ` aligned with Lessons39 and 41–44.
- `Object Omission / Object Drop` should be introduced with one stable Kurdish equivalent or explicitly marked as a pair of English labels for related phenomena.
- `Valency` and `argument structure` need distinct definitions; do not use "توانای کردار" as a catch-all without explaining lexical valency versus realized arguments.
- Verify Sorani morphology and person marking in every example, especially forms with attached pronouns and passive morphology.
- The raw forms `خورا، بینرا، بیسترا، دەگرترێ` should remain preserved verbatim in the source, but their grammaticality, dialect, inflection, and passive/impersonal interpretation need independent review before reuse as paradigms.

## 4. Cross-lesson scope and alignment
- Lesson39 introduces Object as a grammatical function. Lesson40 should explain transitivity and object realization, not redefine Object solely as an affected entity.
- Lesson41 is assigned lexicalized compound verbs and their argument structure. The current Lesson40 draft's sections 11–12 partially duplicate Lesson41 and should be reduced to a cross-reference.
- Lessons42–43 are assigned clitic object paradigms. Lesson40 should not teach the full imperative/non-past/past clitic systems.
- Lesson44 covers passive voice, grammatical Subject, and the former Object. Lesson40 may introduce passive as a limited diagnostic but should not duplicate its full analysis.
- Lesson36's Object/Complement/Adjunct distinctions remain relevant: not every phrase after a verb is an Object, and selected obliques/complements must not be counted as direct objects.
- Lesson37–38 sentence/clause taxonomy is orthogonal to transitivity; keep clause type and argument structure separate.

## 5. Recommended correction queue (not applied)
1. Preserve the raw owner text unchanged; repair the missing transcript-segment reference only after confirming the intended exact span.
2. Retain the rejection of the body-part test and all-body-part participation rule.
3. Define transitivity through valency/argument structure and object function; separate lexical potential from construction-level realization.
4. Refine Object Omission vs generic/intransitive use with context-sensitive diagnostics and carefully sourced examples.
5. Recheck the alleged Chomsky example and citation; do not retain an unsupported attribution.
6. Reanalyse the break/open examples as causative/inchoative and/or active/passive, not as a simple same-verb alternation without evidence.
7. Move the detailed lexicalized compound-verb section to Lesson41; retain only a signpost in Lesson40.
8. Move detailed clitic paradigms to Lessons42–43 and full passive analysis to Lesson44.
9. Populate structured examples/quiz and separate exercises from metadata only through an approved append-only patch.
10. Reconcile section numbering, key_points, course metadata, and source references in an approved patch.

## 6. Change boundary
No changes were made to `main`, the lesson JSON, runtime code, course activation, Botkeep, or Telegram. No terminology owner decision was made. This report is an append-only audit artifact only.

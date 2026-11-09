# Course 4 — Lesson 41 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of main-branch Course 4 JSON Lesson 41, expanded draft, and the Lessons 39–45 composite source. Append-only audit artifact; not an approved lesson revision.

## 1. Provenance verified
- Main JSON: `course_data/grammar_course4_lessons.json`, main blob `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`.
- Lesson record: `grammar_41`, number 41, title `وانەی 41: کردارە سادە و لێکدراوەکان و پەیوەندییان بە بەرکارەوە`, status `owner_review_pending_expanded_draft`.
- Composite source: `docs/source_archive/COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md`, blob `8c2668b3225269fa3ac47db989a4d3db1e1d50c1`, 3125 lines. Its source opening identifies a preserved user-supplied text plus later review/planning/expanded lesson content. The material relevant to lexical compound verbs occurs around lines 830–910, but this is embedded in the composite and must not be described as a standalone raw Lesson41 transcript.
- Expanded draft: `docs/source_archive/staging/drafts/COURSE4_LESSON_041_EXPANDED_DRAFT_2026-11-08.md`, blob `3aaa152e2ab762ed82c87846fc372708e4bca9a6`, 193 lines / 9025 characters.
- The exact transcript segment path cited by the expanded draft, `docs/source_archive/staging/drafts/COURSE4_LESSON_041_DRAFT_TRANSCRIPT_SEGMENT_2026-11-08.md`, returned 404. The draft itself says it relies on a prior transcript, not a distinct owner source. Provenance is incomplete at the segment-reference level.
- The source plan explicitly allocates Lesson41 to simple/compound verbs and lexicalized compounds, following Lesson40's transitivity topic. Lesson41 should not be treated as a separate raw source transcript when only the composite source is present.

## 2. Current JSON shape and mismatches
- The objective is focused: distinguish simple and compound verbs, identify nominal components, and distinguish lexical composition from direct-object function.
- `examples=[]`, `quiz=[]`, `comprehension=[]`, although the Markdown includes multiple worked examples and a five-question quiz.
- `key_points[0]` contains the whole lesson and metadata rather than concise key points.
- `exercises` includes prompts plus answer-key material; it is not a clean exercises-only field.
- Markdown numbering in the JSON body runs from section 13 to section 14/15 inconsistently across fields: the expanded draft itself has sections 1–15, while JSON's key_points copy omits sections 12–13 in its numbering and then displays 14–15. The separate markdown field has sections 1–16. These versions need reconciliation.
- Metadata says `کۆرسی: ١ — بەشی ٤`, although the repository path and project are Course 4. Owner-approved metadata correction is required.
- `source_path` points to the expanded draft, but its own cited transcript-segment file does not exist at the exact checked path.

## 3. Conceptual findings

### 3.1 Keep morphological composition separate from transitivity
The strongest teaching point is sound: simple/compound is a word-formation or lexical-structure classification, whereas transitive/intransitive concerns argument structure and syntactic realization. A simple verb can be transitive or intransitive; a compound predicate can also have different argument structures. Preserve this as the core principle and align it with Lesson40.

### 3.2 The definition of Simple Verb is too narrow
The draft defines a simple verb as one that is not a lexical noun+verb construction. This risks making "simple" merely the negative of one subtype of compound. A sound definition must state the chosen morphological/lexical framework and distinguish:
- simplex (one lexical/morphological base, subject to the language's inflectional morphology);
- morphologically complex/derived verbs;
- lexical compounds;
- multiword predicates/light-verb constructions.
Not every compound verb is necessarily noun+verb; possible structures may include adjective+verb, adverb/preverb+verb, verb+verb, or other language-specific patterns. Do not assert all these patterns are productive in Sorani without examples and source evidence. The current examples mainly cover nominal element + light verb and do not establish a comprehensive taxonomy.

### 3.3 Compound Verb, Light Verb Construction, and lexicalized predicate are not automatically synonyms
Examples such as `قسەکردن`, `شەڕکردن`, `ئیشکردن`, `سوێندخواردن`, and `هەوڵدان` need classification one by one. The terms Compound Verb, Complex Predicate, and Light Verb Construction can describe overlapping but not necessarily identical analyses. State the adopted analysis and diagnostics (lexical unity, inflectional behavior, semantic compositionality, productivity, constituent behavior, and whether the nominal element can independently take modifiers/determiners). Do not classify by orthographic spacing or joining alone.

### 3.4 Nominal component versus Object: correct distinction, but examples need evidence
The draft correctly warns that a nominal element inside a lexicalized predicate is not automatically an independent direct object. However, it then categorically labels `شەڕ` in `ئەو شەڕی کرد`, `قسە` in `ئەو قسەی کرد`, and `سوێند` in `من سوێندم خوارد` as internal nominal components. This is a plausible analysis, not a conclusion established solely by the sentence. Kurdish clitic placement, definiteness/indefiniteness, modifier possibilities, argument structure, and speaker judgments should be tested. The owner source itself presents the split between the nominal and verbal parts as an analysis that needs a way to account for their object-like behavior; preserve this as a debated construction-specific issue, not as an already settled universal rule.

### 3.5 Contrast “نانەکەی خوارد” and “نان خوارد”
This contrast is pedagogically valuable but must be carefully glossed. The form with a definite object may straightforwardly express a transitive verb plus object; the bare form can have a generic object, a lexicalized compound interpretation, or another context-dependent reading. Orthographic separation/joining is not sufficient evidence. Include contextual sentences and native-speaker judgments for the intended readings; explicitly distinguish syntax, lexicalization, and orthography.

### 3.6 The verb table overgeneralizes category assignments
The table classifies `خواردن`, `نووسین`, and `بینین` as transitive and `هاتن`, `چوون`, and `خەوتن` as intransitive. This works as a basic introductory illustration but should be labelled as a typical/basic frame, not an invariant lexical property in every use. Lesson40's valency and object-realization distinctions must carry through. A verb's argument frame may vary by sense and construction.

### 3.7 “All two adjacent words do not make a compound” is correct, but diagnostics are absent
The draft correctly rejects adjacency as a sufficient criterion. It needs operational tests, with cautions that no single test is decisive:
- lexicalization and conventional meaning;
- whether the combination has a stable dictionary entry/lexical sense;
- inflectional behavior and placement of person/tense/clitics;
- internal modification or determiner behavior;
- semantic compositionality and productivity;
- constituent behavior and dialect variation.
Use several converging diagnostics rather than a single spelling or semantic-opacity test.

### 3.8 Agent nouns are a separate word-formation topic
Forms such as `ڕاکەر`, `ئیشکەر`, `شەڕکەر`, and `نانخۆر` are nouns, not verbs, as the draft correctly notes. But the derivational relationship and suffix analysis need checking: the list does not prove a single productive agentive suffix or a uniform derivational path from each compound. Keep agent-noun formation as a short comparison or signpost unless the course scope explicitly includes it; avoid treating every form as a transparent agent noun without lexical verification.

### 3.9 Kurdish orthography and morphological segmentation
The examples alternate joined and separated spellings (e.g. `قسەکردن` vs `قسەی کرد`, `نانخواردن` vs `نان خواردن`). Orthography is not a direct representation of syntactic constituency. Establish a consistent spelling convention, but do not let spelling determine the grammatical analysis. Verify forms in the intended Sorani variety and note dialectal/lexical variation where relevant.

### 3.10 Terminology consistency
- Keep `کرداری سادە / کرداری لێکدراو` distinct from `کاری تێپەڕ / کاری تێنەپەڕ`.
- Introduce and distinguish `Compound Verb`, `Light Verb Construction`, and `Complex Predicate` if all are used; otherwise choose one analytic framework and explain its scope.
- Define `توخمی ناوی` as a structural component, not a grammatical function.
- Keep `بەرکار` as a grammatical function and avoid defining it solely as an affected entity.
- Use one consistent Kurdish term for word formation/morphology when relevant; avoid using "سادە/لێکدراو" sometimes for lexical structure and sometimes for phrase structure.

## 4. Cross-lesson alignment
- Lesson40 establishes that transitivity and lexical composition are independent dimensions. Lesson41 should develop the compound-verb side without changing the transitivity criteria.
- Lesson39 defines Object as a grammatical function; Lesson41 must not equate every nominal component with Object.
- Lessons42–43 handle clitic paradigms. Lesson41 should not infer object status solely from attached pronouns; coordinate the examples with those lessons.
- Lesson44 addresses passive voice. Avoid using passive behavior as a universal compound/transitivity diagnostic.
- Lesson31's complex predicate/light verb discussion and Lessons21/30 compound predicate material should be checked for overlap and terminology consistency.
- The master register's unresolved distinctions between Object, Complement, Adjunct, and internal nominal component remain open; Lesson41 cannot settle them alone.

## 5. Recommended correction queue (not applied)
1. Preserve the composite source and existing expanded draft unchanged.
2. Repair/clarify provenance: identify the exact transcript span for Lesson41 or mark the source as a segment within the composite; do not invent a missing standalone transcript file.
3. Replace the narrow definition of Simple Verb with a framework-explicit definition of simplex, derived, compound, and multiword/light-verb predicates.
4. Distinguish Compound Verb, Light Verb Construction, and Complex Predicate; add converging diagnostics and evidence.
5. Mark the analysis of `شەڕی کرد`, `قسەی کرد`, `سوێندم خوارد`, and `نان خوارد` as construction-specific pending verification, rather than categorical universal rules.
6. Add context-rich examples and native-speaker/dialect validation for bare nominal components, clitic placement, and object diagnostics.
7. Label the simple-verb transitivity table as typical/basic frames and align it with Lesson40.
8. Move agent noun formation to a brief cross-reference or develop it with sourced morphology; verify each form and suffix.
9. Reconcile orthographic conventions separately from syntactic/lexical analysis.
10. Reconcile JSON sections, concise key_points, structured examples/quiz, exercises/answer-key separation, and Course 4 metadata only through an approved append-only patch.

## 6. Change boundary
No changes were made to `main`, the lesson JSON, runtime code, course activation, Botkeep, or Telegram. No terminology owner decision was made. This report is an append-only audit artifact only.

# Course 4 — Lesson 39 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of main-branch Course 4 JSON lesson 39, expanded draft, and the Lessons 39–45 composite source. Append-only audit; not an approved lesson revision.

## 1. Provenance and files verified
- Main JSON: `course_data/grammar_course4_lessons.json`, main blob `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`.
- Lesson record: `grammar_39`, title `وانەی 39: بەرکار و ئەرکی ڕێزمانیی ئەو`, status `owner_review_pending_expanded_draft`.
- Composite source: `docs/source_archive/COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md`, blob `8c2668b3225269fa3ac47db989a4d3db1e1d50c1`, 3125 lines / 79958 characters. It contains raw owner text in lines 1–141, review/planning in lines 142–207, and expanded lessons 39–45 after that. It must not be represented as one uninterrupted raw transcript.
- Expanded draft: `docs/source_archive/staging/drafts/COURSE4_LESSON_039_EXPANDED_DRAFT_2026-11-08.md`, blob `a60695f2655eb2f28168fcf6e1914090bb9a713f`, 203 lines / 8603 characters.
- Literal path named by the JSON/draft, `COURSE4_LESSON_039_DRAFT_TRANSCRIPT_SEGMENT_2026-11-08.md`, was not found at `docs/source_archive/staging/drafts/COURSE4_LESSON_039_OWNER_SOURCE_SEGMENT_2026-11-08.md`; that exact checked owner-segment path returned 404. The composite source does contain the Lesson39 raw text. Do not infer that the composite's whole contents are raw.
- Composite source explicitly states the original user-supplied file was preserved without content editing, and that the raw owner source ends at line 141; the remaining material includes planning and expanded content.

## 2. Main JSON structure and mismatches
- Objectives cover object identification, Subject/Agent/Object distinction, direct object vs recipient/directional phrase, nominal/pronominal/NP realization, Object vs Complement/Adjunct, and the fact not every clause has a direct object.
- `examples=[]`, `quiz=[]`, `comprehension=[]`, although the Markdown contains worked examples and five multiple-choice quiz questions. The exercises array holds exercise text but also includes metadata/provenance lines before the tasks.
- `key_points[0]` contains almost the entire lesson rather than concise key points.
- Draft metadata says `کۆرسی: ١ — بەشی ٤`, inconsistent with its Course 4 repository placement. This is a metadata defect to resolve, not authority to change course identity.
- Markdown section numbering skips 10 (section 9 is followed by 11, 12, 13) in the JSON's long body; expanded draft has its own normalized sequence, so preserve version distinction.
- Draft says the raw transcript is preserved, but the named standalone transcript segment path is not present. Provenance should point to the verified composite source and exact raw span, or to an actual separate source file after confirmation.

## 3. Conceptual findings

### 3.1 Object definition: grammatical function, not merely affected entity
The raw source defines Object as a noun/pronoun/entity that has undergone or will undergo an action, and says it always accompanies a transitive verb and is affected by it. This is too narrow and semantically biased.
The expanded draft improves this by defining Object as a grammatical function/constituent linked to the verb, and explicitly notes that perception/cognition objects need not undergo physical change (e.g. `من تۆم بینی`). Preserve this correction.
Object should not be defined solely as the patient/affected participant: semantic roles such as Theme, Stimulus, Content, and other verb-selected participants can be realized as objects depending on the construction and framework.

### 3.2 Subject versus Agent versus Object
The draft correctly separates Subject as a grammatical function, Agent as a semantic role, and Object as a grammatical function. Preserve this distinction and align with Lessons 33–34 and the owner decision queue.
Do not imply every Subject is an Agent, or every Object is a Patient. In passive and non-agentive clauses these distinctions are especially important.

### 3.3 Direct Object versus Recipient/indirect object
The example `من کتێبێکم بە هاوڕێکەم دا` usefully distinguishes the thing given from the recipient:
- `کتێبێک`: direct object / Theme.
- `بە هاوڕێکەم`: recipient/goal phrase.
However, whether the recipient is labelled Indirect Object, oblique complement, or prepositional recipient depends on the adopted syntactic framework and Sorani construction. The draft responsibly uses a provisional descriptive label `پێکهاتەی وەرگر/ئاراستە`. Do not silently standardize it as Indirect Object before owner decision and cross-lesson reconciliation.
The phrase `لە قوتابییەکە پرسی` requires separate verb-frame analysis; the presence of a preposition does not automatically make a phrase an indirect object.

### 3.4 Object versus Complement versus Adjunct
The draft's distinction is a useful starting point, but the definition of Complement as a "necessary or completing" constituent is not sufficiently precise. Complement is framework-dependent and may include verb-selected prepositional phrases, clauses, predicative complements, and other dependents. Object is one grammatical function in some frameworks; in others the relation between object and complement is categorized differently.
Adjunct cannot be diagnosed only by optionality: some selected complements can be omitted under discourse/contextual conditions, and some adjuncts are pragmatically important. Use syntactic selection, distribution, semantic relation, and construction tests together. Align with Lesson 36 and avoid treating every time/place phrase as automatically adjunct if the verb selects it.

### 3.5 Transitivity and the raw-source body-part test
The raw source argues that a verb is transitive because not all human body parts participate in the action, and intransitive because all body parts participate; it also treats acceptance of suffixes `مان/تان/یان` and passive formation as general tests. These are not valid general linguistic diagnostics.
Transitivity concerns a verb's syntactic argument structure and its constructional use, not how many body parts participate. The raw examples `ئەو نانی خوارد`, `ئەو قسە دەکات`, `ئەو ڕۆیشت`, `ئەو چوو` cannot establish transitivity by anatomy.
Passive formation can be a useful diagnostic in some constructions, but it is not universally available or uniform across all transitive predicates, especially lexicalized compound predicates and dialect-specific patterns. Clitic attachment alone does not establish objecthood or transitivity because clitics may encode different grammatical relations in Kurdish.
The expanded Lesson39 draft appropriately defers detailed transitive/intransitive classification to Lesson40 and lexical compound verbs to Lesson41. Keep that scope boundary; preserve raw material and analyze it in the relevant later lessons.

### 3.6 Lexical compound verbs and argument structure
The raw owner material raises a significant Kurdish-specific issue: lexicalized compound verbs such as `نان خواردن`, `قسەکردن`, `شەڕکردن`, `سوێندخواردن` may incorporate a nominal element that appears to occupy an object-like position when the compound is syntactically realized. The source argues that these should not simply be classified as intransitive because they lack an external object.
This deserves a dedicated analysis in Lesson41, not a rushed generalization in Lesson39. Distinguish lexicalized compound verb structure, light-verb constructions, incorporated/internal nominal components, and an independently realized direct object. The draft's current Lesson39 scope does not explain this issue; note it as deliberately deferred, not discarded.

### 3.7 Kurdish clitic pronouns and tense/aspect
The raw source includes extensive paradigms for clitic pronouns around imperative, non-past, and past transitive verbs, including ordering differences. This is a distinct, substantial topic assigned in the lesson plan to Lessons42–43. The current Lesson39 expanded draft omits these paradigms appropriately for scope, but must preserve the source and ensure it is carried forward into those lessons.
Do not treat the same clitic string as object clitic in every tense/construction without morphological and syntactic analysis; Kurdish past transitive alignment and clitic placement require construction-specific treatment.

### 3.8 Examples and diagnostics
The draft examples `کتێبەکەی خوێندەوە`, `من تۆم بینی`, `نامەکەی نووسی`, and `کتێبێکم بە هاوڕێکەم دا` are useful teaching candidates, but each should be fully segmented for agreement/clitic morphology and dialectal form before final publication.
The draft's classification of `بە هاوڕێکەم` as recipient/goal should be retained provisionally; avoid calling every `بە`, `بۆ`, or `لە` phrase an object.
The claim that all direct objects are required by transitive verbs needs qualification: object omission/implicit objects and contextually understood objects are possible in some Kurdish verb uses. This is the focus of Lesson40 and should not be collapsed into a simple absolute.

## 4. Cross-lesson consistency
- Lesson33: Subject vs Agent is a grammatical-function/semantic-role distinction. Maintain it here.
- Lesson34: Subject/Predicate/Copula terminology decisions remain open; do not reintroduce Subject=Agent.
- Lesson36: Object, Complement, Noun Complement, Modifier, and Adjunct distinctions need one consistent framework. Lesson39's current Complement/Adjunct descriptions are provisional.
- Lesson38: Clause terminology is separate from Object function; object can be realized within a clause without changing clause hierarchy.
- Lesson40: transitivity, intransitivity, object omission, and diagnostics are deliberately deferred.
- Lesson41: lexical compound verbs and their internal nominal component/argument structure are deliberately deferred.
- Lessons42–43: clitic pronoun paradigms and their position with imperative, non-past, and past transitive forms must be preserved for dedicated treatment.
- Lesson44: passive voice analysis must preserve distinction between grammatical Subject and semantic Agent; avoid overgeneralizing passive as a universal transitivity test.
- Owner decision queue remains open on Indirect Object vs Recipient, Object vs Complement/Adjunct, and associated Kurdish term choices.

## 5. Recommended correction queue (not applied)
1. Keep the raw owner transcript immutable and cite its exact span within the composite source.
2. Retain the expanded grammatical definition of Object; remove the "affected by action" requirement as a universal definition.
3. Preserve Subject/Agent/Object as distinct categories.
4. Keep `پێکهاتەی وەرگر/ئاراستە` provisional until the owner chooses the Kurdish label and framework.
5. Refine Complement/Adjunct diagnostics in coordination with Lesson36.
6. Carry raw transitivity tests to Lesson40 for explicit correction; do not lose the original text.
7. Carry lexical compound verb issue to Lesson41, and clitic paradigms to Lessons42–43.
8. Populate structured examples and quiz only through an approved patch; keep Markdown and JSON fields synchronized.
9. Repair stale source reference and Course 1 metadata only through an approved append-only patch.
10. Preserve all poems/examples/source material; any corrected analysis must be a separate, attributable layer.

## 6. Change boundary
No changes were made to `main`, the lesson JSON, runtime code, course activation, Botkeep, or Telegram. No terminology owner decision was made. This report is an append-only audit artifact only.

# Course 4 — Lesson 45 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of main Course 4 JSON Lesson45, expanded draft and composite source segment. Append-only audit only; not an approved revision.

## 1. Provenance
- Main JSON: course_data/grammar_course4_lessons.json, blob e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65.
- Lesson: grammar_45, title "وانەی 45: ڕیزبەندی و گواستنەوەی بەرکار لە ڕستەدا", status owner_review_pending_expanded_draft.
- Composite source: docs/source_archive/COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md, blob 8c2668b3225269fa3ac47db989a4d3db1e1d50c1; Lesson45 spans lines 2761–3031.
- Expanded draft: docs/source_archive/staging/drafts/COURSE4_LESSON_045_EXPANDED_DRAFT_2026-11-08.md, blob 75ff3453e68588c991b2d77538b644fa3cd913a3, 188 lines / 8005 chars.
- Claimed separate transcript segment docs/source_archive/staging/drafts/COURSE4_LESSON_045_DRAFT_TRANSCRIPT_SEGMENT_2026-11-08.md returned 404. The composite segment is available; no standalone source file verified.
- No separate owner source text was identified; the draft describes the transcript as preserved separately, but the named standalone path is missing.

## 2. JSON structure and editorial issues
- Objectives cover word order, grammatical function vs linear position, Subject/Object identification, Object Fronting, Topicalization vs Focus, and information structure.
- examples=[], quiz=[], comprehension=[] although the Markdown/draft contains multiple examples and a five-question quiz.
- key_points[0] contains almost the entire lesson and metadata; exercises combines prompts and answer keys, with no distinct structured answer-key field.
- Draft metadata says "کۆرسی: ١ — بەشی ٤" despite storage in Course4 repository; owner confirmation required.
- Draft section numbering skips from 12 to 15 in the quiz; the JSON Markdown reorders/adds sections, so numbering and section organization need a single consistent scheme.
- Some examples are illustrative but not fully specified for dialect, prosody, punctuation, clitic morphology, or discourse context.

## 3. Conceptual findings

### 3.1 The core distinction is sound
The lesson correctly distinguishes grammatical function from linear position. A constituent at the beginning of a clause is not automatically the Subject; it may be a fronted Object, a topic, or another discourse constituent. The diagnostic must use syntax, verbal argument structure, morphology/clitics, agreement, and discourse context rather than position alone.

### 3.2 Basic Sorani word order should be qualified
SOV (Subject–Object–Verb) is a useful broad description for many Sorani clauses, but not an exceptionless template. Word order varies with clause type, information structure, focus, topicalization, clitic placement, and dialect/register. Avoid presenting SOV as a rule that classifies every initial NP as Subject or every nonfinal NP as Object.

### 3.3 Object Fronting is not synonymous with Topicalization
Object Fronting describes a constituent's placement before its canonical position (a syntactic/linear description). Topicalization is a discourse operation that establishes or reactivates a topic. A fronted Object may be topicalized, focused, contrastive, or otherwise discourse-marked; not every topic is a direct Object, and not every fronted Object is necessarily a topic. The lesson states this distinction in principle but its examples need clearer diagnostics.

### 3.4 Left dislocation vs movement/fronting
Examples such as:
- "نامەکە، کەژیار نووسی."
- "ئەم کتێبە، من خوێندمەوە."
may be left-dislocation/topic constructions with a pause and possible resumptive/clitic dependency, rather than simple constituent movement within one clause. The comma and separate intonation are analytically important. The lesson should distinguish:
1. constituent fronting within the clause;
2. left dislocation with a detached topic;
3. hanging topic/frame setter ("سەبارەت بە کتێبەکە...");
4. focus-fronting/contrastive focus.
Do not label all these as the same Object Fronting operation.

### 3.5 Clitic morphology makes the examples under-specified
The examples "ئەم کتێبە، من خوێندمەوە", "پەیامەکە، کەژیار ناردی", "وانەکە، مامۆستا نووسی" and the contrasting clauses "کەژیار ئاڕگەشی بینی" / "ئاڕگەش کەژیاری بینی" need explicit segmentation and dialect review. In Sorani, past transitive clauses can involve agent clitics and object-related marking whose host/placement is not transparent from linear order alone. The lesson itself points to clitics and agreement as diagnostics but does not actually analyze the clitics in its central examples. Provide morpheme-by-morpheme glosses, grammatical roles, clitic host, and prosody for every example before treating the contrast as proof of a word-order rule.

### 3.6 The two "meaning change" examples need controlled analysis
The pair:
- "کەژیار ئاڕگەشی بینی."
- "ئاڕگەش کەژیاری بینی."
is intended to show Subject/Object reversal, not merely a change in focus. That is conceptually useful if the morphology and naturalness are verified. But the suffixes and case/clitic patterns need explicit analysis; do not infer roles from position alone, especially in past transitive Sorani. Include an unambiguous context and a native-speaker judgment.

### 3.7 Focus is not merely "important information"
Focus is a structured information-status/alternatives relation (new, contrastive, corrective, exhaustive, etc., depending on framework), not just anything the speaker considers important. The definition should distinguish broad/predicate focus, narrow constituent focus, and contrastive/corrective focus if these are part of the course's scope. Prosody and discourse alternatives may be essential; word order alone is not a sufficient diagnostic.

### 3.8 Given/New is not identical to Topic/Focus
The lesson usefully defines Given and New Information, but should not equate Topic with Given or Focus with New. Topics are discourse referents/frames the clause is about; given/new describes information status relative to the discourse. A topic can be newly introduced, and a focused constituent can be discourse-old but contrastively selected. The table currently says topics are "often known" and focus "often distinguished", which is acceptable as tendencies only if explicitly qualified.

### 3.9 "Topic" example is a frame setter, not necessarily a moved Object
"سەبارەت بە کتێبەکە، من هێشتا تەواوم نەکردووە." uses a "concerning/about the book" phrase to establish a discourse frame. It is not evidence that a direct Object has been fronted from inside the clause. Label it as a frame-setting topic and contrast it with an in-clause topicalized Object.

### 3.10 Word order can affect grammatical roles, not just information structure
The lesson correctly shows that changing "کەژیار ئاڕگەشی بینی" to "ئاڕگەش کەژیاری بینی" is intended to reverse Subject and Object roles, unlike fronting that preserves the Object function. However, this contrast must be explained through morphology and syntax, not the position heuristic the lesson warns against. Also distinguish constituent order changes that preserve propositional roles from order changes that alter argument interpretation.

### 3.11 Terminology alignment
Keep distinct:
- Word Order = ڕیزبەندیی وشە/پێکهاتە (choose one consistently);
- Object Fronting = پێشخستنی بەرکار / گواستنەوەی بەرکار (owner-approved preferred term needed);
- Topicalization = بابەتکردن;
- Topic = بابەت;
- Focus = جەخت (but define its technical information-structural sense);
- Given/New Information = زانیاریی کۆن/نوێ (ensure definitions are discourse-relative);
- Subject = unresolved بکەر/نیهاد;
- Object = بەرکار.
Do not conflate Topic with Subject or Focus with Object. Do not infer the syntactic role from initial position.

## 4. Cross-lesson alignment
- Lesson39: Object is a grammatical function, not a linear position.
- Lesson40: lexical valency/transitivity and realized arguments constrain possible roles; omission does not identify voice or topic.
- Lesson42–43: clitic pronouns and Sorani past transitive/ergative patterns are central to analyzing the examples; cross-check clitic host and role.
- Lesson44: passive promotion of former Object to Subject is distinct from Object Fronting/topicalization; do not confuse passive with discourse fronting.
- Lessons33–34: Subject term remains unresolved; preserve distinction between Subject and Agent.

## 5. Recommended correction queue (not applied)
1. Preserve transcript and expanded draft unchanged; repair the missing standalone transcript reference or cite composite source lines 2761–3031.
2. Define Object Fronting, left dislocation, Topicalization, frame-setting topic, and Focus separately.
3. Mark prosodic pauses and explain comma/intonation in detached-topic examples.
4. Add full morphological segmentation/glosses for "خوێندمەوە", "ناردی", "نووسی", "ئاڕگەشی بینی", and "کەژیاری بینی", identifying clitic host and grammatical function.
5. Verify every sentence with competent Sorani speakers for the target standard/dialect, register, and intended reading.
6. Clarify that SOV is a broad default tendency, not a universal rigid order.
7. Separate Topic from Given and Focus from New; add counterexamples showing topic-new and focus-given/contrastive if appropriate.
8. Explain focus types only to the level the course can support, including prosody and contrastive alternatives.
9. Keep Subject=بکەر/نیهاد as an unresolved owner decision; do not infer it from initial position.
10. Normalize section numbering and move examples, quiz, answer keys, and comprehension into distinct structured JSON fields only through an approved append-only patch.
11. Do not score quiz/exercises until clitic analyses and sentence naturalness are validated.
12. Resolve Course1/Course4 metadata only with owner confirmation.

## 6. Change boundary
No changes to main, lesson JSON, runtime, activation, Botkeep, or Telegram. No terminology decision or lesson approval was made. This file is an append-only audit artifact only.

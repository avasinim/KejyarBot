# Course 4 — Lesson 38 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of the Course 4 main-branch JSON lesson, the expanded draft, the composite Lessons 32–38 source, and the additional owner-source file. This report is an append-only audit artifact, not an approved lesson revision.

## 1. Files and provenance verified
- Mainline JSON: `course_data/grammar_course4_lessons.json`
  - Main-branch blob: `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`
  - Lesson key: `grammar_38`, number 38.
- Composite source: `docs/source_archive/COURSE4_LESSONS_032_038_SOURCE_2026-11-07.md`
  - Main-branch blob: `a8f40f5996aee9441b12610451975d8a72bf153e`
  - The Lesson 38 raw discussion appears in the latter part of the composite, including the explanation of Main/Subordinate Clause, Independent/Dependent, the complex-complex example, comma placement, and the Mewlewî and Goran poetry exercises. The composite also contains later review/planning material; it must not be described as a pure raw transcript for all lessons 32–38.
- Additional owner-source file: `docs/source_archive/COURSE4_LESSON38_ADDITIONAL_OWNER_SOURCE_2026-11-08.md`
  - Main-branch blob: `3e41952ab8e859ae67c7117820862b57c39f15f3`
  - 108 lines. It explicitly labels itself as raw owner-provided text, preserved without spelling, dialect, punctuation, or ambiguity correction.
- Expanded draft: `docs/source_archive/staging/drafts/COURSE4_LESSON_038_EXPANDED_DRAFT_2026-11-08.md`
  - Main-branch blob: `2776c6b3ef8c4d959e202ad93496f145ab817d59`
  - 166 lines, 8451 characters.
- The literal source path named inside the JSON/draft, `COURSE4_LESSON_038_OWNER_SOURCE_SEGMENT_2026-11-08.md`, was checked at `docs/source_archive/staging/drafts/COURSE4_LESSON_038_OWNER_SOURCE_SEGMENT_2026-11-08.md` and returned 404. This does not mean no owner source exists: the separately named additional owner-source file above does exist. Update of provenance references requires a separate approved change.

## 2. Current JSON state
- Title: `وانەی 38: پێڕستە، سەرڕستە و بەرڕستە؛ شیکاری و ڕاهێنان`.
- Review status: `owner_review_pending_expanded_draft`.
- `examples=[]`, `quiz=[]`, and `comprehension=[]`; however, the Markdown/source_markdown contains worked examples and five multiple-choice quiz questions. The eight exercise strings include four metadata/provenance statements before the actual tasks.
- `key_points[0]` contains a long, multi-section lesson text rather than a concise key point list. The Markdown numbering skips section 10 (section 9 is followed by 11 and 12).
- Metadata in the draft says `کۆرسی: ١ — بەشی ٤`, inconsistent with the repository's Course 4 location and course identity. This is a metadata defect to resolve, not permission to change the source.
- The lesson's objective includes both complex and compound-complex sentence analysis, but the body focuses more heavily on clause hierarchy; the objective and assessment should be aligned after approval.

## 3. Conceptual and terminology findings

### 3.1 Clause versus sentence
The draft usefully says a clause is a grammatical unit organized around a predicate and that its subject can be unexpressed. Preserve that qualification: Kurdish permits omitted/recoverable subjects, and a clause must not be defined as requiring an overt subject in every case.
The formulation that a clause is merely a constituent "inside a sentence" is too narrow as a general definition: an independent clause can itself constitute a sentence. Distinguish the grammatical unit from its orthographic sentence realization.

### 3.2 Main Clause versus Independent Clause
The raw source and draft repeatedly pair `Main Clause` with `Independent Clause` as if they were exact synonyms. They overlap in the basic complex-sentence teaching example, but describe different dimensions:
- `Main clause` is a hierarchical relation: the matrix/main clause in relation to subordinate clause(s).
- `Independent clause` describes syntactic independence and ability to stand as a clause-level sentence.
In compound and compound-complex sentences, there may be multiple coordinated independent clauses. Calling all of them "the main clause" obscures the hierarchy. Teach the labels separately and show how they overlap in a prototypical complex sentence.

### 3.3 Subordinate versus Dependent
`Subordinate clause` and `dependent clause` also overlap in the intended examples, but should be introduced as related labels, not assumed to be universally interchangeable across frameworks. More importantly, "does not make complete meaning alone" is not a safe defining test. A subordinate clause can express a readily understandable proposition while still being grammatically dependent; conversely, discourse context can make a fragment understandable. Define dependency structurally and functionally, not only semantically.

### 3.4 Subordinating conjunctions and relative markers
The raw list groups `چونکە، لەدوای ئەوەی، بەرلەوەی، ئەگەر، مادام، کاتێک، هەرچەندە` with `کە، کو، ئەوەی` as if all were the same type of marker. The draft partially qualifies the latter, which is good, but the classification needs further precision:
- distinguish subordinating conjunctions/subordinators from complementizers and relative markers;
- do not classify `کە` or `ئەوەی` from form alone; their syntactic role depends on construction;
- not every subordinate clause is necessarily introduced by an overt subordinating conjunction.
The owner term `ئامرازی پەیوەندیی بڕیناویی` needs a definition and contrastive examples before it is treated as a stable category.

### 3.5 Clause functions and internal structure
The long example beginning `بەرلەوەی زەنگ لێ بدات...` is explicitly marked in the draft as requiring further analysis. Keep that warning. It contains coordination, subordinate clauses, omitted subjects, and a potential clausal complement after a verb of causing/forcing. Do not finalize the clause count or labels without a full constituent-by-constituent parse.
The lesson should also distinguish subordinate clauses by function where relevant (e.g. adverbial, complement, relative), rather than implying all subordinate clauses have one single relation to the main clause.

### 3.6 Comma guidance
The draft's qualified guidance—an initial subordinate clause is often followed by a comma, while a final subordinate clause often is not—is appropriately presented as a general tendency, not an exceptionless grammatical law. Preserve the qualification and align final punctuation with the course's approved Sorani orthography.

### 3.7 Compound-complex example
The example `کاتێک میوانەکان گەیشتن، ئێمە پێشوازی‌مان لێکردن و من چایم ئامادە کرد.` is a useful candidate for a compound-complex sentence: one subordinate temporal clause plus two coordinated independent clauses. The analysis should explicitly show that `و` coordinates the two independent clauses, while `کاتێک` introduces the temporal subordinate clause. Verify the coordination and subject reference in the Sorani example before final teaching use.

## 4. Cross-lesson alignment
- Lesson 35 classifies sentences by communicative purpose; Lesson 37 classifies them by sentence structure; Lesson 38 should focus on clause structure and clause relations. These are different axes and must remain distinct.
- Lesson 37's Simple/Compound/Complex/Compound-Complex definitions depend on accurate clause identification. Lesson 38 should use exactly the same definitions and examples, not introduce a conflicting clause count.
- The owner decision queue remains open on `بەرڕستە` versus `ژێرەڕستە`, and on `هاولکی` spelling/category. No owner decision is inferred or made by this audit.
- Independent/Dependent versus Main/Subordinate was already flagged as a cross-lesson conceptual distinction; this lesson confirms that it needs explicit treatment.

## 5. Content preservation and assessment
- The composite source contains the Mewlewî and Goran poetry-based tasks. Keep the original poems and lexical glosses verbatim in their source archive; any modern grammatical analysis should be a separately labelled annotation.
- The additional owner-source file is the exact raw owner-provided material; do not normalize its orthography or silently substitute it for the composite source.
- The five quiz questions currently appear in Markdown but not in the structured `quiz` array. Examples similarly appear in the body while `examples` is empty. This creates a content/runtime mismatch; populate structured fields only in an explicitly approved patch.
- The source path reference is stale/misnamed relative to the verified additional owner-source file. Correct provenance in a separate patch after approval.

## 6. Recommended correction queue (not applied)
1. Keep the raw owner source and composite source immutable.
2. Add a precise clause definition, including omitted subjects and the possibility that an independent clause can stand as a sentence.
3. Teach Main vs Independent as hierarchy vs independence; teach Subordinate vs Dependent with the same care.
4. Distinguish subordinator, complementizer, and relative marker; classify `کە` contextually.
5. Fully parse the long source example and poetry tasks before asserting clause boundaries or counts.
6. Reconcile Lesson 38 with Lesson 37's four sentence structures.
7. Resolve owner decisions on `بەرڕستە/ژێرەڕستە` and conjunction terminology explicitly.
8. Repair structured examples/quiz/exercises and course metadata in an approved append-only patch; do not activate or deploy until explicitly authorized.

## 7. Change boundary
This audit did not modify `main`, the lesson JSON, runtime code, course activation, Botkeep, or Telegram. No owner terminology decision was made. This report is an append-only audit artifact only.

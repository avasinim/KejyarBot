# Course 4 — Lesson 42 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of main-branch Course 4 JSON Lesson 42, expanded draft, and the relevant transcript segment embedded in the Lessons 39–45 composite source. Append-only audit artifact; not an approved lesson revision.

## 1. Provenance verified
- Main JSON: course_data/grammar_course4_lessons.json, main blob e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65.
- Lesson record: grammar_42, number 42, title وانەی 42: جێناوی لکاو و ئەرکی بەرکار لە زمانی کوردیدا, status owner_review_pending_expanded_draft.
- Composite source: docs/source_archive/COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md, blob 8c2668b3225269fa3ac47db989a4d3db1e1d50c1, 3125 lines. Lesson42 text is embedded at lines 1663–2063 (approx.); this is a segment inside a composite source, not a standalone source file.
- Expanded draft: docs/source_archive/staging/drafts/COURSE4_LESSON_042_EXPANDED_DRAFT_2026-11-08.md, blob 821cf4084c7330ce8d7a8adbc113bb290c02f447, 147 lines / 7902 characters.
- The exact transcript-segment path implied by the draft, docs/source_archive/staging/drafts/COURSE4_LESSON_042_DRAFT_TRANSCRIPT_SEGMENT_2026-11-08.md, returned 404. The composite transcript segment is available, but the separate file reference is not.
- The draft explicitly states that the transcript was preserved in a separate file; the exact file was not found at the checked path. Do not claim a standalone owner-source file exists until its path is verified.

## 2. Current JSON shape and mismatches
- Learning objectives: distinguish independent pronouns and clitics; distinguish possessive marking from object clitics; identify clitic function in full clause; distinguish Agent/Subject, Object, and agreement; recognize dialect/tense/construction variation.
- examples=[], quiz=[], comprehension=[], although the Markdown includes examples and five multiple-choice quiz questions.
- key_points[0] contains almost the entire lesson and provenance metadata rather than concise key points.
- exercises mixes four learner prompts with four answer-key items; answer key is not a separate structured field.
- The current Markdown includes the added contrast من تۆم بینی, while the composite source segment has examples such as من دەمناسم, من کەژیار دەناسم, من دەیناسم, ئەوان دەمانناسن, and past forms گرتمن، ناردمیت، گرتتن، گرتتانن، گرتمی، گرتنی. These forms need dialect-specific validation and should not be silently conflated.
- Metadata says کۆرسی: ١ — بەشی ٤, inconsistent with Course 4 repository placement; owner decision required.
- Numbering in JSON Markdown and expanded draft is inconsistent: the JSON's key_points[0] omits some numbering, while the separate markdown body has sections 1–15. Reconcile only in an approved patch.

## 3. Conceptual findings

### 3.1 Clitic is a prosodic/syntactic status, not a grammatical function
The core teaching point is sound: a clitic's form does not uniquely determine whether it expresses possession, object, agent/subject relation, agreement, or another function. The function must be determined from the full construction, dialect, tense/aspect, host, and syntactic relations. Keep the distinction between form/category (clitic) and function (possessor, object, agent-related marker, etc.).

### 3.2 Possessive suffix versus clause-level Object
The examples کتێبەکەم، کتێبەکەت، کتێبەکەی، کتێبەکەمان correctly illustrate possessive marking inside an NP. In کتێبەکەم خوێندەوە, the entire NP کتێبەکەم can function as Object, while ـم remains a possessor marker inside that NP. This is an important distinction: the grammatical function of the phrase is not automatically the function of its internal clitic.
Caution: the sentence has an unexpressed subject and needs contextual interpretation, but the internal possessor/object distinction remains valid.

### 3.3 The proposed present-tense object-clitic examples are internally inconsistent and need correction
The source uses من دەمناسم، ئەو دەتناسێت، ئەوان دەمناسێن، and ئەو هەڵت دەبژێرێت, while elsewhere using من ئەو دەناسم، ئەوان ئێمە دەناسن، ئەوان دەمانناسن، and من دەیناسم. The expanded draft itself warns that دەمناسێت and دەتناسێت need morphological analysis, but it does not resolve them.
Do not teach these as confirmed object-clitic paradigms until the exact Sorani variety, intended person/number, segmentation, and native-speaker judgments are recorded. The sequence دە- + clitic + stem + agreement must be segmented consistently; otherwise the learner may confuse subject agreement with object clitic marking. Lesson43 is the appropriate place for a verified paradigm, but Lesson42 must not present unverified examples as established facts.

### 3.4 The past-transitive example is valuable but its analysis needs careful formulation
The added example من تۆم بینی illustrates a common Sorani past transitive pattern in which the first-person agent-related clitic is hosted by the object NP/pronoun. In this construction, من is an overt independent pronoun, تۆ is the Object, and ـم marks the first-person Agent/ergative agreement relation; it is not a possessive suffix on تۆ, and it is not the Object itself.
However, the lesson should distinguish grammatical Subject, semantic Agent, and agreement/clitic marker with the terminology already unresolved in Lessons33–34. Do not call ـم simply "subject pronoun" without explaining the ergative alignment and construction. The exact analysis must be tied to the course's selected Sorani variety.

### 3.5 Subject, Agent, Object, and agreement must remain separate
The transcript's phrase "نیشاندانی بکەر یان ئەنجامدەری کردار" risks conflating grammatical Subject with semantic Agent. Sorani past transitive clauses may show ergative alignment: the Agent is not necessarily encoded like the Subject of an intransitive or present-tense clause. Preserve separate labels:
- grammatical Subject (syntactic function);
- Agent (semantic role);
- Object (syntactic function);
- person/number agreement or agent-indexing clitic (morphosyntactic relation).
The owner decision queue for Subject=بکەر/نیهاد remains unresolved; do not settle it within this lesson.

### 3.6 Clitic-host position is not a universal function test
A clitic may attach to a noun, verb, or another host; attachment location alone does not determine whether it marks possession, object, Agent, or agreement. The transcript's own warning is sound. Provide construction-specific examples with segmentation and glosses rather than one generalized suffix table.

### 3.7 Past forms in the source are unverified
Forms گرتمن، ناردمیت، گرتتن، گرتتانن، گرتمی، گرتنی are explicitly presented in the draft as unverified. Keep them marked as data awaiting dialect/context/segmentation review; do not use them as model paradigms or build quiz answers on them. The missing source continuation is also noted by the transcript, so do not invent forms to complete the paradigm.

### 3.8 “Independent pronoun” definition needs precision
The draft describes an independent pronoun as appearing "clearly" in the sentence; clarity/visibility is not the defining property. Define it as a form that can occur as an independent syntactic/prosodic word, contrasted with a clitic that requires a host. Avoid using "free" and "independent" loosely if the course later distinguishes phonological word, syntactic word, and clitic.

### 3.9 Object clitic versus agreement marker
The draft correctly notes that clitics and person/number agreement are not always the same thing, but it does not provide a robust diagnostic. In each example, show:
- the lexical verb and its argument frame;
- overt or null Subject/Agent;
- overt or clitic Object;
- clitic host and segmentation;
- agreement morphology on the verb;
- dialect and tense/aspect.
If the same exponent has more than one analysis across constructions, explicitly state the ambiguity rather than force one category.

### 3.10 Terminology and orthography
- Keep جێناوی لکاو / Clitic Pronoun as a form/structural label, not a synonym for Object Pronoun.
- Distinguish Possessive Clitic/Suffix, Object Clitic, Agent-indexing/ergative clitic, and agreement marker where the analysis supports these labels.
- Maintain distinction between grammatical Subject, semantic Agent, and Object; coordinate with Lessons33–34 and Lesson44.
- Specify Central Kurdish/Sorani dialect and orthographic conventions for all paradigms.
- The English title Object Clitics and Their Grammatical Functions in Kurdish is broader than the current lesson's actual content; either scope it carefully or retain the narrower Kurdish title.

## 4. Cross-lesson alignment
- Lesson39 introduces Object as a grammatical function. Lesson42 should distinguish the function of an entire NP from the role of a clitic inside it.
- Lesson40 establishes that clitic presence alone is not a transitivity diagnostic; preserve this rule.
- Lesson41 addresses lexical compounds; clitic placement in compounds must not be inferred from spacing or lexical composition alone.
- Lesson43 is assigned detailed clitic paradigms across past, present, and imperative constructions. Lesson42 should introduce the diagnostic framework and a small set of verified examples, not teach an unverified paradigm.
- Lessons33–34 retain unresolved Subject terminology. Lesson42 must not silently equate Subject and Agent.
- Lesson44's passive analysis must keep former Object, grammatical Subject, and Agent separate.

## 5. Recommended correction queue (not applied)
1. Preserve the composite transcript and expanded draft unchanged.
2. Repair the transcript-segment reference by identifying its exact source path or documenting that the source is embedded at lines 1663–2063 in the composite.
3. Define Clitic structurally (host-dependent) and separate form from grammatical function.
4. Keep possessive clitic inside an NP distinct from the syntactic function of the whole NP.
5. Remove or quarantine the present-tense forms دەمناسێت، دەتناسێت، دەمناسێن، and هەڵت دەبژێرێت until segmentation, person/number, dialect, and native-speaker judgments are verified.
6. Preserve من تۆم بینی as a useful Sorani past-transitive example, but label ـم as an Agent-related/ergative clitic only within the specified construction; explain why it is not Object or possession.
7. Separate Subject, Agent, Object, and agreement terminology; do not settle the outstanding Kurdish Subject term.
8. Keep all listed past forms as unverified data; do not invent missing examples.
9. Replace the "clear appearance" definition of Independent Pronoun with a structural definition.
10. Add a structured table with verified examples, morphological segmentation, gloss, dialect, tense/aspect, and syntactic/semantic roles.
11. Reconcile quiz, examples, exercise answer key, numbering, and metadata only through an approved append-only patch.

## 6. Change boundary
No changes were made to main, the lesson JSON, runtime code, course activation, Botkeep, or Telegram. No terminology owner decision was made. This report is an append-only audit artifact only.

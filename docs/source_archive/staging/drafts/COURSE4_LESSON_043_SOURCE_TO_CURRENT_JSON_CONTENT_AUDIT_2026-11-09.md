# Course 4 — Lesson 43 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of main-branch Course 4 JSON Lesson 43, expanded draft, and the corresponding segment embedded in the Lessons 39–45 composite source. Append-only audit artifact; not an approved lesson revision.

## 1. Provenance verified
- Main JSON: course_data/grammar_course4_lessons.json, main blob e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65.
- Lesson record: grammar_43, number 43, title وانەی 43: جێناوی لکاو لە کردارە تێپەڕەکاندا, status owner_review_pending_expanded_draft.
- Composite source: docs/source_archive/COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md, blob 8c2668b3225269fa3ac47db989a4d3db1e1d50c1, 3125 lines. Lesson43 segment begins at line 2068 and ends at line 2441.
- Expanded draft: docs/source_archive/staging/drafts/COURSE4_LESSON_043_EXPANDED_DRAFT_2026-11-08.md, blob 39e21c43c6815e9411a0fb134316aa9b10753464, 167 lines / 8317 characters.
- The separate transcript-segment path named by the draft, docs/source_archive/staging/drafts/COURSE4_LESSON_043_DRAFT_TRANSCRIPT_SEGMENT_2026-11-08.md, returned 404. The transcript content is present in the composite source segment, not at the asserted standalone path.
- The expanded draft states the transcript is preserved separately, but the exact file was not found at the checked path. Do not claim a standalone transcript artifact exists without verifying its exact path.

## 2. Current JSON shape and content mismatch
- Objectives: distinguish transitive/intransitive uses; overt vs pronominal objects; object clitics vs agent markers and agreement; analyze present, past, and imperative examples only when verified.
- examples=[], quiz=[], comprehension=[], despite a Markdown quiz of five multiple-choice questions, numerous examples, and exercise content.
- key_points[0] contains the near-entire lesson and provenance metadata rather than concise key points.
- exercises mixes four learner tasks with answer-key items; no distinct structured answer-key field.
- The expanded draft contains 15 numbered sections, but the JSON Markdown body is embedded in key_points[0]. Numbering and metadata should be reconciled only through an approved patch.
- Metadata says کۆرسی: ١ — بەشی ٤, inconsistent with the Course 4 repository context; owner decision required.
- The JSON source_path points to the expanded draft, not a standalone owner transcript.
- Current record remains owner_review_pending_expanded_draft; not approved for runtime.

## 3. Conceptual findings

### 3.1 Lesson title and demonstrated content are misaligned
The title promises object clitics in transitive verb constructions. However, the reliable examples mostly demonstrate:
- overt NP objects (من کەژیار دەناسم);
- independent pronoun objects (من ئەو دەناسم);
- possessive marking inside an NP (کتێبەکەی / نامەکەی);
- imperatives with overt NP objects (کتێبەکە بخوێنەوە);
- person/number agreement on an intransitive verb (من دەچم، تۆ دەچیت...);
- unverified strings with clitics (گرتمن، ناردمیت...).
The central target—verified object clitic forms in the selected Sorani variety—is not adequately illustrated by a confirmed paradigm. Keep the lesson as a diagnostic framework until such examples are verified; do not imply that every example directly teaches object clitic placement.

### 3.2 The present-tense forms are explicitly unresolved
The transcript gives من دەمناسم، تۆ دەتناسێت، ئەوان دەمناسێن and says they require detailed analysis of subject person, object person, and verb form. The expanded draft similarly flags من دەمناسێت، تۆ دەتناسێت، ئەوان دەمناسێن as unverified and warns against deriving a general rule.
The forms as written are also not a transparent person/number paradigm: the person of the subject and intended object are not consistently recoverable from the sentence as supplied. No morphological segmentation, gloss, dialect statement, or native-speaker confirmation is attached.
Do not teach these as correct examples of object clitics until the intended meanings, dialect, segmentation, and agreement pattern are confirmed. Do not silently repair or replace them with invented forms.

### 3.3 Independent pronoun object is not an object clitic
من ئەو دەناسم and ئەوان ئێمە دەناسن contain overt independent pronouns serving as objects. They are useful controls for identifying the Object function, but they do not themselves exemplify clitic object marking. Explicitly label them as contrastive baseline examples, not evidence for the lesson's core clitic paradigm.

### 3.4 Possessive clitic inside an object NP is not an object clitic
In کەژیار نامەکەی نووسی / کەژیار کتێبەکەی خوێندەوە, the whole NP can be the Object while ـی marks possession inside that NP. The clitic's internal NP function must not be conflated with the syntactic function of the full NP. This follows the key distinction established in Lesson42.
Caution: depending on intended referent and context, the possessor may be recoverable or omitted; the lesson should not use these examples as direct object-clitic paradigms.

### 3.5 Imperative examples need a construction-specific analysis
The transcript lists وەرم بگرە، بانگم بکەن، بم خوازە. It gives a tentative analysis of ـم in وەرم بگرە as a first-person object clitic, but does not fully segment the construction or specify dialect and intended meaning. It explicitly says بم خوازە requires dialect and intended meaning verification.
The expanded draft is more cautious, marking all these forms as needing review. Preserve that caution. For each imperative example, provide the imperative verb form, clitic host, morpheme boundaries, intended object/person, dialect, and a naturalness judgment from a competent speaker. Do not infer a general imperative clitic-placement rule from one unverified form.

### 3.6 Past transitive alignment and agent indexing must be distinguished from object clitics
The lesson correctly warns that past transitive constructions may differ from present-tense patterns and that clitics cannot be classified by their surface position alone. However, its examples کەژیار نامەکەی نووسی and کەژیار ئەوی بینی do not actually demonstrate an object clitic on the verb:
- in نامەکەی, ـی is analyzed as possessive marking inside the NP;
- ئەو is an independent pronoun object.
These are useful contrast examples, not direct demonstrations of the past-transitive clitic pattern.
Coordinate with Lesson42's analysis of من تۆم بینی and the Course 4 unresolved terminology for grammatical Subject, semantic Agent, and agent-indexing/ergative clitic. Avoid treating Agent and Subject as interchangeable.

### 3.7 The past-form strings remain unanalysable without context
The source strings گرتمن، ناردمیت، گرتتن، گرتتانن، گرتمی، گرتنی appear without full clauses, dialect, intended meaning, or segmentation. The draft correctly labels them as unverified. Keep them quarantined as data for investigation, not as paradigmatic forms, answer keys, or evidence of a general rule. No missing examples should be invented to complete the series.

### 3.8 Verb agreement section is a separate topic and needs precise morphology
The paradigm من دەچم، تۆ دەچیت، ئەو دەچێت، ئێمە دەچین، ئێوە دەچن، ئەوان دەچن illustrates person/number distinctions in the verb, but the lesson does not show morpheme boundaries or distinguish tense/aspect marker, stem, and agreement endings. It is an intransitive verb paradigm and does not demonstrate object clitics.
The form دەچن is compatible with more than one plural person in the presented material; the draft itself qualifies it by context and dialect. Keep the agreement paradigm clearly separate from object clitic marking, and add dialect and segmentation before teaching detailed morphology.

### 3.9 Transitivity is construction- and use-sensitive
The definition "transitive verb takes a direct object" is useful at an introductory level but should be phrased for the verb's use in the clause, not as an immutable lexical property. An omitted or implicit object does not automatically turn a lexically transitive verb into an intransitive verb. This aligns with Lesson40.
The lesson should not use transitivity alone to infer the presence or function of a clitic.

### 3.10 Subject, Agent, Object, and agreement remain distinct
The source uses "نیشانەی بکەر" and "ئەنجامدەری کردار" somewhat loosely. Preserve four separate analytical dimensions:
- grammatical Subject (syntactic function);
- Agent (semantic role);
- Object (syntactic function);
- person/number agreement or agent-indexing clitic (morphosyntactic relation).
The owner decision queue for Subject = بکەر/نیهاد remains unresolved. Do not settle that terminology in this lesson.

## 4. Cross-lesson alignment
- Lesson39 defines Object as a grammatical function; Lesson43 must distinguish an independent pronoun object from a clitic object.
- Lesson40 explains transitivity, argument realization, and why clitic presence alone is not a transitivity test.
- Lesson42 distinguishes clitic form from function and possessive marking inside an NP from the function of the whole NP.
- Lesson43 should provide a bridge to Lesson42's constructional diagnostics, not repeat unverified present and past examples as established paradigms.
- Lesson44's passive analysis must keep Agent, Subject, Object, and agreement separate.
- The Subject terminology conflict in Lessons33–34 remains an owner decision.

## 5. Recommended correction queue (not applied)
1. Keep the source transcript and expanded draft unchanged.
2. Correct the transcript source reference by recording the composite path and exact line range 2068–2441, or locate the claimed standalone file.
3. Retitle or scope the lesson to distinguish its diagnostic framework from verified object-clitic paradigms until examples are supplied.
4. Mark من ئەو دەناسم and ئەوان ئێمە دەناسن as independent-pronoun object controls, not object-clitic examples.
5. Mark کەژیار نامەکەی نووسی and related examples as possessive clitic inside an NP; do not call ـی an object clitic.
6. Quarantine من دەمناسم، تۆ دەتناسێت، ئەوان دەمناسێن pending dialect, meaning, segmentation, and speaker validation.
7. Quarantine وەرم بگرە، بانگم بکەن، بم خوازە pending dialect-specific morphological and usage analysis; retain the source's uncertainty.
8. Keep past strings گرتمن، ناردمیت، گرتتن، گرتتانن، گرتمی، گرتنی as unverified data; do not invent completions.
9. Separate the intransitive agreement paradigm دەچم/دەچیت/دەچێت/دەچین/دەچن from object clitic marking, and add morpheme segmentation if the morphology is taught.
10. Add a verified paradigm table only after the course dialect is fixed; each row should include full clause, intended meaning, morpheme segmentation, gloss, dialect, tense/aspect/mood, clitic host, grammatical function, and speaker validation.
11. Separate exercises, answer key, quiz, examples, and comprehension into their intended structured JSON fields only through an approved append-only patch.
12. Resolve Course 1 versus Course 4 metadata through owner confirmation, not silent correction.

## 6. Change boundary
No changes were made to main, the lesson JSON, runtime code, course activation, Botkeep, or Telegram. No terminology owner decision was made. This report is an append-only audit artifact only.

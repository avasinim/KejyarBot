# Course 4 — Lesson 44 source-to-current JSON content audit
Date: 2026-11-09
Scope: read-only comparison of main Course 4 JSON Lesson44, expanded draft and composite source segment. Append-only audit only; not an approved revision.

## 1. Provenance
- Main JSON: course_data/grammar_course4_lessons.json, blob e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65.
- Lesson: grammar_44, title "وانەی 44: بەرکار لە ڕستەی نەکارادا؛ بکەری ڕێزمانی و ئەنجامدەری کردار", status owner_review_pending_expanded_draft.
- Composite: docs/source_archive/COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md, blob 8c2668b3225269fa3ac47db989a4d3db1e1d50c1; Lesson44 spans lines 2446–2756.
- Expanded draft: docs/source_archive/staging/drafts/COURSE4_LESSON_044_EXPANDED_DRAFT_2026-11-08.md, blob aeb4eff68bbb2d618babf3b4351470d092eaff58, 167 lines / 7591 chars.
- Claimed separate transcript segment docs/source_archive/staging/drafts/COURSE4_LESSON_044_DRAFT_TRANSCRIPT_SEGMENT_2026-11-08.md returned 404. The composite segment is available; no standalone source file verified.
- No separate owner source text was identified; the JSON/draft says the transcript was saved separately, but the named path is missing.

## 2. JSON structure and editorial issues
- Objectives cover active/passive distinction, promotion of Object to grammatical Subject, Subject vs Agent, omitted Agent, passive vs intransitive, and Kurdish passive formation.
- examples=[], quiz=[], comprehension=[] although the Markdown/draft includes examples, four exercises with answers, and a five-question quiz.
- key_points[0] contains nearly the whole lesson plus metadata; exercises mixes prompts and answer keys; no separate structured answer-key field.
- Draft numbering jumps from section 11 to 14 in its quiz; JSON's embedded Markdown has section numbering and key_points packaging inconsistencies.
- Metadata says "کۆرسی: ١ — بەشی ٤" although this is stored in Course4 repository; owner confirmation required.
- The English heading includes "Object, Passive Voice, and Grammatical Subject"; the lesson should state whether it is teaching passive voice generally or specifically object promotion in Sorani.

## 3. Conceptual findings

### 3.1 Core distinction is valuable
The lesson correctly separates grammatical Subject (syntactic function) from Agent (semantic role). In a canonical passive construction, the active clause's Object can become the passive clause's grammatical Subject, while the Agent may be omitted or expressed in an oblique/by-phrase. This is not a change in the Agent's semantic role.

### 3.2 Passive is not the same as intransitive
The contrast "دەرگاکە کرایەوە" (passive analysis intended) versus "کەژیار هات" (intransitive) is pedagogically useful, provided the first construction's passive morphology and dialect are verified. Lack of an overt Object does not by itself diagnose passive voice.

### 3.3 The lesson's definition overstates focus shift
The definition says passive shifts attention from Agent to Object/event. This is a common discourse tendency, not the grammatical definition. Passive should be defined morphosyntactically/constructionally: the patient/theme argument is promoted to Subject-like position and the Agent is demoted, optionally omitted or obliquely expressed. Information structure and focus are pragmatic effects, not necessary conditions.

### 3.4 Kurdish passive formation needs a controlled, dialect-specific account
Examples:
- مامۆستا وانەکەی نووسی ← وانەکە نووسرا
- پۆلیس دزەکەی گرت ← دزەکە گیرا
- کەژیار دەرگاکەی کردەوە ← دەرگاکە کرایەوە
- کەژیار نامەکەی نووسی ← نامەکە نووسرا
- کەژیار پەیامەکەی نارد ← پەیامەکە نێردرا
are illustrative, but cannot alone establish a productive rule for all transitive verbs. Need identify the passive morphology/auxiliary or participial pattern, aspect/tense, agreement, lexical restrictions, and standard Sorani variety. Validate each form for naturalness, register, and meaning with competent speakers. The draft itself acknowledges this requirement.

### 3.5 Some examples need morphology and semantic review
- "وانەکە نووسرا" / "نامەکە نووسرا": check agreement and whether the passive predicate form varies with the grammatical Subject's gender/number or dialect.
- "دەرگاکە کرایەوە": segmentation and the role of the verbal particle/reflexive element need explanation.
- "دزەکە گیرا": validate the passive form and whether it has any lexicalized or resultative reading.
- "پەیامەکە نێردرا" and "پەیامەکە خوێندرایەوە": naturalness and morphology require dialect confirmation.
- "خانووەکە دروست کرا": determine whether the construction is a passive predicate, a resultative/adjectival participle plus auxiliary, or another structure in the chosen framework.
Do not treat the arrows in the draft as automatic, universally valid conversion rules.

### 3.6 The "لەلایەن" Agent phrase is not fully established
"نامەکە لەلایەن مامۆستا نووسرا" and "کتێبەکە لەلایەن چاپخانەکەوە چاپ کرا" intend to express an overt Agent. The exact case/oblique marking and the postposition/phrase structure of لەلایەن ... ـەوە need dialect and normative verification. Do not assume "لەلایەن" is the sole or universal Agent phrase strategy in Kurdish. Include natural examples from the target dialect and distinguish grammatical Agent phrase from instrument/source adjunct.

### 3.7 Passive vs middle, anticausative, and resultative need guarding
Some intransitive-looking or change-of-state constructions may be middle, anticausative, resultative, or lexical intransitives rather than canonical passives. A passive analysis requires an underlying transitive relation and an Agent argument that is syntactically demoted/optional, not simply a clause with no overt Agent. Add diagnostic comparisons and avoid categorizing every form ending in a similar morphology as passive.

### 3.8 "All transitive verbs" and passivizability
The draft correctly cautions that transitivity alone does not guarantee natural passivization. Add that passivizability is construction- and lexical-semantics-sensitive; object type, affectedness, aspect, and dialect may constrain it. Lesson40's distinction between lexical valency and realized arguments remains relevant.

### 3.9 Terminology alignment
Keep distinct:
- Passive Voice = ڕستە/دەنگی نەکارا (owner-approved form needed);
- Active Voice = ڕستە/دەنگی کارا;
- Grammatical Subject = unresolved Kurdish choice بکەر/نیهاد;
- Agent = ئەنجامدەری کردار;
- Object = بەرکار;
- Patient/Theme = semantic role, not automatically a syntactic Object in every construction.
Do not silently resolve the Subject term conflict from Lessons33–34. "بەرکار لە ڕستەی نەکارادا" is an introductory title but the promoted NP is not still an Object in the passive clause under the intended analysis; explicitly state that it is the former Object / promoted Subject.

### 3.10 Exercise and quiz risks
The five quiz questions test the intended basic distinctions, but the question "لە گۆڕینی کارا بۆ نەکارادا بەرکاری کارا چی لێ دەبێت؟" should say "in a canonical passive construction where passivization is licensed", not imply an exceptionless transformation. Exercises use several unverified passive forms; mark them provisional and do not use as scored answer keys until validated.

## 4. Cross-lesson alignment
- Lesson39: Object as grammatical function; in passive, the former Object may be promoted to Subject.
- Lesson40: transitivity/valency is distinct from voice; a transitive verb is not automatically passivizable.
- Lesson41: lexical compound predicates may have construction-specific passive behavior; don't infer from spacing.
- Lessons42–43: clitics and ergative/Agent indexing must not be mistaken for passive morphology.
- Lessons33–34: Subject term and Subject vs Agent distinction remain unresolved/important.
- Lesson45: topicalization/focus are information-structure operations, not passive voice.

## 5. Recommended correction queue (not applied)
1. Preserve transcript and expanded draft unchanged.
2. Replace broken standalone transcript reference with the verified composite source path and lines 2446–2756, or locate the missing file.
3. Define passive morphosyntactically, then discuss discourse focus as a tendency separately.
4. Identify the target Sorani variety and describe the actual passive formation, including segmentation, aspect/tense, agreement, and restrictions.
5. Validate every passive example with full active/passive pair, intended meaning, naturalness judgment, dialect, and morphology.
6. Distinguish canonical passive from middle, anticausative, resultative, and lexical intransitive constructions.
7. Verify the لەلایەن ... ـەوە Agent phrase and distinguish Agent from instrument/source adjunct.
8. Describe promoted Object as former Object / grammatical Subject in passive, not as an Object that retains the same syntactic function.
9. Keep Subject=بکەر/نیهاد as an unresolved owner decision; maintain Agent=ئەنجامدەری کردار and Object=بەرکار.
10. Correct section numbering and separate examples, exercises, answer key, quiz, and comprehension in JSON only through an approved append-only patch.
11. Do not score exercises or quiz items that depend on unverified passive forms.
12. Resolve Course1/Course4 metadata only with owner confirmation.

## 6. Change boundary
No changes to main, lesson JSON, runtime, activation, Botkeep, or Telegram. No terminology decision or lesson approval was made. This file is an append-only audit artifact only.

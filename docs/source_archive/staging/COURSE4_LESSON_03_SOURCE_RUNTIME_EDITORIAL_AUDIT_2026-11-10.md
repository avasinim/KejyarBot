# Course 4 — Lesson 3 source/runtime cross-check and editorial findings (2026-11-10)

## Scope and sources
- Owner-source extract: `docs/source_archive/COURSE4_LESSON_03_NAME_SOURCE_AND_AUDIT_2026-11-07.md` on `main` (blob SHA `d91b5aeba634516a783f946d51264fd8116bc879`). Its header records the original user source as `Pasted text(2).txt`, lines 53–867.
- Runtime baseline: `course_data/grammar_course4_lessons.json` on `main`; lesson object `grammar_03`.
- Reconciliation baseline: `docs/source_archive/staging/COURSE4_ARCHIVE_RECONCILIATION_LESSONS03_07_AND_PATCH45_2026-11-10.md` on `archive/preservation-audit-2026-11-10`.

## Verified runtime inventory
Lesson 3 is present in the 46-lesson runtime and has:
- 35 key points
- 15 structured examples
- 3 activities
- 5 exercises
- 10 comprehension entries
- 8 quiz questions
- 30 appendix entries
- review status: `scientific_review_complete_with_qualified_notes`

This confirms the lesson is populated. It does not by itself prove that every raw-source claim has been validated or that every subtopic is pedagogically assessed.

## Source-to-runtime findings
1. The owner-source extract contains a large noun lesson core: noun categories, definiteness, number, gender, derivation/compounding, reduplication/sound-symbolic forms, diminutives, and candidate forms for plural and linker morphology.
2. The extract also contains material on verbal infinitives and compound verbs. The runtime correctly treats these as cross-references to Lessons 31 and 30 rather than expanding them as core noun content.
3. The later source continuation introduces nominal linkers/interfix candidates `لە`, `نە`, `تا`, `نا`, `ەو`, `او`, and others. Runtime key points 30–35 preserve this material but explicitly distinguish genuine bound word-formation elements from free prepositions, particles, conjunctions, and phonological glides.
4. The runtime appropriately keeps uncertain forms such as `داخلەدڵ`, `شەولەبان`, `کەسنەزان`, `بارنەبەر`, `سەرتاپا`, `تاوناتاو`, and `شارەوشار` as candidates pending lexical, corpus, semantic, and dialect evidence. They are not taught as a settled, universal inventory of Sorani interfixes.
5. The research-backed examples are more tightly controlled: `گوڵەباخ` and `گاکێوی` are linked to Jambrović & Hassan (2023); `گوڵەگەنم`, `سەوزەگیا`, and `ڕەشەبا` to Huseen & Shuani (2024); and `ئاسنگەر` / `کچۆڵە` to the cited Sorani morphology source. The appendix itself correctly limits the scope of these citations.

## Concrete editorial findings (no runtime edits made)
### A. Repetition among key points
The 35-point list contains several close repetitions:
- Points 1 and 9 both define the noun and stress that meaning/labeling alone is insufficient.
- Points 5 and 17 both explain collective nouns and distinguish semantic collectivity from morphological number.
- Points 6 and 18 both contrast common/proper, definite/indefinite, and singular/plural classifications.
- Points 7 and 9 partially overlap on word class, grammatical behavior, and sentence function.

These repetitions are not factual errors, but they increase the lesson's length and obscure the progression. Because the project rule is to preserve all original material, any future editorial pass should consolidate by cross-reference or re-ordering—not silently delete points.

### B. Assessment coverage gap for the interfix subsection
The lesson contains six key points on interfixes/linkers (30–35), structured examples 13–15, and quiz question 8 on the distinction between `-ە-` and `-و-`. However:
- the three activities focus on noun classification and sentence function;
- the five exercises focus on noun forms, categories, gender, derivation/compounding, and selected suffixes;
- no activity or exercise directly asks learners to distinguish a morphological interfix from a free word, conjunction, preposition, or phonological glide.

This is a genuine teaching/assessment alignment gap. A future append-only supplement could add one short classification activity and one worked analysis exercise using only the cited, research-backed examples, while retaining all existing items. It should not turn the unverified candidate list into established rules.

### C. Lesson boundary and content load
The runtime's cross-references for infinitives and compound verbs (Lessons 31 and 30) are appropriate. The interfix section is relevant to noun compounding, but its six-point theoretical block makes Lesson 3 carry both core noun grammar and a specialized word-formation subsection. If retained here, it should be explicitly labeled as an advanced extension, with the detailed treatment cross-referenced to the course's word-formation unit when that unit is verified.

### D. Small structural issue
The 35 points currently move from noun basics to morphology, then back to collective nouns and classification distinctions before moving to gender and word formation. A clearer teaching sequence would group: (1) definition and syntactic behavior; (2) semantic/reference classifications; (3) number and definiteness; (4) natural vs grammatical gender; (5) word structure; (6) interfix extension; (7) cross-references to other lessons. This is a reordering proposal only, not an edit.

## Recommended next step
Prepare a separate, append-only editorial supplement for Lesson 3 containing:
- a proposed non-destructive key-point sequence and cross-reference map;
- one activity and one exercise for interfix recognition, limited to source-supported cases;
- an explicit note that candidate forms remain unverified and dialect-bound until evidence is supplied.

Do not change the runtime JSON or create/apply a patch until the proposed supplement has been checked against the original source and the cited papers. No content was deleted, no runtime file was edited, and no Botkeep, Railway, database, deployment, or Telegram state was changed by this audit.

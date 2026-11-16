# Course 4 terminology consistency audit — evidence snapshot (2026-11-12)

Status: **evidence audit only; no terminology decisions or lesson edits authorized by this note.**
Branch: `release/main-based-reconciled-2026-11-11`
Reviewed runtime source: `course_data/grammar_course4_lessons.json`
Companion draft register: `docs/source_archive/staging/COURSE4_TERMINOLOGY_REGISTER_DRAFT_2026-11-11.md`

## Scope and method

Read-only comparison of the runtime lesson records for Lessons 11, 12, 13, 29 and 31, including their key points, examples, comprehension text, appendices and quiz banks. The purpose is to identify exact internal variants and semantic boundaries before any owner-approved normalization. This note does not choose a preferred Kurdish equivalent.

## Findings

### 1. Enclitic — `پاشبەستە` / `پاشنووس`

- Lesson 11 key point 1 uses `پاشبەستە (Enclitic)`; Lesson 11 appendix glossary uses `Enclitic = پاشنووس (لکاوی دواوە)`.
- Lesson 12 appendix glossary also uses `Enclitic = پاشنووس`.
- Lesson 13 key points, example, comprehension, quiz and appendix prose use `پاشبەستە`; its appendix crosswalk uses `Enclitic = پاشنووس`.
- Lesson 13 explicitly distinguishes an enclitic from a suffix and from the broader bound-morpheme category. Preserve that conceptual distinction regardless of the eventual label.
- Lesson 13 has status `internal_cross_lesson_synthesis_no_external_source_mapping`; it is not an academically approved authority for resolving the label.

**Decision needed:** owner-approved canonical label, with the other observed form retained in the dated history/alias record if approved. Do not replace either form automatically before that decision.

### 2. Inflection — `گەردان` / `لەچۆنایەتی`

- Lesson 29 key points and comprehension use `گەردان (Inflection)`.
- Lesson 29 appendix glossary uses `گەردان (Inflection)`.
- Lesson 29 quiz question 4 and its answer options use `لەچۆنایەتی`; the explanation switches to English `Inflection`.
- Lesson 30 and the runtime cross-course register also use `گەردان` (as recorded in the draft register).

**Decision needed:** owner-approved label and quiz synchronization. Preserve the distinction between Inflection and Derivation; do not infer that either Kurdish form means conjugation in every context.

### 3. Noun Phrase — `گرێی ناوی` / `گروپی ناوی`

- Lesson 31 runtime key points, examples, comprehension and appendix use `گرێی ناوی`.
- Lesson 31 quiz questions/explanations use `گروپی ناوی` in five occurrences (including the nominalization definition, the Kareem example, the Salavati & Ahmadi example, and the distinction question).
- The draft register records `گروپی ناوی` in patch 31-v2 and `گرێی ناوی` in runtime Lesson 31.

**Decision needed:** owner-approved form for lesson prose and quiz bank, while preserving patch/runtime provenance. The concept is a phrase constituent; do not turn the term decision into a claim that it is a single word or a word class.

### 4. Subject — `بکەر` / `بابەت`

- Lesson 12 appendix explicitly maps `Subject = بکەر` and `Object = بەرکار`.
- Lesson 31 describes a nominalized constituent in Subject position as `بابەت (Subject)`; its quiz calls the same role `بابەتی ڕستە`.
- Lesson 31 source discussion is about syntactic position/function, while `بابەت` can also be read more broadly as “topic/subject matter”. The present evidence alone does not authorize treating `بابەت` and `بکەر` as synonyms or replacing one with the other.
- Keep grammatical Subject distinct from Agent (`ئەنجامدەری کردار`) and from discourse Topic until the source/framework mapping is approved.

**Decision needed:** inspect the cited source's syntactic terminology and the intended Sorani grammatical tradition, then approve a contextual mapping. No automatic substitution is safe.

## Cross-cutting guardrails

1. Preserve Clitic (`لکاو`), Enclitic, Affix (`ئەفیکس/گیرەک`), Suffix (`پاشگر`) and bound morpheme as distinct concepts unless a source-backed analysis explicitly relates them.
2. Preserve Derivation vs Inflection; do not infer equivalence from quiz phrasing.
3. Preserve Subject vs Agent vs Theme/Patient vs discourse Topic.
4. Keep patch terminology and runtime terminology separately traceable; do not rewrite archival patches to make them appear consistent.
5. No lesson, quiz, academic review status, reward logic or learner data was modified during this audit.
6. CI success is not an academic terminology approval.

## Recommended next review action

Ask the project owner to approve the four terminology mappings above, preferably against the original lesson sources and the cited grammatical literature. Once approved, apply dated append-only terminology decisions and narrowly scoped runtime/quiz updates with regression tests. Until then, leave the four conflicts unresolved and visible.

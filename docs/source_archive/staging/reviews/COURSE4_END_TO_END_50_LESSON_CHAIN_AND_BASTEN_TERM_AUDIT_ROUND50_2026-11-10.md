# Course 4 — End-to-End 50-Lesson Chain, Cross-Reference and Terminology Audit (Round 50)
Date: 2026-11-10
Branch: `botkeep-menu-clean-2026-11-09`
Source: `course_data/grammar_course4_lessons.json`
Source blob SHA: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
Scope: all 50 lesson records; title, objective, key_points, examples, exercises, comprehension, appendix, activities and structured quiz fields.

## 1. User-approved terminology preference
Use Sorani `بەستێن` in new course prose instead of `سیاق` for the intended linguistic sense (context). This is the preferred editorial equivalent for subsequent work. Do not preserve the old form merely for stylistic consistency.
A literal-string scan found 146 occurrences of `سیاق` in the reviewed fields, across lessons 3–19, 21–24, 26–27, 29–32 and 48. This count is tied to the source SHA above and the stated fields; it is not a quality KPI. The count includes inflected/compound forms detected as the exact substring and does not itself establish that every occurrence is semantically appropriate.
Recommended treatment: prepare an occurrence-level append-only replacement patch using `بەستێن` and grammatically appropriate inflections (e.g. `لە بەستێندا`, `بەپێی بەستێن`, `بەستێنی ڕستە`). Review every sentence for syntax and meaning; do not perform an indiscriminate byte-level replacement that creates ungrammatical Sorani. Raw lesson JSON remains unchanged in this round.

## 2. Course inventory and quiz structure
- Lesson records: 50.
- Structured quiz-bearing lessons: 31 (Lessons 1–31).
- Structured quiz items: 248 (8 per lesson across Lessons 1–31).
- Lessons 32–50: 19 records without a structured runtime quiz array in this source snapshot. Exercises or draft quiz-like text elsewhere in the lesson are not counted as active structured quizzes.
- No Lesson 51 was created or proposed.

## 3. Cross-reference scan
A bounded scan of lesson fields for explicit references matching the Kurdish lesson-reference patterns found 19 references and no target number outside 1–50. This is a pattern-based check, not a full semantic validation: implicit references, alternate spellings and references expressed without the scanned word patterns may not be captured. Lesson references should still be checked during any future lesson-specific revision.

## 4. Cross-course integrity principles reaffirmed
- Preserve the distinction among grammatical function, semantic role, constituent category and word class.
- Do not classify a form by spelling alone when the same form can have more than one function.
- Keep dialect and source scope visible; Central Kurdish/Mukri evidence is not automatically a rule for every Sorani variety.
- Do not convert draft examples or exercises into runtime quizzes without source-backed validation and explicit patch review.
- Keep the Root/Bound Root/Stem/Base/Lexeme crosswalk separate from Sorani verb-paradigm terms such as `بنجی ئێستا` and `بنجی ڕابردوو`.
- Preserve the distinction among Prefix, Suffix, Clitic, Enclitic, Preposition and Verbal Particle; assign categories by framework and construction.
- Keep the distinction between inflection (`گەردان`) and derivation (`داڕشتن`).
- No lesson count beyond 50.

## 5. Editorial action queue
1. Adopt `بەستێن` as the default term in all new lesson text and future append-only patches.
2. Build a sentence-aware patch list for the 146 legacy occurrences identified in this snapshot; inspect every one before applying any source change.
3. Review cross-references again as part of each individual lesson patch, preserving lesson numbering and source provenance.
4. Keep all unresolved dialect-sensitive examples and terminology decisions explicitly marked pending rather than silently normalizing them.

## 6. Preservation and release status
- This report is an append-only archive artifact.
- No raw lesson JSON changed.
- No quiz question, option, answer index or explanation changed.
- No runtime, database, Botkeep or Telegram state changed.
- No merge, deployment, activation or publication performed.
- PR #125 remains a separate open runtime/menu workstream and is not approved for merge by this audit.

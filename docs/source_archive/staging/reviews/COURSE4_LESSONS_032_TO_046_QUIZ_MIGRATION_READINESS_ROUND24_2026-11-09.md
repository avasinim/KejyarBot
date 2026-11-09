# Course 4 — Lessons 32–46
## Quiz migration readiness and release blockers
### Round 24 — 2026-11-09

**Purpose:** identify the finite assessment work that blocks a complete Course 4 release.

## Verified source state
- Source: `course_data/grammar_course4_lessons.json` on `main`.
- Source blob SHA: `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`.
- Lessons 32–46 inclusive: 15 lessons.
- All 15 structured `quiz` arrays are empty.
- Every one of the 15 `source_markdown` lesson drafts contains an embedded quiz with five numbered questions and an answer key: **75 embedded questions total**.
- All 15 lessons are marked `owner_review_pending_expanded_draft`.
- No source JSON, runtime, database, `main`, Botkeep, Telegram, or deployment change was made.

The assessment content is not missing. It is already preserved in Markdown. The task is controlled conversion into the runtime schema, plus correction of a small number of unsafe/ambiguous questions.

## Recommended release strategy
1. Preserve every original embedded quiz verbatim.
2. Convert the 75 items into the existing structured format `{ "q": "...", "options": ["...", "..."], "answer": 0, "explanation": "..." }`.
3. Retain five questions per lesson; do not inflate the sets to eight merely to match older snapshots.
4. Where a question is ambiguous or conflates concepts, preserve it in the original source and add a clearly documented replacement item.
5. Validate schema, option uniqueness, answer indices, and answer/explanation agreement with automated tests.
6. Run Course 4 progression and quiz completion tests before activation.

## Per-lesson migration status

| Lesson | Embedded | Structured | Migration note |
|---|---:|---:|---|
| 32 | 5 | 0 | Convert; preserve Subject/Agent and NP/VP distinctions |
| 33 | 5 | 0 | Convert; retain Subject vs Agent |
| 34 | 5 | 0 | Convert; retain Predicate vs Verb vs Copula |
| 35 | 5 | 0 | Convert; communicative purpose is distinct from clause structure |
| 36 | 5 | 0 | Check Complement/Object/Adjunct and Adverbial labels |
| 37 | 5 | 0 | Retain warning that «هێشتا» is not automatically a conjunction |
| 38 | 5 | 0 | Keep Main/Subordinate separate from Independent/Dependent |
| 39 | 5 | 0 | Keep NP Object separate from the function of `-ی` |
| 40 | 5 | 0 | Keep Transitivity separate from Voice; omitted Object is not proof of intransitivity |
| 41 | 5 | 0 | Compound lexical verb vs noun + light verb remains framework-sensitive |
| 42 | 5 | 0 | Do not infer clitic function from form alone |
| 43 | 5 | 0 | Existing Q2's possessive reading of `-ی` in «کتێبەکەی خوێندەوە» is not safe without context |
| 44 | 5 | 0 | Existing Q3 conflates Passive Voice and Intransitivity |
| 45 | 5 | 0 | Validate fronted-object examples and clitic forms in target dialect |
| 46 | 5 | 0 | Harmonize Compound/Complex terminology with Lesson 37 |

## Required targeted corrections

### Lesson 42
Keep the NP/clitic distinction: in «کتێبەکەم», the whole noun phrase can be the Object while `-م` marks possession. Do not infer a clitic's function from spelling or position alone.

### Lesson 43
Existing Q2 treats `-ی` in «کتێبەکەی خوێندەوە» as possessive. That is not a safe unqualified rule because possessive clitics and person markers can overlap in form in Sorani. Replace the assessment target with the safe principle that clitic function must be identified from host, clause, alignment, context, and morphological analysis. Preserve the original item.

### Lesson 44
Existing Q3 asks whether «کەژیار هات» is passive or intransitive. These are not mutually exclusive labels: Passive is a Voice category; intransitive is a Transitivity category. Replace with two distinct items: classify transitivity, then independently identify whether passive morphology/construction is present. Preserve the original item.

### Lessons 39, 40, 45
Keep Recipient/Goal distinct from Object and Indirect Object; keep transitivity separate from voice; do not infer grammatical function from word order alone. Specific Sorani examples still need target-dialect validation.

## Runtime facts inspected
- `course_lesson_adapters.py` already supports the structured quiz shape and validates non-empty question text, at least two non-empty options, unique options, and an integer answer index in range.
- `bot.py` loads Course 4 from the JSON via the unified orthography adapter with extended sections.
- Startup validation has a Course 4 exception for lessons whose review status begins with `owner_review_pending`, allowing pending lessons without structured quizzes. Therefore, missing structured quizzes are an assessment-completeness blocker, but not necessarily the only startup blocker.
- `course_quiz_review.py` contains legacy Course 1 keys; do not assume it governs Course 4 readiness. Inspect the actual Course 4 callback and completion path before changing activation behavior.

## Automated checks required
1. Exactly 46 lesson IDs in source order, no duplicate IDs/numbers.
2. Exactly 15 expanded drafts at Lessons 32–46.
3. All 75 original embedded quiz items remain preserved.
4. Structured items pass adapter validation and every answer index maps to the intended option.
5. Every Course 4 lesson is reachable in progression order.
6. Every quiz starts, accepts answers, completes, and awards rewards once only.
7. Invalid quiz payloads cannot complete a lesson.
8. No regressions to Courses 1–3, SQLite progress keys, or reward logic.
9. Course 4 remains isolated from legacy Course 1 review keys.

## Immediate implementation task
Create a dedicated append-only structured-quiz migration for Lessons 32–46 from the existing 75 questions. Document replacement items for Lessons 43 and 44; preserve all original Markdown; run automated validation; only then prepare a release candidate.

## Release boundary
This report does not approve lessons academically, change review statuses, or authorize deployment. It narrows the next work to a finite task: migrate and validate the 75 existing questions, then test Course 4 end-to-end. No Lesson 51 is required.

**Integrity:** source SHA remains `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`; no production or live-bot operation was performed.

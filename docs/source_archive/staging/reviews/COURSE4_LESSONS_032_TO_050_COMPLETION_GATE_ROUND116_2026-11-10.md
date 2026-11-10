# Course 4 Lessons 32–50 Completion Gate — Round 116
Date: 2026-11-10
Repository: avasinim/KejyarBot
Inspected working head: c41fc186e8e2482de336d297c3b7dd9758356e08
Branch: audit/course3-diako-20261110
Status: append-only audit; no runtime or source lesson changes

## User authorization and operating rule
The user has authorized autonomous editorial and technical decisions for completing Course 4 Lessons 32–50 and explicitly said not to wait for separate approval on each lesson. This authorizes continuing the content and QA work. It does not waive source accuracy, data integrity, or the separate release/deployment safety gate.

## Verified source state
Inspected `course_data/grammar_course4_lessons.json` at the working head above:
- Exactly 50 lesson records are present.
- Lessons 32–50 (19 lessons) all have expanded `source_markdown` and objectives.
- Lessons 32–46 have 1 key point each, 219 exercises in total, and 15 comprehension items in total.
- Lessons 32–46 have no structured examples and no structured quiz items in the source lesson records.
- Lessons 47–50 currently have empty key_points, examples, exercises, comprehension, and quiz arrays in the source lesson records.
- Lessons 47–50 do have expanded source_markdown (including 9,741; 9,601; 8,620; and 14,742 characters respectively).
- All 19 lessons are currently labelled `owner_review_pending_expanded_draft`.

## Existing quiz candidate inspection
Inspected `docs/source_archive/staging/drafts/COURSE4_LESSONS_QUIZ_INTEGRATED_CANDIDATE_V3_TERMS_2026-11-10.json`:
- Contains 5 quiz items for each of Lessons 32–50: 95 total.
- All 95 quiz items have an answer index within the available options.
- 95/95 explanations are empty.
- Only 27/95 items have exactly three options; option counts vary and require schema/pedagogical normalization.
- 91 unique question stems among 95 items; exact repeated stems require correction before integration.
- No structured examples have yet been populated for Lessons 32–50.
- This V3 file is a staging draft, not the source/runtime lesson file.

## Confirmed content issues requiring correction
1. Lessons 32 and 33 repeat the same question stem about distinguishing grammatical subject from semantic agent. Lesson 33 needs a distinct question aligned to its own lesson objective.
2. Lessons 42 and 43 repeat the same question stem about `ئەو` in `من ئەو دەناسم`; Lesson 43 needs a different item that tests clitic function in a complete sentence and dialect/context.
3. The quiz candidate contains 95 blank explanations. They must be authored and checked, not filled with generic placeholder text.
4. Some questions use only two options; the final candidate should use a consistent, tested option count and plausible distractors.
5. Lesson 32 includes a noun-phrase definition item that overlaps Lesson 47; retain only if it is intentionally a preview, otherwise replace with a sentence-foundation concept.
6. Lesson 43 must not assign a fixed grammatical function to a clitic based only on its written form; require complete clause, dialect, morphological segmentation, and context.
7. Lesson 48 must keep valency distinct from transitivity, grammatical functions distinct from semantic roles, and arguments distinct from adjuncts.
8. Lesson 49 must keep the Gharib & Pye Suleimani/Sanandaj evidence separate from BivalTyp Mahabad Mukri data. Do not conflate Direct/Oblique with VAM/PC.
9. Lesson 50 must use the corrected Round 115 quiz candidate and preserve the direct-source correction: in Bahar (2023) example (9), `aw` is glossed `s/he`; `-y` in `da-y=kr-e` is glossed `it.RES`. The source describes `ka` as an invariant marker introducing post-nominal relative clauses; do not overstate the terminology beyond the paper.
10. Kurdish example forms in Lessons 32–49 still need target-dialect validation. Where not verified, label examples as schematic or avoid presenting them as established dialect facts.

## Required completion sequence
A. Build a new append-only structured candidate for Lessons 32–50; never overwrite the original lesson JSON or V3 draft.
B. Extract and organize lesson-specific key points, examples, exercises, and comprehension items from each preserved source_markdown and existing draft. Keep all existing source text and exercises.
C. Revise the 95 quiz items: remove repeated stems, normalize option counts, add meaningful explanations, validate every answer, and align each item to its lesson.
D. Cross-check terminology across Lessons 32–50 and earlier lessons. Keep the user's preferred term `بەستێن` (not `سیاق`).
E. Run JSON/schema, duplicate, answer-index, lesson-count, source-preservation, and runtime compatibility checks; record exact results.
F. Only after the candidate is validated should it be proposed for integration into the existing PR working head. Do not merge, deploy, sync Botkeep, restart the server, or alter learner data while the Botkeep staging incident remains unresolved.

## Release decision
NOT READY FOR RUNTIME ACTIVATION.
This is not a request for further user approval. Continue autonomously with the completion sequence above; hold only the technical release boundary until the candidate and backend are verified safe.

## Preservation
No source lesson JSON, runtime file, loader, quiz bank, student data, Botkeep state, merge, deployment, sync, or server restart was changed in this round.

# Course 2 — proposed editorial patch (approval pending)

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** proposal only — not applied to the reviewed lesson or quiz files  
**Base reviewed quiz SHA:** `abc88219e2a0e249883e8d62c5117a9b3aaa3108`  
**Base reviewed answer-key SHA:** `879e1525e720bdc25b8f6e896de3e388801238d0`

## Purpose and preservation rule

This proposal turns the findings in `KEJYARBOT_LATIN_COURSE2_62Q_DISTRACTOR_ORTHOGRAPHY_REVIEW_2026-11-11.md` into concrete suggested edits. It is a review artifact only. It does not change either base file, the source-aligned originals, runtime, tests, manifests, database, Botkeep, Telegram, or deployment state.

If approved, apply the edits only to a new dated append-only reviewed-draft/patch artifact. Preserve the current reviewed files and answer key unchanged as the baseline. Then run the structural quiz/key comparison again and document the resulting new blob SHAs.

## A. Lesson 6 — Question 3 terminology

**Current stem**

`Di `hespê beza` de bireser çi ye?`

**Proposed stem**

`Di koma navdêrî `hespê beza` de, kîjan hêman `bireserê navdêrê` ye?`

**Options and key:** retain the current options and keyed answer `beza`, subject to rechecking the sentence against the lesson text.

**Reason:** the lesson distinguishes the noun modifier `bireserê navdêrê` from the sentence-role term `bireser`. The question should use the full term and avoid undoing that distinction.

## B. Lesson 8 — Question 5 distractors

**Current stem**

`-ên û -ine ma yek in?`

**Proposed stem**

`Ma veqetandeka binavkirî ya gelemjimar `-ên` û veqetandeka nebinavkirî `-ine` heman erkê hene?`

**Proposed options**

- A) Erê, her du formên binavkirî ne.
- B) Erê, her du formên nebinavkirî ne.
- C) Na, erkên wan cuda ne.

**Key:** C.

**Reason:** A and B are parallel, recognizable confusions between the definite and indefinite paradigms. The current “erê / her tim” alternatives are near-duplicates and do not test a useful grammatical misconception. Confirm the revised wording against the precise terminology in Lesson 8 before approval.

## C. Lesson 10 — Question 1 object context

**Current stem**

`Kîjan yek ji pronavên bireser e?`

**Proposed stem**

`Di hevoka dema niha de `Tu ___ dibînî`, kîjan pronav li cihê bireserê tê?`

**Proposed options**

- A) `te`
- B) `min`
- C) `me`

**Key:** B (`min`).

**Reason:** the lesson explicitly cautions that forms such as `min` do not have an invariant subject/object role; the clause construction determines the role. The sentence frame makes the intended direct-object function observable rather than attributing a permanent role to the form.

## D. Lesson 10 — Question 2 object context

**Current stem**

`Forma bireserî ya `ew` mê çi ye?`

**Proposed stem**

`Di hevoka dema niha de `Ez ___ dibînim`, kîjan form ji bo pronavê kesê sêyem yekjimar a mê wek bireser tê?`

**Proposed options**

- A) `wî`
- B) `ew`
- C) `wê`

**Key:** C (`wê`).

**Reason:** `wê` also occurs as an inflected agent in past-transitive clauses. A present-tense direct-object frame removes that potential confusion and tests the intended form in context.

## E. Lesson 8 — three mixed-script explanatory lines

The following are proposed full-line replacements for the three affected lines in the reviewed lesson draft. They should be checked against the cited source section before any approved patch is produced.

**Draft line 290 — proposed replacement**

`Ji ber vê yekê formên tewandî divê ji formên bingehîn yên `-ek/-ek/-in` cuda bên fêrkirin.`

**Draft line 292 — proposed replacement**

`Dema ku zêdetir ji yek pêvek bi navdêrê ve tên girêdan, şêweya veqetandekê li gorî mêjer û zayenda pêkhateya dawî tê diyarkirin. Ev hûrgilî di vê dersê de wek rêgezeke pêşketî hatiye pêşkêşkirin, ne wek bingehê destpêkê.`

**Draft line 294 — proposed replacement**

`Nîşe: `-ek/-ek/-in`, `-ekî/-eke/-ine` û `-î/-e/-en` sê komên formên cuda ne; divê her yek li gorî şert û erkê xwe were bikaranîn. Ev form ji veqetandekên binavkirî `ê/a/ên` cuda ne.`

## F. Required validation if approved

1. Preserve the two base reviewed artifacts and create a new dated patch copy; do not overwrite either base file.
2. Apply only the approved wording changes. Do not change answer letters unless a separate source-based reason is recorded.
3. Update the corresponding answer-key rationales so they explain the new context and terminology; keep the 62-row coverage intact.
4. Re-parse all 12 lesson quizzes and the key. Confirm 62 questions, 62 key rows, no missing/orphan/duplicate rows, valid option labels, and exact normalized answer-text matches.
5. Re-scan the full lesson draft for unintended mixed-script fragments and terminology consistency.
6. Append the new report and verification results to the global audit and preservation checkpoint.
7. Keep runtime and deployment untouched unless separately authorized. Tests/CI remain unexecuted unless explicitly run in a later authorized task.

## Approval boundary

No proposed edit in this file has been applied. A separate explicit approval is required before creating the revised lesson/quiz/key patch artifact. The archive branch remains the only writable branch for this work; `main` remains read-only.

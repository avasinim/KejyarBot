# Course 2 — L5 Q1 distractor refinement and L4 Q5 sequencing patch

**Date:** 2026-11-11  
**Status:** Append-only editorial proposal; not approved or applied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## Source versions

- Reviewed quiz: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Reviewed answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`, SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.
- Source grammar: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel 2002, §§52–56 and §66.

## 1. L5 Q1 — replace overlapping distractors

**Current stem:** `Tewang çi ye?`  
**Current key:** B — `guherîna forma peyvê`.

The earlier candidate set proposed gender change and number change as A/C. Source §55 states that nouns are inflected according to gender and number; therefore those distractors can be understood as conditions/dimensions associated with inflection, not fully exclusive alternatives. This is a discrimination flaw even though the current key B is supported by the lesson's broad definition.

**Refined candidate options (key B retained):**

- A) `guherîna erkê peyvê bê guherîna forma wê`
- B) `guherîna forma peyvê li gorî erkê wê`
- C) `guherîna wateya peyvê bê guherîna forma wê`

**Rationale:** B expresses the lesson's form-change definition. A contrasts syntactic role without a morphological form change; C contrasts semantic change without a form change. These are cleaner conceptual alternatives than gender/number changes, which can participate in inflectional paradigms.

**Caveat:** The exact phrasing is a proposed Kurmanji editorial formulation. A native-Kurmanji editor should check idiom and ensure A does not become an overgeneralized claim about every construction.

## 2. L4 Q5 — sequencing correction for the optional contrast

The earlier optional proposal contrasts `hespan` and `hespin`:
- `hespan`: plural oblique/inflected form in the source's §55 examples.
- `hespin`: indefinite plural form in §66.

The contrast is linguistically useful, but its answer requires the concept of `tewang`, formally taught in Lesson 5. Lesson 4 precedes that instruction. Thus, the contrast should **not** be placed in the Lesson 4 end-of-lesson quiz.

**Preferred disposition:**
- Keep the current Lesson 4 Q5 and its current key C unchanged for now.
- Preserve the `hespan/hespin` contrast as a candidate for a cumulative review after Lesson 5, or as a Lesson 5 comparison exercise.
- If later authorized for that cumulative location, candidate stem: `Cudahiya “hespan” û “hespin” çi ye?`
- Candidate key B: `hespan` is the inflected/oblique form; `hespin` is the indefinite plural form.

This placement ensures the distinction is tested after both number and inflection have been taught.

## Preservation boundary

This patch is an editorial proposal only. No lesson, quiz, answer-key, rationale, runtime, parser, manifest, database, Botkeep, Telegram or deployment file was changed. No tests, CI, runtime checks or learner-response analysis were run. `main` remains read-only. Archive branch is not an independent ZIP/offsite backup.

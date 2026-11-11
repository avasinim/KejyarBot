# Course 2 — Editorial refinement E1–E3 source recheck

**Date:** 2026-11-11  
**Status:** Teacher/editor-facing proposal only; not approved or applied.  
**Branch:** `archive/preservation-audit-2026-11-10`

## Inputs re-fetched

- Consolidated 45-rationale pack: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_CONSOLIDATED_45_RATIONALE_EDITORIAL_REVIEW_PACK_2026-11-11.md`, SHA `177faaaa5260879bf4b2211474dede013f8d002c`.
- Editorial preflight: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_45_RATIONALES_EDITORIAL_PREFLIGHT_2026-11-11.md`, SHA `70e075aaddf5848aee1598e6f59c3e4251a455a5`.
- Source-aligned lessons: `course_data/latin_course_2_source_aligned_lessons_01_12.md`, SHA `19090077a11dc9d7211987e958e560b328fcd3d6`.
- Reviewed quiz/lesson draft: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.

## Recheck method

The three editorial flags were checked against the exact lesson definition/example, quiz stem and options, and the consolidated rationale. The check is a source-and-clarity review, not native-speaker certification.

## E1 — Lesson 2, Question 2

**Quiz:** `hesp` is keyed C, `hevenav`.

**Source support:** Lesson 2 defines `hevenav` as the general name of people, animals or things, and says it is used for multiple members of the same category. `hesp` is explicitly listed as an example.

**Finding:** The prior wording `hesp navê giştî yê heywanê hesp e` is circular because it repeats the same lexical item as both category and definition. The key and classification are supported; the explanation should instead state the category membership.

**Suggested wording for qualified editor review:**

> `Hesp` navê giştî ye ku ji bo heywanên vê cureyê tê bikaranîn; ji ber vê yekê hevenav e, ne serenavê kesek an tiştekî taybet.

**Disposition:** Clarity refinement only. Key C unchanged.

## E2 — Lesson 11, Question 2

**Quiz:** asks for the additional demonstrative forms; key C, `yê/ya/yên`.

**Source support:** Lesson 11 explicitly defines `yê/ya/yên` as demonstrative pronouns that identify a person, thing or animal without indicating proximity or distance. The examples use them with relative-pronoun `ko`. The source also distinguishes them from personal pronouns and possessive-pronoun constructions.

**Finding:** The previous rationale retained the technical label but did not restate the distinctive semantic feature. Adding that feature makes the explanation useful without renaming the source category.

**Suggested wording for qualified editor review:**

> `Yê/ya/yên` di vê dersê de pronavên îşarkî yên qerse ne: kes, tişt an heywan nîşan didin bêyî ku nêzîkî an dûrbûna wan diyar bikin. Ew ji pronavên kesîn ên wek `min/te/me` cuda ne û di nimûneyên dersê de bi pronavê girêkî `ko` re tên bikaranîn.

**Disposition:** Explanatory refinement only. Key C unchanged; the source label “qerse” is retained.

## E3 — Lesson 10, Question 2

**Quiz:** asks for the feminine object-pronoun form of `ew`; key C, `wê`.

**Source support:** The Lesson 9/10 paradigm lists `wê` as the feminine form in the pronoun table. Lesson 10's transitive-past example `Wê ew dît` explicitly identifies `wê` as the inflected agent and `ew` as the direct object. The lesson explains that pronoun form and clause role must be distinguished.

**Finding:** The answer remains source-supported. The current phrase “forma mê ya `ew`” is understandable but less precise than explicitly locating `wê` in the paradigm row. The rationale should state both the paradigm form and the clause role in the example, so the learner does not mistake the inflected agent for the direct object.

**Suggested wording for qualified editor review:**

> Di tabloya §86 de, di rêza formên pronavê bireser de, `wê` forma mê ya pronavê `ew` e. Lê di hevoka rabirdûya gerguhêz de, wek `Wê ew dît`, `wê` kirarê tewandî ye û `ew` bireser e. Ji ber vê yekê forma pronavê û erkê wê di hevokê de divê ji hev cuda bên girtin.

**Disposition:** Clarifying refinement only. Key C unchanged. This does not independently certify the quiz stem as optimally worded.

## Scope and limits

- E1–E3 are source-supported editorial refinements, not approved learner-facing replacements.
- The remaining 42 rationale rows were not re-adjudicated in this focused pass; their previous targeted checks remain the evidence base.
- Existing holds remain unchanged: L1 Q4 orthography (`kîtê/kitê`), L12 Q1 definition scope, and L12 Q3 exact compound morphology.
- No lesson, quiz, answer-key, runtime, parser, manifest, database, Botkeep, Telegram or deployment file was changed.
- No tests/CI or live runtime checks were run.
- `main` remains read-only. The archive branch is not an independent ZIP/offsite backup; none is claimed.

# Course 2 Lesson 12 — distractor and answer-rationale quality audit

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** audit and recommendations only; no question, option, answer, or rationale was edited.

## Scope and protected baselines

Reviewed the five questions and their options in `course_data/latin_course_2_reviewed_draft_2026-11-10.md` (blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`) against the reviewed answer key `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md` (blob SHA `879e1525e720bdc25b8f6e896de3e388801238d0`), the Lesson 12 source-grounded reviews, and the previous five-question alignment audit (blob SHA `464b2c284dbff250f979aa03a091d10eaf49350d`).

This pass evaluates distractor plausibility, category boundaries, linguistic clarity, and explanation quality. It does not establish that every distractor is psychometrically validated; no learner-response data exists in this review.

## Question-by-question review

### Q1 — What does an adjective do? Key B

- A: `Têkiliya navdêrê bi lêkerê re diyar dike` — clearly outside the lesson's basic adjective function. It is a plausible grammatical-sounding distractor, but it may be too obviously unrelated for learners who have learned the definition.
- C: `Kes û hejmarê lêkerê li gorî kiryarê diguherîne` — describes verb agreement/inflection rather than adjective function. It is a valid category contrast, although its formulation is comparatively technical.
- B remains the intended answer. The stem tests the introductory definition, not the full distribution of adjectives. Because source §§124–127 also allow predicative and substantivized descriptive adjectives, retain the already-recorded recommendation to qualify the lesson definition rather than changing this key.
- Quality: acceptable basic item; distractors are distinct but A and C are not equally demanding.

### Q2 — `mezin` in `hespê mezin`. Key C

- A `jmarnav` and B `pronav` are meaningful competing word-class labels. Both are incorrect here because `mezin` describes the expressed noun `hesp`.
- C `rengdêra wesfîn` is the intended subclass. The example and answer are directly aligned.
- Quality: strongest of the five items. The distractors test whether the learner can distinguish adjective, numeral, and pronoun categories rather than merely recognize a definition.
- Editorial note: preserve the exact course terminology and capitalization style consistently across all three options; no content correction is required.

### Q3 — `sê` in `sê mal`. Key A

- A `rengdêra jmarîn` is conceptually correct under the course's taxonomy because `sê` modifies the expressed noun `mal`.
- B `rengdêra wesfîn` is a meaningful same-level category distractor: it tests whether the learner distinguishes quantity from descriptive property.
- C `daçek` is a different word class and is comparatively easy to reject.
- Quality: sound concept contrast, but difficulty is uneven because C is less plausible than B.
- Open morphology issue: the option's `rengdêra jmarîn` remains unresolved against the heading `rengdêrên jmarîn` and prose `rengdêrê jmarîn`. Do not normalize it automatically; obtain a Kurmanji editor's judgment in this exact syntactic context.

### Q4 — Numeral classification in the adopted framework. Key B

- A `di bin pronav de` and C `di bin lêker de` are not parallel or well-formed alternatives to B `wek beşeke serbixwe`. The phrase “under a pronoun/under a verb” makes the distractors structurally and conceptually weak: grammatical classes are not ordinarily presented as being “under” those parts of speech in this context.
- The scope marker `Li gorî vê rêbazê` is important and should remain; it frames the answer as the course's adopted analysis rather than a universal classification.
- Quality: weakest distractor design among the five. The keyed answer remains B, but A and C should be replaced only in a future explicitly approved editorial patch by parallel, linguistically coherent alternatives that represent genuine competing analyses (for example, a clearly stated adjective-subclass analysis versus an independent class), after editor review. Do not invent a replacement wording now or alter the current protected quiz.

### Q5 — Use of `nîv` in the numeral section. Key C

- A `rengdêra wesfîn` and B `pronavê kesîn` are recognizable competing categories, but neither is a particularly close alternative for a learner who has just studied the numeral subsection.
- C `nimûneyeke jmarnav` is supported by the lesson's explicit numeral discussion and source §§146–148.
- Quality: correct and clear, but the distractors are relatively easy. A future revision could use more closely related numeral subtypes/forms only if the stem and source evidence are adjusted together; no new option is proposed in this audit.

## Answer-key rationale quality

All five current rationales repeat the same generic sentence: `Li gorî pirs û vebijarkên testa Ders 12, ev vebijarka rast e.` This merely asserts correctness and does not teach the learner why the answer is correct.

Recommended one-sentence rationales for a future approved key revision:

| Item | Key | Proposed explanatory rationale |
|---|---|---|
| Q1 | B | Di vê pênaseya destpêkî de, rengdêr taybetmendî an taybetiya navdêrê rave dike. |
| Q2 | C | `mezin` taybetmendiya navê `hesp` rave dike; ji ber vê yekê rengdêra wesfîn e. |
| Q3 | A | `sê` hejmarê navê `mal` diyar dike û bi navdêrekî eşkere re tê. |
| Q4 | B | Li gorî tesnîfa ku ev kurs pejirandiye, jmarnav wek beşeke rêzimanî ya serbixwe tê pêşkêşkirin. |
| Q5 | C | `nîv` di beşa jmarnavan de wek nimûneyeke jmarnavê hatiye nîşandan. |

These are draft explanations, not approved text. Q1's rationale deliberately says “introductory definition”; it must not imply that adjectives only ever modify nouns. Q4 preserves the course-framework qualification. Q3's rationale explains the concept without settling the unresolved inflectional form of the option label.

## Overall disposition

- Existing key sequence remains **B / C / A / B / C**.
- No key-letter contradiction was found.
- Q2 has the strongest category-level distractors.
- Q4 has the weakest distractors because A and C are not parallel grammatical alternatives.
- Q1, Q3 and Q5 are usable at introductory level, but distractor difficulty is uneven.
- The generic rationales should be replaced with item-specific explanations only after approval.
- Q3's Kurdish morphology remains open and must not be silently normalized.

## Preservation and action boundary

No lesson, exercise, question, option, answer key, source-aligned file, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was modified. No tests/CI or live runtime checks were performed. All work remains on `archive/preservation-audit-2026-11-10`; `main` remains read-only. GitHub archive history is the persisted record, not a separately verified ZIP/off-site backup.

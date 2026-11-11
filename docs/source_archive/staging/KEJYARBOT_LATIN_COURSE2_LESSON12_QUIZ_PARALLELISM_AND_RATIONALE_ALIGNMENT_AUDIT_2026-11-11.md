# Course 2 Lesson 12 — quiz parallelism and rationale alignment audit

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** read-only review; proposals only, no quiz/key text changed.

## Baselines

- Lesson draft: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, blob SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`, blob SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.
- Terminology register: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_MASTER_TERMINOLOGY_REGISTER_2026-11-11.md`, blob SHA `fafe843358ab011745722b9a3daec390ed26e833`.

## 1. Option-shape audit

### Q1 — definition of adjective

The three options are not grammatically parallel:
- A is a finite clause: `Têkiliya ... diyar dike`.
- B is a noun phrase/fragment: `taybetmendî an taybetiya ... rave dike` (predicate phrase with an omitted subject).
- C is a finite clause: `Kes û hejmarê ... diguherîne`.

The key B is also the only option beginning lowercase. This may visually cue the answer. Future revision should choose one consistent frame: e.g. all options as finite clauses with an explicit shared subject, or all as parallel predicate fragments. Preserve B's conceptual meaning, while remembering that it is the introductory/basic definition, not the exhaustive distribution of adjectives.

**Terminology flag:** Q1 C contains `kiryarê`; the controlled terminology register currently records `kirar` for “Subject/agent role”. The spelling difference `kiryar/kirar` is an unresolved cross-document inconsistency, not proof that either form is wrong. Confirm intended lexeme and inflection against the course glossary/source before editing. Do not substitute `kirde` by guess.

### Q2 — class of `mezin`

All options are category labels: `jmarnav`, `pronav`, `rengdêra wesfîn`. This is the most parallel option set. The example `hespê mezin` clearly supports the descriptive-adjective key C. No structural change is needed.

### Q3 — class of `sê` in `sê mal`

A and B are adjective-subclass labels; C is a different part-of-speech label. This is acceptable category-level contrast, although C is easier to reject. The only unresolved issue remains the morphology of `rengdêra jmarîn`; no automatic normalization.

### Q4 — course classification of `jmarnav`

A and C are surface-syntactically parallel (`di bin X de`), but neither is a semantically plausible classification of `jmarnav` in this question. B (`wek beşeke serbixwe`) states a different answer shape and the intended classification. The earlier note that A and C were “not parallel” has been corrected: the A/C pair is parallel in surface syntax; the full A/B/C set is not semantically or syntactically homogeneous.

Future options should all express competing classification claims in the same form. Preserve `Li gorî vê rêbazê` in the stem, because the answer is specific to the course's adopted framework.

### Q5 — function/class of `nîv)

A and B name grammatical categories; C says `nimûneyeke jmarnav` (“an example of a numeral”). C is understandable and supported by the lesson, but the answer types are not strictly parallel. A future revision could make all options category labels or all short descriptions. No current key issue is identified.

## 2. Rationale-to-key alignment

The answer key currently repeats `Li gorî pirs û vebijarkên testa Ders 12, ev vebijarka rast e.` for every item. These statements do not explain the relevant distinction. The following draft rationales align with the actual key and examples, but require Kurmanji copy-edit before approval:

| Q | Key | Draft rationale | What it explains |
|---|---|---|---|
| 1 | B | `Di vê pênaseya bingehîn de, rengdêr taybetmendî an taybetiya navdêrê rave dike.` | Basic adjective function; not an exhaustive claim about predicative/substantivized use. |
| 2 | C | `Peyva “mezin” taybetmendiya navê “hesp” rave dike; ji ber vê yekê rengdêra wesfîn e.` | The adjective's role in the exact noun phrase. |
| 3 | A | `Peyva “sê” hejmarê navê “mal” diyar dike; ji ber vê yekê di vê hevokê de rengdêra jmarîn e.` | Numeral modifies an expressed noun. |
| 4 | B | `Li gorî tesnîfa vê kursê, jmarnav wek beşeke rêzimanî ya serbixwe tê pêşkêşkirin.` | The course's explicit adopted taxonomy; avoids universalizing it. |
| 5 | C | `Di beşa jmarnavan de, “nîv” wek nimûneyeke jmarnav hatiye pêşkêşkirin.` | The lesson's explicit treatment of `nîv`. |

Q3 rationale explains the grammatical concept without settling the unresolved option-label inflection. Q1 rationale says “basic definition” to avoid contradicting the source-supported predicative/substantivized uses. Q4 explicitly scopes the claim to the course framework.

## 3. Consolidated priorities

1. Resolve `kiryar/kirar` against the controlled glossary and source; do not guess a replacement.
2. Standardize Q1 option shape and capitalization.
3. Redesign Q4 with three same-form, meaningful classification alternatives.
4. Optionally normalize Q5 answer type for parallelism.
5. Obtain Kurmanji editor ruling for Q3's `rengdêra jmarîn`.
6. Replace generic key rationales with item-specific explanations after editorial approval.
7. After any approved change, recheck all five key letters and answer texts against the lesson.

## 4. Current disposition and protection

The answer-key sequence remains **B / C / A / B / C**. No key mismatch was found. No edits are applied or authorized by this audit. All proposed rationales are drafts requiring language review.

No lesson, exercise, question, option, key, source-aligned file, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was modified. No tests/CI or live runtime checks were performed. `main` remains read-only. GitHub archive history is not a separate ZIP/off-site backup.

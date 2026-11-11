# Course 2 Lesson 12 — source-grounded adjective, pronoun, and numeral distinction

**Date:** 2026-11-11  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Status:** source-page evidence reconciliation and editorial recommendation; no lesson, quiz, or answer-key edits authorized or applied.

## 1. Source evidence reviewed

Primary source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002.

The following previously completed page-image/source reviews were retrieved and compared:
- `KEJYARBOT_LATIN_COURSE2_LESSON12_PAGE_IMAGE_REVIEW_2026-11-10.md`, blob SHA `c712dd136e36154e5314efc65e9f7eef8c9cf4ab`, reports direct inspection of printed pp.89–100, §§119–152.
- `KEJYARBOT_LATIN_COURSE2_PRONOUNS_PAGE_IMAGE_REVIEW_2026-11-10.md`, blob SHA `db629ed41eeb8783a09b662c75b838a90cd43ca6`, reports direct inspection of printed pp.71–88, §§72–118.
- `KEJYARBOT_LATIN_COURSE2_LESSON12_SOURCE_COMPARISON_2026-11-10.md`, blob SHA `94a413f3c902e8075cede1a0eb7489eab979183c`, records the source/course terminology crosswalk and scope limits.

This pass reconciles those page-image findings with the current source-aligned Lesson 12 text; it does not claim that the original book images were newly re-scanned during this pass.

## 2. Adjective vs pronoun: function in context, not surface form

The source's pronoun section (§72) defines pronouns as words that replace nouns and may take over noun functions. Its demonstrative sections (§§94–96) distinguish demonstratives used with a noun from forms that stand in place of a noun. The adjective section (§§131–133) describes demonstrative adjectives placed before nouns and inflected for gender, number, and oblique case.

Therefore, retain this functional diagnostic:
- `ev keçik`: `ev` modifies an expressed noun; classify it as a demonstrative adjective/modifier in the course's Lesson 12 framework (`rengdêrên îşarkî`).
- `Ev hat.`: `Ev` stands independently in place of a noun; classify it as a demonstrative pronoun (`pronavê îşarkî`).
- Do not classify `ev/ew` by spelling alone; the syntactic relation determines the use.

The same diagnostic applies to possessive forms:
- `hespê min`: the possessive element accompanies an expressed noun; this is possessive-adjective use in the course framework.
- `yê min` (as in the source-review examples `destmalên min — yên min`, `gopalê min — yê min)): the form replaces an understood noun/group; this is possessive-pronoun use.
The course already explains this contrast; preserve it and avoid describing both constructions simply as “possessive pronouns/adjectives” without the expressed-noun test.

Interrogative and indefinite forms can likewise have adjective or pronoun use depending on whether they accompany a stated noun or function independently. The source review records this for forms such as `çend`; the lesson should teach the syntactic test rather than imply that a surface form has one permanent category in every sentence.

## 3. Numeral adjective vs `jmarnav`

The source treats adjective numerals within its adjective discussion (§§134–140) and separately treats numerals and their forms/inflection in §§141–152. The course's adopted teaching distinction is function-based:
- numeral adjective: modifies a stated noun, e.g. `sê mal`, `çar xanî`, `deh bizin), or an ordinal phrase such as `stûna çaran`;
- `jmarnav`: numeral used independently/substantively, with its own syntactic role and the source's numeral inflection patterns.

Do not claim that numeral adjective and numeral pronoun are distinguished merely because the book discusses them in separate sections. The learner-facing test must be whether the numeral modifies an expressed noun or is used independently in the clause. Some forms overlap; form alone is not sufficient.

## 4. Source labels vs course teaching labels

The direct page-image review reports these source/course differences:
| Course 2 label | Source wording recorded in the page-image/source comparison | Editorial treatment |
|---|---|---|
| `rengdêrên wesfîn` | `rengdêrên çilobûn û çawabûnê` | At first mention, give the source label and map `wesfîn` as the course's explanatory equivalent |
| `rengdêrên xwemalîn` | `rengdêrên destdaniyê`; also `rengdêrên xwedîtiyê` | Present `xwemalîn` as the course label, not a verbatim quotation from the source |
| `rengdêrên rêzîn` | `rengdêrên rêzda` | Explicitly map the course label to the source wording |
| `rengdêrên jmarîn` | source adjective-numeral class is recorded in the source comparison as `rengdêrên jmarda`; page-image review records the two types as `jmarîn` and `rêzîn` | Keep the course headword stable, but disclose the source label at first mention and do not silently present the course form as a verbatim source label |

The source page-image review confirms six adjective classes: descriptive, demonstrative, numeral, interrogative, indefinite, and possessive. It also notes that descriptive adjectives can be predicative or used without an expressed noun (§§124–127). Thus, the simplest learner definition (“a word that describes a noun”) is useful but incomplete if read as an absolute rule: adjectives may also be predicative or substantivized. The course should preserve the six-class framework while adding a short qualification.

## 5. Editorial decisions and open items

1. Keep the six adjective classes in the course's adopted framework; at first introduction map course labels to the exact source labels above.
2. Clarify that adjectives typically modify nouns but can also occur predicatively or substantively, as the source §§124–127 indicates.
3. Keep the expressed-noun vs noun-substitution diagnostic for demonstrative and possessive adjective/pronoun pairs.
4. Keep the functional distinction between numeral adjective and `jmarnav`; do not define it by section placement or surface form alone.
5. Retain the existing Lesson 12 numeral-adjective Q3 discrepancy (`rengdêrê jmarîn` in prose vs `rengdêra jmarîn` in the quiz) as unresolved. The source-page review does not settle the exact morphology of that isolated quiz option; obtain a Kurmanji editor's ruling before any normalization.
6. Do not apply any of these recommendations to lesson/quiz/key text without explicit approval.

## 6. Limits and preservation

This reconciliation relies on the recorded direct page-image reviews for printed pp.71–88 and pp.89–100 and the source-comparison note. It is not a fresh independent transcription of every printed line. The exact Q3 morphology remains unresolved. No lesson, exercise, quiz, answer key, source-aligned file, runtime, parser, test, manifest, database, Botkeep, Telegram, or deployment file was changed. No tests/CI or live runtime checks were performed. Work remains on `archive/preservation-audit-2026-11-10`; `main` remains read-only.

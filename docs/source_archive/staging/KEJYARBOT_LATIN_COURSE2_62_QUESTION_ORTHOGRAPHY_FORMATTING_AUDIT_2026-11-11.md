# Course 2 — 62-Question Orthography, Punctuation, and Formatting Audit

Date: 2026-11-11  
Branch: `archive/preservation-audit-2026-11-10`  
Scope: 62 quiz stems/options and their 62 reviewed answer-key rows  
Status: editorial audit only; no source or key edits

## 1. Sources and method

- Quiz source: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`, SHA `abc88219e2a0e249883e8d62c5117a9b3aaa3108`.
- Reviewed answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`, SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.
- Confirmed 62 quiz questions and 62 answer-key rows: L1–L7 have five each, L8 has seven, L9–L12 have five each.
- Checked spelling consistency, Kurdish diacritics, capitalization, punctuation, use of code formatting for forms/suffixes, option layout, and visible correspondence between the key and the quiz text.
- This is not a full proofread of every lesson paragraph or source grammar. It is restricted to quiz items and key entries.

## 2. Overall result

The quiz and key are structurally aligned at 62 items. The main editorial issue is not a large number of obvious misspellings; it is inconsistent presentation and editorial normalization:

1. Lesson 12 uses a different quiz heading and vertical option layout from Lessons 1–11.
2. Capitalization at the start of stems and options is inconsistent, especially in Lesson 12.
3. Inline code formatting for linguistic forms is inconsistent: some lexical forms and suffixes are marked with backticks while comparable forms are not.
4. The answer key's Lesson 1 Q4 rationale writes `kîtê/kitê`, presenting two spellings without explaining whether they are variants or a typo.
5. Several previously identified terminology/orthography questions remain open and must not be silently normalized: Lesson 12 `kiryar/kirar`; `rengdêra/rengdêrê jmarîn`; and Lesson 10 Q2 `forma bireserî`.

No item wording, option, key letter, or answer text has been changed.

## 3. Global formatting rules recommended for a future approved edit

These are proposed house-style rules, not changes already applied:

- Use one heading convention across all lessons: `### Kuis — N pirs`. If the legacy title `10. Testa Kejyar` must be retained for source fidelity, document it as an intentional exception and do not let it silently coexist with two competing quiz formats.
- Use one option layout throughout: either one option per line for every item or a consistent inline format. Recommended for readability and parser safety: one option per line, labels exactly `A)`, `B)`, `C)`, and `D)` only where an item truly has four options. Do not change the current three-option count without authorization.
- Capitalize the first word of every stem and every full-sentence option consistently. For fragments and bare forms, choose one rule and apply it uniformly; do not capitalize some forms merely because they happen to begin an option.
- Use terminal punctuation consistently: complete interrogative stems end with `?`; full-sentence answer options end with a period only if the house style requires it; bare words, suffixes, and noun phrases do not receive arbitrary periods.
- Use backticks consistently for metalinguistic forms, example words under analysis, pronoun forms, and suffixes. Do not use backticks for ordinary prose. Keep slash-separated allomorphs within one code span, e.g. `-î/-e/-en`.
- Preserve Kurdish characters exactly, especially `ê, î, û, ş, ç`; do not transliterate them to plain Latin letters during normalization.
- Keep the key's answer text identical to the corresponding quiz option after any future authorized copy edit. Keep the answer letter and answer text together; do not infer the key from option order alone.
- Keep grammatical distinctions intact while standardizing typography. In particular, do not merge lexical form, grammatical function, case, gender, number, or word-class labels.

## 4. Findings by lesson

### Lessons 1–5

- **L1:** Stems and options are inline; option initial capitalization alternates (e.g. `Tenê` vs `tevahiya`). Q4's answer-key rationale contains `kîtê/kitê` without defining the spelling relationship. The quiz option `kît` and the rationale's two forms should be checked against the course's chosen Kurdish orthographic convention before normalization.
- **L2:** Proper names and lexical examples use backticks in some stems, but the policy is not explicit. The option strings are otherwise compact. No clear diacritic corruption identified in the five questions.
- **L3:** Option capitalization is mixed; the forms `derî`, `çem`, and `dar` retain their Kurdish diacritics. No content-level spelling correction is justified from the quiz text alone.
- **L4:** Option capitalization is mixed. The contrast between `hespek`, `hespê`, `hespa`, and `hespin` is morphological and must not be “corrected” as spelling variants.
- **L5:** The stems use longer contextual wording and include forms such as `hespî`, `mehînê`, and `hespan`. Preserve the stated tense and object context; differences among these forms are grammatical, not typographic.

### Lessons 6–8

- **L6:** Q3 writes the technical label as bare `bireser`, while the lesson's defined term is `bireserê navdêrê`. This is already recorded as a terminology risk, not a simple spelling error. Q5 asks about the full phrase `xencera min`; preserve the distinction between the whole phrase and its pronoun component.
- **L7:** The suffixes `-ê`, `-a`, and `-ên` are presented without a consistent visual convention for metalinguistic suffixes. Future formatting should mark all suffixes consistently while preserving their exact forms.
- **L8:** Seven questions are correctly represented in the source and key. The suffix sets `-î/-e/-en`, `-ek/-ek/-in`, `-ekî/-ekê/-ina`, and `-ên/-a/-ê` should remain in code formatting as whole sets. Do not conflate these sets; their differences are grammatical and environment-conditioned.

### Lessons 9–11

- **L9:** The personal-pronoun forms `min/te/wî/wê/me/we/wan` retain their diacritics. The stem and answer options use a mixture of bare forms and prose; a consistent code-formatting policy would improve scanability.
- **L10:** Q2's phrase `forma bireserî` is not merely a typography issue: it is the unresolved terminology conflict already recorded in the distractor audit. Do not edit its spelling or key until the technical label is resolved. The forms `wî/ew/wê` must remain distinct.
- **L11:** Q3 says `forma girêkî`, whereas the lesson's established full term is `pronavê girêkî`. This is a shortened label/terminology consistency issue. Q3's `ko/ku/kî` contrast is orthographic and grammatical; retain the course's source-specific register note and do not imply universal invalidity of `ku`.

### Lesson 12

- The heading is `### 10. Testa Kejyar`, unlike `### Kuis — 5 pirs` in Lessons 1–11. This is a visible format inconsistency and should be resolved as a house-style decision.
- All five stems/options are vertically arranged, while Lessons 1–11 mostly put A/B/C on the same line as the stem. This is readable but inconsistent. Do not reflow without checking the runtime parser's accepted format.
- Stem capitalization varies: `Rengdêr` starts with uppercase in Q1, while `mezin`, `sê`, and `nîv` start lowercase in Q2/Q3/Q5. Option capitalization also varies within Q1 (`Têkiliya`, `taybetmendî`, `Kes`).
- Q2/Q3/Q5 use unquoted, unformatted example forms. A future style pass should mark the target word consistently, e.g. code-format `mezin`, `sê`, `nîv`, but only after parser compatibility is checked.
- Preserve `rengdêra jmarîn` exactly as currently keyed pending the open morphological/editorial question; do not switch it to `rengdêrê jmarîn` by typographic normalization.

## 5. Answer-key alignment and open spelling decisions

- All 62 key rows are present and align structurally with the question counts. The key stores both answer letter and answer text, which is a good safeguard against option-order drift.
- Lesson 5 Q3's reviewed key correctly uses `mehînê`; the older form `mehinê` is recorded as corrected in the key's own history. Preserve `î`.
- Lesson 1 Q4's `kîtê/kitê` in the rationale needs an explicit orthographic ruling. Do not select one spelling by guess.
- Lesson 12 Q1 `kiryar/kirar`, Lesson 12 Q3 `rengdêra/rengdêrê jmarîn`, and Lesson 10 Q2 `forma bireserî` remain editorial/terminological issues, not safe automatic spell-check substitutions.
- The key's repeated generic rationales are stylistically repetitive but not an orthographic mismatch. This audit does not rewrite rationales.

## 6. Recommended order of work

1. Obtain an explicit editorial ruling on the `kîtê/kitê` variant and the course's chosen spelling.
2. Resolve the technical terms already flagged in L10 Q2 and L12 Q1/Q3 before doing a final proofread.
3. Approve one quiz layout and capitalization/punctuation/code-formatting house style.
4. Apply the approved style to a copy of the staging draft, preserving the original and checking parser compatibility before any runtime proposal.
5. Re-compare every answer-key answer string against its final quiz option; retain all 62 rows and verify the key count.

## 7. Preservation and limitations

This artifact is append-only. No lesson, quiz, option, answer-key row, answer letter, runtime, parser, test, manifest, database, Botkeep bot, Telegram bot, or deployment file was changed. No tests/CI or parser compatibility checks were run. `main` remains read-only. The archive branch is not an independent ZIP/off-site backup; no such backup is claimed.

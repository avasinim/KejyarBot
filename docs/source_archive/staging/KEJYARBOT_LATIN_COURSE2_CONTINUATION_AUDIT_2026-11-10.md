# Latin Course 2 — continuation audit (quiz alignment and Lesson 5 source correction)

Date: 2026-11-10
Branch: archive/preservation-audit-2026-11-10
Source files on main were read-only.

## 1. Full quiz-to-key comparison
Parsed the 12 embedded Course 2 lesson quizzes and the master answer key from main:
- 12 lesson blocks found.
- 60 quiz questions found (5 per lesson).
- 60 answer-key rows found.
- Each question has exactly A, B, C.
- All 60 selected answer texts match the corresponding option text exactly.
- No missing key row, missing question, or answer-text mismatch found.

This is a structural integrity check only. It does not prove that every distractor is pedagogically strong or that every question is scientifically unambiguous. The repository's Python regression test was inspected but not executed in a local project environment.

## 2. Confirmed source correction in Course 2 Lesson 5
A source-audit record in `course_data/LATIN_COURSES_SOURCE_AUDIT_2026-11-01.md` records Celadet Part II §57, printed pp. 57–60, with the exact three regional variants:
- `Soro kevirî tavêje.`
- `Soro kê vir tavêje.`
- `Soro kevir tavêje.`

The current main lesson and the first reviewed draft had the second form as `Soro kê vir tavêje`, omitting the source's word break `ta vêje`. Corrected the reviewed Course 2 draft to the source form. Main remains untouched.

## 3. Additional confirmed editorial correction
- Lesson 1's definition of `tîp` was revised to state that it is a written sign representing a sound, not the sound itself. The earlier phrase implying that the sound is literally fixed/arrested on paper was imprecise.

## 4. Remaining pedagogical review queue
- Recheck each question's *conceptual validity*, not just answer-key matching; prioritize Lessons 4–5, 7–8, 9–11.
- Lesson 4: retain the explicit note that `Mîr` at sentence start is the common noun/title `mîr`, not necessarily a personal proper name. The capital letter is sentence-initial capitalization.
- Lesson 7: ensure suffix labels `-ê/-a/-ên` are consistently called definite determiners/suffixes and distinguished from oblique marking; the current lesson already warns against conflation.
- Lesson 8: preserve the two source patterns `-ek/-ek/-in` and `-ekî/-eke/-ine`; do not normalize the source's feminine examples to an unrelated form.
- Lesson 9: `hon` is source-specific and should remain as Celadet's form; do not silently change it to a modern spelling variant.
- Lesson 10: preserve Celadet's regional note for `êk` and do not substitute forms from another grammar.
- Lesson 11: retain the distinction between demonstrative pronouns `ev/ew`, the `yê/ya/yên` set, relative pronoun `ko`, and conjunction `ko`.
- Lesson 12: keep adjective classes and the independent numeral category separate, and retain the source's qualified classification.

## Preservation
- Updated only `course_data/latin_course_2_reviewed_draft_2026-11-10.md` on the archive branch.
- No main file, runtime, manifest, Botkeep deployment, database, or live bot was changed.


## 5. Further issue identified for source-level adjudication
- **Lesson 10 — source-verified clarification:** The heading `Pronavên bireser` and the list `min/te/wî/wê/me/we/wan` are exactly Celadet's own terminology and forms (§§77–78, 86, pp. 73–76). They should not be renamed. The actual gap in the lesson was that it did not sufficiently explain Celadet's explicit rule: in transitive past clauses, object-pronoun forms become the agent/subject and the corresponding subject forms become the direct object (e.g. `Wê ew dît`). The reviewed draft now includes this rule, contrasts `Ez te dibînim` with `Te ez dîtim`, and notes the different behavior of indirect objects (`min ji wan re got`). Source: printed pp. 72–76.


## 6. Source collation: Lesson 10 and Lesson 11 (2002 edition)
Primary source PDF checked against printed pages 72–84:
- **Lesson 10 — personal pronouns:** §§77–78 (pp. 72–73) explicitly name the two groups `Pronavên kirar` and `Pronavên bireser`, and list the subject/object paradigms. §78 explains that in past-tense transitive clauses the subject pronoun changes to the object form and the object pronoun changes to the subject form; examples include `min got`, `te xwar`, `wî xist`, `wê xwar`, and `Wê ew dît`. §86 (p. 76) restates the underlying object forms and explains their change in transitive past clauses; it also distinguishes indirect objects, e.g. `min ji wan re got`.
- The reviewed Lesson 10 now explicitly contrasts `Ez te dibînim` with `Te ez dîtim`, explains the agent/object role reversal in transitive past clauses, and preserves indirect-object examples. This resolves a pedagogical omission without changing Celadet's terminology.
- **Lesson 11 — demonstratives:** §§94–98 (pp. 81–82) divide demonstrative pronouns into near forms `ev/ew` and distant forms `yê/ya/yên`. §§97 states that `yê/ya/yên` are always subjects and never direct objects, and that the relative pronoun `ko` follows them. The lesson's distinction is source-aligned.
- **Lesson 11 — relative pronoun/conjunction:** §§99–100 (pp. 83–84) distinguish relative `ko` from conjunction `ko`; the current lesson quiz preserves that distinction.

Source PDF used for collation: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002, https://www.kurdishlo.org/pdf/learning/reziman.pdf (Part II, printed pages 72–84). The PDF is the 2002 digital edition; its printed page labels are retained in this note.

## 7. Source collation: Lessons 1–3 and 6 (2002 edition)
Primary source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002; Part II, printed pp. 37–53 and 61.

- **Lesson 1 — §§1–4, pp. 37–44:** The grammar definition matches §1. §3 explains the oral/written relation, the sequence tîp → kît → bêje → komek, gives the same sample sets, and explicitly says a qiset results from the sequence of komeks; the four listed language elements remain the four in the lesson. §4's original definition of tîp has been editorially clarified in the reviewed draft so the written sign is not confused with the sound it represents. The lesson's quiz answers align with the source.
- **Lesson 2 — §§34–37, pp. 51–52:** The noun definition and the hevenav/serenav distinction align with the source. The source defines a hevenav as a name for one or more members of a class and a serenav as the name of a particular person, animal, or thing. The source examples include `Sado`, `Bêlan`, `Herekol`, `Hevind`, `Sîpan`, `Xabûr`, `Hindistan`, `Hezro`, `Kerevan`, `Zîn`, `Dêrgul`, `Kurdistan`, `Agirî`, `Cemîd`, and `Ferezende`. Modernized spellings in the lesson (e.g. `Cemşîd`, `Ferazende`) are retained as editorial spelling choices, not claimed as exact source transcription; they should be checked against the course's orthographic policy before any source-quotation label is applied.
- **Lesson 3 — §§38–45, pp. 51–53:** The source states two grammatical genders and explicitly lists `Herekol` among feminine nouns. It also gives `dar` as feminine with the meaning of a living tree/plant and masculine with the meaning of dry wood. Both points are preserved in the lesson, including the clarification that grammatical gender is not biological sex. The masculine/feminine inventories substantially follow §§40–41; source OCR may omit diacritics/letters in a few proper names, so those names are not silently re-normalized on this pass.
- **Lesson 6 — §§59–60, pp. 61–62:** The source defines `bireser` as an accompanying word that modifies/restricts the noun's meaning, and gives both pre-noun examples (`ev keçik`, `kîjan mirov`, `çar xanî`, `hin çiya`, `çend kitêb`, `deh bizin`, `van zarokan`) and post-noun examples (`hespê beza`, `mehîna spehî`, `xencera min`). The reviewed draft had `mehinên spehî`, which did not reproduce the source's singular example; this has now been corrected to `mehîna spehî`. The note that a word such as `ev` functions as a modifier before a noun but as a demonstrative pronoun when standing alone is a pedagogical clarification, not a quotation from this paragraph.

### Quiz semantics — Lessons 1–3 and 6
- The five questions in each of these lessons have one clearly intended answer under the lesson's definitions and examples.
- Lesson 3, Q5 is appropriately framed as grammatical gender rather than biological sex.
- Lesson 6, Q2–Q5 correctly test noun head, modifier, position, and the compound modifier example. The source example `mehîna spehî` has been restored in the lesson body; no quiz option or answer-key row needed changing.
- This pass checks the validity of the intended answer and obvious ambiguity. It does not certify every distractor as optimally diagnostic or validate all spelling variants against manuscript-level originals.

Source lines used for this collation: §§1–4 (printed pp. 37–44), §§34–45 (printed pp. 51–53), §§59–60 (printed pp. 61–62), in the 2002 digital edition.
## 8. Lesson 12 — source and quiz review
Cross-check against Celadet's sections 119–123, 134–137, and 141–147 (Part II; printed pagination in the 2002 Nefel edition is to be retained when checked against that edition; the searchable Hawar compilation reproduces the original section numbering).

- **Six adjective classes:** the lesson's six groups (wesfîn, îşarkî, jmarîn, pirsiyarkî, nebinavkirî, xwemalîn) match the sixfold classification in §122. §123 also supports the broad position patterns: possessive adjectives follow the noun with a veqetandek, while demonstrative, interrogative and indefinite adjectives precede it; numeral adjectives have more than one position pattern.
- **Cardinal and ordinal numeral adjectives:** §§134–136 distinguish cardinal numerals, which indicate number/quantity, from ordinal forms, which indicate order. The lesson's separation of cardinal examples (`sê mal`, `deh mirov`) from ordinal examples (`stûna çaran`, `a pêncan`, `ê heftan`) is source-aligned. The source also explicitly shows that the noun following a cardinal numeral changes form according to its syntactic role.
- **Numeral pronouns:** §§141–147 treat `jmarnav` as a separate category, define it as expressing number/quantity and either accompanying a noun or replacing it, distinguish definite and indefinite numeral pronouns, and subdivide definite numeral pronouns into four groups. The lesson correctly keeps numeral adjectives separate from numeral pronouns and preserves the four-way subdivision.
- **Lesson 12 quiz:** Q1–Q5 each have one clearly intended answer under the lesson's definitions. Q3 tests a numeral adjective (`sê` modifying `mal`); Q4 tests the independent grammatical category `jmarnav`; Q5 treats `nîv` as a numeral-pronoun example. No answer-key change is required on this pass.

### Terminology and source-form items to verify before certification
- The lesson uses `rêzîn` for ordinal numeral adjectives and also uses `rêzîn` in the four-way subdivision of definite numeral pronouns. The searchable Hawar compilation's OCR renders the latter as `razîn` (§143), while it renders the adjective label in §136 as `rezîn`. OCR is not sufficient evidence to normalize the 2002 Nefel text; retain both lesson forms provisionally and inspect the printed 2002 page image before certifying the spelling. Do not merge the two labels without that check.
- The lesson's `xwemalîn` is a normalized form; §122 in the searchable compilation is OCR-rendered as `xwemanî`. This is recorded as an orthographic/source-form check, not yet as a confirmed error.
- The expanded explanations of `nîv`, `yek`, and `hezar` are retained as lesson editorial material. This pass did not fully collate every detailed inflection example for those forms against the printed 2002 page images.

Result: Lesson 12's grammatical architecture and five intended answers are source-consistent. Two source-spelling points (`rêzîn/razîn` and `xwemalîn/xwemanî`) and detailed numeral inflection examples remain open for image-level collation; therefore this is not a final source certification.
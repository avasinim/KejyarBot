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

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
- **Lesson 10 terminology:** The section titled `Pronavên Bireser` lists `min/te/wî/wê/me/we/wan`, which are oblique forms used in agent positions in transitive past clauses (e.g. `Wê ew dît`), while `ew` is the direct object in that example. The section currently risks conflating oblique/agent forms with direct-object pronouns. Do not rename the section until the exact terminology and examples in Celadet §§86–93 are checked; add a source-grounded distinction between syntactic role and morphological case if supported.

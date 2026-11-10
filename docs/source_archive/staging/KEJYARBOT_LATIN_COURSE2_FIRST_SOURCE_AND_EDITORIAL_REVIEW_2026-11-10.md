# KejyarBot — Latin Course 2 first source and editorial review pass

Date: 2026-11-10
Repository: avasinim/KejyarBot
Source branch: main (read-only)
Reviewed output: `course_data/latin_course_2_reviewed_draft_2026-11-10.md`
Primary reference: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002, Part II, printed pp. 37–100.

## Source verification
- The 2002 digital edition confirms Part II begins at printed p. 37 and its contents map the grammar topics through printed p. 100.
- The reviewed sections were checked against the source's relevant sections:
  - Grammar definition and four language elements: §1–4, pp. 37–38.
  - Noun classes and gender: §§34–45, pp. 51–52.
  - Number and declension: §§47–57, pp. 55–59.
  - Definite/indefinite suffixes: §§61–68, pp. 62–67.
  - Pronoun topics: §§76–117, pp. 71–87.
  - Adjectives and numerals: §§134–152, pp. 93–100.

## Confirmed editorial changes in reviewed draft
1. **Lesson 4 — Mîr ambiguity:** The source's examples “Mîr hat / Mîr hatin” use *mîr* as a common noun/title (emir), not a personal proper name. Since the word is capitalized at sentence start, learners could mistake it for a proper noun. Added an explicit note to distinguish the common-noun use from a proper name. Source: §§48–49 and §51, pp. 55–56.
2. **Lesson 12 — spelling:** Corrected `bêhtir` to `bêtir` in the indefinite numeral list, matching the source's `bêtir`. Source: §142, p. 97.
3. **Lesson 3 — source classification note:** Preserved `Herekol` in the feminine-gender list because the source itself places it there (§41, p. 52), and added a note that this is the source's grammatical classification, not a biological or geographical claim.

## Review observations — no silent correction
- Lesson 1 follows the source's four language elements: tîp, kît, bêje, komek; the source treats qiset as an outcome formed by sequences of komek, not a fifth element. (§3, p. 37)
- Lesson 2's hevenav/serenav distinction and examples are aligned with §§34–37, p. 51.
- Lesson 3's two grammatical genders and the special semantic behavior of `dar` are directly supported by §§39–45, pp. 52–53.
- Lessons 4–5 distinguish number from declension and preserve the source's three accepted variants for `Soro kevirî tavêje / Soro kê vir tavêje / Soro kevir tavêje`. (§§47–57, pp. 55–59)
- Lesson 7/8 preserve the source distinction between definite suffixes `-ê/-a/-ên` and indefinite patterns `-ek/-ek/-in` and `-ekî/-eke/-ine`. (§§61–68, pp. 62–67)
- Lesson 10's combined pronouns `jê/lê/pê/tê` and variants `jev/jêk, lev/lêk, pev/pêk, tev/têk` align with §§91–93, pp. 79–80. Its warning not to duplicate a preposition already contained in a combined pronoun is source-supported.
- Lesson 11 correctly separates the relative pronoun `ko` (§99) from the conjunction `ko` (§100), and retains the source forms `kîjik/kîjan` (§103). These are not typographical errors.
- Lesson 12 keeps the six adjective classes separate from the independent numeral category and preserves the source's four definite numeral classes. §§134–152, pp. 93–100.

## Quiz and answer-key status
- The master Course 2 answer key contains 60 rows (12 lessons × 5 questions).
- Existing repository test `tests/test_latin_course_2_quiz_keys.py` is designed to parse all embedded questions, compare each correct answer string to the selected A/B/C option, and check both uses of `ko`.
- This pass inspected the test and answer-key artifacts but did not execute the test suite in a local project environment. No test pass is claimed here.

## Safety and preservation
- Reviewed draft was created only on `archive/preservation-audit-2026-11-10`.
- Main source lesson file and main answer key remain unchanged.
- No runtime code, manifest, active course data, database, Botkeep server, or deployment was modified.
- This is a first pass, not a complete copyedit or a certification of every lexical example. Continue lesson-by-lesson, with source-specific page checks, before proposing any runtime activation.

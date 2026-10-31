# Latin Courses — Content Completeness and Release Gate

**Checked:** 2026-10-31  
**Branch:** `work/latin-courses-source-alignment-2026-10-31`  
**Status:** editorial drafts only; not loaded by the bot runtime.

## Scope separation

The bot's two Latin courses are distinct:
- **Course 1:** Kurmanji Latin orthography, sourced from Part I, *Elfabêya kurdî*, pp. 11–34.
- **Course 2:** Kurmanji grammar, sourced from Part II, *Bingehên gramera kurdmancî*, pp. 37–100.

Do not substitute the separate Sorani/Arabic-script 22-lesson `orthography_foundations.json` course for either Latin course. Do not apply Avasin Academy Arabic-script orthography rules to these bot courses.

## Course 1 — 12 lessons

| Lesson | Draft status in this branch | Quiz/key status |
|---:|---|---|
| 1 | Corrected draft present | Separate key; exact option test |
| 2 | Recovered draft restored from `Pasted text(1).txt` | Five options restored; master key matches exact option text |
| 3 | Recovered draft restored from `Pasted text(1).txt` | Five options restored; master key matches exact option text |
| 4 | Replacement draft present; not verbatim restoration; vowel-length explanation checked against printed p. 11 | Separate key; exact option test |
| 5 | Replacement draft present; not verbatim restoration; vowel-length explanation checked against printed p. 11 | Separate key; exact option test |
| 6 | Recovered draft restored from `Pasted text(1).txt` (brand casing/layout normalized) | Five options restored; master key matches exact option text |
| 7 | Corrected draft present | Separate key; exact option test |
| 8 | Replacement draft present | Separate key; exact option test |
| 9 | Replacement draft present | Separate key; exact option test |
| 10 | Corrected draft present | Separate key; exact option test |
| 11 | Corrected draft present | Separate key; exact option test |
| 12 | Corrected draft present | Separate key; exact option test |

**Recovery completed:** Lessons 2, 3, and 6 have been restored from the user's Library file `Pasted text(1).txt`. Their original teaching text and quiz option order were recovered; the master answer-key entries were corrected to match the exact selected option text. Lesson 6 received only Markdown/layout and brand-casing normalization. Lessons 4 and 5 remain transcript-confirmed, but their exact message bodies have not yet been restored; do not reconstruct them and label them verbatim.

## Course 2 — 12 lessons

- One source-aligned 12-lesson draft is present.
- Lessons 1–3 are explicitly marked as newly written source-aligned drafts, not recovered verbatim originals. Lesson 1 was reworked against printed pp. 37–38: the source's four elements are Tîp, Kît, Bêje, and Komek; Qiset is described as arising from the sequence of Komek units, not as a fifth item in that list. The lesson's grammar definition, Kurmanji-language introduction, source examples, quiz, and key were aligned accordingly. Lesson 9 now explicitly includes the source's three-way pronoun gender distinction (nêr, mê, nêtar), including the neutral use of ew, and has a regression guard. Lesson 1 was reworked against printed pp. 37–38: the source's four elements are Tîp, Kît, Bêje, and Komek; Qiset is described as arising from the sequence of Komek units, not as a fifth item in that list. The lesson's grammar definition, Kurmanji-language introduction, source examples, quiz, and key were aligned accordingly.
- Lessons 4–12 are editorially revised from recovered lesson material.
- Lesson 12: the expanded six-category draft is now selected and copied into the canonical 12-lesson master. The former baseline section was replaced; the separate replacement file is retained only as an editorial snapshot. The consolidated master key was aligned to the selected quiz options and is regression-tested. Do not load the snapshot as a second lesson.
- The consolidated key must match the exact quiz options in the selected lesson draft. The current canonical Course 2 Lesson 1 quiz and key are source-aligned and regression-tested; this does not convert the new draft into a recovered original.

## Regression protection added

The manifest test suite now checks that per-lesson quiz keys have unique question IDs and cover the complete expected 1–5 set, rather than accepting a correct total row count that could conceal a missing lesson/question and a duplicate. The Course 1 master answer key now contains all 60 question rows across all 12 lessons; a regression test verifies complete coverage, uniqueness, and agreement with the selected per-lesson key files. It also compares the exact answer text in the Course 1 Lessons 4–5 replacement key against the selected option text in both replacement drafts, and guards the short/long vowel grouping and source-grounded explanation. This validates only the current replacement drafts; it does not claim to restore the unavailable earlier transcript wording or option order.

## Release blockers

- [x] Restore Course 1 Lessons 2, 3, and 6 from the recovered source file, record provenance, and verify their exact quiz keys.
- [x] Reconcile the Course 1 master key into 60 unique rows (five per lesson); cross-check the consolidated rows against the selected per-lesson keys, while the existing lesson tests verify answer text against the quiz options.
- [x] Select the expanded Course 2 Lesson 12 version, copy it into the master, align the consolidated key, and mark the snapshot as non-runtime.
- [ ] Complete human linguistic/source review for all 24 lessons.
- [ ] Add runtime integration and progress-isolation tests only after content selection is approved.
- [ ] Preserve the existing voice workflow; keep dynamic speech disabled.
- [ ] Do not modify `main`, production bot/token/database, or deploy without explicit user approval.


## Course 1 vowel classification source check

The replacement explanations for Lessons 4–5 were corrected against Celadet Alî Bedir-Xan, *Elfabêya kurdî*, printed p. 11 (PDF page 11): the book states that Kurdish has eight vowels and classifies them by duration into short vowels **e, i, u** and long vowels **a, ê, î, o, û**. The replacement drafts now explain this duration-based classification directly rather than implying that length is not the basis of the grouping. The regression test guards the two exact vowel sets and the corrected explanation.

Source: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 Lesson 1 source-alignment check

Checked against Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 37–38 (PDF lines around the start of Part II). The lesson now preserves:
- Grammar as the totality of rules for correct speaking and writing.
- The book's short introduction to Kurmanji as the language of the Kurmanji people.
- The four listed language elements: **Tîp → Kît → Bêje → Komek**.
- **Qiset** as the result of successive combinations of **Komek**, not as a fifth item in the four-element list.
- The source's examples (Par ez çûbûm Rewanê, Îro dinya sar e, Gundê me di navbera du avan de ye) without the earlier malformed Parêz transcription.

The five-question quiz and its answer key were revised together; a regression test now checks the four-element sequence, the qiset distinction, and exact key-to-option text. This is a source-alignment edit to a new draft, not a verbatim restoration of the unavailable earlier lesson.

Source: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 Lesson 9 source-alignment check

The pronoun section in printed pp. 71–73 distinguishes three grammatical genders for pronouns: masculine, feminine, and neuter. The recovered Course 2 Lesson 9 draft previously listed only masculine and feminine third-person singular rows. It now adds the neuter row and explains that wî is masculine, wê feminine, and the remaining personal forms are treated as neuter in the source's classification. The quiz's existing masculine agent-form question remains unchanged. A regression test guards the presence of all three categories and the forms ew, wî, and wê.

Source: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf


## Course 2 pronoun completeness — source pages 76–89

A second pass against the source table of contents and printed pp. 76–89 found that the 12-lesson draft did not yet teach every pronoun class named by Bedir-Xan. The missing coverage is now added without changing the Latin-course boundary or importing Course 1 material:

- Lesson 10 adds **Pronavên lihevxisitî** (printed pp. 76–81), including the source's preposition-pronoun combinations `jê`, `lê`, `pê`, `tê` and compound forms such as `jev/jêk` and `pev/pêk`. The caution about not duplicating a preposition already contained in a fused form is included. It also restores the reflexive `xwe` (p. 87) and the singular neuter pronoun `ê` (pp. 88–89), with examples and a distinction from plural `wan`.
- Lesson 11 adds **Pronavên nebinavkirî** (printed pp. 86–87), with source-grounded examples such as `yek`, `her yek`, `kes`, `tu kes`, `her kes`, `tişttek`, `hin`, `hinek`, `çend`, `hemî`, `gişt`, and `gelek`.
- Lesson 11 adds **Pronavên xwemalîn** (printed pp. 87–89), showing the source's `yê/ya/yên` plus personal-pronoun pattern, and distinguishing these full pronouns from possessive adjectives such as `hespê min`.
- A regression test guards the new source categories and examples.

Source: Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, 2002, printed pp. 76–89. The six broad pronoun classes are listed on printed p. 74; the additional lihevxisitî section begins on p. 76. Source PDF: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf

This is an editorial source-alignment completion, not a claim that the new explanatory prose is a verbatim transcription of the book.

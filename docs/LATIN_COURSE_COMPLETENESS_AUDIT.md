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
| 4 | Replacement draft present; not verbatim restoration | Separate key; exact option test |
| 5 | Replacement draft present; not verbatim restoration | Separate key; exact option test |
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
- Lessons 1–3 are explicitly marked as newly written source-aligned drafts, not recovered verbatim originals.
- Lessons 4–12 are editorially revised from recovered lesson material.
- Lesson 12: the expanded six-category draft is now selected and copied into the canonical 12-lesson master. The former baseline section was replaced; the separate replacement file is retained only as an editorial snapshot. The consolidated master key was aligned to the selected quiz options and is regression-tested. Do not load the snapshot as a second lesson.
- The consolidated key must match the exact quiz options in the selected lesson draft.

## Regression protection added

The manifest test suite now checks that per-lesson quiz keys have unique question IDs and cover the complete expected 1–5 set, rather than accepting a correct total row count that could conceal a missing lesson/question and a duplicate.

## Release blockers

- [x] Restore Course 1 Lessons 2, 3, and 6 from the recovered source file, record provenance, and verify their exact quiz keys.
- [ ] Reconcile the Course 1 master key so all 12 lessons have one selected, exact option key.
- [x] Select the expanded Course 2 Lesson 12 version, copy it into the master, align the consolidated key, and mark the snapshot as non-runtime.
- [ ] Complete human linguistic/source review for all 24 lessons.
- [ ] Add runtime integration and progress-isolation tests only after content selection is approved.
- [ ] Preserve the existing voice workflow; keep dynamic speech disabled.
- [ ] Do not modify `main`, production bot/token/database, or deploy without explicit user approval.

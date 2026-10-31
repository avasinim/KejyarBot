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
| 2 | No lesson draft file found | Five answer-key rows exist in legacy key draft; source lesson/options need recovery |
| 3 | No lesson draft file found | Five answer-key rows exist in legacy key draft; source lesson/options need recovery |
| 4 | Replacement draft present; not verbatim restoration | Separate key; exact option test |
| 5 | Replacement draft present; not verbatim restoration | Separate key; exact option test |
| 6 | No lesson draft file found | Five answer-key rows exist in legacy key draft; source lesson/options need recovery |
| 7 | Corrected draft present | Separate key; exact option test |
| 8 | Replacement draft present | Separate key; exact option test |
| 9 | Replacement draft present | Separate key; exact option test |
| 10 | Corrected draft present | Separate key; exact option test |
| 11 | Corrected draft present | Separate key; exact option test |
| 12 | Corrected draft present | Separate key; exact option test |

**Do not invent replacement content for Lessons 2, 3, or 6 and label it recovered/source-verbatim.** Recover the original lesson text and quiz options from the user's supplied book/material or a verified repository artifact first. The legacy answer-key table alone is not enough to reconstruct the exact option order.

## Course 2 — 12 lessons

- One source-aligned 12-lesson draft is present.
- Lessons 1–3 are explicitly marked as newly written source-aligned drafts, not recovered verbatim originals.
- Lessons 4–12 are editorially revised from recovered lesson material.
- Lesson 12 has two competing drafts and two corresponding answer keys. Exactly one must be selected before runtime integration; never load both under one lesson ID.
- The consolidated key must match the exact quiz options in the selected lesson draft.

## Regression protection added

The manifest test suite now checks that per-lesson quiz keys have unique question IDs and cover the complete expected 1–5 set, rather than accepting a correct total row count that could conceal a missing lesson/question and a duplicate.

## Release blockers

- [ ] Recover/author and review Course 1 Lessons 2, 3, and 6 with explicit source provenance.
- [ ] Reconcile the Course 1 master key so all 12 lessons have one selected, exact option key.
- [ ] Select one Course 2 Lesson 12 version and retire/clearly archive the alternative.
- [ ] Complete human linguistic/source review for all 24 lessons.
- [ ] Add runtime integration and progress-isolation tests only after content selection is approved.
- [ ] Preserve the existing voice workflow; keep dynamic speech disabled.
- [ ] Do not modify `main`, production bot/token/database, or deploy without explicit user approval.

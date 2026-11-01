# KejyarBot — Latin course source separation audit
Date: 2026-11-01
Branch: audit/latin-course1-source-correction-2026-11-01

## Verified distinct source books

### Course 1 — Bingehên Rastnivîsîna Kurdî ya Latînî
Source PDF present in the user's Library:
- Dr. Efrasîyab Şikofteh, *Rê zimanê Kurmancî*.
- The title page gives the author and identifies the book as a Kurmanji grammar.
- The preface explicitly says the book teaches reading and writing Kurmanji in the North Khorasan Kurmanji dialect.
- The contents list Lesson 1, “Alfabê ya zimanê kurmancî” (printed p. 11) and Lesson 2, “Alfabê ya kurmancî bi dîtina dengnasînê” (contents list: printed p. 44).
- The alphabet section states that the Kurmanji alphabet has 31 letters (printed p. 12). Its following pages provide letter-specific examples and sentences (e.g. printed pp. 13–18).

### Course 2 — Bingehên Gramera Kurmancî
Source:
- Celadet Alî Bedir-Xan, *Elfabêya Kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002.
- Course 2 uses Part II, “Bingehên gramera kurdmancî” (printed p. 37 onward).
- This source is not the source book for Course 1.

## Corrections made on this isolated branch

1. Corrected the Course 1 source attribution in `course_data/latin_course_1_source_aligned_lessons_01_12.md` to Şikofteh's *Rê zimanê Kurmancî*.
2. Corrected the source separation section in `course_data/latin_courses_master_draft.md`.
3. Explicitly marked Course 1 as **not yet scientifically source-approved**. The corrected source identity does not imply that all 12 lesson bodies or quiz keys have already been checked against the book.

## Initial content checks / remaining audit

- The 31-letter alphabet count in Course 1 Lesson 1 agrees with the Şikofteh source (printed p. 12).
- Şikofteh's alphabet pages give concrete dialect-specific words and sentences. The current Course 1 draft uses some examples not yet verified against those pages (for example, its I-vowel example `kin` is not among the examples visible on printed p. 18, where the source lists `bivir, bizin, dil, hêstir, hingiv, zivistan`). This is a source-alignment check to complete, not proof that `kin` is linguistically invalid.
- Course 1 Lesson 2–12 still need lesson-by-lesson mapping to the relevant Şikofteh sections. The current lesson sequence may be pedagogically useful, but it must not be attributed to the book without a direct match.
- Course 1's five-question answer key is an editorial draft; it must be reconciled with the final corrected lesson bodies and source examples.
- Course 2 remains tied only to Celadet Alî Bedir-Xan. Its pronoun/adjective/numeral content and 60 quiz answers still need a separate source audit; no Course 1 material was imported into it.

## Safety / release boundary

- This branch was created from `fix/course3-latin-finalization-2026-11-01`.
- No edits were made to `main`, production data, production bot, Botkeep, live runtime, or deployment.
- No PR was created or merged.
- Dynamic speech remains disabled.
- This audit is editorial and source-provenance work; it does not claim runtime activation or deployment.

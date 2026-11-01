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
- The alphabet section states that the Kurmanji alphabet has 31 letters (printed p. 12). Its following pages provide letter-specific examples and sentences (e.g. printed pp. 13–28).
- Printed p. 29 explicitly lists 8 vowel letters and 23 consonants, matching the 31-letter inventory. Printed pp. 45–46 divide vowels into 3 short (`E, I, U`) and 5 long (`A, Ê, Î, O, Û`), and identify `W` and `Y` as semivowels. Printed pp. 56–60 provide letter-specific phonetic descriptions and distributions.

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

- The 31-letter alphabet count in Course 1 Lesson 1 agrees with Şikofteh (printed pp. 12, 29).
- Replaced the Lesson 1 example for `I` (`kin`) with `dil`, which appears in Şikofteh's I-letter examples (printed p. 18).
- Removed three imported Bedir-Xan source notes from Course 1 Lessons 4, 6, and 7 and replaced them with Şikofteh references (printed pp. 45–46, 56–60). Course 1 no longer cites the Course 2 book inside its lesson bodies.
- Corrected Course 1 Lesson 8 to distinguish `V` (consonant) from `W` and `Y` (semivowels), following Şikofteh's phonetic section (printed p. 46).
- Şikofteh's alphabet pages give concrete dialect-specific words and sentences. The current Course 1 draft uses some examples not yet verified against those pages (for example, its I-vowel example `kin` is not among the examples visible on printed p. 18, where the source lists `bivir, bizin, dil, hêstir, hingiv, zivistan`). This is a source-alignment check to complete, not proof that `kin` is linguistically invalid.
- Course 1 Lesson 2–12 still need a full lesson-by-lesson mapping to the relevant Şikofteh sections. The source has an internal numerical inconsistency: printed p. 46 says there are 32 consonants, while printed p. 29 gives the 8-vowel + 23-consonant inventory that totals 31 letters. The draft follows the internally consistent 31/8/23 count from p. 29 and does not repeat the apparent p. 46 error.
- KejyarBot footer branding (`🤖 کەژیار — KejyarBot@`) has now been standardized across all 12 lessons in both Latin course documents. The current lesson sequence may be pedagogically useful, but it must not be attributed to the book without a direct match.
- Course 1's five-question answer key is an editorial draft; it must be reconciled with the final corrected lesson bodies and source examples.
- Course 2 remains tied only to Celadet Alî Bedir-Xan. Its pronoun/adjective/numeral content and 60 quiz answers still need a separate source audit; no Course 1 material was imported into it.

## Safety / release boundary

- This branch was created from `fix/course3-latin-finalization-2026-11-01`.
- No edits were made to `main`, production data, production bot, Botkeep, live runtime, or deployment.
- No PR was created or merged.
- Dynamic speech remains disabled.
- This audit is editorial and source-provenance work; it does not claim runtime activation or deployment.

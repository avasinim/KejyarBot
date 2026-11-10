# Course 2 — Orthography and example consistency pass
**Date:** 2026-11-10  
**Branch:** `archive/preservation-audit-2026-11-10`  
**Scope:** Targeted internal spelling scan of the reviewed Course 2 draft, followed by source-context checks for the affected forms. This is not a full diplomatic transcription of all 12 lessons.

## Confirmed internal inconsistency and correction
The reviewed draft used two spellings for the same recurring noun:
- Lesson 3 source-inventory line: `mehin`
- Lessons 4–5 and the rest of the draft: `mehîn`
- Lesson 12 demonstrative examples: `vê mehinê / van mehinan` and `wê mehinê / wan mehinan`

The reviewed draft has been normalized to `mehîn`, `mehînê`, and `mehînan` in all three affected locations. This is an internal consistency normalization, not a claim that the PDF's OCR extraction independently establishes every diacritic: the source extraction splits syllables and does not return the exact joined spelling reliably. The underlying noun, examples, lesson structure, and answer-key content were not otherwise changed.

## Source context checked
- The source's noun-gender and noun-inflection sections include the noun in examples/inventory around printed pp.52–61.
- The source adjective section uses forms corresponding to `mehîneke boz` and references the noun with descriptive adjectives around printed pp.90–91.
- Demonstrative-adjective paradigms are treated in §132, printed p.93.
- The source PDF's OCR line breaks and character encoding are imperfect; ambiguous diacritics should be confirmed against page images before claiming exact source spelling.

## Other orthographic checks
- `hon` is retained, not changed to `hûn`: the source itself uses `hon` in its personal-pronoun inventory and examples (§§75, 77–78, printed pp.72–76).
- `ko` is retained in the source-specific relative/conjunctive treatment in Lesson 11; the draft already explains that it is preserving Celadet's source form rather than silently replacing it with `ku`.
- User-requested supplemental names `Ferzane`, `Kejyar`, and `Argesh` remain explicitly labelled as added teaching examples, not as Celadet quotations.

## Preservation and validation
- Updated only `course_data/latin_course_2_reviewed_draft_2026-11-10.md` on this archive branch, after fetching its current blob SHA; fetched it again after the update and verified the new blob SHA and corrected forms.
- No original lesson file, quiz, master answer key, `main`, active manifest, runtime, database, Botkeep bot, Telegram bot, or deployment was changed.
- This pass does not certify every spelling or example in every lesson. Further page-image review is still needed where OCR has split or corrupted Kurdish letters.
- No tests or runtime execution were performed.

## Source
Celadet Alî Bedir-Xan, *Elfabêya kurdî & Bingehên gramera kurdmancî*, Nefel, Stockholm, 2002, printed pp.52–61 and 90–93. PDF: https://kurdshop.net/content/upload/1/root/celadet-ali-bedir-xan-elfabeugramer-02.pdf

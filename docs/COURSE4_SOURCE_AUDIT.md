# Course 4 — Source Audit (Preliminary)

Status: **source inspection in progress; no lesson content approved**

This audit belongs to the isolated branch `reset/grammar-course4-content`. It does not activate Course 4, alter other courses, or deploy anything.

## Source files and provenance

1. `Rezmany_axawtny_kurdy.pdf`
   - Source commit: `f7f5236d861aaa5f9f26e81b0d7a25ceb992914e`
   - Blob: `e144eac2937c4f13a4f852fc403c17cc0fee3671`
   - Visible title page (PDF p. 3): **ڕێزمانی ئاخافتنی کوردی**
   - The copyright/publication page (PDF p. 4) indicates an original publication in 1990 and a second printing in 2011. The author/editor attribution still needs careful confirmation from the full title/copyright pages.
   - PDF length: 400 pages.

2. `ڕێزمانی ڕاناوی لكاو.pdf`
   - Source commit: `bde4b44ddf5127e6c9762d014fd7d2cde2dc0423`
   - Blob: `68da93bc3cb9e37f492b13f346a2c7961b9639dc`
   - Visible title page (PDF p. 3): **ڕێزمانی ڕاناوی لکاو**
   - Visible author name: **ڕیا عومەر ئەمین** (transcription should be checked against the title page before final bibliography).
   - PDF length: 32 pages.

## Direct visual observations

### Source 1 — spoken Kurdish grammar

- PDF p. 3: title page identifies the work as **ڕێزمانی ئاخافتنی کوردی**. This is a scope warning: it must not automatically be treated as a comprehensive grammar of every Kurdish variety.
- PDF p. 4: publication information indicates 1990 and second printing 2011.
- PDF p. 11: the section on **ناو** begins.
- PDF p. 12: discusses simple nouns and gives examples attributed to named writers/speakers; the page also includes a definition.
- PDF pp. 13–15: continues the distinction and discussion of simple and compound nouns, with examples and classification. These examples must be transcribed exactly before reuse.
- No general rule from these pages is approved for a course lesson yet. The dialect/register scope of each example and analysis still needs confirmation.

### Source 2 — enclitic pronouns

- PDF p. 3: title page identifies **ڕێزمانی ڕاناوی لکاو** and shows the author's name.
- PDF p. 6: references **W. O. Amin (1976), “Some Fundamental Rules of Kurdish Syntax Structure”**.
- PDF p. 7: explicitly mentions transformational grammar; therefore the author's theoretical analysis must be distinguished from the forms/examples being described.
- PDF pp. 8–11: contain diagrams/tables and discussion of forms and their behavior in sentence structure. These pages require page-by-page transcription and analysis; the OCR output is not reliable.
- The work is only 32 pages, so a complete manual review is feasible before any of its claims are used.

## Extraction reliability

The GitHub Actions extraction run `41982256365` completed successfully and produced visual page previews.

However:
- Source 1: 397 pages were extracted as embedded text, but the extracted text is visibly unreliable/garbled in many places; only 3 pages used OCR.
- Source 2: 31 of 32 pages used Arabic+English OCR marked **UNVERIFIED**; only one page used embedded text.
- Therefore, the extracted TXT files are navigation aids only. They are **not authoritative transcriptions** and must not be used to write rules or examples without visual checking.

## Verification rules before lesson drafting

For every proposed rule/example, record:
1. Exact source title and edition/publication details where available.
2. Printed page number and PDF page number (both, when different).
3. Exact transcription of the relevant Kurdish text/example.
4. Scope: Central/Sorani, another variety, spoken register, written register, or unspecified.
5. What the source actually claims, separately from our interpretation.
6. Independent corroboration from a reliable linguistic source, or an explicit note that corroboration is not yet found.
7. Decision: verified for teaching / needs clarification / conflicting evidence / exclude.

Do not silently normalize the source's orthography, dialect forms, or terminology. Preserve the original form in the evidence record and place any editorial explanation separately.

## Current decision

**No lesson text is approved.** Course 4 remains planned and inactive. No other course, `main`, production database, Botkeep runtime, or deployment has been changed.

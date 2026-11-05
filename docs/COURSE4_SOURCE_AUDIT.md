# Course 4 — Source Audit (Preliminary)

Status: **single-source curriculum decision adopted; source inspection in progress; no lesson content approved**

This audit belongs to the isolated branch `reset/grammar-course4-content`. It does not activate Course 4, alter other courses, or deploy anything.

## Adopted source policy

The user has chosen to build Course 4 using only **ڕێزمانی ئاخافتنی کوردی** as its curriculum's primary and sole course-content book.

The separate book `ڕێزمانی ڕاناوی لكاو.pdf` is **excluded from Course 4 content development**. Do not use its lessons, classifications, examples, or theoretical framework in the course. It is recorded below only for provenance/history and is not an active course source.

Independent linguistic publications may still be consulted strictly to verify or challenge claims from the primary book. They must not silently replace its curriculum structure or be blended into lesson content as if they came from the primary book. Any disagreement must be documented, and unresolved claims must be excluded or clearly qualified.

## Active primary source and provenance

- File: `Rezmany_axawtny_kurdy.pdf`
- Source commit: `f7f5236d861aaa5f9f26e81b0d7a25ceb992914e`
- Blob: `e144eac2937c4f13a4f852fc403c17cc0fee3671`
- Visible title page (PDF p. 3): **ڕێزمانی ئاخافتنی کوردی**
- The copyright/publication page (PDF p. 4) indicates an original publication in 1990 and a second printing in 2011. The author/editor attribution remains to be transcribed carefully from the title/copyright pages.
- PDF length: 400 pages.

## Excluded source — provenance only

- File: `ڕێزمانی ڕاناوی لكاو.pdf`
- Source commit: `bde4b44ddf5127e6c9762d014fd7d2cde2dc0423`
- Blob: `68da93bc3cb9e37f492b13f346a2c7961b9639dc`
- Visible title page (PDF p. 3): **ڕێزمانی ڕاناوی لکاو**
- Visible author name: **ڕیا عومەر ئەمین**.
- The title page identifies the Kurdish Department, University of Baghdad.
- PDF length: 32 pages.
- **Decision: excluded from Course 4 content.** No rules, examples, terminology, or theory from this book are to be incorporated into lessons.

## Direct visual observations from the active source

### ڕێزمانی ئاخافتنی کوردی

- PDF p. 3: title page identifies the work as **ڕێزمانی ئاخافتنی کوردی**. This is a scope warning: it must not automatically be treated as a comprehensive grammar of every Kurdish variety.
- PDF p. 4: publication information indicates 1990 and second printing 2011.
- PDF p. 11: the section on **ناو** begins.
- PDF p. 12: discusses simple nouns and gives examples attributed to named writers/speakers; the page also includes a definition.
- PDF pp. 13–15: continues the distinction and discussion of simple and compound nouns, with examples and classification. These examples must be transcribed exactly before reuse.
- No general rule from these pages is approved for a course lesson yet. The dialect/register scope of each example and analysis still needs confirmation.

## Extraction reliability

The GitHub Actions extraction run `41982256365` completed successfully and produced visual page previews.

However:
- Source 1: 397 pages were extracted as embedded text, but the extracted text is visibly unreliable/garbled in many places; only 3 pages used OCR.
- Source 2: 31 of 32 pages used Arabic+English OCR marked **UNVERIFIED**; only one page used embedded text. Source 2 is excluded from the course regardless.
- Therefore, the extracted TXT files are navigation aids only. They are **not authoritative transcriptions** and must not be used to write rules or examples without visual checking.

## Verification rules before lesson drafting

For every proposed rule/example from the active primary source, record:
1. Exact source title and edition/publication details where available.
2. Printed page number and PDF page number (both, when different).
3. Exact transcription of the relevant Kurdish text/example.
4. Scope: Central/Sorani, another variety, spoken register, written register, or unspecified.
5. What the author actually claims, separately from our interpretation.
6. Independent corroboration from a reliable linguistic source, or an explicit note that corroboration is not yet found. Independent sources are for validation only, not a second curriculum source.
7. Decision: verified for teaching / needs clarification / conflicting evidence / exclude.

Do not silently normalize the source's orthography, dialect forms, or terminology. Preserve the original form in the evidence record and place any editorial explanation separately.

## Current decision

**No lesson text is approved.** Course 4 remains planned and inactive. The single-source decision is adopted, but the primary book still requires systematic page-by-page inspection and independent validation of claims. No other course, `main`, production database, Botkeep runtime, or deployment has been changed.

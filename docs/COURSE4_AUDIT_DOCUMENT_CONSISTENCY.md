# Course 4 — audit-document consistency check

Date: 2026-11-05  
Branch: `reset/grammar-course4-content`  
Scope: cross-check of the audit documents currently committed on this branch. This is a documentation-consistency review, **not** a new inspection of the original PDF images.

## 1. p.398 / p.222 discrepancy: three inconsistent records

The current documents do not agree on the contents-page transcription:

1. In `COURSE4_SOURCE_AUDIT.md`, the verified contents-page table currently lists p.398 as **5 — چاوگ**.
2. In the later discrepancy discussion within that same file, the text says the contents-page reading is **جێناو** and contrasts it with the p.222 chapter heading **چاوگ**.
3. `COURSE4_SOURCE_DISCREPANCY_P222_P398.md` also records p.398 as **جێناو** and p.222 as **چاوگ**.

Therefore, the repository contains an internal documentation conflict. The two strings must not be treated as settled until the original p.398 image is reopened at readable size and checked against the page image. The p.222 chapter heading **چاوگ** remains separately recorded. No term is being normalized or interpreted here.

**Required repair after image verification:** update the p.398 row in the contents table, the discrepancy log, the proposed outline note, and any evidence-register references so every document reflects the verified printed form. Do not make that repair from OCR or memory.

## 2. pp.31–79: visual coverage versus transcription

`COURSE4_VISUAL_MAPPING_031_079.md` records contact-sheet review of all pages and individual-page review of pp.31, 36, 41, 66, 67, 70, 72, and 79. This is a page map and selective visual inspection, not full sequential close reading or diplomatic transcription.

The p.72 second heading is recorded provisionally as **داراژ** after a magnified crop. It remains a source-faithful visual reading pending independent linguistic validation; do not silently normalize it or teach it as a verified modern category.

## 3. Verb chapter: known gap before the sequential block

The current register describes pp.80–160 as spot-checked, with the detailed sequential page-image block beginning at p.121. The existing notes pp.121–160 and pp.161–221 do not establish sequential review of pp.80–120.

Accordingly:
- pp.80–120 remain a documented coverage gap for sequential page-image review.
- Existing spot checks (including pp.81, 88, 93, 112–114, and 120) are not a substitute for page-by-page review.
- Dense verb paradigms across the reviewed range still require diplomatic transcription and independent validation.

## 4. Next actions, in order

1. Reopen original PDF p.398 and p.222 images side by side; resolve only the printed-word discrepancy.
2. Generate/retrieve original page images for pp.80–120 and inspect them sequentially; create a separate review note with clear coverage and limits.
3. Continue crop-level transcription of selected verb paradigms, preserving every dialect label and attribution.
4. Reconcile the contents table, discrepancy log, evidence register, and proposed outline only after the source image is verified.

## Status and guardrails

- This file records inconsistencies and next steps; it does not claim to resolve them.
- The sole Course 4 curriculum source remains **ڕێزمانی ئاخافتنی کوردی**. The separate book **ڕێزمانی ڕاناوی لکاو** remains excluded.
- Independent publications remain validation-only.
- Course 4 remains planned/inactive with zero lessons. No lesson, quiz, activation, course metadata, other-course data, production database, Botkeep runtime, merge, or deployment was changed.

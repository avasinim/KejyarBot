# Course 4 owner-review beta handoff — 2026-11-06

## Decision
The project owner explicitly approved making the first eight lessons available earlier as an owner-review beta and correcting wording, grammar, and content iteratively together.

## Scope
- Course: `grammar`, order 4.
- Lessons: `grammar_01` through `grammar_08`.
- Source: `Rezmany_axawtny_kurdy.pdf` only.
- Source cutoff: page 342. Section 9 (surprise particle, pages 349–373) is excluded.
- All eight lessons remain marked `owner_review`; this is not a claim of final linguistic validation.

## Safety and release boundaries
- This branch is a candidate for the owner-review test branch only.
- No merge to `main`, production database change, or production deployment is authorized or performed.
- Runtime validation and CI must be checked before treating the beta as runnable in the Telegram bot.
- If source transcription or terminology is disputed, preserve the uncertainty and ask the owner to supply/correct the text; do not silently normalize.

## Working notes
Selected source reviews are recorded in the accompanying crop-review and terminology-audit documents. Preserve distinctions such as `بەکار` vs `بەرکار`, and retain author/regional attribution where the source does so.

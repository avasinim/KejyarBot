# Round 57 — Temporary-Copy Regression Verification
Date: 2026-11-10
Source branch: `botkeep-menu-clean-2026-11-09`
Source blob SHA: `fd8dfbde7e6937841214cacac653ef10d0c6097d`
Proposal: `COURSE4_BASTEN_TERM_REVERSIBLE_PATCH_PROPOSAL_ROUND57_2026-11-10.md`

## Verified temporary-copy results
The Round 57 candidate map was applied in memory to a temporary parsed copy only; the repository source file was not written or changed.

- Candidate replacements: **72 occurrences** across **68 JSON string paths**.
- Quiz-linked: **18 occurrences** in **17 quiz string paths**.
- Course lesson count: **50**, unchanged.
- JSON structural shape / object-key / array shape: unchanged.
- Per-lesson quiz counts: unchanged.
- All answer-bearing fields and answer indices: unchanged.
- Remaining mapped legacy forms in the scanned lesson fields: **0**.
- Original source SHA remains the reference snapshot; no source commit was created.

## Interpretation and limitation
This validates only the mechanical proposal's structural invariants. It does **not** validate the academic appropriateness or naturalness of every proposed inflection. The full before/after strings in the Round 57 ledger still require human-quality Sorani editorial review, particularly in quiz stems and explanations. Bare `سیاق` forms and unlisted compounds were deliberately held.

## Decision
Round 57 proposal is structurally reversible and passes the listed temporary-copy invariants. It is **not approved for application to the raw lesson JSON**. Keep the proposal in staging until phrase-by-phrase linguistic review and explicit authorization for source patching.

## Change-control
No raw lesson JSON, quiz object, answer key, runtime, database, Botkeep, Telegram, deployment, PR merge, or production configuration changed.

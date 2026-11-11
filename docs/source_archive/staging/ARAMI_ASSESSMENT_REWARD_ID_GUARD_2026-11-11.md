# Arami assessment reward helper hardening

**Date:** 2026-11-11  
**Candidate PR:** #150  
**Merge commit:** `1fdeec97534e8415bca88e1b0a79af8265215693`

## Change

The Arami assessment reward helper now accepts only lesson IDs registered to `arami_orthography_foundations`. It rejects unknown lesson IDs and IDs belonging to other courses before calling the official quiz-reward ledger. Registered Arami lessons still require explicit academic approval through the shared review gate.

## Tests

Regression assertions cover:
- a pending Arami lesson;
- an unregistered lesson ID;
- a lesson ID belonging to Course 4.

The CI-only mirror PR #151 used byte-identical versions of all seven relevant code/test files and passed all three workflows:
- Python checks: **539 tests passed, 11 skipped**.
- Course 4 beta review safety: passed.
- Orthography course structure: passed.

PR #150 was squash-merged into the candidate branch only. PR #151 was closed unmerged after validation.

## Safety

No main-branch merge, Botkeep import, restart, deployment, or live database write was performed. Written Node17 clearance is still required before test-bot import.

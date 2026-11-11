# Runtime-branch and candidate synchronization checkpoint

**Date:** 2026-11-11

## Verified GitHub branch state

- PR #125, `Harden academic course menus, lesson access, and pagination`, is merged into `botkeep-runtime-2026-11-09`.
- PR #125 merge commit / current runtime branch base observed: `2637c121bf04f6cce1777a9932d60914ceca1bb7`.
- PR #148 (unified fail-closed academic approval) and PR #150 (Arami reward helper ID guard) are merged only into `botkeep-menu-clean-2026-11-09`.
- Comparison of `botkeep-runtime-2026-11-09` to `botkeep-menu-clean-2026-11-09` shows the candidate branch is 3 commits ahead and 1 commit behind, with 8 changed files.
- The changed files include the Arami assessment/reward gates, shared approval policy, tests, and disposable SQLite rehearsal record.
- Comparison against `main` still shows the branches diverged; no changes from these candidate PRs were merged into `main`.

## Operational interpretation

The runtime Git branch has received PR #125, but it does **not** yet contain the later PR #148 and #150 changes. The candidate branch therefore remains a separate, newer test candidate.

No Botkeep import, restore, restart, or deployment has been performed as part of this checkpoint. Do not sync or import the candidate into the Botkeep test bot until written Node17 clearance is received and the user-authorized test-bot transfer can be performed safely.

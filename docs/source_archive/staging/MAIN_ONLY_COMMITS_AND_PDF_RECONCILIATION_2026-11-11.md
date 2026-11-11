# Main-Only Commit and PDF Asset Reconciliation — 2026-11-11

## Compared refs
- Main: `7db20f242087e3eb9149e2e788f6c20529870f32`
- Candidate: `botkeep-menu-clean-2026-11-09`
- Merge base: `1037ddc85aa92d2eb08e95d598f1cfeb06a9cb92`
- Compare result: main is 12 commits ahead of the merge base; candidate is 233 commits ahead of the merge base. The refs have diverged.

## Twelve main-side commits identified
1. `7db20f24` — Archive Lesson 13 internal source map and terminology crosswalk.
2. `08842fcb` — Clarify 240 Lesson 1–30 quiz overrides versus 248 total quiz questions.
3. `7b97ab1f` — Restore protected Kurdish orthography reference PDF.
4. `0b0b0a84` — Remove remaining PDF asset per user instruction.
5. `b0bd6efa` — Harden academic lesson search; clear stale daily-conversation state and add regression tests.
6. `22b97403` — Redesign academic course menus and add lesson search; retain special lesson handlers/access guards; commit message reports 482 tests.
7–12. `a11a0433`, `4f44a6b6`, `4bd625b3`, `1535d085`, `020f9555`, `48c8c2fc` — six commits titled “Remove unneeded PDF from main”.

## PDF presence check
The compare endpoint reports these candidate-side removals relative to main:
- `بەرگی ١ حا.pdf`
- `بەرگی ٢.pdf`
- `بەرگی ٣.pdf`
- `بەرگی ٤.PDF`
- `بەرگی ٥.pdf`
- `پوختەی ڕێنووس و خاڵەبەندی..pdf`
- `ڕێزمانی ڕاناوی لكاو.pdf`

Direct content lookup by the displayed names was inconclusive for most paths (404 on both refs); the exact path `پوختەی ڕێنووس و خاڵەبەندی..pdf` is present on main (blob `07a88a571c2a25caa9588708d0173d7f33e04a7a`) and absent on candidate. Do not infer the other six assets' contents or recoverability from filenames alone. The restoration commit `7b97ab1f` specifically says it restored a protected Kurdish orthography reference PDF; that file must be preserved in any promotion if it is the confirmed protected source. Do not reintroduce files removed at the user's instruction without verifying their intended status.

## Candidate-only promotion implications
The main-side commits include two relevant runtime changes (academic lesson search hardening and academic menu redesign), as well as lesson 13 archival / quiz-count documentation and PDF cleanup/restoration. A future release branch must selectively reconcile these changes with candidate's newer course and review-gate work. Do not merge candidate wholesale into main, and do not drop main's menu/search improvements.

## Safety / limitations
This is source-history and path-level inspection only. Commit diff bodies were not returned by the connector, so the six PDF removal commits were identified by commit messages and the aggregate compare file list, not by full per-commit patches. No repository runtime code was modified in this audit; no Botkeep import/restart, live DB write, Railway deployment, or main-bot deployment occurred. Node17 written support clearance remains required before test-bot import.

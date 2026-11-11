# Arami review-gate CI validation and candidate merge record

**Date:** 2026-11-11

## Code and test validation

The Arami review-only assessment/reward gate was validated on a temporary mirror against the CI-enabled `botkeep-runtime-2026-11-09` base. The seven changed code/test files in that mirror were byte-identical (same Git blob SHAs) to the corresponding files in PR #146.

All latest validation workflows completed successfully:

- Python checks — run `43009376780`: `python -m compileall -q .` passed; `python -m unittest discover -s tests -v` passed, **538 tests, 11 skipped**.
- Course 4 beta review safety — run `43009376577`: compile and full test suite passed.
- Orthography course structure — run `43009376709`: passed.

An earlier validation attempt exposed failures in Lesson 1/Lesson 5 handler compatibility and outdated assessment-menu expectations. Those were fixed, the validation mirror was synchronized, and the latest runs above passed.

## Pull-request disposition

- PR #146, `Block official Arami assessments until academic approval`, was squash-merged into candidate branch `botkeep-menu-clean-2026-11-09`.
- Merge commit: `67b844a5fdb8c731872177ab33da6114b3255597`.
- PR #147 was a temporary CI-only mirror targeting `botkeep-runtime-2026-11-09`; it was closed unmerged after successful validation.
- No change was merged to `main`.
- No Botkeep import, restore, restart, or deployment was performed.

## Safety boundary

This validation does not replace Botkeep's written Node17 clearance. Candidate code remains un-deployed until Botkeep support confirms the resource/file-staging issue is resolved and the user authorizes the test-bot transfer.

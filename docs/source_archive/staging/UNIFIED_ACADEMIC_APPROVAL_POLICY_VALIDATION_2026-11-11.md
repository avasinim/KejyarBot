# Unified academic approval policy — implementation and validation record

**Date:** 2026-11-11  
**Candidate branch:** `botkeep-menu-clean-2026-11-09`  
**Candidate PR:** #148  
**Merge commit:** `4f57b2691eba8b21aa597ff77bed289abfff5325`

## Policy

All active courses now require an explicit academic approval status before official assessments, quiz rewards, lesson rewards, or badges can be issued.

The shared allowlist is imported from `arami_course1_telegram.py`:

- `scientific_review_complete`
- `scientific_review_complete_with_qualified_notes`
- `approved`

For every active course, an unknown status, missing status, or status outside this allowlist is treated as review-only (fail closed). Reading remains available. Existing Beta progress stays in its separate ledger and does not become official completion or rewards.

The policy applies automatically to every course marked active in `courses.json`, so a newly activated course is review-gated by default.

## Course-specific results

- Arami Course 1: lessons with pending, source-received, source-preserved, or missing approval status remain review-only. Receipt and preservation of source material do not count as academic approval.
- Courses 2 and 3: editorial drafts remain review-only.
- Latin courses: editorial drafts remain review-only.
- Course 4 lessons 1–31: `scientific_review_complete_with_qualified_notes` remains explicitly approved; this includes Lesson 13.
- Course 4 lessons 32–50: `owner_review_pending_expanded_draft` remains review-only.
- Unknown or missing future statuses fail closed.

## Regression coverage

Added a regression test verifying:
- every active course ID is included in the review-gated set;
- Course 4 Lesson 13 remains approved under its qualified scientific-review status;
- unknown, draft, and missing statuses are review-only.

Earlier Arami gate tests also cover the shared Course 1 callback, dedicated Lesson 1 and Lesson 5 callbacks, global assessment menu, and reward rejection.

## CI validation

A validation-only mirror was opened as PR #149 against the CI-enabled runtime base. The seven relevant source/test files were checked against the candidate by matching Git blob SHAs.

All three workflows passed:

- Python checks: **539 tests passed, 11 skipped**.
- Course 4 beta review safety: passed, including compile and full test suite.
- Orthography course structure: passed.

PR #148 was squash-merged into the candidate branch only. PR #149 was closed unmerged after validation.

## Operational safety

- No changes were merged to `main`.
- No Botkeep import, restore, restart, or deployment was performed.
- No live database writes were performed.
- Disposable SQLite migration and Beta-ledger rehearsals remain separate and passed.
- Botkeep Node17 written clearance is still required before importing the candidate into `KejyarBot-Test`.

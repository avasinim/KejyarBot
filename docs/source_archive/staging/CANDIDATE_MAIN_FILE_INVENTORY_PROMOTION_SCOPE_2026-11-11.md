# Candidate-to-Main File Inventory and Promotion Scope — 2026-11-11

## Compared refs
- Base: `main` (snapshot SHA recorded in prior audit: `7db20f242087e3eb9149e2e788f6c20529870f32`)
- Head: `botkeep-menu-clean-2026-11-09`
- Merge base: `1037ddc85aa92d2eb08e95d598f1cfeb06a9cb92`
- GitHub compare status: diverged; candidate ahead 233, main ahead 12.
- Aggregate changed paths: 204 (173 added, 24 modified, 7 removed).

## Inventory by scope
- 166 paths under `docs/source_archive/` — preservation/review material; not runtime release payload. Keep on the candidate/archive history and do not bulk-promote as application files.
- 7 added outside the source archive:
  - `.github/workflows/course4-50-beta-review.yml`
  - `.github/workflows/course4-quiz-overrides.yml`
  - `.github/workflows/review-gate-validation.yml`
  - `course_data/grammar_course4_quiz_overrides.json`
  - `docs/archives/2026-11-09-END-OF-DAY-PRESERVATION.md`
  - `tests/test_academic_course_menu.py`
  - `tests/test_lesson_search.py`
- 24 modified outside the source archive:
  - Workflows: `.github/workflows/course4-beta-review.yml`, `.github/workflows/orthography-course-structure.yml`, `.github/workflows/python-checks.yml`
  - Runtime: `arami_course1_telegram.py`, `arami_lesson1_telegram.py`, `arami_lesson5_telegram.py`, `bot.py`, `course_runtime.py`
  - Course data: `course_data/grammar_course4_lessons.json`, `courses.json`, `curriculum/grammar_course4_plan.json`
  - Documentation: `docs/COURSE4_GRAMMAR_APPENDIX.md`
  - Tests: `tests/test_activated_courses.py`, `tests/test_arami_course1_telegram.py`, `tests/test_arami_lesson1_telegram.py`, `tests/test_arami_lesson5_telegram.py`, `tests/test_bot_message_mode.py`, `tests/test_bot_quiz_callbacks.py`, `tests/test_content.py`, `tests/test_course3_runtime_ux.py`, `tests/test_course4_beta_review.py`, `tests/test_course4_grammar_runtime.py`, `tests/test_database.py`, `tests/test_orthography_course_structure.py`.
- 7 removed paths, all PDF assets:
  - `بەرگی ١ حا.pdf`
  - `بەرگی ٢.pdf`
  - `بەرگی ٣.pdf`
  - `بەرگی ٤.PDF`
  - `بەرگی ٥.pdf`
  - `پوختەی ڕێنووس و خاڵەبەندی..pdf`
  - `ڕێزمانی ڕاناوی لكاو.pdf`

## Promotion classification
1. Runtime and course-data files require manual, file-level reconciliation against current main. Do not replace whole files blindly: main contains 12 later commits, including academic menu/search improvements and Lesson 13 source-map/terminology work.
2. The 1,408-line quiz override JSON is a candidate addition and must be validated against the lesson JSON, source answer keys, question IDs, and the recorded distinction between 240 overrides for lessons 1–30 and 248 total questions before activation.
3. Tests should be carried with the corresponding runtime changes; candidate's successful CI mirror (538 tests, 11 skipped) is evidence for the tested candidate snapshot, not a substitute for rerunning CI on a new main-based promotion commit.
4. Workflows should be reviewed individually; retain main's current workflow behavior while adding only needed review-gate coverage.
5. The 166 source-archive files are preservation records, not a blanket release list.
6. The seven PDF removals must be treated as explicit content deletions. Do not restore or delete any of them based only on filenames. Confirm the protected orthography PDF and user's prior removal instruction against exact commit/file history before release. The compare endpoint identifies the seven paths as removed on the candidate side relative to main; direct path lookup confirmed `پوختەی ڕێنووس و خاڵەبەندی..pdf` exists on main and not candidate, while other path lookups were inconclusive due to path resolution.

## Recommended release sequence
- Create a fresh release branch from current main.
- Apply a reviewed allowlist of runtime, course-data, tests, and selected workflows.
- Reconcile main-side 12 commits, particularly lesson 13 source map and current menu/search behavior.
- Preserve all original lesson text; validate quiz overrides and reward gates.
- Run compile, full unit suite, all relevant workflows, and disposable SQLite migration rehearsal against the exact release SHA.
- Keep Node17 import blocked until written Botkeep support clearance. No runtime import/restart or live database changes are authorized by this inventory.

## Validation boundary
This report is based on GitHub compare metadata and source-file reads. It is an inventory and release-planning record, not a merge, code deployment, Botkeep import, Railway deployment, or live DB change.

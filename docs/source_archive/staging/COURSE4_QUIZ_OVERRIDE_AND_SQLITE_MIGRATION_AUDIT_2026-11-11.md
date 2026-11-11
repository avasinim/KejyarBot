# Course 4 quiz override and SQLite migration audit
## 2026-11-11 | Read-only verification | Append-only

### Source examined
- Repository: `avasinim/KejyarBot`
- Ref: `botkeep-menu-clean-2026-11-09`
- Files: `course_data/grammar_course4_lessons.json`, `course_data/grammar_course4_quiz_overrides.json`, `database.py`, `tests/test_course4_beta_review.py`

### Quiz override validation
A read-only structural validation of the exact source files found:
- 50 override entries.
- 50 unique `(lesson_id, question_index)` keys; no duplicate keys.
- Every referenced lesson and question index exists.
- Every `original_snapshot` exactly matches the corresponding authored source quiz item.
- Every replacement has a non-empty question and explanation, exactly four distinct non-empty options, and an integer answer index from 0 through 3.
- No structural/snapshot problems were found in this pass.
- The 50 overrides affect 23 lesson IDs: grammar_01, grammar_02, grammar_03, grammar_04, grammar_06, grammar_07, grammar_09, grammar_10, grammar_12, grammar_13, grammar_14, grammar_16, grammar_18, grammar_20, grammar_22, grammar_23, grammar_25, grammar_26, grammar_27, grammar_28, grammar_29, grammar_30, grammar_31.

This verifies structural integrity and exact snapshot matching only; it does not certify every replacement's academic correctness or dialectal suitability. The runtime also performs fail-closed snapshot/schema validation when loading overrides.

### SQLite compatibility review
- `database.py:init_db()` creates the legacy `users` table if absent, then inspects `PRAGMA table_info(users)`.
- It adds `completed_quizzes` and `beta_completed_lessons` only when absent, using additive `ALTER TABLE users ADD COLUMN` statements.
- The migration does not rename, drop, or rewrite existing learner progress columns.
- The beta ledger is read/written by column name; the legacy completed lessons, badges, coins, and chest indexes remain in their original positions because new columns are appended.
- `complete_beta_lesson()` uses `BEGIN IMMEDIATE` and an idempotent comma-separated ledger; it does not award XP, coins, chests, or badges.
- Existing regression test `test_existing_progress_survives_beta_column_migration` creates a legacy schema and asserts that existing completed lessons remain and the new columns are added.
- The preserved Botkeep test backup inspected on 2026-11-11 was reported to lack `beta_completed_lessons`; its SQLite integrity check was `ok`. The migration test is encouraging, but the live backup must only be tested on a separate disposable copy before any live migration.

### Remaining blockers
1. Resolve the separate Lesson 13 status/gate inconsistency recorded in `COURSE4_LESSON13_BETA_GATE_CONSISTENCY_FINDING_2026-11-11.md`.
2. Run the full suite on the exact release candidate, not just structural checks.
3. Run migration and restore rehearsal against a copy of the preserved Botkeep backup; never rehearse against the live DB.
4. Wait for Botkeep support to confirm Node17 staging recovery before attempting import or deployment.
5. Rotate the exposed Telegram token securely before further user-facing testing.

### Non-actions
No source file, quiz, database, Botkeep runtime, or production bot was changed. No PR was merged, no import/restore/redeploy was performed, and no live database migration was run.

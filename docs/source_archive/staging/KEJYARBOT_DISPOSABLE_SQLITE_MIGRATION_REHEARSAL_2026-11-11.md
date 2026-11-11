# KejyarBot — disposable SQLite migration and beta-ledger rehearsal

**Date:** 2026-11-11  
**Scope:** KejyarBot-Test backup only; disposable copies; no Botkeep runtime access.

## Immutable source archive verification

- Source archive: `botkeep-backup-a0beb5f8-16df-4fc7-be61-353821a8941b (3).tar.gz`
- Archive SHA-256: `5d75b7498a00c22d1f9f167250b3c4103fffca6e24d378769ef89fe31c8f7059` — matched the preserved verification record.
- Embedded `kejyar.db` SHA-256: `88eeae02eb8ef4d274cf3bd7960325c765149a73febff09c1f8255cd606b5c46`.
- Archive path/link safety inspection: 1,014 members; no unsafe paths or links.
- Baseline SQLite `PRAGMA integrity_check`: `ok`.
- Baseline tables: `users` (1 row), `speech_quota` (0 rows).
- The original archive and extracted baseline copy were not modified.

## Disposable migration rehearsal

The candidate `database.py:init_db()` schema-creation and additive-column SQL sequence was rehearsed on a separate disposable database copy. No live or original database was opened for writing.

- Pre-existing user columns: `user_id, score, xp, level, correct_answers, completed_lessons, badges, tests, coins, chests, completed_quizzes`.
- Added missing column: `beta_completed_lessons`.
- Existing user values across every pre-existing column were identical before and after migration.
- Existing `completed_quizzes` value remained intact.
- New `beta_completed_lessons` defaulted to an empty string.
- Table row counts remained unchanged.
- Re-running the migration did not add duplicate columns or fail (idempotent).
- Post-migration SQLite `PRAGMA integrity_check`: `ok`.

## Disposable beta-progress rehearsal

A second disposable copy was used to exercise the beta-ledger transaction pattern.

- First completion of a test-only lesson ID: `True`.
- Repeated completion of the same ID: `False` (idempotent).
- The beta ledger recorded the test lesson exactly once.
- Official reward/progress fields remained unchanged: `score, xp, tests, coins, chests, completed_lessons, badges, completed_quizzes`.
- Post-test SQLite `PRAGMA integrity_check`: `ok`.

## Boundaries and remaining checks

- These are isolated SQLite copy tests, not a live Botkeep migration or a full in-process deployment test.
- No `.env` content, Telegram token, or other secret was read or included.
- No Botkeep import, restore, restart, deployment, or live database write was performed.
- Botkeep Node17 written clearance is still required before any test-bot import.
- Candidate code must continue to pass the complete GitHub test suite before promotion.

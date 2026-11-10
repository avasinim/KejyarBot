# KejyarBot Botkeep active reward transaction and SQLite integrity-path review — 2026-11-10

## Scope and safety
Read-only inspection of `bot.py` and `database.py` on GitHub `main`, focused on whether the active Botkeep entry point uses atomic/idempotent reward paths and whether older reward helpers found in the database module are part of the active runtime. No code, database, Botkeep setting, deployment, or process was changed.

## Findings
1. The active `bot.py` lesson-completion handler calls `complete_lesson_with_rewards(user_id, lesson)` for normal lessons and `complete_beta_lesson(user_id, lesson)` for beta-review lessons. Beta-review completion explicitly does not award XP, coins, chests, or badges.
2. The active quiz-submission handler calls `complete_quiz_with_rewards(user_id, lesson)`. Its in-memory `answer_in_progress` guard prevents overlapping callback submissions in one process; the database ledger independently prevents repeated quiz rewards after a retry/restart.
3. The corresponding database functions use `BEGIN IMMEDIATE`, check the stored completion ledger, update completion and rewards in the same transaction, commit on success, roll back on exceptions, and close connections in `finally`. This is a positive idempotency/atomicity design for the inspected active lesson and quiz reward paths.
4. Legacy helpers such as `add_score`, `add_coins`, `add_chest`, and `complete_lesson` remain defined in `database.py`, but a direct call-site scan of the active `bot.py` found no calls to these legacy helpers. The active handler instead uses the atomic reward functions. The separately executable `bot_backup.py` remains a legacy entry point and should not be selected as the intended Botkeep start command.
5. SQLite connections in the inspected database module use a 10-second connection timeout and explicit close/commit/rollback handling. No explicit WAL journal mode, synchronous setting, busy-timeout pragma, or online backup routine was found in the inspected module; SQLite defaults therefore apply unless configured externally.
6. Synchronous SQLite work is invoked directly from asynchronous Telegram handlers. A database lock or slow disk can therefore block the event loop while the SQLite call waits (up to the configured 10-second timeout). This is an operational responsiveness risk, not evidence of current corruption or a Botkeep outage.
7. The database file remains `BASE_DIR / "kejyar.db"`, inside the project source directory. Its actual live Botkeep persistence and backup status remain unverified; this note does not imply the database is present, intact, or backed up.

## Limits and safe next steps
The review covers source code only. It cannot inspect live Botkeep SQLite contents, filesystem persistence, journal files, process state, backups, or runtime latency. Do not run restore, restart, redeploy, or a second poller while the stuck Botkeep restore remains unresolved. Before any later restart/update, obtain a completed successful backup and an independent copy.

## Result
The active lesson and quiz reward paths are atomic/idempotent in source. Legacy non-atomic reward helpers exist but were not called by the inspected active `bot.py`. No production changes made.

# SQLite persistence and startup safety audit — 2026-11-14 18:01Z

Branch: `release/main-based-reconciled-2026-11-11`
Inspected source revision: `53393395224ffb6f676c660d51e0e6f7cdda425c`
Scope: read-only inspection of `database.py`, `bot.py`, `course_runtime.py`, `latin_course_runtime.py`, `arami_course1_runtime.py`, and the Arami manifest.

## Verified findings

1. `database.py` resolves `KEJYARBOT_DB_PATH` once at import time. If the variable is absent, it falls back to `<project directory>/kejyar.db`. A configured-but-empty value raises an error.
2. `init_db()` creates the parent directory and calls `sqlite3.connect(DB_NAME)`; it then creates the `users` table if absent and adds missing `completed_quizzes` and `beta_completed_lessons` columns. Therefore, if the selected path points to a missing file, SQLite can create a new empty database. There is no explicit existence/identity check for an original learner database before this operation.
3. The inspected `database.py` contains no explicit `PRAGMA journal_mode=WAL`, no explicit journaling-mode configuration, and no application-level SQLite backup/restore routine. It uses SQLite's default connection behavior unless the database or environment has been configured otherwise. This does not establish the journal mode of any existing learner database.
4. Database operations use explicit commits/rollbacks and close connections. Several progress/reward operations use `BEGIN IMMEDIATE`; this is a positive transactional safeguard, but it does not replace a verified backup or correct persistent path.
5. `bot.py` loads `.env` before importing `database.py`, checks Telegram credentials, validates all active course runtime data, and only then calls `init_db()`. This ordering protects against creating a database when credentials or course data are invalid, but it does not protect against a missing original DB at a valid path.
6. The runtime validator checks the six active courses and expected lesson counts, including Arami's 21 lessons, daily conversation 42, unified orthography 66, grammar 50, and the two Latin courses 12 each. Arami's dedicated Lesson 1 and Lesson 5 source/interaction banks are explicitly loaded and checked before database initialization.
7. No source changes, database changes, deployment actions, panel actions, starts, restarts, restores, or token access were performed during this audit.

## Required safety gate before any bot start

- Identify the exact original learner database file from the authoritative source; do not infer a path or accept a newly-created empty file.
- Keep the source bot quiescent before copying the database.
- Preserve the database together with any applicable `-wal` and `-shm` sidecars during a consistent transfer; inspect the actual journal mode before deciding the exact transfer procedure.
- Verify the restored file's SQLite integrity and learner/progress record counts without modifying the original.
- Configure `KEJYARBOT_DB_PATH` to the verified persistent location, and add a fail-closed existence/identity guard before allowing `init_db()` to run. Do not let the current fallback silently initialize an empty learner database.
- Only after those checks, and after confirming that no other instance is polling with the same Telegram token, consider a single controlled start.

## Current deployment conclusion

The source course runtime is strongly guarded, but the SQLite startup path is not yet fail-closed against a missing original learner database. Deployment remains blocked on locating and verifying the original database and its persistent destination. This audit is append-only and does not replace earlier operational records.

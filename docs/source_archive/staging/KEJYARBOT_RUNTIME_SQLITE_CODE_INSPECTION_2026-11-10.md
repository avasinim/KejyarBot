# KejyarBot Runtime and SQLite Code Inspection — 2026-11-10

## Inspection scope
Read-only source inspection of bot.py, database.py, tests/test_database.py, and tests/test_railway_persistent_db.py on branch infra/railway-persistent-db-2026-11-10. No source code was changed and no database was opened or modified.

## Confirmed implementation details
1. Environment load order: bot.py imports database before its manual .env parser. database.py captures KEJYARBOT_DB_PATH into module-level DB_NAME during import. A DB path supplied only in the local .env file therefore does not update DB_NAME. Host-injected variables set before Python starts are available at import time and are not affected by this ordering issue.
2. Database initialization: init_db() creates the parent directory, creates the users table if missing, adds the completed_quizzes and beta_completed_lessons columns when absent, commits on success, rolls back on failure, and closes the connection.
3. SQLite connections: the inspected database functions use a 10-second connection timeout and explicitly close connections. Several state transitions use BEGIN IMMEDIATE to serialize read-modify-write operations.
4. Atomic reward paths: complete_lesson_with_rewards() and complete_quiz_with_rewards() update completion ledgers, progress/reward values, and level in one transaction. Existing tests exercise repeat completion and concurrent claims to ensure rewards are not granted twice.
5. Persistent path regression coverage: tests/test_railway_persistent_db.py confirms that init_db() can create a missing parent directory for a DB path. It does not test persistence across a Railway redeploy or volume recreation.
6. Backup/restore gap: no backup/restore implementation, integrity-check routine, or backup/restore round-trip test was found in the inspected files. This remains an operational gap, not proof that no backup exists outside the inspected repository.
7. Startup sequence: main() validates activated course runtime, initializes the database, checks for TELEGRAM_BOT_TOKEN or BOT_TOKEN, builds the Telegram application, registers handlers, and starts polling. A missing token causes an explicit startup error. The code inspection does not verify whether a valid token exists in the hosting environment.
8. Single-poller requirement: the app uses run_polling(); the hosting process must be unique for this token. Do not start a second polling process while Botkeep's actual process state remains unresolved.

## Priority
- P0 — Recovery evidence: identify the authoritative Botkeep SQLite backup and verify it on an isolated copy before provisioning or switching production storage.
- P1 — Configuration correctness: before a local .env-only database path is relied upon, load .env before importing database, or resolve the DB path after environment loading. This is not required for a path injected by Railway before process startup.
- P1 — Operational recovery test: after obtaining a verified backup and a persistent volume, perform an isolated restore, run SQLite PRAGMA integrity_check, validate schema and user/progress counts, then verify persistence across a controlled restart/redeploy.
- P2 — Regression coverage: add a backup/restore round-trip test using a temporary database and ensure it never touches production data.

## Explicitly not done
No code edits, PR merge, Railway staged-change acceptance, volume provisioning, database copy/restore, Botkeep retry/cancel, service restart, deployment, or Telegram polling was performed.
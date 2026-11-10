# KejyarBot — Railway deployment runbook

## Scope and safety

This runbook prepares a Railway deployment without changing the production Botkeep service.
Do not run two Telegram polling instances with the same bot token. Do not launch the Railway
poller until Botkeep is confirmed stopped and the SQLite backup has been inspected and verified.

The Railway service must remain on the approved source branch. Course content and draft review
branches are outside this infrastructure change.

## Required Railway configuration

- Runtime: Python 3.12 (the repository dependency is python-telegram-bot 22.x).
- Build: Railpack automatic Python build using requirements.txt.
- Start command: `python bot.py`.
- Persistent volume mount: `/data`.
- Environment variable: `KEJYARBOT_DB_PATH=/data/kejyar.db`.
- Existing secret: `TELEGRAM_BOT_TOKEN` (do not print, copy into logs, or commit it).

The database module now reads KEJYARBOT_DB_PATH and creates its parent directory before
initializing SQLite. If the variable is absent, local development continues to use the
historical project-local kejyar.db path.

## Safe migration sequence

1. Confirm Botkeep support has clarified whether its paused GitHub update is recoverable.
2. Obtain a verified SQLite backup from the currently authoritative Botkeep data directory.
3. Inspect the backup read-only: SQLite integrity_check, schema, row counts, and file size.
4. Create and attach a Railway persistent volume mounted at /data.
5. Configure KEJYARBOT_DB_PATH and the start command; review all staged changes before commit.
6. Restore the verified database backup to /data/kejyar.db before starting the poller.
7. Confirm Botkeep is stopped, then launch exactly one Railway polling instance.
8. Verify Telegram /start, existing user progress, lesson completion, quiz ledger, and reward state.
9. Keep Botkeep data and backup untouched until the Railway service has passed acceptance checks.

## Explicit non-goals

- No automatic database copy or overwrite.
- No production deployment from this branch without review.
- No merge of Course 3 Lessons 67–68 draft PR.
- No change to lesson content or user progress schema beyond the existing idempotent init_db migrations.

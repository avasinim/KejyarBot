# First-start clarification and SQLite initialization decision — 2026-11-14

Branch: `release/main-based-reconciled-2026-11-11`
Inspected source revision: `53393395224ffb6f676c660d51e0e6f7cdda425c`
Scope: read-only source inspection plus owner clarification received in this conversation.

## Owner clarification

The project owner states that KejyarBot is unused, no learner has used it, and this is intended to be its first start. On that stated premise, there is no prior learner-progress database that must be migrated or restored. The earlier operational gate requiring discovery of an existing learner database is therefore not applicable if the premise is accurate.

## Source facts rechecked

1. `.gitignore` excludes `.env`, `kejyar.db`, SQLite database files, and SQLite WAL/SHM sidecars. The repository is not intended to carry the live database or Telegram token.
2. `database.py` defaults to `<project directory>/kejyar.db` when `KEJYARBOT_DB_PATH` is absent. `init_db()` creates the parent directory and initializes the users table and required progress columns.
3. A first-run empty database is technically valid for an unused bot. SQLite creates the file when `init_db()` connects to a missing path.
4. The configured database path must still be on storage that survives the host's app restart/redeploy lifecycle. This persistence property has not been verified for the current Altare app.
5. `bot.py` validates credentials and active course runtime before calling `init_db()`; after that it starts Telegram polling. Thus a valid first start will create an empty learner database before polling begins.

## Updated decision

- Do not require recovery of a nonexistent learner database if the owner's statement is correct.
- Do not restore an old database or use Emergency Recovery merely to create a first-run database.
- Before first Start, confirm the app's intended persistent filesystem location and ensure `KEJYARBOT_DB_PATH` is either unset (project-local default) or points to that verified persistent location.
- Keep the first Start to one active polling instance only. Do not start Botkeep and Altare simultaneously with the same Telegram token.
- After the first successful start, verify the console reports successful Telegram initialization/polling and verify that the SQLite file is created at the intended persistent path. Do not expose the token in logs or screenshots.

## Current blocker remains separate from SQLite migration

The owner's clarification removes the need to locate old learner progress. It does not prove that the Altare app's source files have been uploaded or that the app's filesystem is persistent. The last panel observation recorded in the previous audit was `Stopped / Node down`, with the file manager not showing the complete project package. No Start, Restore, Emergency Recovery, upload, or settings change was performed in this audit.

This note supplements, and does not overwrite, earlier append-only operational audits.

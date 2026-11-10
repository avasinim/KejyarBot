# KejyarBot Database Backup/Restore Readiness Check — 2026-11-10

## Scope
Read-only inspection of the infrastructure branch `infra/railway-persistent-db-2026-11-10`, focused on SQLite persistence, backup/restore readiness, startup configuration, and the existing database tests. No database was opened, copied, migrated, restored, or modified. No service operation or deployment was triggered.

## Verified findings
- `database.py` selects `DB_NAME` at module import from `KEJYARBOT_DB_PATH`, falling back to the repository-local `kejyar.db`.
- `bot.py` imports `database` before it loads its local `.env` file. Therefore a DB path defined only in local `.env` is too late for the already-imported `database.DB_NAME`. Host-injected environment variables present before Python starts are read correctly.
- `init_db()` creates the parent directory and creates/upgrades the `users` table. It does not implement a backup or restore operation.
- `tests/test_railway_persistent_db.py` verifies creation of a missing parent directory for a configured database path. It does not verify that existing user data survives backup/restore, redeployment, volume replacement, or migration.
- `tests/test_database.py` covers schema initialization, idempotent schema upgrade, concurrency, progress/reward ledgers, and chest/badge operations. The inspected tests do not provide a backup/restore round-trip or SQLite integrity-check workflow.
- The inspected `.gitignore` excludes `.env`, `kejyar.db`, SQLite files, and WAL/SHM sidecars. This is appropriate for avoiding accidental credential/database commits, but does not itself create a backup.
- The inspected README documents local startup and test commands but does not define an operational backup/restore procedure.
- Railway production remains offline with no active deployment. The proposed `kejyarbot-data` volume remains staged-create at `/data`; no live volume or restored database was verified.
- The staged Railway source branch is `infra/railway-persistent-db-2026-11-10`, while the live source branch remains `main`. Do not commit these staged changes until branch strategy and database recovery are resolved.
- Existing CI success (487 tests, 11 skipped, from the prior inspection) does not prove Telegram connectivity or recovery of real user progress.

## Risk assessment
**High operational risk: database recovery is not yet demonstrated.** The code can point SQLite at a mounted path, but no verified source backup, restore drill, or live persistent volume was established in this inspection.

## Safe next steps (not executed)
1. Obtain and identify the authoritative Botkeep SQLite database backup through the platform owner/support process; do not infer that a local or repository copy is current.
2. Preserve the original backup unchanged and verify its SHA-256 before any test restore.
3. Restore only into an isolated test location, never over the original source; run SQLite `PRAGMA integrity_check`, inspect schema/table counts, and compare key user/progress totals against a trusted baseline where available.
4. Add automated backup/restore round-trip tests and a documented recovery procedure. For a live SQLite database, use SQLite's online backup API or a coordinated clean shutdown; do not assume copying only the main `.db` file is safe when WAL mode is active.
5. Only after the backup is verified, configure and provision persistent storage, confirm the DB path points inside the mounted volume, and test restart/redeploy persistence before enabling Telegram polling.
6. Ensure only one active polling process uses the Telegram bot token.

## Safety boundary
No Botkeep restore/retry/cancel action, Railway accept-deploy/restart/deploy, GitHub merge, Telegram polling, or live database mutation was performed.

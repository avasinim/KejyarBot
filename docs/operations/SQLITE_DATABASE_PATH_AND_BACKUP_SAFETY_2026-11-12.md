# SQLite database path and backup safety checkpoint

Date: 2026-11-12
Branch: `fix/load-env-before-database-2026-11-12`
Related pull request: #153 — `fix: load .env before resolving database path`

## Purpose

Record the production data-safety findings discovered while reviewing the startup environment-order fix. This document is a preservation checkpoint, not permission to change Botkeep, restore a database, or restart the workload.

## Verified source behavior

- `bot.py` resolves `BASE_DIR` and calls `load_dotenv(BASE_DIR / ".env")` before importing `database.py`.
- `database.py` resolves `KEJYARBOT_DB_PATH` at module import time. If the variable is absent, it falls back to `kejyar.db` beside `database.py`.
- The host's pre-existing environment variables take precedence because `load_dotenv` is called without `override=True`.
- `init_db()` creates the parent directory and opens the configured path, then creates/upgrades the schema. It does not verify that the path points to the intended populated production database.
- The database module does not set SQLite WAL mode. Do not assume the live database is in WAL mode or that copying a single file is a sufficient backup strategy without checking the live journal state.
- Existing source tests cover import-time environment selection and source ordering. They do not inspect Botkeep's actual Environment settings or prove which database file the live workload currently opens.

## Mandatory production verification gate

Before any source update or database operation on Botkeep:

1. Obtain a fresh completed Botkeep backup of the workload and database, and download an independent copy.
2. In Botkeep Environment, inspect the value *presence and path* of `KEJYARBOT_DB_PATH` without copying secrets into chat or logs. Do not expose Telegram tokens or other credentials.
3. If the variable is absent, establish from the live file listing and runtime configuration whether the intended database is the project-root `kejyar.db`. If the variable is present, verify that its path resolves to the existing populated database, not a newly created or empty file.
4. Confirm the target file exists, its size and modification time are plausible, and the expected `users` table and learner records are present using a read-only inspection or an isolated copy. Do not run `init_db()` against an unverified path as a diagnostic.
5. If the effective path is uncertain, empty, missing, or inconsistent with the known learner database, stop. Do not start, restart, import, migrate, overwrite, or restore.

## SQLite backup guidance

- Prefer SQLite's online backup API (`sqlite3.Connection.backup()`) to produce a transactionally consistent copy while the source database is in use.
- Run the backup to a separate destination file; never use the source database path as the destination.
- After backup, open the destination independently and run `PRAGMA integrity_check`. Require the result `ok`.
- Record the source path, destination path, backup timestamp, file size, integrity-check result, and the Botkeep workload/revision identity in the preservation log.
- Keep the original Botkeep backup and independent downloaded copy unchanged. A new SQLite snapshot supplements them; it does not replace them.
- Do not copy only the main database file if live inspection reveals WAL mode or sidecar files. Use the SQLite backup API or a documented, quiesced backup procedure.
- Do not put `.env`, tokens, credentials, `.botkeep`, or the production database into Git.

Illustrative Python pattern for a controlled backup utility (not executed against production):

```python
import sqlite3

with sqlite3.connect(source_path, timeout=10) as source:
    with sqlite3.connect(destination_path) as destination:
        source.backup(destination)

with sqlite3.connect(destination_path) as check:
    result = check.execute("PRAGMA integrity_check").fetchone()[0]
    if result != "ok":
        raise RuntimeError(f"SQLite backup integrity check failed: {result}")
```

## Current status and limitations

- The code ordering fix and two path-selection regression tests are on the isolated PR branch.
- A further subprocess test verifies that `database.DB_NAME` uses an explicit environment path and otherwise retains the project-local default.
- These tests have not been confirmed by CI for the latest PR head at the time this checkpoint was written.
- No Botkeep Environment value, live database path, database contents, WAL state, or new backup has been independently verified from the hosting panel.
- No production files, database, secrets, or Botkeep settings were changed. No deployment, restart, restore, or migration was performed.

## Next safe action

Obtain the fresh Botkeep backup and independently verify the live effective database path before considering any import or restart. Keep the PR in draft until CI is green and the production path/backup gates are satisfied.

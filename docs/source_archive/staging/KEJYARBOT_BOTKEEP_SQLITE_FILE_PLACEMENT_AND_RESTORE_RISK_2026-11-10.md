# Botkeep SQLite file-placement and restore-risk review — 2026-11-10

## Scope
Read-only inspection of the repository default branch `main` for Botkeep deployment compatibility and SQLite data placement. No Botkeep panel operation, deployment, restart, restore, database mutation, or production code change was performed.

## Verified source facts
- `README.md` documents Python 3.10+, installation with `python -m pip install -r requirements.txt`, and startup via `python bot.py`.
- `requirements.txt` contains `python-telegram-bot>=22,<23`.
- `bot.py` defines `BASE_DIR = Path(__file__).resolve().parent`, loads `.env` from that directory, and invokes `validate_activated_course_runtime()`, `init_db()`, then reads `TELEGRAM_BOT_TOKEN` or `BOT_TOKEN`, builds the Telegram application, and calls `app.run_polling()`.
- `database.py` defines `BASE_DIR = Path(__file__).resolve().parent` and `DB_NAME = str(BASE_DIR / "kejyar.db")`. SQLite is therefore placed inside the application source directory, not a separately configured persistent-data directory.
- `database.py` contains additive `CREATE TABLE IF NOT EXISTS` / `ALTER TABLE ... ADD COLUMN` initialization logic; the inspected initialization does not drop tables or recreate the database.
- `.env.example`, `Procfile`, `runtime.txt`, and `pyproject.toml` are absent from the inspected `main` root (GitHub returned 404 for these paths).

## Operational implications and risks
- Because the live SQLite file path is inside the source/project directory, any restore/import operation that replaces or cleans that directory could potentially replace, omit, or remove `kejyar.db`. This is a conditional filesystem risk; the Botkeep restore implementation and actual server filesystem were not accessible, so no claim is made that Botkeep has deleted or will delete the database.
- The repository `.gitignore` exclusion of `kejyar.db` prevents normal Git tracking but is not a backup and does not establish that Botkeep stores the file persistently.
- The current code does not expose a configurable external SQLite path such as `KEJYARBOT_DB_PATH`; changing this would require a reviewed code change and a migration/backup plan. No such change was made.
- Startup initializes the database before validating that the Telegram token exists. This means a missing token can still cause the local database file/schema initialization before startup exits; it does not itself imply data loss.
- The `.env` loader in `bot.py` runs after importing `database.py`; currently harmless for DB placement because the database path is hardcoded, but it means a future DB-path setting read at module import time would need to be loaded earlier or injected by the host environment.

## Safe recovery requirements
1. Keep the stuck Botkeep GitHub restore operation untouched until Botkeep support confirms it is resolved and states whether project files and untracked runtime files (especially `kejyar.db`) are preserved.
2. Before any restart, restore, sync, or redeploy, obtain a completed successful Botkeep backup and an independent downloadable copy; verify the backup includes the SQLite database, not just source files.
3. If Botkeep cannot guarantee persistent storage for `kejyar.db`, first plan a controlled migration to a persistent data location, with a verified pre-migration backup and a tested restore path. Do not improvise this during the current incident.
4. After support confirms the restore operation is cleared, inspect the Botkeep file manager and Console read-only first; verify the project root, Python runtime, start command, token secret presence (without displaying its value), and whether `kejyar.db` exists and has a plausible non-zero size before any restart.
5. Never start a second polling process while the existing Telegram token may still be used by another active process.

## Explicit limitations
- No authenticated Botkeep panel, filesystem, Console, environment-secret view, backup artifact, or support-ticket status was available to this inspection.
- No evidence was obtained that the production SQLite database is currently intact, backed up, or recoverable.
- No changes were made to the Botkeep server or production source.

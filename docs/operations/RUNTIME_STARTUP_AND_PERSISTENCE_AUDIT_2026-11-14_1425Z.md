# Runtime startup and persistence requirements audit — 2026-11-14 14:25Z

## Audited source
Repository: `avasinim/KejyarBot`
Revision: `db2016f5bc687560ef7ccaca80e0a8f174791443`
Release branch at time of audit: `release/main-based-reconciled-2026-11-11`

## Verified runtime requirements
- `requirements.txt` contains:
  - `python-telegram-bot>=22,<23`
  - `python-dotenv>=1,<2`
- README instructs Python 3.10 or newer, install with `python -m pip install -r requirements.txt`, then run `python bot.py`.
- `bot.py` loads a root `.env` file before importing `database.py`.
- Startup reads `TELEGRAM_BOT_TOKEN`, falling back to legacy `BOT_TOKEN`; it raises a clear error if both are missing.
- Startup calls `init_db()` before constructing the Telegram application and starting polling.
- `database.py` supports `KEJYARBOT_DB_PATH`. If absent, it defaults to `kejyar.db` in the project directory. If configured, it resolves that path and creates the parent directory during `init_db()`.
- Root `.gitignore` excludes `.env` and SQLite database/journal files.

## Operational implications
- A correct deployment needs a protected host environment variable named `TELEGRAM_BOT_TOKEN` (or legacy `BOT_TOKEN`); it must not be committed to Git.
- To preserve learner progress across redeploys/restarts, `KEJYARBOT_DB_PATH` must point to a host-mounted persistent storage location. Merely setting a path inside an ephemeral application filesystem is not persistence.
- Startup command should execute `python bot.py` from the application root, after dependencies are installed.
- This is source-level configuration evidence only. It does not verify that Altare exposes the required environment variables or persistent mount correctly, nor that Botkeep/Altare have deployed this revision.

## No changes performed
No host variables, secrets, startup commands, storage mounts, database files, source files, or provider settings were changed. No Start/Restart or deployment action was taken.

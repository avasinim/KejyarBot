# KejyarBot Main-Branch Database Path Configuration Finding — 2026-11-10

## Verified source comparison
- `main` commit: `7db20f242087e3eb9149e2e788f6c20529870f32`.
- `main:database.py` blob: `812df0aeb6dba9b8cf33e7582ec677e509f9462d`.
- PR #141 head branch `infra/railway-persistent-db-2026-11-10`: `database.py` blob `c7685d515f58e2799d4d1d2397897217d48738de`.

## Finding
`main:database.py` sets `DB_NAME = str(BASE_DIR / "kejyar.db")` and does not read `KEJYARBOT_DB_PATH`. The PR #141 version adds `os.environ.get("KEJYARBOT_DB_PATH", ...)` and creates the parent directory in `init_db()`.

Therefore the Railway persistent-volume environment variable and mount plan are not supported by the currently inspected main-branch database module. They work only if the corresponding PR code is included in the deployed source. Deploying main with only the Railway variable/volume configuration would continue writing to the project-local `kejyar.db`, not the intended `/data/kejyar.db`.

## Additional ordering note
`bot.py` imports `database` before it reads its local `.env` file. Since the PR branch reads `KEJYARBOT_DB_PATH` at module import time, a path override defined only in `.env` is also too late; host-injected environment variables (such as Railway variables set before process start) are available in time. Local `.env` path support would require loading dotenv before importing `database`, or resolving the path at connection time.

## Safety / action status
No source was changed, no PR was merged, no Railway patch was accepted, no volume was provisioned, and no deployment/restart occurred. Existing data has not been copied or modified.

## Required gate before deployment
1. Ensure the exact DB-path implementation is part of the deployed commit.
2. Verify the authoritative Botkeep SQLite backup and integrity.
3. Restore it to the persistent mount and verify row counts/application reads before starting the bot.
4. Confirm the old Botkeep poller is stopped before starting another poller with the same Telegram token.
# KejyarBot Persistent-Database Regression Test Coverage Gap — 2026-11-10

## Verified test
`tests/test_railway_persistent_db.py` on PR #141 patches `database.DB_NAME` directly to a temporary path, calls `init_db()`, and checks that the parent directory and SQLite file are created.

## Coverage gap
The test does not verify that `KEJYARBOT_DB_PATH` is read from the process environment, that a missing variable falls back to the local database path, or that the bot's `.env` loading order works. It therefore tests directory creation after `DB_NAME` is already patched, not the complete configuration path from environment variable to SQLite connection.

## Related verified code behavior
`bot.py` imports `database` near the top of the module, before its manual `.env` loader executes. PR #141's `database.py` reads `KEJYARBOT_DB_PATH` at import time. Host-injected variables are available before import, but a value present only in `.env` is not available when `DB_NAME` is initialized.

## Recommended test cases before production use
1. Set `KEJYARBOT_DB_PATH` in `os.environ`, reload/import `database`, and assert the selected DB path.
2. Remove the variable and assert the default project-local path.
3. Verify `.env`-only override behavior after correcting import order or moving path resolution to connection time.
4. Open the configured database, write a sample user record, reopen it, and verify persistence at the configured location.

No code, tests, runtime settings, or user data were changed by this audit.
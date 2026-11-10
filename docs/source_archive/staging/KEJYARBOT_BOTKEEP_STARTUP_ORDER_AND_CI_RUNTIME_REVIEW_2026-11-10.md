# Botkeep startup order and CI/runtime compatibility review — 2026-11-10

## Scope
Read-only review of `main` startup sequence, README runtime guidance, and the Python GitHub Actions workflow. No Botkeep server action, production code edit, or deployment was performed.

## Verified findings
- README states Python 3.10 or newer and gives `python -m pip install -r requirements.txt` followed by `python bot.py`.
- `.github/workflows/python-checks.yml` currently configures only Python 3.12. It installs `requirements.txt`, runs `compileall`, then discovers and runs the unittest suite. This workflow does not demonstrate compatibility on Python 3.10 or 3.11, nor does it test Botkeep's actual runtime/container.
- `requirements.txt` specifies `python-telegram-bot>=22,<23`; this is a version range rather than a fully pinned lockfile.
- In `main()`, the order is: validate activated course runtime; initialize SQLite via `init_db()`; then read `TELEGRAM_BOT_TOKEN` or `BOT_TOKEN`; then build the Telegram application and start polling.
- Therefore, if the token is absent but course validation succeeds, startup still initializes/creates the local SQLite database before raising the missing-token error. This is not itself evidence of data loss, but it means a failed startup can still create a database file.
- The runtime validator loads active course manifests and question-bank assets before DB initialization; a missing/invalid activated course asset can stop startup before the database is initialized.
- The inspected current main commit SHA is `7db20f242087e3eb9149e2e788f6c20529870f32`. No associated PR-triggered workflow runs were returned by the GitHub commit-workflow lookup, so this review does not claim a current successful CI run for that main commit.

## Botkeep deployment implications
- Verify the Botkeep Python runtime explicitly rather than assuming README's broad Python 3.10+ statement is proven by CI.
- Verify the configured start command is `python bot.py` from the project root.
- Confirm the token secret is present in Botkeep Environment without exposing its value.
- Because SQLite is stored beside source files, verify `kejyar.db` and a completed independent backup before any operation that can replace project files.
- Do not restart or redeploy while the Botkeep GitHub restore operation remains stuck.

## Limitations
- No Botkeep panel, runtime console, environment-secret view, live filesystem, backup artifact, or support ticket status was accessible.
- No claim is made that the live Botkeep instance currently starts, that its database is intact, or that the current main commit has passed CI.
- No source code, database, or hosted service was changed.

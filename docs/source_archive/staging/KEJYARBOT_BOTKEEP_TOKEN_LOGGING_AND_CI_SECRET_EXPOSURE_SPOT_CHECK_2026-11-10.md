# KejyarBot Botkeep token logging and CI secret-exposure spot check — 2026-11-10

## Scope
Read-only spot check of the active and legacy bot entry points and the tracked GitHub Actions Python-check workflow. No token values, Botkeep secrets, or runtime logs were accessed. No code, workflow, deployment, Botkeep setting, process, or database was changed.

## Findings
- In the inspected active `bot.py`, the token is read from `TELEGRAM_BOT_TOKEN` or `BOT_TOKEN` and passed to `Application.builder().token(token)`. The inspected logger messages do not explicitly print or interpolate the token; the startup log only says Telegram initialization succeeded and polling is starting.
- In the inspected legacy `bot_backup.py`, the token is read from `TELEGRAM_BOT_TOKEN` and passed to the Telegram application builder. The scanned lines do not explicitly log or print the token.
- The tracked `.github/workflows/python-checks.yml` has `contents: read` permissions, checks out source, installs requirements, runs compileall and unittest, and does not define or inject Telegram token secrets in the inspected workflow.
- The entry points use standard Python logging, including exception logging in active handlers. This spot check found no explicit token logging, but it is not a complete audit of every dependency, every possible exception payload, GitHub Actions history, or external log collector.
- The workflow runs on pushes to configured branches and pull requests targeting main; it uses Python 3.12. This does not validate Botkeep's live Python version or deployment configuration.

## Limits and safe next steps
This cannot establish whether a token has ever been committed in Git history, appeared in external logs, or is configured correctly in Botkeep. No live secret value was requested or exposed. If the token may have been disclosed anywhere, rotate it through the appropriate secure control plane; do not paste it into chat or commit it.
The unresolved Botkeep restore remains a stop condition: do not restart, retry, redeploy, or start another poller until support resolves it and a completed successful database backup plus independent copy are verified.

## Result
No explicit token-print/log statement was found in the inspected entry points; the inspected CI workflow does not inject a Telegram secret. This is a limited source/workflow spot check, not a historical credential scan or live-hosting verification.

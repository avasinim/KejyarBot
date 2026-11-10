# KejyarBot Botkeep environment configuration and secret-file exposure review — 2026-11-10

## Scope and safety
Read-only review of the public GitHub `main` tree and selected source/configuration files for Botkeep environment-variable compatibility and accidental tracking of local environment files. No Botkeep panel, runtime, secret values, logs, or server filesystem were accessed. No production code, Botkeep setting, deployment, process, or database was changed.

## Findings
1. The tracked `.gitignore` explicitly excludes `.env`, Python bytecode/cache, virtual environments, `kejyar.db`, generic `*.db` files, and SQLite WAL/SHM sidecars.
2. The recursive GitHub tree for `main` contains no exact `.env`, `.env.example`, or other path matching the environment/secret/config filename scan used in this review. This is a current-tree observation only; it is not a full historical secret scan and does not prove no credential was ever committed.
3. README instructs operators to set `TELEGRAM_BOT_TOKEN` in a local `.env`, never commit or share the real token, and launch the active entry point with `python bot.py`. It also documents that host-provided environment variables take precedence over `.env`.
4. `bot.py` manually loads `.env` from `BASE_DIR` at module import. It skips blank lines, full-line comments and lines without `=`; splits on the first `=`; strips whitespace and surrounding quote characters; and uses `os.environ.setdefault`. Therefore Botkeep-injected environment variables win over local `.env` values. The parser is intentionally minimal, not a full dotenv implementation: inline comments, `export KEY=` syntax, escaped/multiline values and complex quoting are not handled reliably. Keep the production token as a simple single-line value and prefer Botkeep's Environment settings.
5. The startup code reads `TELEGRAM_BOT_TOKEN` first, then legacy `BOT_TOKEN`. If neither is present, it raises a clear startup error. The token value was not read or printed.
6. No `.env` file is tracked in the current tree, but this does not establish whether Botkeep has a correctly configured secret, whether its project root contains a local `.env`, or whether a token has ever appeared in Git history, logs, screenshots, or another system.
7. `requirements.txt` contains only `python-telegram-bot>=22,<23`; no external dotenv package is required by the active entry point because the minimal loader is implemented directly in `bot.py`.

## Operational implications
- Once Botkeep support has safely cleared the stuck restore operation, verify that the configured start command is `python bot.py`, the project root points to the directory containing `bot.py` and `requirements.txt`, and the Python runtime/dependency installation match the project.
- In Botkeep Environment, verify presence of `TELEGRAM_BOT_TOKEN` without exposing its value in chat, screenshots, logs, or commits. Avoid defining conflicting `TELEGRAM_BOT_TOKEN` and `BOT_TOKEN` values.
- Do not create, upload, expose, or inspect a plaintext production `.env` as part of this audit.
- Do not restart, retry restore, redeploy, or start another poller while the Botkeep infrastructure operation remains unresolved. Before any later restart/update, obtain a completed successful database backup and an independent copy.

## Limits
This review cannot determine live Botkeep Environment values, project root, start command, runtime version, process count, current filesystem, database integrity, backup availability, or support-ticket status. No claim is made that the live bot is configured correctly or that user data is safe/backed up.

## Result
Configuration-source review completed. No production changes made. No current-tree environment-file tracking issue found; historical secret exposure and live Botkeep configuration remain unverified.

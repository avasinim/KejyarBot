# KejyarBot — Active Entry Point vs Legacy Backup Entrypoint Review
Date: 2026-11-10
Scope: read-only entry-point and Botkeep start-command safety review.

## Files inspected
- `bot.py` on `main`, blob SHA `e825b7e277beda99e35cfa046cab349630ea2bfb`.
- `bot_backup.py` on `main`, blob SHA `dda80768a1bc2200725bc4b959f720b728d2f6fc`.
- `README.md` on `main`, blob SHA `b2bed9db6856ebf406012703ec19c933763e2d64`.

## Verified findings
1. README line 42 documents `python bot.py` as the launch command.
2. Current `bot.py` is the active entry point: it runs activated-course preflight validation, initializes the current database schema, accepts `TELEGRAM_BOT_TOKEN` or `BOT_TOKEN`, registers the current course handlers, and starts polling.
3. The repository also contains `bot_backup.py`, which is independently executable and calls `app.run_polling()`. It accepts only `TELEGRAM_BOT_TOKEN`, initializes the database, loads legacy `lessons.json` using a current-working-directory-relative path, and registers a smaller legacy handler set.
4. The backup file's legacy lesson-completion handler calls `complete_lesson()` and then calls `add_score()` / `add_chest()` without checking whether the lesson was already completed. If that legacy entry point is used, repeat taps may award points/chests again, unlike the active source's idempotent reward path. This is a source-level difference, not a claim that Botkeep is currently running it.
5. Both `bot.py` and `bot_backup.py` can start a Telegram polling process with a bot token. Running both concurrently with the same token risks Telegram getUpdates polling conflicts. No evidence is available about how many processes Botkeep currently has running.
6. The intended command from the repository README is `python bot.py`; the actual Botkeep panel start command cannot be inspected in this session.

## Operational recommendation
After Botkeep support clears the stuck restore operation and confirms filesystem stability, verify the configured start command is exactly `python bot.py` (with the correct project root) and not `python bot_backup.py`. Confirm there is only one active polling process for the token before starting or restarting anything.

## Boundaries
- No Botkeep setting, server, process, or database was accessed or changed.
- No source file was changed.
- This is a static repository review; it does not establish which entry point is configured or running in production.

# KejyarBot Botkeep Polling Defaults and Update Queue Review — 2026-11-10

## Scope
Read-only review of the active `bot.py` polling call and comparison with python-telegram-bot 22.x official documentation. No production code or Botkeep settings changed.

## Source facts
- Active code calls `app.run_polling()` without explicit arguments.
- `requirements.txt` allows `python-telegram-bot>=22,<23`; the exact installed patch version on Botkeep is unknown.
- The application builder does not call `concurrent_updates()`, and no custom update processor is configured in the inspected active code.
- The application does not register a custom error handler.

## PTB 22.x documented defaults and implications
- `run_polling()` defaults include `timeout=10` seconds for long polling, `bootstrap_retries=0` (no retry during bootstrap), and `drop_pending_updates=False` (do not discard pending updates). See official PTB Application docs: https://docs.python-telegram-bot.org/en/latest/telegram.ext.application.html
- PTB documents that when `concurrent_updates()` is not called, updates are processed one by one. This is consistent with the bot's stateful `context.user_data` quiz/session logic and avoids introducing parallel handler races by default. See official PTB ApplicationBuilder docs: https://docs.python-telegram-bot.org/en/stable/telegram.ext.applicationbuilder.html
- Polling errors are forwarded to registered application error handlers; without a custom handler, the application has no project-specific policy for classifying, alerting on, or recovering from them. PTB docs explain the forwarding path in `run_polling()`.

## Risk assessment
1. **Medium — bootstrap resilience:** with the documented default `bootstrap_retries=0`, a Telegram API/network failure during initial bootstrapping is not retried by PTB's polling bootstrap. Whether Botkeep subsequently restarts the process is unknown and must be checked in the panel/logs after the stuck restore is resolved.
2. **Low/intentional — sequential updates:** one-by-one processing is a sensible default for the current in-memory quiz state and sequential callback logic. Do not enable concurrent updates casually; first design/test per-user state isolation and DB contention.
3. **Positive — pending updates:** documented default `drop_pending_updates=False` preserves pending Telegram updates at startup rather than intentionally clearing them. The exact effective behavior should be confirmed against the installed PTB version and Botkeep runtime.
4. **Unknown — request timeouts:** builder-level request timeouts and actual package patch version are not explicitly pinned in the repository and cannot be inspected on Botkeep.

## Recommended later verification (read-only first)
- After Botkeep support confirms the restore operation is resolved, inspect the actual Console logs and installed PTB version.
- Confirm Botkeep process restart policy and whether a failed process is automatically restarted.
- Before any configuration change, test bootstrap failure/recovery behavior in a separate non-production bot/token or controlled test environment.
- Preserve sequential update processing unless a separately reviewed concurrency design is implemented.

## Limits and safety
- These are documented library defaults, not proof of the current Botkeep runtime configuration.
- No Botkeep panel access, process restart, deployment, Telegram polling, or database action was performed.

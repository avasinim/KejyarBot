# KejyarBot — Botkeep Polling Failure Recovery and Error Handling Review
Date: 2026-11-10
Scope: read-only source review for Botkeep-hosted KejyarBot. No Botkeep panel access, no runtime changes, no production source changes.

## Sources inspected
- `bot.py` on `main`, blob SHA `e825b7e277beda99e35cfa046cab349630ea2bfb`.
- `database.py` on `main`, blob SHA `812df0aeb6dba9b8cf33e7582ec677e509f9462d`.
- `requirements.txt` on `main`, blob SHA `8ed54d385f6f3c6180c376165b2097dcfcb62b54`.
- `.github/workflows/python-checks.yml` on `main`, blob SHA `cf03af7be9be09c83922987193de899520764af6`.
- python-telegram-bot v22 Application docs: https://docs.python-telegram-bot.org/en/latest/telegram.ext.application.html
- python-telegram-bot v22.0 ApplicationBuilder callback docs: https://docs.python-telegram-bot.org/en/v22.0/telegram.ext.applicationbuilder.html

## Verified findings
1. `main()` builds the application with `.post_init(log_polling_start)` and calls `app.run_polling()` without explicit polling arguments. The only registered lifecycle callback is `post_init`; no `post_stop` or `post_shutdown` callback is configured.
2. The project does not register an application-level PTB error handler with `app.add_error_handler(...)`. The only explicit exception logging found in `bot.py` is local handling around quiz delivery and selected catalogue operations. Some quiz delivery failures clear transient quiz state, log the exception, and re-raise; this does not provide a central error classification, operator alert, or recovery policy.
3. PTB v22 documentation states `run_polling` forwards polling errors to registered error handlers, with `update=None`. Since this project does not register one, it has no project-specific handler for those polling errors. Framework-level logging behavior is separate; this review does not claim that errors are completely unlogged.
4. PTB v22 `run_polling` defaults include `bootstrap_retries=0`, `timeout=10 seconds`, and `drop_pending_updates=False`. Because the source calls `run_polling()` with no overrides, those defaults apply if the installed dependency is a compatible v22 release. `requirements.txt` permits any `python-telegram-bot>=22,<23`, so the exact deployed patch version remains unknown.
5. The PTB docs describe `post_stop` and `post_shutdown` as optional callbacks invoked during the graceful `run_polling` shutdown sequence. Their absence is not itself a defect for this bot's current synchronous SQLite connection-per-operation pattern; it simply means there is no custom shutdown hook.
6. `database.py` opens and closes SQLite connections per operation and uses a 10-second connection timeout. No long-lived connection is configured for shutdown cleanup. SQLite still resides at `BASE_DIR / kejyar.db`; the independent file-placement/restore risk is covered in the prior Botkeep SQLite audit note.
7. The main runtime source contains no `send_photo` or `send_document` calls in the inspected `bot.py`; lesson infographic delivery is explicitly a no-op. Therefore, no image/document transmission failure path was identified in this active entry point during this review.
8. The CI workflow checks Python 3.12 only; it does not establish the Python runtime version actually selected by Botkeep. This is consistent with the earlier runtime compatibility review.

## Operational interpretation
- These source findings do not establish the cause of the current Botkeep server outage or stuck GitHub restore operation.
- A bootstrap Telegram/API failure can fail the process's initial polling startup without PTB retrying at the default `bootstrap_retries=0`. Whether Botkeep then restarts the process, and how often, cannot be determined from this repository.
- Polling-time errors have no bot-specific error handler or alert path in this source. That is a resilience/observability gap, not proof that the bot stopped because of it.
- Quiz delivery exceptions may leave the current in-memory quiz cleared so the learner can restart. Persistent reward ledgers mitigate duplicate reward grants; in-progress quiz state is not durable across process restarts.

## Safe recommendations (not applied)
1. After Botkeep support clears the stuck infrastructure operation and confirms the project filesystem is stable, inspect the Console logs before any restart.
2. Confirm the Botkeep Python runtime, project root, start command, and installed `python-telegram-bot` version.
3. Consider a small, reviewed code change in a separate branch later: register a central PTB error handler that classifies network/time-out/conflict/rate-limit errors, logs useful context without secrets, and alerts the operator for persistent failures.
4. Consider explicit bounded bootstrap retry settings only after choosing an operational policy; do not switch to indefinite retries blindly.
5. Do not start a second polling process or retry/redeploy the stuck Botkeep operation while the existing process/operation state is unknown.
6. Obtain a completed Botkeep backup and an independent database copy before any destructive restore/redeploy action.

## Boundaries
- No code was changed on `main`.
- No Botkeep action was taken.
- No secrets, live logs, process state, deployed package version, SQLite file, or verified backup were accessible.
- This note is an append-only audit record, not a deployment or a declaration that production is healthy.

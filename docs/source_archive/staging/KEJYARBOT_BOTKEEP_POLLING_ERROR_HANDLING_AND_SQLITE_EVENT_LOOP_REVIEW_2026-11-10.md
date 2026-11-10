# KejyarBot Botkeep Runtime Polling, Error Handling, and SQLite Blocking Review — 2026-11-10

## Scope
Read-only source review of the `main` branch for Telegram polling lifecycle, exception handling, external network dependencies, and SQLite execution behavior. Botkeep remains the intended host. No Botkeep panel/server action, deployment, restart, restore, or production-code change was performed.

## Findings

### 1. Polling lifecycle
- Active entry point is `bot.py`; `main()` validates activated course assets, initializes SQLite, resolves the Telegram token, builds the PTB Application, registers handlers, then calls `app.run_polling()`.
- No explicit polling/network timeout, bootstrap retry, or pending-update policy is configured at the call site; the behavior therefore depends on the installed python-telegram-bot 22.x defaults.
- The application has a `post_init` callback that logs successful initialization immediately before polling begins.
- Exactly one polling start call exists in the active `bot.py`; the separate `bot_backup.py` is a legacy snapshot and is not imported by the active entry point. This source scan does not establish how many processes are running on Botkeep.

### 2. Error handling and observability
- The active Application registers no custom `add_error_handler`.
- A small number of quiz delivery paths catch exceptions, clear transient quiz state, log a stack trace, and re-raise. Some optional UI edits catch exceptions and log at debug level.
- Course catalogue/manifest paths have local exception handling and log failures before sending a user-facing message.
- Many other async handlers do not wrap their full handler body in a local try/except. PTB's framework-level error logging may still report uncaught handler exceptions, but the application has no centralized, project-specific error classification or recovery policy.
- Logging is configured at INFO level to the process's standard logging stream; Botkeep log retention/visibility was not accessible during this review.

### 3. External network dependencies
- The active Python source files were scanned for common direct HTTP clients and blocking network primitives (`requests`, `httpx`, `aiohttp`, `urllib`, `urlopen`, `time.sleep`, subprocess calls). No such application-level call was found in the scanned active Python source.
- Telegram API traffic is handled by python-telegram-bot. `daily_chat.py` is deterministic/local rule-based text logic and does not call an external AI/API service.
- This does not rule out network behavior inside third-party packages or platform infrastructure.

### 4. SQLite and async event-loop contention
- `database.py` creates a fresh SQLite connection per operation, sets `timeout=10`, and closes connections with `finally` blocks. Transactional reward/progress functions use `BEGIN IMMEDIATE`, commit/rollback, and idempotency checks.
- The database functions are synchronous, while the Telegram handlers are asynchronous. The active bot imports and calls these synchronous database functions directly from async handlers (for example, user/progress lookup and completion/reward paths). SQLite lock waits and disk I/O therefore occur on the asyncio event-loop thread.
- If the database is locked or storage is slow, a synchronous SQLite call can hold up processing of other Telegram updates for up to the configured 10-second connection timeout. This is a credible responsiveness risk, not proof that it is currently happening on Botkeep.
- The existing transactional/idempotent reward logic is a positive safeguard and should be preserved if this is refactored.

## Priority assessment
1. **Medium — central error handling:** add a project-level PTB error handler with structured exception logging and safe user-facing handling where appropriate. Avoid swallowing exceptions silently.
2. **Medium — event-loop blocking:** consider moving SQLite operations off the async event loop (for example, a carefully bounded worker-thread strategy or an async persistence layer). Keep each SQLite connection created/used/closed within its worker thread; preserve transaction boundaries and idempotency.
3. **Low/conditional — polling configuration:** explicitly document and test selected polling timeouts/retry/pending-update behavior against the actual Botkeep runtime and installed PTB version, rather than relying indefinitely on library defaults.

## Verification limits
- The Botkeep runtime, installed PTB version, environment variables, console logs, process count, actual database lock state, and service health were not accessible.
- GitHub source inspection cannot establish that the currently deployed Botkeep files match `main`.
- No claim is made that the bot is currently polling, currently failing, or experiencing SQLite contention.

## Safety status
Read-only inspection only. No source changes to `main`, no Botkeep actions, no polling process started, and no backup/restore action taken.

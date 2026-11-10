# KejyarBot Botkeep Telegram Callback Acknowledgement and Handler Review — 2026-11-10

## Scope
Read-only review of active `main` branch callback handlers and quiz flow. No production source edits and no Botkeep actions.

## Findings

### 1. Delayed callback acknowledgement in lesson completion
- `finish_lesson()` performs synchronous database work before calling `query.answer()` on its successful path. This includes user/progress/reward reads and writes, and in some branches badge/level checks.
- Because database operations are synchronous and may wait up to the configured SQLite connection timeout, the Telegram inline-button spinner can remain active while this work runs. Under storage contention or a slow filesystem, callback acknowledgement can be delayed.
- Most early rejection paths acknowledge the callback before replying; the delay is concentrated in the successful completion path.
- Improvement: acknowledge promptly before potentially slow database work, while preserving idempotent transaction claims and safe duplicate-click behavior. If refactored, ensure that acknowledgement does not create a window where duplicate callbacks can award progress twice; existing database idempotency is a safeguard and must remain.

### 2. Quiz callbacks
- Quiz selection stores the selected index before the first await, then acknowledges the callback. This is deliberate to avoid a fast submit racing ahead of the selected answer.
- Quiz submission claims `answer_in_progress` and invalidates the current question message id before awaiting Telegram acknowledgement, preventing duplicate callbacks from scoring the same question twice within the in-memory session.
- Quiz completion rewards use persistent idempotent database ledger functions. This is a positive design property.
- Some Telegram delivery failures clear transient quiz state and log the exception, allowing the learner to restart rather than remain stuck in a half-active quiz.

### 3. Other callback handlers
- Course navigation, quiz menu pagination, month selection, and lesson opening generally call `query.answer()` immediately at handler start, before content/database reads and message sends.
- `finish_lesson()` is the main notable exception found in the inspected callback paths.

### 4. Recovery limitations
- Quiz state and other `context.user_data` session values are in-memory and are not backed by a PTB persistence backend in the active application. A process restart therefore loses an in-progress quiz/session, although durable user progress/reward records remain in SQLite.
- This is a user-experience limitation, not evidence of database loss or a Botkeep failure.

## Priority
- **Medium:** move successful `finish_lesson()` callback acknowledgement earlier, preserving database idempotency and duplicate-click protection.
- **Low/optional:** consider persistence for in-progress quiz state only if product requirements call for surviving process restarts; this requires careful compatibility and privacy design.

## Verification limits
- This is source-level evidence only. The actual Botkeep process, Telegram callback latency, deployed commit, SQLite lock status, and runtime logs were not accessible.
- No live callback was triggered and no production behavior was changed.

## Safety
Read-only inspection only. No deployment, restart, restore, polling start, or database operation was performed.

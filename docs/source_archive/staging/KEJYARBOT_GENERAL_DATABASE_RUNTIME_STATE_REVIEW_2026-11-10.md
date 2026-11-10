# KejyarBot General Database and Runtime State Review — 2026-11-10

## Findings from read-only inspection of main
1. SQLite access in `database.py` consistently uses parameterized SQL for user-provided values in the inspected statements; no dynamic SQL interpolation was found in the file's execute calls.
2. Database connections are explicitly closed with `finally` in the inspected functions. Core lesson and quiz reward flows use `BEGIN IMMEDIATE` and idempotent ledgers, reducing duplicate-reward and concurrent-write risks.
3. The main-branch database schema is upgraded additively for `completed_quizzes` and `beta_completed_lessons`; no destructive schema operation was found in the inspected init path.
4. Some legacy helpers such as `add_score()` update score/XP, coins, and level in multiple separate transactions. This is less robust against a process interruption than the newer atomic lesson/quiz reward functions. The primary inspected lesson completion path uses the atomic function; this is a maintainability/consistency concern, not proof of current data corruption.
5. `bot.py` creates `Application` without a persistence backend. `context.user_data` stores active quiz state and daily-chat session state in memory. A process restart or redeploy will lose in-progress quiz selections and daily-chat stage, although durable lesson progress/rewards are stored in SQLite.
6. No admin-only command or admin ID check was found in the inspected `bot.py`/`database.py` search results. No administrative destructive command was identified in this scan. This is a limited source scan, not a complete security certification.

## Priority
- P1 remains the previously documented main-branch database path mismatch with Railway's `KEJYARBOT_DB_PATH` plan.
- P1 remains the absence of a verified authoritative DB backup and restore drill.
- P2: Consider persistent conversation/session storage if resuming active quizzes and daily-chat sessions across restarts is a product requirement.
- P2: Consolidate or retire legacy multi-transaction reward helpers to reduce partial-update risk.

## Limitations
No live user database, Botkeep filesystem, Telegram token, Railway secret values, or production logs were accessed. No claim is made that the live database is intact or that the running bot is secure/healthy.

No code, tests, data, service settings, or deployments were changed.
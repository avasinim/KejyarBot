# Reward-path source audit checkpoint

Date: 2026-11-12
Branch: `fix/load-env-before-database-2026-11-12`
Pull request: #153

## Scope

Reviewed the application Python source files in the current branch (18 non-test Python files), focusing on the active lesson and quiz reward paths, legacy reward helpers, badge reconciliation, and database transaction boundaries.

## Findings

1. Active official lesson completion in `bot.finish_lesson()` uses `complete_lesson_with_rewards()`. The helper starts `BEGIN IMMEDIATE`, checks the persistent completion ledger, and writes completion, score, XP, coins, chest, and level in one transaction. A duplicate completion returns `False` without issuing rewards.
2. Active quiz completion in `bot.quiz_answer()` revalidates `lesson_quiz_is_available()` immediately before calling `complete_quiz_with_rewards()`. The helper records the quiz ledger, test count, score, XP, and level in one transaction. A duplicate quiz returns `False` without repeating XP.
3. Arami assessment awards go through `award_arami_assessment()`, which first calls `can_take_arami_assessment()` and only then claims the assessment through the same idempotent quiz reward helper.
4. Badge writes are separate from the lesson reward transaction. `add_badge()` uses `BEGIN IMMEDIATE` and an idempotent membership check. The preceding checkpoint now makes official lesson retries re-run badge reconciliation, covering a crash after lesson commit but before badge persistence.
5. Legacy `add_score()`, `add_xp()`, `add_coins()`, and `add_chest()` remain in `database.py`, but the active `bot.py` runtime does not call them. The only additional source call site found for `add_score()` / `add_chest()` is the historical `bot_backup.py` snapshot. No active runtime change was justified by this audit.
6. `get_user()` creates the user row before the reward transaction. If the process fails between row creation and reward transaction, the effect is limited to an empty/default user row; the reward transaction remains independently atomic.
7. No SQLite WAL mode is configured explicitly in the inspected source. Production journal mode and any sidecar files remain unknown and must be checked on the host before a physical database copy. This source audit does not establish the live Botkeep database path or identity.

## Decision

No further reward-path code change was justified by this pass. Existing idempotent transaction design is retained. The only source correction in this area is the already committed retry-safe badge reconciliation and its regression test.

## Verification and operational boundary

The previous code head `2193bcdfd5c0d3d6509b4aae89b6b5fa626dbff6` passed GitHub Actions: compileall succeeded and 577 unit tests passed (11 skipped). This audit adds documentation only; CI for the new documentation commit is not yet confirmed.

No production database was opened, copied, migrated, restored, or modified. No Botkeep import, merge, restart, or deployment was performed. PR #153 remains a draft and must not be merged until the host's effective database path and a fresh consistent backup are verified.

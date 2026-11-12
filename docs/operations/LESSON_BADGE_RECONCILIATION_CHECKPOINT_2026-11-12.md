# Lesson badge reconciliation checkpoint

Date: 2026-11-12
Branch: `fix/load-env-before-database-2026-11-12`
Pull request: #153

## Finding

The official lesson completion transaction in `database.complete_lesson_with_rewards()` atomically records first completion and its XP/score, coins, and chest. Badge persistence is a separate idempotent operation performed by `check_badges()`.

Before this checkpoint, `bot.finish_lesson()` called `check_badges()` only when `complete_lesson_with_rewards()` returned `True`. If the lesson transaction committed and the process then failed while persisting badges, a learner's retry would receive `False` from the idempotent completion ledger and would not retry the missing badge write.

## Safe correction

- Official lesson completion now calls `check_badges(user_id)` after the completion claim, whether it is the first completion or an idempotent retry.
- Beta-review lessons remain excluded from official badge writes.
- Existing badge persistence is idempotent, so the retry does not duplicate a badge.
- XP, score, coins, and chest are still awarded only by the first-completion transaction; duplicate completion receives no repeated rewards.
- A regression test verifies that duplicate official completion retries badge reconciliation without repeating lesson rewards.

## Verification

Latest PR head at checkpoint:
`2193bcdfd5c0d3d6509b4aae89b6b5fa626dbff6`

GitHub Actions run:
https://github.com/avasinim/KejyarBot/actions/runs/43232345798

Observed checks:
- dependency installation: success
- `python -m compileall -q .`: success
- `python -m unittest discover -s tests -v`: success
- 577 tests passed; 11 skipped
- overall workflow: success

## Safety boundary

This is a source-only change on the isolated draft PR branch. It has not been merged or deployed. No Botkeep workload, production database, learner records, secrets, or hosting settings were modified. No restore, import, migration, restart, or deletion was performed.

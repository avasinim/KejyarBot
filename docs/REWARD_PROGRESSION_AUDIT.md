# KejyarBot rewards and progression audit

Branch reviewed: `fix/kejyarbot-stability-2026-10-25`

## Verified behavior in code and tests

- Lesson completion records the lesson and grants its score/XP, 5 coins, and one chest in one SQLite transaction.
- Repeated or concurrent completion of the same lesson does not grant duplicate rewards.
- Quiz completion records a quiz once and grants 20 XP/score only on the first completion.
- Chest opening decrements inventory and adds the selected coin reward in one transaction; an empty inventory cannot be overdrawn.
- Badge writes use a SQLite write transaction to avoid concurrent badge updates overwriting one another.
- XP level thresholds are now covered at each boundary, including 49/50, 99/100, 149/150, 299/300, 449/450, 599/600, and 799/800.

## Follow-up finding — resolved

- The `check_badges` mapping now assigns a distinct completion badge to all six lessons, including `وانە_6` (`🏅 زانای ماڵ و قوتابخانە`).
- `tests/test_content.py::test_every_lesson_has_a_completion_badge` checks the complete six-lesson mapping.
- The code change is commit `5e8629586a42bb98aefdffde066c64c038fc65c0`; the regression test was added in `494ad93f67e1beba7ae45917b284fb22eb74dd3e`. The branch was subsequently rechecked and the latest code CI runs passed.

## CI

- The XP threshold tests were committed as `5d8622a0cd25ac61dacf31a94a1a1042fa3e9228`.
- Both observed workflow runs for that commit completed successfully:
  - https://github.com/avasinim/KejyarBot/actions/runs/40195006107
  - https://github.com/avasinim/KejyarBot/actions/runs/40195003391

## Safety boundaries

This audit does not change `main`, production bot settings, production databases, or prerecorded voice assets. Dynamic speech remains gated pending confirmation of the original approved voice and Kurdish pronunciation quality.

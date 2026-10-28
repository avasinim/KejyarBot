# KejyarBot pre-release smoke test

This checklist is for the isolated test bot only. It does not authorize merging PR #4, changing `main`, deploying, or touching the production bot.

## Before starting

- [ ] Use a separate Telegram test bot and its own token; do not copy the production token into this checkout.
- [ ] Confirm `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`. Keep it false unless the project owner explicitly approves enabling it.
- [ ] Keep `.env` and `kejyar.db` local and untracked.
- [ ] Start from the reviewed feature branch and install dependencies in its virtual environment.
- [ ] Run `python -m compileall -q .` and `python -m unittest discover -s tests -v`; both must pass before Telegram testing.
- [ ] Run `python check_telegram_connection.py`; confirm it reports the isolated test bot username/ID without showing the token. This checks authentication/network only and does not start polling.

## Telegram test sequence

Use a dedicated test account. Record pass/fail and any visible error without sharing tokens or personal data.

1. **Start/menu:** send `/start`; confirm the menu responds and Course 1, Course 2, and Course 3 appear separately. Course 4 should remain a planned/unavailable placeholder.
2. **Course 1 lesson:** open Lesson 1; confirm lesson text arrives before its optional infographic and the navigation keyboard remains usable.
3. **Long message safety:** open a lesson with long text; confirm all chunks arrive in order and the navigation keyboard appears only on the final chunk.
4. **Sequential access:** try opening the next lesson before satisfying the completion rule; confirm the bot applies the expected lock. Then complete the required step and retry.
5. **Quiz gates:** confirm quizzes for lessons 2, 4, 8, 13, 14, 16, 18, 19, and 21 are not offered. If an old/stale quiz callback is triggered, it must not start or score the blocked quiz.
6. **Available quiz:** run one available Course 1 quiz from start to finish; check feedback, explanation, final score, and that first-completion XP is awarded only once.
7. **Progress/restart:** verify progress is retained after a bot restart using the test database only.
8. **Draft courses:** confirm Courses 2 and 3 remain visibly marked/unavailable for review and their lesson callbacks cannot bypass the draft gate.
9. **Daily conversation and voice:** check text interaction only. Confirm no generated speech is attempted while `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`; preserve the existing approved voice configuration.
10. **Failure handling:** test with an invalid/missing optional infographic file in the isolated checkout; lesson text should still be delivered. Restore the file afterward.

## Release decision

- [ ] Automated tests pass on the exact candidate commit.
- [ ] A human has reviewed source and language risks for the intended active lessons.
- [ ] The isolated Telegram smoke test is recorded as pass.
- [ ] The owner explicitly approves the production release.
- [ ] Only after approval: prepare a separate release/merge/deployment plan. Do not treat this checklist as permission to merge or deploy.

## Current known limits

- Course 1 quiz content remains gated for the nine lessons listed above pending source review.
- Courses 2 and 3 are draft content, not approved for learners.
- Only Course 1 Lesson 1 currently has an infographic configured; do not represent the infographic set as complete.
- This checklist does not certify linguistic correctness, production reliability, or Telegram behavior until the manual test is actually performed.

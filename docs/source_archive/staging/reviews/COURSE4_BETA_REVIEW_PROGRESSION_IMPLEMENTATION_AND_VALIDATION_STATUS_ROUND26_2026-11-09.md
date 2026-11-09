# Course 4 — Beta review progression
## Implementation and validation status
### Round 26 — 2026-11-09

## Scope
A narrow runtime change for Course 4 expanded review drafts, Lessons 32–46. The objective is to let learners read these drafts and advance their Course 4 beta sequence without falsely presenting them as academically approved or awarding rewards for unapproved material.

## Changes in this branch
- `course_runtime.py`: added `is_beta_review_lesson`, a strict allowlist policy requiring all of:
  - course ID `grammar`;
  - lesson number 32 through 46 inclusive;
  - lesson ID matching `grammar_NN`;
  - exact review status `owner_review_pending_expanded_draft`.
- `database.py`: added a separate `beta_completed_lessons` ledger through a backward-compatible SQLite column migration, plus idempotent read/write helpers. Beta progress is never inserted into official `completed_lessons`.
- `bot.py`:
  - labels eligible lessons with a beta marker in the course menu;
  - displays a clear beta/review notice in the lesson;
  - permits the existing finish button only for the 15 eligible Course 4 drafts;
  - records progress idempotently in the separate beta ledger, with no XP, coins, chests, official completion, or badges;
  - does not award badges for beta-review lessons;
  - prevents quizzes for these lessons while the review status remains pending, even if structured quiz data is later added before approval;
  - leaves all other pending-review lessons blocked.
- `tests/test_course4_beta_review.py`: added nine unit tests covering lower/upper boundaries, other courses, status mismatches, lesson-ID mismatch, and Boolean-as-integer rejection.

## Safety and compatibility
- No lesson source text was edited.
- No embedded or structured quiz data was edited or migrated.
- No review status was changed to approved.
- Adds one backward-compatible SQLite column only; all existing columns and official progress IDs remain intact. Beta completion is stored separately and never counts as official completion.
- Existing approved lesson rewards and Course 1–3 quiz behavior are unchanged by the new eligibility policy.
- No changes to `courses.json`, the 46-lesson manifest, or `main`.
- No Botkeep, Telegram, production, or live deployment action was performed.

## Validation state
- All three changed/new files were fetched back from the feature branch after writes.
- The new test file was fetched back and its seven cases were inspected.
- GitHub Actions workflow runs for the final branch commit: none were returned.
- Combined commit status: no statuses were returned.
- Therefore the tests are **added but not yet executed** in a project runtime. Do not describe this change as tested, merged, or deployed.
- Draft PR: #120, `https://github.com/avasinim/KejyarBot/pull/120`.

## Acceptance checks still required
1. Run `python -m unittest discover -s tests -p 'test_course4_beta_review.py' -v` (or repository test discovery), including the isolated temporary-database migration and idempotence test.
2. Run `python -m compileall -q .`.
3. Run the full existing test suite.
4. Exercise Telegram callback flow with a test database: open Lesson 32 after Lesson 31, finish it, verify Lesson 33 unlocks, verify XP/coins/chests/badges remain unchanged, and verify quiz launch is blocked.
5. Exercise the same flow for Lesson 46 and verify no phantom Lesson 47 is generated.
6. Verify approved lessons and Courses 1–3 retain their prior rewards and quiz behavior.
7. Only after checks pass, prepare the PR for review/merge; deployment remains a separate explicit operational step.

**Release state:** implementation proposed on an isolated feature branch; draft PR open; no production activation.

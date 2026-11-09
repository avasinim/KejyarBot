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
- The new test file was fetched back and its nine test methods were inspected.
- GitHub Actions passed on PR head `450d248c111999cd5259a655e3eea92df39e5bed`: compilation passed; the full unittest suite passed **476 tests with 11 skipped**.
- Course 4 beta review safety workflow: success (run #12).
- Repository-wide Python checks: success (run #5772).
- Orthography course structure workflow: success (run #1595).
- These are automated CI results; Telegram callback smoke tests and production activation remain outstanding.
- PR #120 was squash-merged into `main` as commit `755d1d9e6dc98d06b187638ce627bb09848c1c2b`.

## Remaining release checks
1. Exercise the Telegram callback flow against a dedicated test database: open Lesson 32 after Lesson 31, finish it, verify Lesson 33 unlocks, verify XP/coins/chests/badges remain unchanged, and verify quiz launch is blocked.
2. Exercise Lesson 46 and verify no phantom Lesson 47 is generated.
3. Confirm approved lessons and Courses 1–3 retain their prior rewards and quiz behavior (covered by the passing full suite, with live Telegram smoke testing still separate).
4. Production Telegram/Botkeep activation remains a separate operational step; no deployment workflow was found or executed.

**Release state:** implementation is merged into `main`; pre-merge CI passed (476 tests, 11 skipped). No Telegram/Botkeep production activation or live smoke test was performed.

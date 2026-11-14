# Cross-course review-gate runtime audit — 2026-11-12

## Scope and method
Read-only source inspection of the PR branch `release/main-based-reconciled-2026-11-11` in `avasinim/KejyarBot`. Inspected `bot.py`, `course_runtime.py`, `course_lesson_adapters.py`, `arami_course1_telegram.py`, the Arami manifest, all four Course 2 source JSON chunks, the Course 3 source JSON, `latin_course_runtime.py`, the Latin course manifest, and PR-triggered CI for the then-current PR head. No source, lesson, quiz, manifest, approval status, learner record, or Botkeep runtime was changed by this audit.

## Exact source/manifest status inventory
- Course 1 (Arami): 21 manifest lessons. Explicit status distribution: 16 `source_review_pending`; 2 `source_received_preserved`; 1 `user_supplied_source_received_and_preserved`; 1 `source_received_preserved; lesson_identity_confirmed_as_5`; 1 lesson has no per-lesson status. None carries one of the explicit academic approval statuses (`scientific_review_complete`, `scientific_review_complete_with_qualified_notes`, `approved`).
- Course 2 (daily conversation): 42 source records across four JSON chunks; all 42 have `review_status=draft_editorial_review`.
- Course 3 (unified orthography): 66 source records; all 66 have `review_status=draft_editorial_review`.
- Latin Course 1 and Latin Course 2: 12 lessons each. `latin_course_runtime.py` assigns `review_status=draft_editorial_review` to every parsed lesson. The Latin source manifest itself labels both course records `status=draft`; runtime registration in `courses.json` currently marks both active. This is a distinction between source-manifest draft state and runtime activation, not proof of academic approval.

## Runtime gate behavior observed
- `bot.py::_lesson_requires_academic_approval` fails closed for active courses when the lesson record is absent or its `review_status` is not in `ACADEMIC_APPROVAL_STATUSES`. Arami uses its separate manifest approval check.
- `lesson_quiz_is_available` denies quizzes while `lesson_is_beta_review` is true. `start_quiz` checks availability before launch; `quiz_answer` checks again before processing answers and again immediately before the reward-ledger write.
- `finish_lesson` routes review lessons through the separate Beta completion ledger; it rejects pending lessons that are not valid Beta-review lessons. Beta completion does not award XP, coins, chests, or badges.
- `can_open` enforces course sequence and counts Beta completion only for lessons currently classified as review/Beta. Old Beta records do not count as official completion after approval.
- Course 4 Beta classification in `course_runtime.py` is narrowly defined for grammar lessons 32–50 with the exact `owner_review_pending_expanded_draft` status. Other active-course review lessons are classified by the generic fail-closed academic gate in `bot.py`.
- Arami dedicated Telegram handlers permit practice when the learner can open the lesson, but show/allow official assessment only when the manifest lesson has explicit academic approval. The assessment mode rechecks approval and sequence, and `award_arami_assessment` rechecks before XP is written. Thus source receipt or the presence of practice/assessment question banks is not itself academic approval.

## Safety/interpretation notes
- Runtime activation (`courses.json`) is not equivalent to academic approval. Courses 2, 3 and both Latin courses are registered active, but their inspected lesson records remain editorial-review drafts and therefore are not eligible for official quizzes/rewards under the current gate.
- The Arami manifest contains practice and assessment banks, but no lesson currently has an explicit approval status. The code keeps practice distinct from official assessment/rewards.
- The current audit verifies source code and manifest logic, not live Telegram behavior or deployed Botkeep state. No learner data or database was inspected or changed.
- No approval status was promoted, no quiz was opened, no term or lesson text was edited, and no deployment/import/restart was attempted.
- Follow-up validation should add/confirm automated tests for the Course 2/3 and Latin review-gate cases, Arami manifest states with missing/pending/approved statuses, and the transition from Beta completion to approved official completion. Do not weaken fail-closed behavior to make draft lessons reward-eligible.

## PR and CI evidence at audit time
- PR: https://github.com/avasinim/KejyarBot/pull/152
- PR head reported by GitHub metadata: `58f4bb386be8c8c4a042d8e19531f8a9b02c12f0`; PR open, unmerged, mergeable.
- Four PR-triggered workflows for that exact head completed successfully: Python checks, Kurdish months tests, Course 4 beta review safety, Orthography course structure tests.
- This audit is evidence-only. It does not authorize merge, import, restart, deployment, or Telegram rollout.


## Regression-test coverage inspected (read-only)
- `tests/test_launch_readiness_matrix.py` asserts the six active courses contain 203 unique lesson IDs, exactly 30 lessons are outside Beta/review-only state, and all 173 review-only lessons fail `lesson_quiz_is_available`. This includes the 42 Course 2 and 66 Course 3 draft lessons and the 24 Latin draft lessons through the aggregate inventory.
- `tests/test_bot_quiz_callbacks.py` includes a Lesson 13 start attempt while quiz availability is false and asserts no quiz session is created; it also includes a stale Lesson 13 quiz-session answer attempt after availability is revoked and asserts the session is discarded and the reward function is not called.
- `tests/test_arami_course1_telegram.py` covers missing assessment permission callback, missing unlock callback, permission revocation during an active assessment session, and successful assessment reward routing for an explicitly permitted lesson.
- `tests/test_activated_courses.py` asserts Arami review lessons remain out of official assessment menus, cannot receive official rewards, and that unknown/missing review statuses fail closed.
- `tests/test_course3_runtime_ux.py` tests Course 3 sequential lesson access and text-only lesson flow; its separate quiz UX tests patch quiz availability true, so the cross-course gate coverage is supplied by the launch-readiness matrix and generic quiz callback tests, not by that UX test alone.

## Test-coverage conclusion and remaining limitation
The inspected suite has direct regression coverage for aggregate fail-closed eligibility, generic quiz start/answer revocation, Arami assessment revocation, and no implicit Arami approval. It does not constitute a live Telegram/Botkeep smoke test, nor does it independently validate every source term or academic decision. No code or test file was changed in this audit; no test command was executed in a local runtime. The four successful GitHub Actions runs remain the execution evidence for the exact audited commit, not a claim that the bot is deployed or live-tested.

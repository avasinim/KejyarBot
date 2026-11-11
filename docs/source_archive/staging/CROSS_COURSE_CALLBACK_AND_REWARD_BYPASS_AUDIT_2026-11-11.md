# Callback and reward-path audit — cross-course draft gates
## 2026-11-11 | Append-only source-backed finding
Candidate inspected: `botkeep-menu-clean-2026-11-09`

### Confirmed bypasses for editorial draft statuses
1. `lesson_is_pending_review()` in `bot.py` recognizes only `owner_review_pending_expanded_draft`. `lesson_quiz_is_available()` excludes only the special Course 4 beta gate and the separate quiz-review helper. It does not reject `draft_editorial_review`, `source_review_pending`, or the Latin manifest's `draft` state.
2. `finish_lesson()` blocks only that same narrow owner-pending status (unless it is a designated beta lesson). Other draft statuses go to `complete_lesson_with_rewards()`, then `check_badges()`; first completion grants +10 XP, +5 coins, and a chest. `check_badges()` skips only beta lessons, not general editorial drafts.
3. `start_quiz()` validates course active state, `lesson_quiz_is_available()`, source quiz existence, completion and sequence. Since the availability helper omits the general draft statuses, Latin Course 1/2 and Course 2/3 editorial drafts can enter standard quiz flow.
4. `quiz_answer()` rechecks `lesson_quiz_is_available()` immediately before `complete_quiz_with_rewards()`; this is a useful stale-session defense, but the predicate still does not include the draft statuses. Therefore it does not close the above gap.
5. Unified Orthography Course 3 can automatically open the next lesson after completion. The next lesson's own completion button is required, but the auto-open does not impose editorial approval; it inherits the same narrow lesson keyboard gate.

### Arami Course 1 specific path
- The 21-lesson catalogue marks many records `source_review_pending`, while 14–16 have received/preserved statuses. The general `finish_lesson()` callback accepts these statuses because it only checks `owner_review_pending_expanded_draft`; unless the beta predicate applies (it does not for Arami), a learner can receive normal lesson XP/coins/chest and badges.
- The Arami course menu creates read/practice/assessment actions whenever a question bank exists; it does not check an academic approval status.
- Dedicated Arami Course 1 assessment callbacks call `award_assessment`, which grants 20 XP through `complete_quiz_with_rewards()`. The inspected Lesson 1, Lesson 5 and shared Arami Course 1 callbacks check lesson sequence and bank validity, but do not require an academic approval status before assessment rewards.
- Practice sessions do not appear to award XP; assessment sessions do. Therefore the approval gate must be applied to assessments and their reward callbacks, not just the generic quiz handler.
- Lesson 1 and Lesson 5 have dedicated callbacks, and Lessons 2–21 route through `arami_course1_telegram.py`; all must share the same authoritative status policy to avoid inconsistent paths.

### Severity and remediation requirements
- Release blocker: general draft/review-pending content currently can reach normal completion and reward ledgers via more than one callback family.
- A complete fix must use one explicit status policy and enforce it at: course visibility/open, lesson read/finish, generic quiz start/submit/reward, Arami practice/assessment start and assessment reward, badge progression, and any auto-advance path.
- Preserve beta-only progress behavior for the explicitly approved Course 4 beta set; do not collapse it into normal rewards.
- Do not retroactively rewrite learner progress or revoke rewards as part of a code patch without owner approval and a separate data-reconciliation plan.
- Owner decision still needed on intended treatment of unapproved material: hidden until approved, readable-only, or beta progress without rewards. Do not silently choose.

### Non-actions
No code, manifest, lesson, quiz, reward logic, learner DB, Botkeep state, PR, or deployment was changed. No merge, deploy, import, restore, restart, or Railway activation was performed.

# Course 2–3 draft-review reward-gate inconsistency
## 2026-11-11 | Append-only source-backed finding
Candidate inspected: `botkeep-menu-clean-2026-11-09`

### Scope and evidence
- `course_data/daily_conversation_lessons_01_06.json`: 6/6 lessons carry `review_status=draft_editorial_review`.
- `course_data/daily_conversation_lessons_07_30.json`: 24/24 lessons carry the same status.
- `course_data/daily_conversation_lessons_31_36.json`: 6/6 lessons carry the same status.
- `course_data/daily_conversation_lessons_37_42.json`: 6/6 lessons carry the same status.
- `course_data/unified_orthography_lessons_01_66.json`: 66/66 lessons carry the same status.
- All 108 records have titles, objectives, exercises, comprehension prompts, quiz items and review status. The 108 lessons contain 288 quiz questions in total (87 conversation + 201 unified orthography); all inspected question records passed structural checks for non-empty prompt, options, and in-range integer answer index. This does not establish academic correctness.
- Conversation lessons have 10 recorded review-finding entries across 10 lessons, including explicit requests for language review and safeguarding review. Course 3 has no `review_findings` entries, but all 66 records remain explicitly marked draft editorial review.
- `course_lesson_adapters.py` copies `review_status` into runtime lesson data, but does not itself block quiz availability or completion based on `draft_editorial_review`.
- `bot.py:lesson_is_pending_review()` returns true only when status equals exactly `owner_review_pending_expanded_draft`.
- `bot.py:lesson_quiz_is_available()` blocks beta-review lessons and otherwise delegates to `course_quiz_review.quiz_is_available()`.
- `course_quiz_review.py:quiz_is_available()` only contains the legacy Course 1 key allowlist; it does not gate Course 2 or Course 3 draft statuses.
- `bot.py:lesson_keyboard()` and `finish_lesson()` also only block the exact owner-pending status. For other records the ordinary completion/reward path remains reachable.
- `bot.py:validate_activated_course_runtime()` validates that these courses are active and that lesson and quiz records are loaded, but does not require editorial approval status for their release.

### Risk
If this candidate is promoted unchanged, Course 2's 42 and Course 3's 66 draft-editorial-review lessons can enter the normal quiz/completion/reward path despite not being approved. The catalogue labels both courses active. This is a release policy mismatch, not a quiz JSON structural failure.

### Required remediation before release
1. Define an explicit status policy for each course: approved, beta/read-only, owner-review-pending, and draft-editorial-review.
2. Fail closed for all unapproved statuses at quiz entry, completion callback, and reward issuance; do not rely only on hiding buttons.
3. Decide with the owner whether these 108 lessons should be read-only preview, beta progress without rewards, or withheld until approval. Do not silently choose or rewrite their academic status.
4. Add regression tests covering all three enforcement points and prove no XP, coins, chests, badges, or official completion are granted to draft lessons.
5. Keep existing learner progress and legacy Course 1 behavior intact; rehearse any DB or runtime changes on a disposable copy.
6. Re-run full course and reward tests on the exact release commit.

### Quiz structural counts (not academic approval)
- Daily Conversation: 87 quiz items across 42 lessons; no structural invalidity found in this pass.
- Unified Orthography: 201 quiz items across 66 lessons; no structural invalidity found in this pass.
- Total: 288 quiz items.

### Non-actions
No runtime code, lesson source, quiz content, progress DB, rewards, course activation, or Botkeep configuration was changed. No merge, deployment, import, restore, restart, or Railway activation was performed.

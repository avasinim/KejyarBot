# Main-Based Release Branch and Remaining Runtime Gate Findings — 2026-11-11

## Release branch
Created a non-deployment integration branch:
- `release/main-based-review-gates-2026-11-11`
- Base: `main`
- Branch creation only; no runtime files changed and no pull request opened.

## Confirmed main-side safety gaps relative to candidate
1. Main `bot.py::quiz_answer` validates quiz state and answer callbacks but does not re-check the active quiz lesson's current academic approval/quiz availability before accepting an answer. Candidate adds a fail-closed check against `quiz["lesson"]`, clearing stale quiz state and denying scoring if the lesson is no longer eligible.
2. Main `award_arami_assessment` directly calls `complete_quiz_with_rewards` without independently checking that the lesson belongs to Arami Course 1 and is academically approved. Candidate adds both checks before writing the reward ledger.
3. Main Arami Course 1 menu callback modules do not accept or enforce the candidate's `can_take_assessment` permission callback; candidate adds the parameter and uses it to hide/deny assessment entry in shared and dedicated Lesson 1 / Lesson 5 paths. The application-level `bot.py` wiring must also be included; helper-only changes are insufficient.
4. Candidate callback function signatures retain `can_take_assessment=None` for compatibility, and in that case some dedicated menu paths preserve their old assessment-enabled default. Current candidate `bot.py` wiring supplies the permission callback to all three handlers. The main-based integration must preserve this explicit wiring and add tests that missing permission callbacks cannot accidentally activate official assessments in production call paths.

These are code-level differences observed by reading the actual main and candidate source files. They are the reason a file-scoped integration is needed rather than copying only a small helper or replacing a whole file.

## Course 4 quiz override data validation
Candidate files were parsed read-only:
- `course_data/grammar_course4_lessons.json`: 50 lessons.
- Existing authored quiz bank: 31 lessons × 8 questions = 248 questions.
- Lessons 1–30 account for 240 questions; Lesson 31 adds 8.
- `course_data/grammar_course4_quiz_overrides.json`: 50 override records across 23 lessons.
- 44 override records target Lessons 1–30; 6 target Lesson 31.
- All 50 `original_snapshot` records exactly match the current source quiz item at the recorded lesson ID and question index.
- All 50 replacement records passed basic structural checks: non-empty question and explanation, exactly four non-empty unique options, and valid integer answer index.
- No override points to lessons 32–50; those lessons retain empty quiz arrays.
- Candidate `bot.py` applies the override only after exact snapshot validation and rejects duplicate keys / invalid replacement schema before replacing the in-memory quiz entry.
- Main does not yet contain this override loader or JSON file.

This is structural/source-integrity validation, not a linguistic or academic review of every replacement question. The original authored quiz source remains unchanged by the append-only override design.

## Exact integration tasks still required
- Port the candidate academic approval helper and explicit status allowlist into main without overwriting main's newer search/menu code.
- Port quiz-answer revalidation and the direct Arami reward-helper guard.
- Port the three Arami callback assessment guards plus all production handler wiring and tests.
- Integrate the Course 4 override file and loader with source snapshot checks; retain the 50 original lesson records and all 248 original quiz items.
- Preserve Course 4 Lesson 13's actual `scientific_review_complete_with_qualified_notes` status and its main-side source map/terminology crosswalk.
- Carry all relevant tests and workflows, then run the full test suite and required workflows on the exact main-based branch SHA.

## Deployment boundary
No application code has yet been changed on the release branch. No import, restart, Botkeep deployment, Railway deployment, live DB write, or main-bot deployment occurred. Node17 written support clearance remains a hard prerequisite before any test-bot import.

# Main-Based Release Branch — Quiz Override Integration Checkpoint — 2026-11-11

## Branch and commits
Branch: `release/main-based-review-gates-2026-11-11`, created from `main`.
- `e371a02f6549dc8c0cad4c7f3d4ec655d0b2562e`: added the candidate's Course 4 append-only quiz override JSON.
- `1994d0cb4354c678f681dc779460c8f0a152aaf6`: added strict source snapshot, duplicate-key, and replacement schema validation in main-based `bot.py`.
- `3c555abdf2b6b17891e339f917e08871e776ccef`: added four dedicated override tests.
- `2814d501d1d51d5dff1b323948705455a01c80fb`: enabled Python checks on `release/**` branches and triggered CI.

## Cross-check against main source
All 50 override original snapshots match the current main `grammar_course4_lessons.json` at their exact lesson IDs and question indices (50/50). Main has 46 lessons and 248 original quiz questions; candidate source had 50 lessons and the same 248 quiz questions. Override distribution is 44 questions in Lessons 1–30 and 6 questions in Lesson 31. No override points to Lessons 32–50.

The override JSON is added as a separate file. Original lesson JSON and original quiz questions were not edited. The loader rejects mismatched snapshots, duplicate override keys, invalid question text/options/answer index/explanation, and only then replaces the in-memory runtime question.

## CI result
GitHub Actions run `43011298559`:
- Workflow: Python checks
- Commit: `2814d501d1d51d5dff1b323948705455a01c80fb`
- Result: success
- `python -m compileall -q .`: passed
- `python -m unittest discover -s tests -v`: 490 tests passed, 11 skipped
- All four new `Course4QuizOverrideTests` passed.

Run: https://github.com/avasinim/KejyarBot/actions/runs/43011298559

## Remaining integration scope
The release branch still needs the cross-course academic approval gate, the quiz-answer revalidation, Arami assessment callback gates and explicit production wiring, plus review-aware progress handling. The exact main-side Lesson 13 source-map/terminology changes and main's newer menu/search code must be preserved. This checkpoint is not a complete release and must not be imported into Botkeep yet.

## Safety
Only the isolated GitHub release branch was changed. No main branch update, merge, PR, Botkeep import/restart, live DB write, Railway deployment, or main-bot deployment occurred. Node17 written support clearance remains required before test-bot import.

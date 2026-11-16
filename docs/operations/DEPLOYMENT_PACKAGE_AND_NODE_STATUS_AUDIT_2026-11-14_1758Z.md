# Deployment package and node-status audit — 2026-11-14 17:58Z

## Audited source
- Repository: `avasinim/KejyarBot`
- Branch: `release/main-based-reconciled-2026-11-11`
- Head at inspection: `53393395224ffb6f676c660d51e0e6f7cdda425c`

## Altare public status recheck
- At the time of this check, Altare's public status page reported **44/44 components operational** and **20/20 nodes operational**.
- This is platform-level evidence only. It does **not** prove that the individual `kejyarbot` server is reachable, its file manager is healthy, its prior files exist, or its SQLite data is present.
- The app's last directly observed panel state in the user-provided session remains `Stopped / Node down`; no new panel session was available to verify a change.
- Official Altare guidance says not to repeatedly restart, reinstall, or delete a server during a node incident. This checkpoint performed no Start, Restart, Emergency recovery, restore, delete, or other panel operation.

## Runtime import closure
The direct runtime import closure for `python bot.py` was inspected. The Python source files required by that closure are:
- `bot.py`
- `database.py`
- `daily_chat.py`
- `course_runtime.py`
- `quiz_option_order.py`
- `course_lesson_adapters.py`
- `course_quiz_review.py`
- `lesson_image_delivery.py`
- `latin_course_runtime.py`
- `arami_lesson1_telegram.py`
- `arami_lesson5_telegram.py`
- `arami_course1_runtime.py`
- `kurdish_months.py`
- `arami_course1_telegram.py`
- `arami_lesson1_interaction.py`

`ai_tutor.py`, `arami_lesson1_presentation.py`, and `bot_backup.py` are not in the inspected import closure of `bot.py`; do not include them by assumption. This is a source-level import audit, not a completed package build.

## Runtime data requirements observed
The startup path reads:
- `courses.json`
- `course_data/daily_conversation_lessons_01_06.json`
- `course_data/daily_conversation_lessons_07_30.json`
- `course_data/daily_conversation_lessons_31_36.json`
- `course_data/daily_conversation_lessons_37_42.json`
- `course_data/unified_orthography_lessons_01_66.json`
- `course_data/grammar_course4_lessons.json`
- `course_data/grammar_course4_quiz_overrides.json`
- `course_data/latin_courses_manifest_draft.json`
- `course_data/arami_course1_manifest.json`
- `course_data/arami_course1_source_quiz_banks.json`
- `course_data/arami_course1_lesson_01_content.json`
- `course_data/arami_course1_lesson_01_interactions.json`
- `course_data/arami_course1_lesson_05_interactions.json`
- The 21 lesson source files named by the Arami manifest (one Lesson 1 JSON source and the lesson source Markdown files).
- The four Latin source and answer-key Markdown files:
  - `course_data/latin_course_1_source_aligned_lessons_01_12.md`
  - `course_data/latin_course_2_source_aligned_lessons_01_12.md`
  - `course_data/latin_course_1_quiz_answer_key_draft.md`
  - `course_data/latin_course_2_quiz_answer_key_draft.md`

The 7 approved PNGs in the repository tree remain the only image assets identified for the runtime: six Course 1 infographics for lessons 1, 2, 3, 4, 6, and 7, plus the shared Lesson 5 / Latin Lesson 1 image. No PDF, audio, SVG, JPG, or additional image was added to the package allowlist.

## Dependencies and startup
- `requirements.txt`: `python-telegram-bot>=22,<23`, `python-dotenv>=1,<2`.
- Startup remains `python bot.py`; this is a Telegram polling worker, not an HTTP web server.
- Root `.env` is excluded from Git/package. The user's private token must not be copied into this audit or repository.

## Database safety gate
- `database.py` resolves `KEJYARBOT_DB_PATH` when configured; otherwise it defaults to `kejyar.db` in the project directory.
- `init_db()` creates the parent directory and opens the configured path, creating a new SQLite database if that file does not already exist.
- Therefore **do not start the bot until the original learner database is located and verified**, and the configured path is confirmed to point to that exact database in storage that survives redeploy/restart. Do not permit a blank replacement database.
- Preserve the database file and any SQLite `-wal` / `-shm` sidecars together during a safe, quiesced transfer.
- The current Altare `.env` reported by the user contains only the Telegram token; no database path has been configured or verified.

## Actions not performed
No source code or course content was changed. No deployment archive was built or uploaded. No token was read or copied. No database was created, copied, migrated, or opened. No Altare panel settings or server controls were changed. No Botkeep process was started or stopped. No second Telegram poller was launched.

## Next safe gate
1. Re-check the individual Altare app and file manager after the user-visible node state is refreshed.
2. Locate and verify the original SQLite database before any bot startup.
3. Confirm the actual durable storage path and only then set `KEJYARBOT_DB_PATH`.
4. Build and validate the deployment package from the audited source revision, excluding secrets, databases, backup scripts, unused modules, and unapproved assets.
5. Start only after the database gate is passed and no other instance is polling with the same Telegram token.

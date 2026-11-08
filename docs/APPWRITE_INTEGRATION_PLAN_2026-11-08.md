# Appwrite Integration Plan for KejyarBot
Date: 2026-11-08
Status: Design only — no Appwrite resources created and no runtime code changed.

## 1. Current architecture observed

- Telegram bot runtime is Python (`python-telegram-bot>=22,<23`).
- Course and lesson content is loaded from version-controlled JSON/Markdown files in the repository.
- Learner state is stored by `database.py` in a local SQLite file named `kejyar.db`.
- The current SQLite `users` row combines XP, score, level, completed lesson IDs, badges, quiz count, coins, chests, and a comma-separated quiz-completion ledger.
- The project loads a local `.env` file, while host-provided environment variables take precedence.
- No Appwrite SDK dependency or Appwrite configuration was found in the inspected runtime files.

## 2. Recommended responsibility split

Keep GitHub as the authoritative source for authored course content and keep the Telegram bot host responsible for running the bot.

Use Appwrite TablesDB as the future managed persistence layer for learner progress and rewards. Do not move lesson content out of the repository in the first migration. Do not treat Appwrite as a replacement for Botkeep/runtime hosting.

The existing SQLite database remains authoritative until an Appwrite migration has been tested against a copy and verified. Do not delete, rename, overwrite, or automatically migrate the live `kejyar.db`.

## 3. Proposed TablesDB model

Create one database (suggested ID: `kejyar_main`) only after the owner confirms the schema and the Appwrite project is ready.

Suggested tables:
- `learners`: stable document ID; unique `telegram_user_id`; score, XP, level, correct_answers, tests, coins, chests, created_at, updated_at.
- `lesson_completions`: unique `telegram_user_id + course_id + lesson_id`; completion timestamp; reward-granted marker.
- `quiz_completions`: unique `telegram_user_id + course_id + quiz_id`; completion timestamp; reward-granted marker.
- `learner_badges`: unique `telegram_user_id + badge_id`; awarded timestamp.
- `reward_events` (optional audit ledger): event ID, learner ID, event type, reference ID, XP/coin/chest deltas, timestamp, idempotency key.

Use stable IDs and unique indexes for idempotency. Store Telegram IDs as strings if the selected Appwrite column type or SDK requires it; validate the exact supported types before creation. Avoid storing bot tokens, API keys, or unnecessary personal data.

## 4. Safe migration sequence

1. Inspect the actual Botkeep deployment/runtime configuration and determine whether `kejyar.db` is on persistent storage. Do not infer persistence from the repository.
2. Confirm Appwrite project/region and account permissions. The project endpoint observed in the owner's console is `https://sgp.cloud.appwrite.io/v1`; project ID is `6af01234002092643d9e`. These are identifiers, not secrets.
3. Create the TablesDB database and tables only after the schema is approved.
4. Add an Appwrite adapter behind a feature flag; do not change the existing SQLite code path by default.
5. Export a copy of SQLite data and run an idempotent importer against a test database. Verify row counts, IDs, XP/score totals, completions, badges, quiz counts, coins, and chests.
6. Test reward idempotency and concurrent completion behavior. The current SQLite implementation uses atomic transactions; preserve equivalent guarantees in the Appwrite path and never award a reward twice on retry.
7. Run a controlled shadow-read or explicit test cohort. Compare SQLite and Appwrite results without allowing both stores to independently award rewards.
8. Only after successful verification, plan a separately approved cutover and rollback window. Keep the original SQLite file and the downloaded Botkeep backup untouched.

## 5. Security and operational safeguards

- Never paste an Appwrite API key into chat, GitHub, source code, screenshots, or a committed `.env`.
- If a server API key becomes necessary, create it only at the implementation stage, with the minimum database/table permissions required, and store it only in the Botkeep secret/environment settings.
- Never expose a server API key in Telegram client code or public browser code.
- Do not create a client app registration merely to connect the server-side Python bot.
- Do not modify `.env`, `kejyar.db`, Courses 1–3, or the Botkeep deployment during the design stage.
- Appwrite free-plan limits and the availability of TablesDB features must be checked in the console before production use.

## 6. Current decision

Recommended: proceed with a staged Appwrite TablesDB integration for learner progress, while leaving lesson content in Git and leaving SQLite untouched until the migration has passed verification.

This document is a design proposal only. It does not claim that an Appwrite database, table, API key, Botkeep setting, or production integration has been created.

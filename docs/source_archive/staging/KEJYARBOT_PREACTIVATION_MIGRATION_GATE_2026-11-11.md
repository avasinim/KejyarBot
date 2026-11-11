# KejyarBot — pre-activation migration gate and evidence register

Date: 2026-11-11
Scope: Railway persistent SQLite migration and safe single-poller activation.

## User authorization

The owner explicitly approved all previously proposed work and requested preservation, backups, activation of the prepared changes, and transition to robot activation. This authorization covers the intended deployment. It does not make an unavailable production database backup available, nor does it resolve the separately documented Botkeep source-staging incident.

## Verified repository and CI state

- Repository: `avasinim/KejyarBot`.
- PR #141, `[DRAFT] Prepare KejyarBot for Railway persistent SQLite storage`, remains Draft/Open/Unmerged; head `259d746cab1e546fa76d39bc1dc0be5d2c394176`, base `main`.
- PR #141 changes only `database.py`, `docs/RAILWAY_DEPLOYMENT_RUNBOOK.md`, and `tests/test_railway_persistent_db.py`.
- On the exact PR #141 head, GitHub Actions reports three completed successful workflows: Orthography course structure tests, Python checks, and Course 4 beta review safety. This is repository CI evidence; it is not a live Railway deployment test or SQLite migration test against production data.
- The PR runbook specifies the safe order: verified SQLite backup, read-only inspection, persistent volume, DB path, restore before poller, confirmed Botkeep stop, exactly one poller, then acceptance tests.

## Verified Railway production state

- Project: `melodious-enthusiasm`; environment: `production`; service: `KejyarBot`.
- Latest `environment_status` read-back: service `Offline`, no active deployment, no attached live volume.
- One staged environment patch remains pending (patch `67e44e6b-10ed-4523-95b8-888840ef2321`) with three reported changes: service resource update, `KEJYARBOT_DB_PATH` variable set, and volume resource update.
- The staged volume previously inspected is named `kejyarbot-data`, size 1 GB, staged-create and empty. It is not a restored copy of the existing Botkeep database.
- Service configuration's intended start command is `python bot.py`; no deployment has been triggered.

## Botkeep incident and source-of-truth gate

- PR #125 remains Open/Unmerged and its release boundary says not to merge or touch Botkeep until source-staging support clarifies recoverability and backup/database recovery is verified.
- The latest PR #125 timeline entries available in this check continue to describe the staging/recovery hold; no later support resolution was found in the retrieved timeline.
- The Botkeep source database's current authoritative path, exact file, backup timestamp, backup checksum, SQLite integrity result, row counts, and restore verification are not available in this environment.
- No Botkeep-native connector/tool is available in the current toolset to inspect or export that source database directly.

## Gate decision

**Do not accept the Railway staged patch or start the Telegram poller yet.** Although the owner authorized activation, committing the current staged patch would provision an empty volume and direct the bot to `/data/kejyar.db` without proof that the authoritative learner database has been restored. Starting a second poller while Botkeep may still be active also risks duplicate Telegram polling.

The next safe operation is to obtain the actual SQLite backup from the authoritative Botkeep environment, preserve the original untouched, and verify a copy read-only:

1. Record source identity, backup creation time, file size and SHA-256.
2. Run SQLite `PRAGMA integrity_check` and require `ok`.
3. Inventory tables/schema and row counts for users, progress, completions, quiz attempts/ledger, rewards and any other state-bearing tables actually present.
4. Restore a copy to the Railway volume at `/data/kejyar.db` while the service remains stopped.
5. Re-run integrity/schema/row-count checks on the restored copy and compare source and destination.
6. Obtain explicit confirmation that Botkeep's poller is stopped and the source remains preserved.
7. Only then commit the staged Railway changes and start exactly one poller; validate existing user progress and core Telegram flows.

## Actions deliberately not performed

- No Railway `accept_deploy`, deployment, restart, or Telegram polling start.
- No Botkeep Resume, Cancel/restore, Replace, Sync, or server restart.
- No creation of an empty replacement database as a substitute for the authoritative database.
- No change to lesson content, quizzes, answer keys, runtime, or `main`.
- No claim of a verified database backup or independent offsite backup.

This record is a pre-activation evidence register, not a claim that the robot is live.

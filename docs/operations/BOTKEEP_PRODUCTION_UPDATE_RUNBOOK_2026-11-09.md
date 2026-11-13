# KejyarBot on Botkeep — production update runbook
Last reviewed: 2026-11-13

## Purpose and safety boundary

KejyarBot is hosted on the existing Botkeep workload `KejyarBot-Test`. The objective is to update and reactivate that same workload, not migrate to another host.

This runbook is operational guidance, not evidence that a deployment has happened. Never claim the bot is online until Botkeep reports a confirmed healthy runtime and Telegram polling has been verified.

**Never use “Replace files” for the current recovery.** Do not delete/recreate the workload, overwrite the SQLite database, expose secrets, or change the hosting provider as part of routine recovery.

## Current verified release and hosting state (2026-11-13)

- Repository: `avasinim/KejyarBot`
- Intended Botkeep source branch: `release/main-based-reconciled-2026-11-11`
- Verified release head: `6fd58338b05a110262ddff32b3696a8df852d272`
- Botkeep GitHub tab previously showed the branch but still displayed the old linked-source revision `main` / `bdd08e6`; the current release head is `6fd5833` and has not been confirmed imported.
- Import mode selected: **Merge files** (overwrite matching files, retain other files/folders).
- The linked-source panel still showed the old `main` revision `bdd08e6` and last sync 2026-11-04 16:38:19 before the attempted sync.
- The attempted sync returned: `Source staging was interrupted. Existing application files were not changed. Resume or cancel the import.`
- Therefore the new source has **not** been verified as applied. Do not infer that a sync completed.
- Botkeep panel displayed Offline and “Waiting for a fresh runtime update. The displayed state is not yet confirmed.” This is not a confirmed live runtime state.
- Botkeep support incident: `#a1a7aa05`. A support escalation was sent on 2026-11-13 asking for Node17/Wings and GitHub staging investigation, current-commit comparison, recovery validation, and an ETA.
- A completed Botkeep backup exists: `KejyarBot_PreManualTransfer_2026-11-13` (8.4 MB); a local downloaded copy was confirmed. The backup snapshot was taken while the panel showed Offline.
- No Botkeep restart or successful source sync has been verified.

## Current release review hold (2026-11-13)

- The release branch contains the latest intended source revision `6fd58338b05a110262ddff32b3696a8df852d272`.
- Its four checked CI workflows pass, but this is not sufficient deployment approval.
- A source-level review found a likely regression: the new global academic-review gate treats every active course as requiring explicit approval, while the course adapters default missing review metadata to `draft_editorial_review`. This likely blocks lesson completion and rewards for Courses 2 and 3 and the two active Kurmanji courses. See PR #152's 2026-11-13 high-priority review comment. Do not sync this revision until the gate is corrected and the unaffected course paths are verified.
- The owner's intended media inventory is instructional text and images; no PDF or audio lesson files are expected. The release tree has 17 image/vector assets and no PDF/audio/video media. Preserve those image assets.
- The downloaded 2026-11-13 backup's inspected tar listing showed six root-level files; that partial listing does not prove nested image assets are included. Obtain a complete recursive backup inventory and Botkeep's live-file comparison before relying on it as a complete media recovery point.

## Verified repository runtime contract

- Project root: repository root (contains `requirements.txt` and `bot.py`)
- Botkeep runtime shown: Python 3.12
- Dependencies: `python-telegram-bot>=22,<23` and `python-dotenv>=1,<2`
- Expected start command: `python bot.py`
- Token environment variable: `TELEGRAM_BOT_TOKEN`; legacy `BOT_TOKEN` is also accepted
- SQLite default path: `kejyar.db` beside `database.py`, unless `KEJYARBOT_DB_PATH` is configured
- `bot.py` loads the project-root `.env` before importing `database.py`.
- The application uses Telegram polling; only one active polling process should use this bot token.

The code's default DB path does not independently prove which database path the live Botkeep process used. Keep the existing DB and Environment settings intact unless Botkeep support verifies the actual configuration.

## Backup and preservation

1. Keep the completed 2026-11-13 Botkeep backup and its downloaded local copy.
2. Never share or print `.env`, Telegram tokens, credentials, or secret values.
3. Never import a repository copy of `kejyar.db` over the existing server database.
4. Preserve server-only files and Botkeep configuration. The merge preview must be inspected before any further sync attempt.
5. Do not treat a successful archive inventory as proof of the live server's changed-file list.

## GitHub source update procedure

1. Confirm repository `avasinim/KejyarBot`, branch `release/main-based-reconciled-2026-11-11`, and the exact reviewed head. At this checkpoint, `6fd58338b05a110262ddff32b3696a8df852d272` is the current head but is **on review hold**; do not import it until the global academic-review gate regression is fixed and CI/source review passes.
2. Select **Merge files**. Never select **Replace files**. Do not use “Import into a folder” unless the runtime root/start command is deliberately reconfigured and reviewed.
3. Inspect the exact changed-file preview. Confirm that `.env`, `.botkeep`, `kejyar.db`, and existing server-only files are not overwritten or removed.
4. If source staging is interrupted, stop repeated retries. Record the exact message and ask Botkeep support to diagnose/recover the staging job and confirm whether it is safe to resume. The panel message stated existing application files were not changed; verify this with the provider.
5. Do not enable “Pull before Start / Restart” until the first manual sync has succeeded and the effect on local edits is understood.
6. After a confirmed sync, verify startup settings and dependencies before a separately planned restart.
7. Watch Console for successful initialization and Telegram polling. A panel status alone is insufficient.
8. Run controlled Telegram smoke tests: `/start`, course menu, Course 4 beta progression, quiz suppression, and no official XP/coins/chests/badges for beta lessons. Explicitly verify Courses 2 and 3 and both Kurmanji courses can still open, complete lessons, take their existing assessments, and receive expected rewards.
9. If startup or smoke tests fail, stop and use the verified backup/recovery path. Do not delete the workload or database while investigating.

## If the workload was uploaded as ZIP

Build a clean archive from the verified release branch. Include required runtime modules, `requirements.txt`, `bot.py`, and course data. Exclude `.env`, tokens, credentials, local environments, caches, and the production SQLite database. Preserve production data separately through a verified backup/restore process.

## Post-update verification

- Botkeep reports a confirmed healthy runtime.
- Console confirms Telegram initialization and polling.
- The existing bot responds to `/start`.
- Existing progress/data remain intact.
- Course 4 beta lessons remain clearly marked as beta review drafts.
- Beta completion does not grant official completion, XP, coins, chests, or badges.
- Quizzes remain unavailable for beta review drafts.
- Lesson 46 does not unlock or fabricate Lesson 47.
- Previously approved lessons and Courses 1–3 retain expected behavior.

## Historical note

The previous version of this runbook named `main` as the production source branch and described the workload as active. Those details are stale for the current recovery. The release branch and hosting state above supersede those historical statements.

## Official Botkeep references

- GitHub deployment guide: https://botkeep.cloud/docs/github
- Hosting and backup guidance: https://botkeep.cloud/docs/hosting
- FAQ (restart, backup, runtime state): https://botkeep.cloud/faq

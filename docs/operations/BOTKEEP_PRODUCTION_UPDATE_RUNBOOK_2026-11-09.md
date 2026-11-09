# KejyarBot on Botkeep — production update runbook
Date: 2026-11-09

## Purpose and safety boundary

KejyarBot is already hosted and active on Botkeep, as confirmed by the project owner. This document records a safe update procedure for the existing Botkeep workload. It is not a deployment instruction and does not authorise a restart, replacement, deletion, token rotation, or hosting migration.

**Never move this bot to another host as part of routine Course 4 work.** Do not stop or recreate the existing Botkeep workload merely to apply a code update.

## Verified repository runtime contract

- Repository: `avasinim/KejyarBot`
- Intended production source branch: `main`
- Project root: repository root (contains `requirements.txt` and `bot.py`)
- Runtime: Python 3.10 or newer (use a Python version offered by Botkeep and compatible with the project)
- Dependencies: `python-telegram-bot>=22,<23`
- Start command: `python bot.py`
- Token environment variable: `TELEGRAM_BOT_TOKEN`; legacy `BOT_TOKEN` is also accepted
- SQLite database path: `kejyar.db` in the project root (resolved relative to `database.py`)
- The application uses Telegram polling; keep a single active polling process for this bot token.

## Pre-update checklist (mandatory)

1. Open the existing Botkeep workload and confirm its current state is running/healthy from observed panel data and recent console output. Do not infer health solely from a successful deploy/import acknowledgement.
2. Record the currently deployed source revision or uploaded archive/version, if Botkeep exposes it.
3. Create a completed Botkeep backup and download an independent copy of the backup. Confirm the backup completed successfully before proceeding.
4. Preserve a separate copy of the currently deployed source/configuration. Never rely on the Botkeep backup as the only copy.
5. Confirm `TELEGRAM_BOT_TOKEN` (or the legacy `BOT_TOKEN`) is configured in Botkeep Environment. Do not print, copy into chat, commit, or include the token in an archive.
6. Confirm the Botkeep workload uses one process and the expected command `python bot.py`.
7. Review the proposed GitHub diff. Do not apply unrelated changes or overwrite the live SQLite database with a blank development database.

## GitHub source update procedure

If the existing Botkeep workload is connected to GitHub:

1. Confirm the selected repository is `avasinim/KejyarBot`, branch `main`, and project root is the repository root.
2. In Botkeep's GitHub tab, preview the pending revision and inspect the changed-file list.
3. Confirm the revision includes the intended merged commit and no unexpected source/data deletion.
4. Only after the pre-update checklist is complete, apply the source update.
5. Choose restart only in the planned maintenance window, understanding that Botkeep documents this update/restart path as not zero-downtime.
6. Watch the Botkeep Console until the Telegram application initialises and polling starts successfully.
7. Test the existing bot in Telegram with a controlled account. Verify /start, course menu, Course 4 lesson 31→32→33 beta progression, beta quiz suppression, and no XP/coin/chest/badge award for beta completion.
8. Verify approved lessons and Courses 1–3 still behave normally.
9. If startup or smoke tests fail, use Botkeep's recovery options and the verified pre-update backup. Do not delete the workload or database while investigating.

Botkeep's documentation states that GitHub source updates are previewed/applied in the GitHub tab, restart is a separate choice, and optional pull-on-start/push updates must be enabled explicitly. Do not enable automatic update/restart until the owner has approved that operating model and backup/rollback has been tested.

## If the workload was uploaded as ZIP

Build a clean archive from the verified `main` source. Include `requirements.txt`, `bot.py`, `database.py`, course data and all runtime modules. Exclude `.env`, tokens, credentials, local virtual environments, caches and editor metadata. Treat ZIP import as a source revision; separately preserve and restore the production `kejyar.db` only through a verified backup/restore process. Do not replace a populated production database with an empty file.

## Post-update verification

- Botkeep reports the workload running, and console output confirms Telegram initialization and polling.
- The existing Telegram bot responds to /start.
- Existing learner progress remains intact after the update.
- Course 4 Lessons 32–46 are visibly identified as beta review drafts.
- Beta completion records beta progress only; it does not award official completion, XP, coins, chests or badges.
- Quizzes remain unavailable for beta review drafts.
- Lesson 46 does not unlock or fabricate Lesson 47.
- Courses 1–3 and previously approved lessons retain their prior behavior.

## Current verified code state (2026-11-09)

- Course 4 beta progression implementation was merged into `main` in commit `755d1d9e6dc98d06b187638ce627bb09848c1c2b`.
- Pre-merge CI passed: Python compilation and full unittest suite (476 passed, 11 skipped), including the Course 4 beta review safety workflow.
- No Botkeep deployment or live Telegram smoke test was performed by this code change.
- The owner confirms that the bot is already active on Botkeep; the exact Botkeep workload settings, selected source revision, persistence configuration, and live runtime state have not been independently inspected from the hosting panel.

## Official Botkeep references

- GitHub deployment guide: https://botkeep.cloud/docs/github
- Hosting and backup guidance: https://botkeep.cloud/docs/hosting
- FAQ (restart, backup, runtime state): https://botkeep.cloud/faq

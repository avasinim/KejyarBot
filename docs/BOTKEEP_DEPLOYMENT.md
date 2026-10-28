# Botkeep deployment checklist for KejyarBot

This guide is for a **separate test deployment**. It does not authorize a production Telegram bot launch, merging a pull request, or changes to `main`.

## Repository and branch

- Repository: `avasinim/KejyarBot`
- Development branch: `fix/four-course-structure-2026-10-27`
- Project root: repository root (the folder containing `bot.py` and `requirements.txt`)
- Runtime: Python
- Install command: `python -m pip install -r requirements.txt`
- Start command: `python bot.py`

Do not deploy from `main`: it does not contain the current four-course development state.

## Prepare the ZIP upload

From the repository root on the development branch, run:

```powershell
python .\tools\prepare_botkeep_zip.py
```

The script creates `KejyarBot-Botkeep-Source.zip` beside the repository folder and checks Botkeep's limits before writing it (fewer than 200 files and less than 5 MiB uncompressed). It includes runtime Python modules, JSON course data, and text-based SVG assets. It excludes `.env`, SQLite databases, test/docs folders, old backup scripts, and binary audio files. Do not manually add secrets or a local database to the ZIP.

### Preserve the existing prerecorded voice

Botkeep's ZIP uploader rejects binary files, so the existing MP3 recordings are intentionally not included. After the server is provisioned and SFTP access is available, upload the existing `voices/` directory (including `kejyar.mp3`, `lesson_start.mp3`, `lesson_done.mp3`, and `reward.mp3`) to the server's project root without renaming or replacing the recordings. Confirm the remote files exist before starting the bot. Do not substitute newly generated audio. The current repository's four event MP3 files are byte-identical; this is known and must not be silently changed.

## Environment variables

Add secrets in Botkeep's Environment/Secrets settings; never commit them to GitHub.

- `TELEGRAM_BOT_TOKEN`: use a **separate test bot token** for the first deployment, not the production bot token.
- `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`: keep dynamic speech disabled.
- `KEJYAR_DB_PATH`: set only after confirming Botkeep's documented persistent-storage mount path; if a persistent volume is available, point this variable to a database file on that volume (for example, `/data/kejyar.db` only if Botkeep actually mounts persistent storage at `/data`).

Do not add ElevenLabs credentials while dynamic speech is disabled.

## Before starting the service

1. Confirm Botkeep's filesystem/database persistence behavior. Student progress, XP, and quiz records are stored in SQLite; an ephemeral filesystem can lose that data after a rebuild or restart.
2. Use only a test Telegram bot token until deployment health, restart behavior, and persistence are verified.
3. Ensure only one running service polls a given Telegram bot token. Do not run the same token locally and in Botkeep at the same time.
4. Start one worker only. Do not enable extra replicas for a polling bot.
5. Confirm courses 2 and 3 remain drafts and are not exposed to learners.
6. Check Botkeep logs for startup errors, then test `/start`, lesson access, quiz callbacks, daily chat, and a restart using the test bot.
7. Confirm the welcome voice is sent from `voices/kejyar.mp3`; verify the audio files remain present after a restart before considering voice delivery complete.

## Safety boundary

A successful GitHub connection or Botkeep project creation is not the same as a verified live deployment. Do not merge PRs, change `main`, or switch to the production Telegram token without explicit approval.

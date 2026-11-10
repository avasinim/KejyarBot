# Botkeep Hosting Compatibility and Recovery Review — 2026-11-10

## Scope
Botkeep is the selected hosting target for KejyarBot. Railway is explicitly out of scope for this recovery path. This review uses public Botkeep documentation/status evidence and repository source already inspected; it does not access the user's authenticated Botkeep panel or server filesystem.

## Verified Botkeep requirements and compatibility
- Botkeep's GitHub deployment guide accepts Python projects with `requirements.txt` at a predictable project root and a non-interactive start command. It requires an explicit repository/branch/root selection and says to review the detected runtime and startup command.
- Botkeep's GitHub update flow supports previewing changed files and selecting whether to restart. Its documentation explicitly says this is not a zero-downtime build-and-swap pipeline and that recovery options remain available if an import fails.
- KejyarBot's repository root contains `requirements.txt`; its main entry point is `bot.py`, and `main()` calls `app.run_polling()`. The expected start command for this repository is therefore `python bot.py`, subject to confirming the actual Botkeep project root and Python runtime setting in the panel.
- The code reads `TELEGRAM_BOT_TOKEN` or `BOT_TOKEN` from the process environment and raises a clear startup error if neither exists. The live Botkeep secret values cannot be inspected from repository access.
- Botkeep documentation says runtime credentials belong in Environment/secrets, not Git history. The repository `.gitignore` excludes `.env`; this is appropriate, but does not establish that Botkeep currently has the correct token configured.

## Important recovery-state finding
- The previously reported server state is an individual GitHub restore operation stuck at `Restoring the previous files` / `The update is paused` / `Infrastructure operation failed. Staff review or explicit retry is required.` This is not equivalent to a normal application crash. Do not issue another import, retry, cancel/restore, redeploy or restart while the operation is unresolved.
- Botkeep's documentation says failed imports have recovery options, but the exact available recovery action and safety of the user's in-progress operation cannot be inferred from public docs. Staff should inspect and resolve the stuck operation while preserving the current server files and data.
- The public machine-readable status snapshot retrieved for this review was generated at 2026-11-09 15:46:44 UTC, more than a day before this review. Its freshness window is 180 seconds, so it is stale and cannot establish Botkeep's live platform health at review time.
- In that snapshot, Console/WSS and Files/SFTP were marked unknown (manual verification), so public monitoring cannot verify the exact management channels needed to inspect this user's server.

## Safe next steps (read-only until support confirms recovery)
1. Wait for Botkeep support to confirm the infrastructure operation's state and the safe recovery path; ask them to preserve the server's current files and data.
2. After support confirms the operation is cleared, inspect the Botkeep Files view and Console output before any restart or source import.
3. Confirm the selected GitHub repository, branch and project root; confirm Python runtime and `python bot.py` start command.
4. Verify the Telegram token exists as a Botkeep environment secret without exposing it in chat, logs, GitHub or support messages.
5. Before any restart or update, obtain and download a completed successful Botkeep backup and keep an independent copy. Botkeep's FAQ says only completed successful backups count as recovery points and recommends independent copies.
6. Start only one polling process for this Telegram token; do not create a second active bot instance.

## Limitations
No authenticated Botkeep account, server panel, file manager, console, environment secret, support ticket status, or server-side backup was accessible in this review. No operational action was taken. No claim is made that the server files or SQLite user database are currently safe or backed up.

No Railway configuration, deployment, code, database or Botkeep server state was changed.
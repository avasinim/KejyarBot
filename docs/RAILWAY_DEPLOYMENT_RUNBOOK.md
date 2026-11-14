# KejyarBot — production migration and Railway runbook

## Scope
This runbook prepares the reviewed release candidate for Railway production without changing the live Botkeep project. The application must be deployed from the reviewed release branch, not from the infrastructure-only branch or an unreviewed draft.

## Runtime configuration
- Python 3.12; install dependencies from `requirements.txt`.
- Start command: `python bot.py`.
- Persistent volume: mount at `/data`.
- Database path: `KEJYARBOT_DB_PATH=/data/kejyar.db`.
- Existing secret: `TELEGRAM_BOT_TOKEN`; never print, copy into logs, or commit it.
- Keep exactly one polling process active for each Telegram bot token.

## Database safety and cutover
1. Identify the authoritative learner database and its current host. Do not assume the test database is the production database.
2. Obtain a fresh, consistent SQLite backup from the authoritative database while its writer is stopped or using a documented SQLite-consistent backup method.
3. Verify the backup read-only: `PRAGMA integrity_check`, schema, user-row counts, progress/quiz/reward ledgers, and file size. Preserve the source database and every prior backup.
4. Confirm the Railway `/data` volume is provisioned and that `/data/kejyar.db` contains the verified database before starting the bot. An empty volume is not a valid production database.
5. Confirm the previous host is stopped for this production token before starting Railway. Never run two pollers with the same token.
6. Deploy the exact reviewed commit and verify the running commit SHA and one healthy replica.
7. Run Telegram end-to-end checks: `/start`, menus, lesson reading, search and pagination, Beta labels/progress, official quiz eligibility, reward idempotency, and persistence after restart.
8. Keep the original database, backup, and previous host recoverable until all acceptance checks pass.

## Learner-content release gates
The application must preserve explicit academic approval gates. Approved lessons may use official assessment/reward paths. Review-only material may appear only through the clearly marked Beta/reading/practice paths; it must not grant official quiz eligibility, XP, coins, chests, badges, or official completion. Missing or unknown review status fails closed.

## Do not do
- Do not start the poller against an empty volume.
- Do not overwrite, reset, or delete the authoritative database or existing backups.
- Do not run Botkeep and Railway simultaneously with the same Telegram token.
- Do not treat passing GitHub CI as proof of live Telegram acceptance.
- Do not activate all review-only lessons as official assessed content.

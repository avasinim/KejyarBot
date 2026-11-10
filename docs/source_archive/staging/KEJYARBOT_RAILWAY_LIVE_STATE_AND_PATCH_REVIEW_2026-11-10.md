# KejyarBot Live Railway State and Staged Patch Review — 2026-11-10

## Read-only state check
Project melodious-enthusiasm, production environment, service KejyarBot. Checked through Railway read-only environment inventory, environment health, service description, staged-change detail, deployment history, and available build/deploy logs. Also fetched GitHub PR #141 metadata.

## Current production state
- Service state: OFFLINE. No active deployment or running replica is reported.
- One unresolved critical notification is reported by Railway; the health summary does not expose its detail.
- No live volume is attached. The only volume, kejyarbot-data (1024 MB, ams, mount /data), is staged-create and therefore is not provisioned/live.
- No latest deployment is present. The newest listed deployment was created 2026-08-20 and is REMOVED. Historical build logs exist, but there are no current runtime deploy logs to inspect.
- The service has a staged patch with 10 changes; it remains STAGED, not applied.

## Staged patch review
The patch is reported as non-destructive by Railway. It would:
- Change source branch from main to infra/railway-persistent-db-2026-11-10.
- Add start command python bot.py and restart policy ON_FAILURE with 10 retries.
- Create and mount the new 1 GB volume at /data in ams.
- Add KEJYARBOT_DB_PATH (value redacted by Railway).
- Preserve TELEGRAM_BOT_TOKEN as an existing variable name; secret values are not exposed.
Although the patch is marked non-destructive, accepting it would provision infrastructure and trigger a deployment. It was not accepted.

## GitHub PR #141
- PR remains open and draft, base main, head infra/railway-persistent-db-2026-11-10.
- The PR description explicitly says not to merge/deploy until the authoritative Botkeep DB has been backed up, integrity-checked, and restored to /data/kejyar.db, and Botkeep is confirmed stopped.
- The PR description's validation paragraph reflects the PR creation snapshot and says tests had not yet run at that time; this inspection does not reinterpret it as a current CI status.

## Operational assessment
1. Production is not running, so current Telegram behavior cannot be validated from Railway runtime logs.
2. The staged volume is not an existing backup and is not yet available to the service.
3. The staged branch switch from main to a temporary infra branch is a deployment-maintenance risk if left as the long-term source.
4. The unresolved critical notification needs detail from Railway's notification/monitor view; the current summary only exposes its count.
5. The authoritative Botkeep database remains unlocated and unverified. No Botkeep account connector or read-only filesystem/backup retrieval tool is available in this inspection.

## Actions not performed
No staged changes accepted, no volume provisioned, no source branch changed live, no deploy/restart/rollback, no DB access or restore, no Botkeep retry/cancel, no PR merge, and no Telegram polling.
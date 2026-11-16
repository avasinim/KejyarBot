# Altare provider documentation and target compatibility audit — 2026-11-14 14:26Z

## GitHub source / CI state
Repository: `avasinim/KejyarBot`
Release branch: `release/main-based-reconciled-2026-11-11`
Audited source revision: `88a705fc80009dda4bcf3f6c406c5b5f3589baad`
The branch head matched this revision during inspection.
All 10 GitHub Actions runs associated with this revision completed successfully.

## Official Altare documentation findings
Checked current official Altare help/documentation:
- Generic Python runtime is supported; code and `requirements.txt` are uploaded using the file manager, and the Startup setting controls the command/main file.
- Altare states its Always Free servers do not sleep when idle.
- Altare states there is no built-in database for app hosting and that file-based SQLite works well on one server.
- Startup template variables are passed as environment variables. If a template does not expose a needed variable, Altare documents putting it in a root `.env` file and loading it with `python-dotenv`.
- Always Free team pool is 6 GB RAM, 150% CPU, 10 GB disk, and up to 4 server slots, shared across team apps.
- Altare distinguishes per-app file backups from offsite snapshots; scheduled automatic backups and daily snapshots have separate configuration/cost/slot behavior.

## Relevance to KejyarBot
- Source requirements are Python dependencies and the documented startup command is `python bot.py`.
- Source accepts `TELEGRAM_BOT_TOKEN` (or legacy `BOT_TOKEN`) and supports `KEJYARBOT_DB_PATH`.
- A root `.env` is a documented alternative if Altare's template does not expose custom variables. Secret must remain private and out of Git.
- SQLite is plausible on this single-server workload, but actual data persistence still depends on the app's file storage lifecycle and correct backup configuration. The provider documentation reviewed does not prove the existing KejyarBot app currently has a correct persistent DB file or restore point.
- The app's actual Startup variables, file tree, resource allocation, backup status, and source files still require direct panel inspection. Previously observed state: app files page was empty except a manually created `/course_data` folder; no source package was uploaded; `GIT_ADDRESS` was blank and `AUTO_UPDATE=0`. This audit did not revisit or mutate the panel.
- The official generic web-app guide discusses binding a web service to a port; KejyarBot is a Telegram polling worker, so do not add a web server or port listener merely to satisfy the generic web-app guide. A Python worker/bot-specific guide or provider confirmation is needed if the template imposes a port requirement.

## Explicitly not done
No Altare console/API operation, file upload, environment change, token entry, backup/snapshot creation, server start/restart, Git sync, deploy, database migration, or provider-side test was performed.
No source asset or runtime code was changed in this checkpoint.

## Safe next steps
1. Confirm the Altare Python template can run a long-lived Telegram polling worker without a required inbound HTTP listener.
2. Inspect the actual app file-storage/backup semantics and ensure the SQLite path is within durable app storage.
3. Prepare a complete source package from the reviewed release SHA, excluding secrets, databases, caches, and non-approved assets.
4. Only after user approval and independent DB/backup gates, configure secret and persistent DB path and test in isolation. Do not start a second poller with the production token while Botkeep may still own it.

# Active KejyarBot deployment target — 2026-11-16

## Authoritative project scope

The active bot for ongoing project work is the main **KejyarBot** deployment on **Altare**, app name `kejyarbot`.

- Altare app: `kejyarbot`
- Altare app/server identifier: `67a1d06e-aae9-48fc-a482-c4accfce2423`
- Runtime reported by the owner: Python 3.12, entrypoint `bot.py`
- `AUTO_UPDATE=0`: GitHub changes do not automatically deploy to this app.
- The owner reports that this main Altare app is active.

## Explicitly out of scope

`KejyarBot-Test` on Botkeep is no longer the target for project work. Do not inspect, restore, start, restart, deploy to, or otherwise spend effort on that test workload unless the owner explicitly reopens it.

Historical Botkeep notes remain historical records only; they must not be interpreted as the current production target.

## Daily monitoring robot

The owner wants the daily monitoring function associated with the main `kejyarbot` deployment, not the abandoned test workload.

At this checkpoint:
- The Altare app being active is owner-reported.
- The actual Altare Schedules configuration and successful daily execution are **not yet independently verified**.
- Do not claim that daily monitoring is running until the schedule and a successful execution are confirmed.
- Inspecting the Schedules page is read-only. Do not create or edit schedules, change files or environment variables, or start/restart the app without explicit approval.

## Preservation and deployment safety

- Keep all existing course content, images, learner records, SQLite data, and progress.
- GitHub review branches and draft pull requests are source-review work only; they do not update Altare because auto-update is disabled.
- Do not merge or deploy without explicit owner approval.
- Before any production update or restart, verify the exact persistent SQLite database path and an independently restorable backup. Preserve applicable SQLite WAL/SHM state or use a consistent SQLite backup.
- Never expose or request Telegram tokens in chat.

This is an append-only operational clarification. It does not modify the Altare app, its files, schedules, environment, database, or runtime.

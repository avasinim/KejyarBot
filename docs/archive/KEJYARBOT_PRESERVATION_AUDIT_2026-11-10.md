# KejyarBot preservation audit — 2026-11-10

## Library inventory
A recursive, paginated ChatGPT Library inventory completed on 2026-11-10.
It returned 186 items across files and folders, with no remaining cursor and no warnings.
The detailed audit record is also stored in the ChatGPT Library at:
`/KejyarBot/Safety_Archive_2026-11-10/KEJYARBOT_PRESERVATION_AUDIT_2026-11-10.md`

## Preserved material located
- Course 4 append-only lesson patches and ZIP packages, including lesson-specific records for lessons 1–45.
- Consolidated Course 4 archives/checkpoints, including lesson 29–45 checkpoints and 46-lesson review material.
- Book-based review/addenda for lessons 1–9, source transcription, appendix coverage/review records, and Kurdish morphology reference PDF.
- Runtime policy, schema, callback/review gate, patch loader, renderer, regression, integration, and restructure artifacts.
- Source snapshots including bot.py, course_lesson_adapters.py, courses.txt, and grammar_course4_lessons.txt.
- Related image/chart assets and pasted source snapshots.

## Remote and live-data exclusions
- This index does not mirror the full repository or all remote branches.
- It does not contain a verified live Botkeep filesystem snapshot or SQLite database backup.
- The Botkeep GitHub restore operation is still unresolved; do not retry, resume, unlink, restart, or restore without support guidance.
- Railway preparation PR #141 remains draft and unmerged. No deployment or Telegram bot activation is authorized by this archive.
- The Railway persistent volume must not be used until a verified database backup is restored and Botkeep is confirmed stopped.

## Preservation policy
- Append new snapshots only; never overwrite or delete existing lesson archives.
- Keep original lesson content intact.
- Verify SQLite backups read-only with integrity_check, schema inspection, and table row counts before any migration.
- Never run two Telegram polling instances using the same bot token.

This file is an index, not a claim that unavailable remote/live data has been backed up.

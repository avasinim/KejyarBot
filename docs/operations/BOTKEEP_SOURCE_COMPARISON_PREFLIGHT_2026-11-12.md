# Botkeep source comparison preflight — 2026-11-12

## Scope and exact references

- Botkeep-reported currently linked GitHub revision: `bdd08e6` (support's prior incident note).
- Proposed import revision checked by Botkeep: `f5142caf85d78ec2dc8dcb12b0d288d085254de3`.
- GitHub compare URL: https://github.com/avasinim/KejyarBot/compare/bdd08e6...f5142caf85d78ec2dc8dcb12b0d288d085254de3
- Botkeep's email confirms archive inventory only: 444 files / 12,405,342 bytes; no PDF, audio, `kejyar.db`, `.env`, or `.botkeep`; `/voices` empty.

## GitHub-to-GitHub comparison (not a live-server diff)

The repository comparison reports:
- 273 commits ahead, 0 behind.
- 271 changed paths: 247 added, 24 modified.
- Largest source changes include `bot.py` (+558/-82), `arami_course1_telegram.py` (+180/-37), `arami_lesson1_telegram.py` (+65/-19), `arami_lesson5_telegram.py` (+62/-20), `database.py` (+58/-1), and `courses.json` (+54/-3).

This is a comparison between two Git revisions only. It does **not** establish which files differ on the live Botkeep filesystem, because server-side edits, generated files, or a different deployed revision may exist. Botkeep support explicitly says the live path comparison is still pending.

## Critical database-path ordering finding

At proposed revision `f5142caf`, `bot.py` imports `database.py` before it calls `load_dotenv(BASE_DIR / ".env")`. In `database.py`, `DB_NAME` is resolved at import time from `KEJYARBOT_DB_PATH`, falling back to project-local `kejyar.db`.

Consequently:
- If Botkeep's Environment panel already supplies `KEJYARBOT_DB_PATH`, that host variable is present before imports and should take precedence.
- If the path is supplied only by the workload's `.env`, the current `f5142caf` import order can resolve the fallback path before dotenv loads the file.
- The live Botkeep Environment value and actual populated database path have not yet been verified. Do not infer either from the repository or the runbook.

PR #153 is a separate draft branch based on `f5142caf`. It moves dotenv loading before the database import, adds a regression test, and records the backup/path safety gate. The PR is not merged. Botkeep's verified archive currently points to `f5142caf`, so it does not include that fix yet.

## Required gate before any update

1. Botkeep must produce a fresh, completed, independently verifiable recovery copy of the current workload and the actual populated `kejyar.db`.
2. Support must compare the candidate archive paths against the live server file list and report every overwrite/addition, with special attention to `bot.py`, `database.py`, course data, and local-only files.
3. The effective `KEJYARBOT_DB_PATH` must be confirmed without exposing secrets, and the target DB must be verified as the populated production database. If uncertain, stop.
4. Resolve whether PR #153 should be incorporated into a revised release candidate after backup/path verification; do not assume the current `f5142caf` archive contains the fix.
5. No import, resume, apply, restore, reset, migration, or restart until the owner has reviewed the backup evidence and live-path comparison and explicitly approved the operation.

## Current state

- Botkeep support reports no active import or restore and says deployment remains on hold.
- Fresh verified recovery copy: pending.
- Live server path comparison: pending.
- Effective production database path and identity: unverified.
- PR #153: draft, open, unmerged.
- No production files, database, or hosting settings were changed by this preflight.

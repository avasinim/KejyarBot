# Botkeep runtime working-directory and filesystem-write audit — 2026-11-10

## Scope
Read-only scan of all non-test Python files on repository `main` for file reads/writes, runtime path assumptions, and Botkeep working-directory sensitivity. No production code or Botkeep server was changed.

## Findings
- Active startup in `bot.py` uses `BASE_DIR = Path(__file__).resolve().parent` and its `load_json()` helper resolves JSON inputs relative to that directory. Active Arami course readers likewise receive `BASE_DIR` and resolve source files under the project root. Latin course reader uses a path rooted from its configured base directory.
- The inspected non-test runtime Python files show no application-level writes to lesson/course JSON, source text, or local image assets. The expected durable write path identified in this scan remains SQLite in `database.py`, at `BASE_DIR / "kejyar.db"`. Botkeep-side logs/metadata are outside this repository-code scan.
- `ai_tutor.py` contains a module-level `open('dictionary.json', ...)`, which depends on the process current working directory. However, the inspected `bot.py` does not import or reference `ai_tutor`, `answer_word`, or `find_word`; therefore this is an isolated/unused-module path defect in the inspected active entry point, not evidence of a current startup failure. If this module is activated later, it should resolve the dictionary relative to `Path(__file__).resolve().parent`.
- `bot_backup.py` also uses relative paths, but it is a legacy snapshot and is not imported by the active `bot.py` path in the inspected source.
- Runtime lesson and course data are read-only source assets in the inspected code paths; the scan found no writes to them.
- SQLite connections are the runtime persistence mechanism. Existing progress/rewards remain dependent on the actual `kejyar.db` file being preserved by the host.

## Operational conclusion
- The main working-directory dependency appears controlled for active course/content reads through `BASE_DIR`.
- The strongest unresolved operational risk remains SQLite placement inside the project source directory and unknown Botkeep restore semantics.
- No basis exists to assert that the live Botkeep SQLite file currently exists, is intact, or is backed up.

## Safe handling
- Do not retry/cancel/continue the stuck GitHub restore, restart, redeploy, or restore files until Botkeep support resolves the operation and confirms preservation.
- Require a completed Botkeep backup that explicitly includes `kejyar.db`, plus an independent copy, before any operation that can replace project files.
- Once support confirms recovery, inspect the file manager read-only and verify the database file before any restart. Do not expose token values while checking environment configuration.

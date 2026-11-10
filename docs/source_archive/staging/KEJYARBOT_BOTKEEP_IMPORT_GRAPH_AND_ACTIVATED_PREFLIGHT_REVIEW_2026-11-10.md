# Botkeep runtime import graph and activated-course preflight review — 2026-11-10

## Scope
Read-only inspection of the active `main` entry point, its directly imported project modules, activated-course startup validator, and tracked runtime assets. No lesson text was reviewed or modified, and no server operation was performed.

## Verified findings
- Every direct project-module import found in the active `bot.py` import block has a corresponding tracked Python source file in the repository tree. The imported third-party Telegram package is declared in `requirements.txt` as `python-telegram-bot>=22,<23`.
- Active runtime course/data readers inspected use a stable project-root path (`BASE_DIR` passed by `bot.py`, or `Path(__file__).resolve().parent` in the Latin runtime) rather than depending on the process current working directory.
- Arami course readers construct their data paths under the supplied project root and `course_data/`.
- The Arami infographic sender checks that a requested image path stays within the project root and exists before opening it. The six assigned Course 1 PNG files (Lessons 1–4, 6, and 7) are present in the tracked repository tree.
- Startup validation is intentionally strict: it checks the activated Arami course manifest, banks, lesson 1 and lesson 5 assets, and then checks activation and expected lesson counts for daily conversation (42), unified orthography (66), Latin orthography (12), Latin grammar (12), and grammar (46). It also checks lesson/quiz presence, with an explicit owner-review-pending exception for grammar quizzes.
- Consequence: a missing or invalid required data file, inactive required course, unexpected lesson count, or unapproved empty quiz can stop the whole bot before database initialization and Telegram polling. This is a fail-fast readiness gate, not proof that any such file is currently missing.
- The active Telegram application is built with the declared python-telegram-bot API, registers command/callback/message handlers, then invokes `run_polling()`. No custom application error handler or persistent ConversationHandler/Telegram persistence backend was found in the inspected entry point. Transient `context.user_data` sessions therefore should not be treated as durable across process restarts.

## Botkeep implications
- Keep the configured project root intact: the startup validator depends on multiple root-level modules and JSON/Markdown/image assets, not only `bot.py` and `requirements.txt`.
- Before any file replacement or restore, verify the complete project tree and a separate successful SQLite backup.
- If Botkeep support confirms the stuck restore is cleared, inspect startup console output first and verify the active runtime and asset tree before considering a restart.
- Ensure only one active polling process uses the Telegram token.

## Limitations
- Repository-tree presence is not a live Botkeep filesystem check.
- No Botkeep environment, installed package version, console logs, running process, database file, or backup artifact was accessible.
- No production source, lesson, database, or hosted service was changed.

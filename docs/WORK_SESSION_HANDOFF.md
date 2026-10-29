# KejyarBot — Work Session Handoff

**Date:** 2026-10-28  
**Purpose:** Safely pause work and resume from this checkpoint in the next session.

## Active workspace and safety boundary

- Repository: `avasinim/KejyarBot`
- Working branch: `fix/four-course-structure-2026-10-27`
- This is a test-branch checkpoint only.
- Do not merge to `main`, deploy, change the production bot/token/service, or touch production data without the user's explicit permission.
- Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`. Do not replace the existing woman's voice or modify voice files.
- Do not edit lesson language/content or orthography unless the user specifically asks; the user will identify content issues for correction.
- Course 1 follows the user's specified source/orthography for the bot and must not be confused with the separate Avasin website orthography.

## Work completed / verified

- Four-course manifest is documented in README:
  - Course 1 — introductory orthography: 22 lessons.
  - Course 2 — daily conversation: 12 lessons.
  - Course 3 — unified orthography: 12 lessons.
  - Course 4 — grammar: planned, with no active lessons.
- Runtime course separation, lesson unlocking, namespaced lesson IDs for courses 2 and 3, quiz callback validation, duplicate reward prevention, startup token guard, speech quota checks, and Botkeep packaging have dedicated tests.
- The catalog warns that courses 2 and 3 are technically available for owner testing on this branch while their editorial review remains unfinished.
- Branding check: runtime course-one lesson headers and the lesson-one infographic caption use **کەژیار**.
- A failed branding test had searched the entire lesson body and accidentally matched a linguistic example in lesson 18. The test was narrowed to inspect the actual lesson header only; lesson content was left untouched.
- CI for commit `0ee813a99468d1b3bc04c97b7dc58cd5ddd0f69b` succeeded: https://github.com/avasinim/KejyarBot/actions/runs/40756095356
- Handoff documentation commit `661d8f257790236ed63013bf562e709161000abf` also passed CI: https://github.com/avasinim/KejyarBot/actions/runs/40756398723
- Latest verified test-branch commit at the start of the 2026-10-28 session: `661d8f257790236ed63013bf562e709161000abf`.
- Recent CI run for the test that only blocks direct callbacks to planned courses also succeeded: https://github.com/avasinim/KejyarBot/actions/runs/40755119546

## Remaining work for the next session

1. Re-check the current branch head and latest GitHub Actions result before making further edits.
2. Continue a focused technical audit of course navigation, progress persistence, quiz/reward idempotency, and the Botkeep ZIP contents; add or fix tests only where a concrete gap is found.
3. Keep all changes on the test branch, and re-read changed files after edits.
4. Report clearly what is verified versus still pending. Do not claim production readiness just because CI passes.
5. Do not create or upload the Botkeep package, change the running bot, or deploy unless specifically authorized.
6. Keep infographics as a later task, after lesson intake/content work; do not interrupt technical stabilization with new image design.

## Safe local test commands

From the project directory, with the project's virtual environment activated:

```powershell
python -m unittest discover -s tests -v
python -m compileall -q .
git diff --check
git status --short --branch
git log -5 --oneline --decorate
```

If the project uses its Windows virtual environment, prefer:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Do not commit local secrets, `.env`, SQLite databases, backups, or generated runtime data.

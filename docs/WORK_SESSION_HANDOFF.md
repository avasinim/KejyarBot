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


## Continuation checkpoint — 2026-10-29

- Latest verified test-branch commit: `2465e230cbe719a1ee7f270725cbc9ec60977e79` (`test: guard lesson infographic SFTP packaging rule`).
- CI succeeded for that commit: https://github.com/avasinim/KejyarBot/actions/runs/40822621759. The run completed the compileall and full unittest steps successfully.
- The root image `photo_2026-10-27_00-13-52.jpg` is tracked in the development branch and is the optional Course 1, Lesson 1 infographic. `tools/prepare_botkeep_zip.py` intentionally excludes JPG/binary files; the image must be transferred separately by SFTP after the server exists. The lesson text is designed to remain available if the image is absent.
- `docs/BOTKEEP_DEPLOYMENT.md` now states this correctly. `tests/test_botkeep_packager.py` includes a guard asserting that the exact image exists in the repository but is excluded from the ZIP package.
- No ZIP was created or uploaded. No production service/token/data was changed, no merge/deployment occurred, and dynamic speech remains disabled unless the user explicitly approves otherwise.
- Next safe work: continue focused review of course navigation, progress persistence, quiz/reward idempotency, and package constraints; make only evidence-based changes on this test branch and verify CI after each change.

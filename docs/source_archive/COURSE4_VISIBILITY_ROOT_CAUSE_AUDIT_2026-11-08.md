# Course 4 Visibility Root-Cause Audit — GitHub, Botkeep, Telegram

Date: 2026-11-08
Working branch inspected: `feat/course4-clean-port-main-20261106`
Scope: KejyarBot Course 4 (Grammar) only.
Status: Read-only diagnosis and documentation; no deployment or runtime mutation.

## Executive finding

The strongest confirmed cause is a **source-branch mismatch**.

- GitHub's `main` branch does not contain an active Course 4 record in `courses.json`, and its `bot.py` does not load `course_data/grammar_course4_lessons.json`.
- The working branch `feat/course4-clean-port-main-20261106` contains the Course 4 loader, an active `grammar` course record, and 31 contiguous lesson records.
- The prepared branch `deploy/course4-safe-20261108` also contains the Course 4 loader, active manifest entry, and the same 31-lesson runtime file.
- The previously reviewed Botkeep connection showed the linked source branch as `main` (source configuration recorded in the prior handoff audit). Therefore Botkeep would continue to import/run the branch that lacks Course 4, even though the course exists on the other branches.

This explains why the course can be present in a working/deploy branch yet absent from the default GitHub view and from the Botkeep-backed Telegram bot.

## Evidence

### 1. GitHub main

- `courses.json`: no course with `id: "grammar"`.
- `bot.py`: no reference to `grammar_course4_lessons`; no Course 4 loader.
- The generic course menu is built from `courses.json`, so Course 4 is not offered by this branch.
- The file `course_data/grammar_course4_lessons.json` exists on main as a file, but the inspected `bot.py` does not load it. A data file that is not loaded and registered does not become a visible course.

### 2. Working branch and prepared deploy branch

Both inspected branches contain:
- `courses.json` with `id: "grammar"`, `status: "active"`, and lesson IDs `grammar_01` through `grammar_31`.
- `bot.py` loading `course_data/grammar_course4_lessons.json` through `adapt_unified_orthography_lessons(..., include_extended_sections=True)`.
- The course is routed through the generic course menu and course-page renderer.

The working branch's runtime JSON has:
- 31 lessons, numbered contiguously 1–31.
- Every lesson has an objective.
- 31/31 lessons have key points (328 total), examples (221), exercises (155), comprehension items (310), quizzes (248), appendices (272), and activities (93).
- The adapter explicitly includes appendix and activity sections for Course 4, in addition to objectives, explanations, examples, exercises, comprehension questions, and quizzes.

This shows that the current 31 lessons are already structurally rich and have interactive learning material. It does not mean that lessons 32–46 are in the runtime file.

### 3. Botkeep and Telegram

The Botkeep source-branch value `main` is based on the earlier reviewed Botkeep handoff/configuration, not a fresh authenticated read of the live dashboard in this audit. The live Botkeep dashboard and Telegram process were not accessed or changed here.

Botkeep's current GitHub deployment guide says to select the repository, branch, and project root explicitly, then review and apply a repository update. Its guide also says pull-on-start and push updates must be enabled explicitly; a GitHub change alone is not a deployment. After applying an update, the runtime state and Console output must be checked.

Official guide: https://botkeep.cloud/docs/github

## Why the three places disagree

| Location | What it displays/uses | Course 4 result |
|---|---|---|
| GitHub default `main` | Default branch files | Not registered or loaded |
| GitHub feature branch | Working files | Registered, active in manifest, 31 lessons |
| GitHub deploy branch | Prepared deployment files | Registered, active in manifest, 31 lessons |
| Botkeep linked source (previously observed) | `main` | Imports the branch without Course 4 |
| Telegram bot | Whatever source revision Botkeep last imported and started | Expected not to show Course 4 while running the `main` revision |

## Content count and activation are different

The word `active` in `courses.json` is a code-level manifest status. It does not publish a branch to GitHub's default branch, import that branch into Botkeep, start the process, or guarantee Telegram visibility.

At this inspection:
- Runtime JSON: 31 lessons.
- Staged lesson records: 32–46 are preserved as source/draft/review material, not yet included in runtime JSON.
- The 32–46 staging register keeps `runtime_ready: false` for all 15 lessons.
- No staged lesson has been silently promoted to runtime.

## Safe next sequence

1. Continue enriching and validating Course 4 lessons 32–46 in draft/staging files, preserving original source and the agreed terminology.
2. Once the owner-approved content and runtime structure are ready, prepare one release branch from the verified working branch and run structural checks (contiguous lesson IDs, valid quiz answers, menu registration, loader, and no missing dependencies).
3. Back up Botkeep's current files/data and confirm the exact selected repository, branch, project root, start command, and environment configuration.
4. In Botkeep, preview/import the intended branch update with restart disabled; verify changed files and import result.
5. Only after content and import checks pass, explicitly authorize restart/start and test the actual Telegram bot menu and Course 4 lesson navigation.
6. Merge to GitHub `main` only when the owner intends Course 4 to appear in the default branch.

## Changes made by this audit

- No source lesson text edited.
- No `bot.py`, `courses.json`, runtime lesson JSON, dependency, start command, or manifest changed.
- No GitHub branch merge.
- No Botkeep import, sync, restart, start, or unlink.
- No database, environment, secrets, or Telegram bot state changed.

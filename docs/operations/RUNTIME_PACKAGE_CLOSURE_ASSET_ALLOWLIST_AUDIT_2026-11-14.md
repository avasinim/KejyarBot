# Runtime package closure and asset allowlist audit — 2026-11-14

Branch: `release/main-based-reconciled-2026-11-11`
Inspected source revision: `53393395224ffb6f676c660d51e0e6f7cdda425c`
Scope: recursive Git tree inspection and read-only runtime reference inspection.

## Verified repository inventory

The inspected Git tree contains 463 tracked files (not truncated). It includes documentation, tests, legacy files, archived assets, and current runtime material. A deployment package must not be made by copying the entire repository.

## Runtime package closure

A conservative runtime file closure was assembled from:
- the `bot.py` import closure (15 Python modules, including `bot.py`);
- top-level runtime configuration/data files (`courses.json`, `requirements.txt`);
- all JSON and Markdown files read by `bot.py` and the Latin runtime loader;
- the Arami manifest's 21 explicit lesson source files and its required interaction/content banks;
- the seven approved PNG image assets.

The closure contains 61 unique paths. Every one of those 61 paths was found in the inspected Git tree; no missing referenced file was found.

The Arami manifest declares 21 lessons and references 21 content files. Its two dedicated interaction-bank paths are present. The shared question-bank file used by the Arami course loader is also present.

## Asset policy

The seven approved unique PNG assets remain:
- `assets/course1_infographics/lesson_01.png`
- `assets/course1_infographics/lesson_02.png`
- `assets/course1_infographics/lesson_03.png`
- `assets/course1_infographics/lesson_04.png`
- `assets/course1_infographics/lesson_06.png`
- `assets/course1_infographics/lesson_07.png`
- `assets/lessons/kejyar_lesson5_kurdish_letters_v2.png`

The shared lesson image is used for the approved Arami Lesson 5 and Latin Orthography Lesson 1 placements. Do not add the other repository SVGs, root JPG, or unrelated visual assets to the deployment package. No PDF or audio asset is part of this closure.

## Exclusions

The deployment package should exclude:
- `docs/`, `tests/`, `.github/`, and curriculum/audit-only materials not read by the runtime;
- `ai_tutor.py`, `bot_backup.py`, and `arami_lesson1_presentation.py` (not in the inspected `bot.py` import closure);
- legacy JSON lesson stores not read by the current runtime;
- archived SVG/JPG assets outside the explicit seven-PNG allowlist;
- `.env`, Telegram token material, SQLite databases, and SQLite sidecars.

## Deployment limitation

This is a source-tree closure audit, not an uploaded deployment archive. GitHub tree metadata confirms that the referenced paths exist, but this audit did not download, assemble, upload, or start the package on Altare. The app's file manager was last reported as showing only `/course_data`, and the individual server state was last reported as `Stopped / Node down`.

## Next safe step

Use this exact 61-path closure to prepare a minimal package from the audited branch, then verify its archive contents and checksums before any upload. Keep `.env` separate and private. Confirm the Altare persistent data path for `kejyar.db` before the first controlled start.

This note supplements earlier append-only records; it does not replace or modify them.

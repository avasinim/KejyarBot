# Runtime file closure and media allowlist audit — 2026-11-14 18:02Z

Branch: `release/main-based-reconciled-2026-11-11`
Tree inspected at commit: `5a65cd93290c71f8d51e5a2cd4d9ac17d2524e46`
Scope: compare the inspected `bot.py` import/runtime file reads, Arami manifest references, Latin loader paths, and image delivery paths against the repository tree.

## Verified file closure

- The 15 Python files in the inspected direct runtime import closure are present.
- All startup JSON files explicitly loaded by `bot.py` are present.
- All four Latin lesson-source / answer-key Markdown files read by `latin_course_runtime.py` are present.
- Arami manifest contains 21 lesson source references; all 21 referenced paths exist in this branch.
- The 19 shared Arami quiz-bank scopes and dedicated Lesson 1 / Lesson 5 interaction data are referenced by the active runtime loaders and the required JSON files exist.
- The exact six Course 1 infographic PNG paths and the shared Lesson 5 PNG path exist.
- Across the above explicit runtime paths and the 21 Arami manifest source references, there are 61 unique required files and zero missing paths.
- `requirements.txt` contains only `python-telegram-bot>=22,<23` and `python-dotenv>=1,<2`.

## Media and package exclusions

The repository tree contains exactly seven PNG files, matching the approved set:
- `assets/course1_infographics/lesson_01.png`
- `assets/course1_infographics/lesson_02.png`
- `assets/course1_infographics/lesson_03.png`
- `assets/course1_infographics/lesson_04.png`
- `assets/course1_infographics/lesson_06.png`
- `assets/course1_infographics/lesson_07.png`
- `assets/lessons/kejyar_lesson5_kurdish_letters_v2.png`

The repository also contains ten legacy SVG infographics and one JPG (`photo_2026-10-27_00-13-52.jpg`). None is referenced by the inspected runtime file-read paths; exclude them from the deployment package to preserve the approved PNG-only media rule. `course_data/arami_course1_audio_catalog.json` exists as metadata but is not read by the inspected active runtime closure; do not package it as an audio asset. No audio or PDF media files were found in the tree.

Other legacy/draft material in `course_data/` and unused root JSON files must not be swept into the deployment package merely because they exist in the repository. Include only the verified runtime closure, required data/source files, requirements file, and approved PNGs.

## Database boundary

No `.db`, `.db-wal`, or `.db-shm` file exists in the repository tree. The learner database must be recovered from the authoritative hosting/source location separately. It must never be replaced by a newly initialized empty database.

## Limitations and next gate

This is a source-tree completeness audit, not a built archive, a successful host upload, or a runtime test. No binary archive was produced, no Altare panel action was taken, and no bot was started. Next gate: obtain and verify the original learner database and its sidecars; separately assemble and test a whitelist-only deployment package without including the database or secrets.

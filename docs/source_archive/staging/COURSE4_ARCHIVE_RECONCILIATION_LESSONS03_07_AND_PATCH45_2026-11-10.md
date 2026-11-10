# Course 4 — archive reconciliation: lessons 3–7 and recovered lesson 45 patch (2026-11-10)

## Executive correction
This note supersedes any interpretation that lessons 3–7 are missing lessons or that lesson 45 has no archived append-only patch. The Library-wide inventory and a root-level combined ZIP reveal a more precise status.

## 1. Root-level combined archive verified
Library file:
`/Course4_AppendOnly_Combined_Archive_Patches_01-02_08-45_Lesson46Review_2026-11-09.zip`

The ZIP was materialized and inspected. It contains 69 members, including 40 append-only patch JSON files for lessons 1, 2, and 8–45 (lesson 31 uses its v2 filename), plus lesson 46 review materials and provenance manifests.

### Lesson 45 patch
- File inside ZIP: `grammar_45_append_only_patch.json`
- SHA-256: `52d1e7011294bd1e4d3c6a7d1213d0d2b434699ab76e3449a154f01995bbf9d9`
- The checksum matches `PROVENANCE_SHA256SUMS_CHECKPOINT29-45.txt` inside the same ZIP.
- JSON parses successfully.
- `patch_type=append_only`, `operation=append_only_additions`, `preserve_existing=true`, `source_lesson_unchanged=true`.
- Source baseline points to `course_data/grammar_course4_lessons.json` on `main`, the expanded draft and draft transcript for lesson 45, and review status `owner_review_pending_expanded_draft`.
- Original inventory recorded: 1 key point, 0 structured examples, 0 activities, 23 exercises, 0 comprehension, 0 quiz, 0 appendix.
- Additions recorded: 6 examples, 9 appendix entries, 3 activities.
- This is an append-only patch to an expanded draft, not evidence of final owner approval or production activation.

The earlier statement that lesson 45 was not found in `/KejyarBot/Course4_Archive/` remains true for that folder listing. It was incomplete as a Library-wide statement: the patch is present inside the root-level combined ZIP.

## 2. Lessons 3–7: no patch is required by the archived baseline decision
The Library file `COURSE4_PATCH_INVENTORY_AND_LESSON_STATUS_2026-11-09.md` and the ZIP member `LESSONS_03-07_BASELINE_REVIEW_STATUS_2026-11-09.md` agree:
- Lessons 3–7 are present in the 46-lesson runtime JSON.
- Their structured lesson fields are populated.
- Their review label is `scientific_review_complete_with_qualified_notes`.
- Their append-only patches were intentionally not created because the baseline review determined that no append-only additions were needed at that checkpoint.

Therefore lessons 3–7 are **not missing lessons** and the lack of patch files is **not automatically an archive defect**. Do not generate empty, fabricated, backdated, or duplicate patches for these lessons. Any future change must be a separately justified append-only addition supported by evidence.

### Verified structured inventory (current main JSON)
| Lesson | Key points | Examples | Activities | Exercises | Comprehension | Quiz | Appendix |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 35 | 15 | 3 | 5 | 10 | 8 | 30 |
| 4 | 9 | 6 | 3 | 5 | 10 | 8 | 6 |
| 5 | 12 | 6 | 3 | 5 | 10 | 8 | 7 |
| 6 | 9 | 6 | 3 | 5 | 10 | 8 | 6 |
| 7 | 8 | 5 | 3 | 5 | 10 | 8 | 5 |

The runtime JSON blob SHA is `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`; the same blob is present on `main` and historical branch `archive/course4-lesson03-07-2026-11-09`.

## 3. Source and research materials located for lessons 3–7
- Lesson 3 owner-source extract: `docs/source_archive/COURSE4_LESSON_03_NAME_SOURCE_AND_AUDIT_2026-11-07.md`; its header records extraction from `Pasted text(2).txt`, lines 53–867.
- Lesson 4 book addendum: Library file `KEJYAR_COURSE4_LESSON04_BOOK_ADDENDUM.md`.
- Lesson 5 book addendum: Library file `KEJYAR_COURSE4_LESSON05_BOOK_ADDENDUM.md`.
- Lesson 6 book addendum: Library file `KEJYAR_COURSE4_LESSON06_BOOK_ADDENDUM.md`.
- Lesson 7 book addendum: Library file `KEJYAR_COURSE4_LESSON07_BOOK_ADDENDUM.md`.
- These four book addenda are research/review supplements whose stated lesson baseline is the runtime JSON. They are not original owner-source transcripts and must not be mislabeled as such.
- `grammar_course4_lessons.txt` in the Library is an older 31-lesson snapshot (its curriculum state says owner-supplied lessons 1–25 plus researched lessons 26–31); it is not the current 46-lesson runtime baseline.
- The seven `Course4_Lesson03_01...` through `Course4_Lesson03_07...` ZIP files are Lesson 3 subdivision/draft packages, not append-only patches for lessons 3–7.

## 4. Current archive interpretation
- Append-only patches: 40 files, lessons 1, 2, and 8–45; lesson 45 is inside the root-level combined ZIP.
- Lessons 3–7: structured baseline reviewed; no patch required under the 2026-11-09 baseline decision.
- Lesson 46: review/duplication assessment only; no new content patch.
- The individual Library folder `/KejyarBot/Course4_Archive/` is not the only archive location. Root-level combined ZIPs and standalone audit/addendum files must be included in any Library-wide inventory.

## 5. Safety and next work
Preserve all ZIPs, patch files, manifests, addenda, and older snapshots unchanged. For lessons 3–7, continue cross-lesson terminology/source checks only where a concrete issue is identified; do not create patches merely to make the numbering look continuous. For lesson 45, retain the verified patch and checksum; do not deploy or apply it to Botkeep/Telegram as part of this archival check.

This reconciliation changed no runtime JSON, lesson, quiz, database, Botkeep state, Railway deployment, or Telegram process. No merge, deploy, restore, restart, or activation was performed.

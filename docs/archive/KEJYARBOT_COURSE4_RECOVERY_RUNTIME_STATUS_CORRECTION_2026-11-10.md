# KejyarBot Course 4 — corrected recovery and runtime status (2026-11-10)

## Corrections to earlier preservation notes
This note supersedes earlier statements that PR #119 was still draft/unmerged, that Course 4 was not yet in main, and that lesson 45–46 source material was absent. Those statements were stale or conflated separate archive layers.

## Verified GitHub main state
- PR #119 is **merged** into `main` (merge commit `5f0df30e6aaa6ac3f37e03dfeb84f3a43a56b5bd`, merged 2026-11-08T17:15:26Z).
- Current `course_data/grammar_course4_lessons.json` on `main` contains 46 lessons, from `grammar_01` through `grammar_46`.
- Current `courses.json` marks course `grammar` active with all 46 lesson IDs.
- Review-state counts in the current runtime JSON: 30 `scientific_review_complete_with_qualified_notes`, 1 `internal_cross_lesson_synthesis_no_external_source_mapping`, and 15 `owner_review_pending_expanded_draft`.
- Lessons 32–46 remain owner-review-pending expanded drafts and have no active quiz until approval. This is beta/read access, not final scientific approval.
- The separate Railway PR #141 remains open, draft, and unmerged; its own PR description says automated tests have not yet been run in this environment.

## Verified source recovery material for lessons 32–46
- Lesson 32: owner material and expanded draft are preserved in the combined 32–38 source record; it requires scientific correction and separation of versions.
- Lessons 33–36: owner-source material is present in the combined source record and separately segmented under `docs/source_archive/staging/COURSE4_LESSON_033..036_OWNER_SOURCE_SEGMENT_2026-11-08.md`. These segments preserve source excerpts, but do not by themselves constitute approved final lessons.
- Lessons 37–38: additional owner-source segments are preserved under `docs/source_archive/staging/COURSE4_LESSON_037..038_OWNER_SOURCE_SEGMENT_2026-11-08.md`; they are explicitly bounded source excerpts, not proof that every missing portion has been recovered.
- Lessons 39–45: the combined source transcript `COURSE4_LESSONS_039_045_SOURCE_2026-11-07.md` exists. It includes source excerpts, expanded lesson drafts, review notes, and inter-lesson transitions; distinguish these layers rather than treating the whole file as a raw owner transcript.
- Lesson 46: both `COURSE4_LESSON_046_OWNER_SOURCE_TEXT_2026-11-07.md` and `COURSE4_LESSON_046_DRAFTS_AND_REVIEW_2026-11-07.md` exist. The draft is not approved.
- The 2026-11-08 source completeness audit and segmentation map remain useful, but they are dated snapshots. Newer staging segments provide additional recovered source evidence for 33–38.

## Library append-only patch inventory (separate from runtime lesson availability)
In the inspected `/KejyarBot/Course4_Archive/` folder, README inventories and patch files evidence individual append-only patches for lessons 1, 2, and 8–44. Lessons 3–7 are explicitly absent from the README inventory. No individual patch file for lessons 45 or 46 was verified in that folder listing. This does **not** mean lessons 45–46 are absent from GitHub source or runtime.
Consolidated ZIP checkpoints exist for selected ranges; they are not a full 46-lesson patch set.

## Next safe work
1. Preserve all source segments, expanded drafts, patches, and README snapshots unchanged.
2. Reconcile the combined 32–38 source record against its six staging segments; identify overlap and any missing ranges before building a lesson-specific source packet.
3. For 39–45, separate owner-supplied source excerpts, expanded drafts, answers, and editorial/review notes lesson by lesson.
4. Keep lessons 32–46 in owner-review-pending state until the owner/scientific review gate is satisfied.
5. Do not merge PR #141, deploy Railway, restart Botkeep, alter SQLite, sync GitHub into Botkeep, or activate another Telegram poller until the authoritative database is backed up and Botkeep's paused infrastructure operation is resolved.

## Safety
This is an archival and documentation correction only. No Botkeep files, SQLite database, Railway production configuration, or Telegram runtime were changed. No deployment, restore, restart, or activation was performed.

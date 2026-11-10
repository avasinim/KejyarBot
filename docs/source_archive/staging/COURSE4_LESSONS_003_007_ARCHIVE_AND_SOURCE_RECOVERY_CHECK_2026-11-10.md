# Course 4 — Lessons 3–7 archive and source recovery check (2026-11-10)

## Verified runtime baseline
The following check was made against `course_data/grammar_course4_lessons.json` on both `main` and historical branch `archive/course4-lesson03-07-2026-11-09`. Both refs return the same Git blob SHA: `e8fcc4f4d5bedf001e21ce8f68f26ee99b917e65`. Therefore the historical branch is not a distinct runtime-content recovery point for these lessons; it matches the current main JSON.

| Lesson | Title (short) | Key points | Examples | Activities | Exercises | Comprehension | Quiz | Appendix |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 3 | پێناسە و تایبەتمەندییەکانی ناو | 35 | 15 | 3 | 5 | 10 | 8 | 30 |
| 4 | ناو لە ڕووی ژمارە و ڕەگەزەوە | 9 | 6 | 3 | 5 | 10 | 8 | 6 |
| 5 | ناو لە ڕووی ناوەرۆک، ناسینەوە و پێکهاتەوە | 12 | 6 | 3 | 5 | 10 | 8 | 7 |
| 6 | هاوەڵناو — پێناسە و بنەماکانی ناسینەوە | 9 | 6 | 3 | 5 | 10 | 8 | 6 |
| 7 | هاوەڵناو — جۆربەندی و پێکهاتەی مۆرفۆلۆژی | 8 | 5 | 3 | 5 | 10 | 8 | 5 |

All five lessons currently carry `scientific_review_complete_with_qualified_notes`. This is the runtime review label, not proof that every claim is source-verified or that the Library patch archive is complete.

## Source evidence located
- **Lesson 3:** A distinct owner-supplied source extract exists at `docs/source_archive/COURSE4_LESSON_03_NAME_SOURCE_AND_AUDIT_2026-11-07.md`. Its header records extraction from `Pasted text(2).txt`, lines 53–867, and identifies the content as the noun source for Lesson 3. It is a source extract and audit record, not a final approved lesson text.
- **Lessons 4–5:** The combined `COURSE4_LESSONS_01_05_FOUNDATION_NOUN_AUDIT_2026-11-07.md` records a direct runtime review of lessons 1–5. It documents the lesson contents, counts, issues and proposed boundaries. In the inspected `docs/source_archive/` and `docs/source_archive/staging/` directory listings, no separate owner-source transcript for lesson 4 or 5 was identified.
- **Lessons 6–7:** `COURSE4_LESSONS_06_08_ADJECTIVE_SEQUENCE_AUDIT_2026-11-07.md` records a runtime-only sequence audit of lessons 6–8. It documents lesson 6 as adjective identification and lesson 7 as classification/morphology. In the inspected source archive and staging listings, no separate owner-source transcript for lesson 6 or 7 was identified.

## Patch archive gap
The inspected Library `/KejyarBot/Course4_Archive/` README inventories omit individual patches for lessons 3–7. This agrees with the previously recorded gap. It does **not** mean that the lessons themselves are missing: all five are present in the runtime JSON, with their structured material and quizzes as counted above.

## Safe decision
Do not fabricate or backdate append-only patches for lessons 3–7 from the current runtime snapshot. A runtime snapshot and a review audit do not reveal the original patch additions, their prior baseline counts, or their exact historical provenance. Preserve the existing runtime JSON, Lesson 3 source extract, and both audits unchanged. If the original append-only patch files or owner-source files are later found in another Library folder, branch, ZIP, or user-provided source, compare them before creating a recovery patch. Any newly created archival record must be labelled as a reconstruction from identified evidence, never as an original recovered patch.

## Scope and safety
This was a read-only comparison and an archival status note. No runtime JSON, lesson text, quiz, Botkeep server, SQLite database, Railway deployment, or Telegram bot was modified. No production operation was performed.

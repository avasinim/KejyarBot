# Three-course completion plan — updated 2026-10-27

## Scope decision
- Course 4 (ڕێزمان) is explicitly deferred. Do not draft, activate, or integrate it in this work phase.
- Finish and verify Courses 1–3 only:
  1. Course 1 — ڕێنووسی سەرەتایی: 22 existing lesson IDs (`وانە_1`–`وانە_22`).
  2. Course 2 — وتووێژ: 12 draft lessons split across `daily_conversation_lessons_01_06.json` and `daily_conversation_lessons_07_12.json`.
  3. Course 3 — ڕێنووسی یەکگرتوو: 12 draft lessons in `unified_orthography_lessons_01_12.json`.
- Course 2 and Course 3 are drafts for review, not yet editorially approved. Their presence in JSON must not be represented as completion until linguistic/source review and integration tests pass.
- Course 4 remains in `courses.json` as a planned placeholder only; it is out of scope for activation.

## Current integration state
- Course 1 is loaded in the current runtime using its legacy stable lesson IDs. Preserve these IDs and existing student progress.
- Course 2 and Course 3 lesson data files are now loaded through validated adapters into `LESSON_DATA`/`QUIZ_DATA` using namespaced keys. The manifest contains their 12 ordered IDs each and marks both `draft_for_review`; the menu therefore keeps them visible but unavailable until editorial/source review is complete.
- Course 2: 12 dialogue lessons and 27 quiz questions pass structural index validation. All 12 are explicitly flagged `draft_source_check_required`, because the current JSON drafts do not include traceable sources; their missing source citations are recorded rather than invented.
- Course 2 quiz audit: formative explanations have been added to all 27 quiz questions, and a regression assertion requires them. Dialogue-dependent questions have visible lesson-level review notes; the course remains locked pending source/language review.
- Course 3: 12 lessons and 12 quiz questions pass structural index validation. Formative explanations have been added to all 12 quiz questions and are regression-tested. Incomplete or unverified examples/claims in lessons 1, 4, 6, 7, 9, 10, 11, and 12 are flagged visibly as editorial-review findings. All 12 lessons remain `draft_source_check_required`.
- `course_lesson_adapters.py` contains separate adapters for conversation-style and unified-orthography lessons; both render source notes and visible review findings. Adapter rendering does not itself approve the content for activation.
- The menu must show the three in-scope courses distinctly. Each course must have independent ordered lesson access, quiz routing, completion progression, and namespaced IDs; Course 1 legacy IDs must remain unchanged.
- The existing daily-chat feature is not a substitute for the structured 12-lesson Course 2.

## Required completion gates — prioritize Courses 2 and 3

The user has asked to stop spending disproportionate time on Course 1. The next work phase prioritizes completing Courses 2 and 3; do not reopen Course 1 review unless a blocking regression is found.

1. **Course 2 — daily conversation:** review all 12 lessons for natural dialogue, consistent spelling, useful vocabulary, and quiz-answer correctness. Record source/edition and page or clearly mark a lesson as original editorial material rather than implying it is source-derived. Resolve all lesson-level language/source flags before activation.
2. **Course 3 — unified orthography:** review all 12 lessons against selected, accessible references. For each rule/example, record edition and page(s), verify the example, and separate source statements from editorial recommendations. Replace unresolved placeholders and resolve all review findings before activation.
3. **Integration checks:** verify all 46 records load (22 + 12 + 12), lesson IDs are unique, each course has independent ordered unlocking/next-lesson behavior, quiz start/answer/completion routing works, and progress remains isolated by course.
4. **Manual Telegram smoke test:** run the checklist in `docs/PRE_RELEASE_TELEGRAM_SMOKE_TEST.md` only with an authorized isolated test bot/token.
5. **Course 1:** keep the existing active course and its legacy lesson IDs stable. Defer non-blocking source-review items until Courses 2 and 3 are ready; do not let them hold up the current workstream.
6. Do not mark Course 2 or 3 active until language/source review and integration checks pass. Automated tests do not count as editorial approval.
## Safety boundaries
- Do not merge PRs, change `main`, touch production bot/database/tokens, or deploy without explicit approval.
- Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`; preserve the existing approved voice.
- Automated structural checks are not a substitute for human linguistic and source review.

## Source audit follow-up (2026-10-28)

- The listed Kurdipedia record for **پوختەی ڕێنووس و خاڵبەندی 2024** identifies دیاکۆ هاشمی as preparer and describes the 2024 updates/editions, including the second-edition update dated 21 February 2024 and a later update dated 16 August 2024. This is a useful bibliographic anchor, but it does not by itself validate each lesson rule.
- Source record: https://kurdipedia.org/default.aspx?lng=1&q=20220823204947429918
- Search result for the same record also identifies the earlier 2021 publication separately: https://kurdipedia.org/default.aspx?lng=1&q=20211004184500395359. Do not mix the 2021 record with the 2024 edition when citing page-specific rules.
- Course 3's current per-lesson source notes are editorial reminders, not precise citations: they generally lack page numbers and verbatim evidence. Keep all 12 lessons in `draft_source_check_required` until a reviewer records the selected edition, page(s), and the rule/example verified for each lesson.
- Course 2 remains without traceable lesson-level sources; no bibliography was invented. Its 27 quiz items have formative explanations in the current JSON drafts, but those explanations do not verify the keyed answers or replace source/language review.
- External reference check performed for bibliographic metadata only; it is not a substitute for reviewing the actual PDF pages or approving Kurdish language content.
- Course 3 formative explanations were added to all 12 quiz questions. Explanations are general learning feedback, not evidence that the keyed answers or orthographic rules have been source-validated. Lessons 9 and 11 include visible flags where example slots are still placeholders.

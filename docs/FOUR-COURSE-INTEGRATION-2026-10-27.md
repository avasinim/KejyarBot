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
- Course 2 quiz audit: all 27 quiz questions currently lack explanations. This is an editorial improvement item, not a structural parser failure.
- Course 3: 12 lessons and 12 quiz questions pass structural index validation; all 12 lessons remain flagged `draft_source_check_required`.
- `course_lesson_adapters.py` contains an adapter for conversation-style lessons. The unified-orthography draft has a different schema and requires a dedicated renderer/adapter before activation.
- The menu must show the three in-scope courses distinctly. Each course must have independent ordered lesson access, quiz routing, completion progression, and namespaced IDs; Course 1 legacy IDs must remain unchanged.
- The existing daily-chat feature is not a substitute for the structured 12-lesson Course 2.

## Required completion gates
1. Review all 22 Course 1 lessons and quiz items; prioritize source flags for lessons 4, 8, 13, 18, 19, and 21.
2. Review all 12 Course 2 dialogue lessons for naturalness, consistent Kurdish spelling, useful vocabulary, and valid quiz answers.
3. Review all 12 Course 3 lessons against cited sources; resolve every `draft_source_check_required` flag and distinguish source claims from editorial recommendations.
4. Runtime integration has been added for Courses 2 and 3 on this isolated branch. Confirm CI passes, then continue source/language review before changing either course from `draft_for_review` to `active`.
5. Add/run tests for course catalog, all 46 loaded lesson records (22 + 12 + 12), unique lesson IDs, ordered unlocking, course-specific next lesson, quiz start/answer/completion, and progress isolation. The default legacy roadmap and quick lesson menu must remain scoped to Course 1.
6. Run manual Telegram checks only with an authorized isolated test bot/token.

## Safety boundaries
- Do not merge PRs, change `main`, touch production bot/database/tokens, or deploy without explicit approval.
- Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`; preserve the existing approved voice.
- Automated structural checks are not a substitute for human linguistic and source review.

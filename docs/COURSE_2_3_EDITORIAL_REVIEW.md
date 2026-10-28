# Course 2–3 Editorial Review Queue
Updated: 2026-10-28
Branch: `fix/four-course-structure-2026-10-27`

## Scope and safety

This queue is for Course 2 (daily conversation) and Course 3 (unified orthography). Course 1 is out of scope unless a regression blocks integration. Course 4 remains planned and empty. This document is a review tracker, not a claim that the courses are linguistically or bibliographically approved.

Do not activate either draft course until the checks below are completed. Do not merge the draft PR, deploy, modify the production bot/token/database, or enable dynamic speech without explicit user approval. Keep `KEJYAR_ENABLE_DYNAMIC_SPEECH=false`.

## Course 2 — Daily conversation (12 lessons)

### Completed in this pass
- Rechecked the dialogue against the quiz keys for lessons 4, 5, 10, and 11.
- Confirmed the key answers against their corresponding dialogue lines:
  - Lesson 4: Kêjyar says he has five sisters and no brothers; Argesh says he has two sisters and two brothers.
  - Lesson 5: Argesh asks Kêjyar to call before visiting; Kêjyar agrees.
  - Lesson 10: the library is beside the school and opposite the park.
  - Lesson 11: the pair agree to meet at 8 a.m. at the bus station.
- Rewrote the four quiz explanations to state the relevant dialogue evidence and cleared only those four lessons' dialogue-answer findings.
- CI passed after a test assertion was adjusted to check that review status is rendered independently of whether a lesson still has findings.

### Remaining release gates
1. Review all 12 dialogues for natural Kurdish, consistency of names/terms, useful real-life phrasing, and spelling.
2. Check all quiz keys against their dialogue or lesson text; do not rely on explanations alone.
3. Add sources where claims depend on a reference; clearly label original editorial dialogue/vocabulary as original teaching material rather than implying a published source.
4. Keep each lesson marked `draft_source_check_required` until the editorial review is actually complete.

## Course 3 — Unified orthography (12 lessons)

All 12 lessons remain drafts. The current JSON has unresolved source/example review findings in lessons 1, 4, 6, 7, 9, 10, 11, and 12. The following are the concrete unresolved tasks recorded in the lesson data:

| Lesson | Topic | Required evidence or correction |
|---|---|---|
| 1 | Unicode and unified spelling | Add a technically correct Unicode code-point example for visually similar letters; distinguish the actual Kurdish code point from Arabic/Latin lookalikes. |
| 4 | Consonant clusters and syllables | Verify pronunciation and syllabification for the cited examples, with exact source/page and a clear phonological explanation. |
| 6 | Difference between ڕ and ر | Verify example words against a reliable dictionary/source and cite the chosen spelling rule. |
| 7 | ک/ك, ھ/ه and ە | Add whole-word examples and verify the relevant Unicode code points; explain the orthographic rule, not just visual similarity. |
| 9 | Particles and joined spelling | Replace generic placeholders with real examples from the selected source and record edition/page. |
| 10 | Compound and derived words | Add real source-attested examples, analyze their components, and cite edition/page. |
| 11 | Adverbs, loanwords and compound numerals | Add real examples and a source-backed rule for each included topic; record edition/page. |
| 12 | Final review | Build a short authentic proofreading passage and an answer key whose corrections each point to a verified rule/source. |

### Source-verification protocol
- Select and consistently identify the intended edition of Diyako Hashemi's *پوختەی ڕێنووس و خاڵبەندی* and any supplementary reference.
- For every rule or example, record the edition and page/section; verify it against the actual text rather than inferring from the source title or a broad topic label.
- Do not invent page numbers, quotations, rules, or examples. If the source text/page is unavailable, keep the item explicitly unresolved.
- Review the quiz answer key against the approved lesson content after the source audit, then rerun the adapter, course integrity, and full unit tests.

## Integration verification

The automated suite currently checks that all 46 configured lesson IDs across Courses 1–3 load without collisions, Courses 2–3 remain review-gated, and Course 4 remains empty. Automated checks do not replace editorial/source review or a manual Telegram smoke test.

Manual smoke test must use an authorized isolated test bot/account only. Confirm course navigation, next-lesson unlocking, quiz answer handling, progress isolation, long-message chunking, and optional infographic delivery. Do not use the production bot token for this check.

## Current status

- Runtime/CI: automated suite passed on commit `ebcc9c2f508fefcddaf912491bde78303610f314`.
- Course 2: four dialogue-to-quiz findings resolved; full editorial/source review still pending.
- Course 3: lesson-specific source/example findings listed above remain unresolved.
- Pull request #4 remains a draft and must not be merged without explicit approval.

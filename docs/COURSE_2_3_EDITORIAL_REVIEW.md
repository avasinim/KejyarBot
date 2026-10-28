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

### Targeted Course 2 review queue

These are editorial checks to perform, not claims that the wording is necessarily wrong:

| Lesson | Focus for review |
|---|---|
| 1 | Check greeting and farewell expressions for naturalness and consistency across the remaining lessons. |
| 2 | Review the naturalness of the self-introduction and the question/answer about where someone is from. |
| 3 | Check question-word usage and the sequence of questions for a natural conversation. |
| 4 | Quiz keys were checked against the dialogue; review family vocabulary definitions and consistency of singular/plural forms. |
| 5 | Quiz key was checked against the dialogue; review the polite invitation and pre-visit phone-call phrasing. |
| 6 | Review the daily routine for tense consistency and natural time expressions. |
| 7 | Review food vocabulary and repeated expressions for preference and drinking/eating; check colloquial naturalness. |
| 8 | Arithmetic is internally consistent: 2 kg apples at 3,000 dinars/kg plus 1 kg oranges at 3,000 dinars/kg totals 9,000 dinars. Check the pricing exchange remains clear for learners. |
| 9 | The date “twenty-seventh of the month” has no named month or situational anchor; decide whether it is an intentional date-reading exercise or should be contextualized. Check the “today/tomorrow” timeline stays clear. |
| 10 | Quiz keys were checked against the dialogue; review the distinction between “beside,” “opposite,” and “behind” with a simple spatial diagram/example if needed. |
| 11 | Quiz key was checked against the dialogue; review travel-planning phrasing and consistency of the transport terms. |
| 12 | Check the final dialogue consolidates earlier vocabulary without introducing unexplained new phrasing; review all three quiz keys against the full dialogue. |

### Remaining release gates
1. Complete the targeted editorial checks above for all 12 dialogues, including natural Kurdish, consistent names/terms, useful real-life phrasing, and spelling.
2. Recheck every quiz key against the dialogue or lesson text; do not rely on explanations alone.
3. Clearly label original editorial dialogue/vocabulary as original teaching material; cite sources only for claims that actually depend on a reference.
4. Keep each lesson marked `draft_source_check_required` until editorial review is complete.

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

- Runtime/CI: automated suite passed on commit `55c6a2525b4493c933ae58325a7d61908d45c3dd`.
- Course 2: four dialogue-to-quiz findings resolved; full editorial/source review still pending.
- Course 3: lesson-specific source/example findings listed above remain unresolved.
- Pull request #4 remains a draft and must not be merged without explicit approval.

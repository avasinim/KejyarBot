# Course 2–3 Editorial Review Queue
Updated: 2026-10-28
Branch: `fix/four-course-structure-2026-10-27`

## Scope and safety

**Editorial principle clarified on 2026-10-28:** These are beginner-friendly educational bot courses. Learner-facing lessons should not contain source lists, citations, page numbers, or bibliographic discussion. Do not hold simple teaching material to a publication-level evidence standard. Focus review on clear Kurdish, useful examples, beginner accessibility, internal consistency, and quiz answers matching the lesson. Use external references privately only if a concrete factual uncertainty needs resolving; do not require a source for every lesson or example.


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
| 8 | Arithmetic is internally consistent: 2 kg apples at 3,000 toman/kg plus 1 kg oranges at 3,000 toman/kg totals 9,000 toman. The lesson's currency wording has been changed from dinar to toman. Check the pricing exchange remains clear for learners. |
| 9 | The date “twenty-seventh of the month” has no named month or situational anchor; decide whether it is an intentional date-reading exercise or should be contextualized. Check the “today/tomorrow” timeline stays clear. |
| 10 | Quiz keys were checked against the dialogue; review the distinction between “beside,” “opposite,” and “behind” with a simple spatial diagram/example if needed. |
| 11 | Quiz key was checked against the dialogue; review travel-planning phrasing and consistency of the transport terms. |
| 12 | Check the final dialogue consolidates earlier vocabulary without introducing unexplained new phrasing; review all three quiz keys against the full dialogue. |

### Remaining release gates
1. Complete the targeted editorial checks above for all 12 dialogues, including natural Kurdish, consistent names/terms, useful real-life phrasing, and spelling.
2. Recheck every quiz key against the dialogue or lesson text; do not rely on explanations alone.
3. Keep dialogue natural, useful, and understandable for beginners; source citations are not a lesson requirement.
4. Keep each lesson in draft until its practical editorial review and quiz-key checks are complete. Do not require page citations or bibliographic proof as a release gate.

## Course 3 — Unified orthography (12 lessons)

All 12 lessons remain drafts for practical editorial review, not bibliography review. Learner-facing lessons do not need source notes, citations, page numbers, or bibliographies. Focus on whether the explanations are simple, examples are familiar and clear, the Kurdish spelling is consistent with the intended course, and the quiz checks what the lesson actually teaches. The following are the remaining beginner-usability tasks recorded in the lesson data:

| Lesson | Topic | Practical improvement |
|---|---|---|
| 1 | Unicode and unified spelling | Show the difference between visually similar letters with a simple example; distinguish Kurdish letters from lookalikes. |
| 4 | Consonant clusters and syllables | Make the explanation of consonant clusters and syllables clear, with simple examples and a beginner-friendly explanation. |
| 6 | Difference between ڕ and ر | Unicode code points are recorded (ڕ U+0695, ر U+0631). Use familiar words to demonstrate the distinction clearly. |
| 7 | ک/ك, ھ/ه and ە | Unicode code points are recorded: ک U+06A9 / ك U+0643; ھ U+06BE / ه U+0647; ە U+06D5. Add whole-word examples and a short, clear explanation. |
| 9 | Particles and joined spelling | Replace generic placeholders with familiar, practical examples. |
| 10 | Compound and derived words | Add familiar compound and derived words and explain their components. |
| 11 | Adverbs, loanwords and compound numerals | Add simple examples for each topic and explain the intended pattern clearly. |
| 12 | Final review | Build a short proofreading passage and an answer key that matches the rules taught in the lessons. |

### Practical review checklist
- Is the explanation easy for a beginner to understand?
- Are examples familiar, correctly written, and sufficient to practice the point?
- Does each exercise teach the stated objective?
- Does every quiz answer match the lesson text, with no ambiguous or duplicate options?
- Keep internal editorial notes out of learner-facing lesson text.
- Do not require citations, page numbers, or a bibliography for these beginner lessons.

## Integration verification

The automated suite currently checks that all 46 configured lesson IDs across Courses 1–3 load without collisions, Courses 2–3 remain review-gated, and Course 4 remains empty. Automated checks do not replace editorial/source review or a manual Telegram smoke test.

Manual smoke test must use an authorized isolated test bot/account only. Confirm course navigation, next-lesson unlocking, quiz answer handling, progress isolation, long-message chunking, and optional infographic delivery. Do not use the production bot token for this check.

## Current status

- Runtime/CI: automated suite passed on commit `6ed2c74fc1629102320d8cca3136ecc58edc5e12`; the latest lesson-data edits need a fresh CI result.
- Course 2: four dialogue-to-quiz findings resolved; practical editorial review still pending.
- Course 3: lesson-specific clarity and example improvements listed above remain unresolved.
- Pull request #4 remains a draft and must not be merged without explicit approval.


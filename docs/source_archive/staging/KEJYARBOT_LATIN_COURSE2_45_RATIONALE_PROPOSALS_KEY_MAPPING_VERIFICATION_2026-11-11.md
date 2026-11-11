# Course 2 — 45 rationale proposal key-mapping verification
**Date:** 2026-11-11  
**Status:** Structural mapping verification only; no editorial approval.

## Sources and verified blobs
- Base 44-row proposal: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_44_PROPOSED_ANSWER_KEY_RATIONALE_REWRITES_2026-11-11.md`, SHA `133c9105a9a3315ceed3d5e2d84d69bf1d472b28`.
- Refinement delta: `docs/source_archive/staging/KEJYARBOT_LATIN_COURSE2_RATIONALE_REFINEMENT_PATCH_2026-11-11.md`, SHA `a38d463ab2683762d879a45a21678602aaa280ab`.
- Reviewed answer key: `course_data/latin_course_2_quiz_answer_key_reviewed_draft_2026-11-10.md`, SHA `879e1525e720bdc25b8f6e896de3e388801238d0`.

## Method
Parsed each lesson/question/key-letter row from the base proposal tables and compared it with the corresponding lesson/question/key-letter row in the reviewed answer-key table. Then checked the separately added L10 Q2 rationale in the refinement patch against its answer-key row.

## Results
- Base proposal: 44 rationale rows.
- Base proposal rows with a corresponding answer-key row: 44/44.
- Missing mappings: 0.
- Key-letter mismatches: 0.
- Refinement patch: 11 rows are refinements of items already present in the base 44; they are not 11 new unique items.
- Additional rationale introduced by the patch: L10 Q2, key C (`wê`), matching the reviewed answer-key row.
- Total distinct items with proposed rationale wording across base + patch: 45 (44 base items plus the additional L10 Q2 item).
- Reviewed answer-key rows in total: 62.

## Interpretation and limits
This check verifies association and key-letter consistency only. It does not prove that the keyed answers are linguistically correct, that the rationale fully explains each distractor, or that any proposal is suitable for learners without editorial review. L12 Q1 and L12 Q3 remain held; L1 Q4 remains a separate notation hold. L10 Q2's key letter remains C; the patch explains the distinction between the §86 paradigm form and the role in the clause `Wê ew dît`.

No source, lesson, quiz, answer-key or learner-facing content was changed. No runtime/parser/manifest/database/Botkeep/Telegram/deployment change, tests/CI, learner-response analysis or psychometric validation was performed. `main` remains read-only. GitHub archive history is not an independent ZIP/off-site backup; none is claimed.

# Cross-Course Reward Ledger Call-Site Audit — 2026-11-11

## Scope
Read-only audit of candidate branch `botkeep-menu-clean-2026-11-09`, covering official lesson completion, quiz completion, beta progress, and Arami assessment reward call sites. No code or live database was changed.

## Call-site inventory
- `complete_lesson_with_rewards`: one application call site in `finish_lesson`; the handler first classifies the lesson with `lesson_is_beta_review` and routes review lessons exclusively to `complete_beta_lesson`. A pending non-beta lesson is rejected.
- `complete_quiz_with_rewards`: standard quiz completion revalidates `lesson_quiz_is_available` immediately before writing the ledger. Arami's dedicated award helper independently checks course membership and the academic-review gate before calling the same reward ledger.
- `complete_beta_lesson`: used only by the review-only lesson completion branch; its SQL updates only `beta_completed_lessons`, without XP, score, coins, chests, badges, official lesson completion, or quiz completion.
- Badge checks occur only after first official lesson completion; beta-review lessons do not enter that branch. Badge display paths also filter beta-review lessons.

## Result
No unguarded application-level call site to the official lesson/quiz reward ledgers was found in the reviewed candidate source. The generic database functions themselves do not know academic review metadata and are not independently policy-aware; the application handlers are the enforcement boundary. Any future direct call added to application code must use the same gate. This remains an architectural consideration, not a presently identified callback bypass.

## Safety boundary
Read-only source audit. No Botkeep import, runtime restart, live database write, Railway deployment, or main-bot deployment occurred. Node17 support clearance remains required before runtime import.

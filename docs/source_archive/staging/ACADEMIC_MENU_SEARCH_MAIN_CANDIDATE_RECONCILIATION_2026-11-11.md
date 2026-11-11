# Academic Menu and Lesson Search Reconciliation — Main vs Candidate — 2026-11-11

## Source refs
- Main: `7db20f242087e3eb9149e2e788f6c20529870f32`
- Candidate: `botkeep-menu-clean-2026-11-09`

## Verified main-side behavior
Main contains the academic lesson search entry and search result construction in `message()`, and has a generic course catalogue. It includes the recent academic menu redesign and lesson-search hardening commits in its history. The main-side Arami course selector call currently passes completed lessons and sequential access, but the inspected call does not pass the candidate's separate beta-completed lesson state.

## Verified candidate-side behavior
Candidate contains a paginated lesson-search result keyboard and callback handler (`lessonsearch:`), clears stale search results when entering a new search, and exits search mode when a reply-keyboard menu action is selected. This prevents a menu command from accidentally being treated as a title query. Candidate's course menu also:
- gives access/lock state precedence over stale completion labels;
- filters beta completion counts to review lessons in the course;
- HTML-escapes course title and description;
- passes the beta-progress ledger into the Arami selector.

## Reconciliation finding
The two versions contain complementary behavior. Candidate has review-aware progress presentation and search-mode lifecycle protections; main has the newer menu/search integration commits and should remain the promotion base. Do not replace main's full `bot.py` with candidate's file wholesale. The future release must transplant only the candidate's review-gate and beta-progress changes into a main-based release branch, then preserve main's current search/menu functionality and combine the candidate's specific fixes after regression testing.

## Tests required before promotion
- Search mode starts clean after previous searches and stale daily-conversation state.
- Choosing any reply-keyboard menu item while search mode is active does not search that menu label.
- Search results paginate and callback identities remain correct across Arami and non-Arami courses.
- Locked lessons never appear available because of stale completion records.
- Beta progress displays separately and never counts as official completion.
- Arami selector accurately displays beta progress while preserving lesson 1 and lesson 5 dedicated handlers.
- Full existing suite and all three workflow checks pass on the exact main-based release commit.

## Safety
Read-only source comparison and documentation only. No application code changed. No Botkeep import/restart, live database write, Railway deployment, or main-bot deployment occurred. Node17 written support clearance remains required before any test-bot runtime import.

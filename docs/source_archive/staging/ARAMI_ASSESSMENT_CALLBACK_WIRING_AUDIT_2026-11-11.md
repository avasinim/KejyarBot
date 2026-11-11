# Assessment Callback Wiring Audit — 2026-11-11

## Scope
Read-only review of Arami Course 1 assessment callback entry points on candidate branch `botkeep-menu-clean-2026-11-09`. No runtime code was changed and no deployment/import was attempted.

## Verified production wiring
The three Telegram callback registrations in `bot.py` pass `can_take_assessment=lambda user_id, lesson_id: not lesson_is_beta_review(lesson_id)`:
- `arami1:` dedicated Lesson 1
- `aramiC:` shared Course 1
- `arami5:` dedicated Lesson 5

The assessment entry points call this guard when it is supplied. The Arami award helper independently checks course membership and `lesson_is_beta_review` immediately before writing the assessment reward ledger. Therefore the production application wiring has both an entry gate and a reward gate.

## Hardening observation
The callback function signatures retain `can_take_assessment=None` for compatibility. In that unconfigured mode, the dedicated Lesson 1 and Lesson 5 menus default assessment availability to True, and the action handlers do not reject assessment solely because the guard callback is absent. The shared callback likewise only performs the approval check when the callback is supplied. The current production `bot.py` registrations do supply it, so this is not evidence of a currently reachable production bypass; it is a fail-open integration hazard for any future caller or test harness that registers these callbacks without the guard.

## Recommendation
For a future isolated patch, make absence of `can_take_assessment` fail closed for assessment mode while leaving practice and reading available, and add regression tests for all three callback modules. Do not silently change compatibility behavior without running the full suite and CI.

## Safety boundary
Source-level audit only. No Botkeep import, restart, live database write, Railway deployment, or main-bot deployment occurred. Node17 support clearance remains a prerequisite for runtime import.

# Candidate-to-Main Promotion Boundary Audit — 2026-11-11

## Ref verification
- Main: `7db20f242087e3eb9149e2e788f6c20529870f32`
- Candidate: `botkeep-menu-clean-2026-11-09`
- GitHub compare reports the branches have diverged: candidate is 233 commits ahead and 12 commits behind main. They are not a safe fast-forward pair.

## PR status correction
- PR #145 is confirmed merged into candidate at `c30edf143a7304856b02cb4faa2bda46314cefde`.
- PR #146 is confirmed merged into candidate at `67b844a5fdb8c731872177ab33da6114b3255597`.
- PR #145's description still contains stale wording that says it is not merged; GitHub metadata confirms it is merged. The actual base is candidate, not main.
- PR #146 likewise targets candidate, not main.

## Critical runtime file comparison
The following file blob IDs were checked directly on main and candidate:
- `bot.py`: differs
- `database.py`: identical
- `course_runtime.py`: differs
- `arami_course1_telegram.py`: differs
- `arami_lesson1_telegram.py`: differs
- `arami_lesson5_telegram.py`: differs
- `courses.json`: differs
- `course_data/grammar_course4_lessons.json`: differs

The candidate's differing files include the review-gate changes, but the branch-wide comparison also shows unrelated historical differences and removed PDF assets. Therefore do not merge the whole candidate branch into main or import it as an assumed safe release.

## Decision
Keep candidate as a staging/integration branch. Any eventual release must be assembled as a reviewed, file-scoped promotion from a current main base, with an explicit allowlist of runtime files and required tests. First reconcile the 12 commits by which main is ahead, inspect all candidate-only changes and removed assets, and then run CI against the exact promotion commit. No main merge or deployment is authorized by this audit.

## Safety
No files were changed on main or candidate. This was a read-only comparison. No Botkeep import/restart, live database write, Railway deployment, or main-bot deployment occurred. Node17 written support clearance remains a hard prerequisite for test-bot runtime import.

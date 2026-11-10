# KejyarBot Main Branch CI and Workflow Coverage Review — 2026-11-10

## Read-only checks
Reviewed main branch commit and branch metadata, latest 15 repository Actions runs, all four workflow files on main, and job/step summaries for the three latest PR checks.

## Findings
1. Current main head at inspection: 7db20f242087e3eb9149e2e788f6c20529870f32, commit time 2026-11-10 08:36:40 UTC.
2. GitHub branch metadata reports main as protected=false. The dedicated branch-protection endpoint returned 403 (resource not accessible by integration), so individual protection rules/required checks could not be inspected.
3. The latest 15 visible Actions runs were all pull_request or pushes to the work/course3-lessons67-68-practice-archive-2026-11-10 branch. The three latest PR workflows on infra/railway-persistent-db-2026-11-10 all completed successfully: Course 4 beta review safety, Orthography course structure tests, and Python checks.
4. The successful PR jobs ran their listed compile/test steps to completion. This is evidence for the PR head commit 259d746cab1e546fa76d39bc1dc0be5d2c394176, not the main head commit.
5. The main head commit combined-status endpoint returned an empty statuses list, and the commit-workflow-runs endpoint returned an empty workflow_runs list. Therefore no CI result was established for the current main head during this check.
6. Workflow coverage is fragmented: Python checks run on main pushes and PRs to main; orthography tests run on main pushes/PRs; Kurdish-months tests are scoped to a specific feature branch and matching file paths; Course 4 beta safety is scoped to PRs and one named feature branch. This is not itself a failure, but means not every workflow runs on every branch change.

## Priority assessment
- P1: Confirm that main receives a current successful CI run before treating it as validated. The successful PR checks must not be described as main-branch checks.
- P1: Enable appropriate branch protection / required status checks on main if this repository is intended to prevent untested direct changes. The branch metadata currently says protected=false.
- P2: Review whether branch-specific workflows should remain narrowly scoped or be generalized to avoid accidental coverage gaps.

## Actions not performed
No workflow was dispatched or rerun, no branch settings were changed, no PR was merged, and no source files were edited.
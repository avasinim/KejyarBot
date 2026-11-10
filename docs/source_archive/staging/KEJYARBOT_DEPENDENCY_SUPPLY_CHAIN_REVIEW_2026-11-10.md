# KejyarBot Dependency and Deployment Reproducibility Review — 2026-11-10

## Read-only findings on `main`
- `requirements.txt` contains only `python-telegram-bot>=22,<23`. This constrains the major version but permits any future compatible minor/patch release within 22.x. There is no committed lock/constraints file in the inspected root configuration, so a rebuild at a later date may resolve a different dependency set.
- `.github/workflows/python-checks.yml` installs directly from `requirements.txt` on Python 3.12. This is useful CI coverage, but it does not lock dependency hashes or preserve a resolved environment manifest as a build artifact.
- The workflow references `actions/checkout@v7` and `actions/setup-python@v7` by major-version tags rather than immutable full commit SHAs. SHA pinning would improve supply-chain reproducibility and reduce exposure to mutable action tags.
- The inspected workflow grants `contents: read`, installs dependencies, compiles source, and runs unit tests; it does not receive deployment secrets or publish a release/deployment artifact.
- Lesson HTML rendering escapes source text with `html.escape(..., quote=False)` before wrapping it in Telegram HTML tags. The inspected course listing and lesson rendering paths therefore do not show a direct unescaped-user-text HTML injection issue.

## Recommended hardening (not applied)
1. Add a reproducible dependency lock/constraints file with hashes or an equivalent controlled dependency-resolution process.
2. Pin third-party GitHub Actions to verified full commit SHAs and use automated, reviewed updates.
3. Optionally preserve the resolved dependency manifest in CI for later incident investigation.

## Scope and limitations
Only repository source/configuration on `main` was inspected. No package installation, workflow run, deployment, secret inspection, or live runtime action was performed. This is a reproducibility hardening recommendation, not evidence of a known compromise or current outage.

No code, dependency, workflow, database, service, or deployment setting was changed.
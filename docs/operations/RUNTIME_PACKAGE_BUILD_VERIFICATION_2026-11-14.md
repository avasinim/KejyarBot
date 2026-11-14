# Runtime package build and archive verification — 2026-11-14

## Result

A runtime ZIP archive was built from the immutable source commit and downloaded from the successful GitHub Actions artifact.

- Repository: `avasinim/KejyarBot`
- Source commit checked out by workflow: `53393395224ffb6f676c660d51e0e6f7cdda425c`
- Branch containing the build workflow and audit records: `release/main-based-reconciled-2026-11-11`
- Package workflow commit: `655d56bd03ccee540108bb548f6e7e1ed2ec4f78`
- Workflow run: [43624965006](https://github.com/avasinim/KejyarBot/actions/runs/43624965006) — completed successfully
- Artifact ID: `14124993828`
- Artifact digest (outer GitHub artifact): `sha256:fa1a6c50d85e6d5ca9a1aca9701495e07e20732dafa4dc1445f488b53ae9ffdd`

## Verified runtime ZIP

- Filename: `KejyarBot-runtime-5339339.zip`
- Entries: 61
- Uncompressed source bytes: 6,489,919
- ZIP size: 4,763,895 bytes
- SHA-256: `f95eb920eef76684e102a78890a11da6fb8a0e39bdb48b191ea7727344b797f4`
- Archive contains exactly the 61 allowlisted paths from `DEPLOYMENT_PACKAGE_FILE_MANIFEST_2026-11-14.md`; the build script asserts path-set equality and refuses missing files.
- Local inspection confirmed 61 entries and no `.env`, SQLite database/sidecars, PDF, audio, JPG/JPEG, or SVG files.
- Seven approved PNG assets are included.

## CI validation

The package workflow and the Python checks, orthography structure tests, Kurdish months tests, Course 4 beta safety, Course 4 quiz override validation, review-gate regression validation, and Course 4 50-lesson beta validation all completed successfully for the package workflow commit.

## Deployment boundary

This is a built and verified archive, not an Altare upload. The Telegram token remains in Altare's separate `.env`. No Altare files were changed and the bot was not started. Before first start, confirm the persistent location for the newly-created `kejyar.db`. The user confirmed the bot has never been used and has no learner data to migrate.

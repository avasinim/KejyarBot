# Image asset inventory audit — 2026-11-14 13:09Z

## Source revision
Release branch: `release/main-based-reconciled-2026-11-11`
Audited commit: `04bd078cba7dd2113d5e0b6bc02195e683d4e302`
Git tree was complete (not truncated): 457 tracked files.

## Inventory
- 18 tracked image files in total:
  - 7 PNG files: six approved Course 1 infographic PNGs under `assets/course1_infographics/`, plus `assets/lessons/kejyar_lesson5_kurdish_letters_v2.png`.
  - 10 SVG files under `assets/infographics/`.
  - 1 JPG at repository root: `photo_2026-10-27_00-13-52.jpg`.
- No tracked audio files with extensions MP3, WAV, OGG, M4A, FLAC, or AAC.
- No tracked PDF files.

## Runtime reference audit
- `arami_course1_telegram.py` explicitly allows and sends exactly six Course 1 PNG infographics for lesson numbers 1, 2, 3, 4, 6, and 7.
- `lesson_image_delivery.py` routes the single shared PNG to exactly two lesson IDs: Arami Lesson 5 and Latin Orthography Lesson 1.
- `bot.py` has no-op compatibility infographic sender for the legacy text-only path; the current generic course callbacks send only exact allowlisted shared-image pairs.
- A scan of the current production Python modules found no runtime references to the 10 files in `assets/infographics/` or the root JPG. They are therefore classified as unreferenced by the scanned current runtime, not deleted or declared permanently obsolete.
- The six-image test in `tests/test_arami_course1_telegram.py` explicitly asserts only the six approved course1 PNG infographics are sent and Lesson 5 has no separate `lesson_05.png`.

## Packaging constraint / unresolved
- The repository currently tracks 18 image files, while the runtime-approved educational image set identified here is 7 unique files shared across 8 lesson placements.
- `.gitignore` excludes secrets, databases, Python caches, and virtual environments; it does not exclude the 10 SVG files or the root JPG.
- No dedicated image allowlist, package manifest, or deploy-time asset-filter configuration was identified in the repository root.
- Consequently, a full Git checkout/archive currently contains all 18 tracked image files. Actual provider-specific packaging behavior has not been verified.
- The user's package constraint is 8 or 9 educational images. The present audit verifies 7 runtime-used educational image files; the remaining one or two slots are not assumed or filled.
- No asset was deleted, moved, renamed, or excluded. No packaging/deployment setting was changed. A cleanup or packaging-filter change requires a separately approved, exact scope.

## Verification limits
- Static code and repository tree inspection only.
- No live Telegram image send, provider package build, deployment, Start, or Restart was performed.

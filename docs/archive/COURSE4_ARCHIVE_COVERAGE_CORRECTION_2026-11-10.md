# Course 4 archive coverage correction — 2026-11-10

## Why this correction exists
A second, direct inspection of `/KejyarBot/Course4_Archive/` and its README files found that the earlier preservation audit overstated the per-lesson append-only patch coverage as lessons 1–45. This note corrects that claim without modifying or deleting any prior archive.

## Verified coverage in the inspected Library folder
- README inventories explicitly list individual patches for lessons 1, 2, and 8–28.
- The folder listing also contains individual patch JSON files for lessons 20–44 (some duplicates/versioned files exist).
- Therefore individual patch files are evidenced for lessons 1, 2, and 8–44, with lessons 3–7 absent from the archive README and explicitly identified as missing.
- No individual patch file for lesson 45 or lesson 46 was present in the inspected folder listing.
- Consolidated ZIP checkpoints were present for lessons 29–38 and 29–41. These are checkpoint archives, not proof of a complete 46-lesson archive.
- A source baseline for the 46-lesson course is referenced in older README files, but a source baseline is not the same as an append-only patch for every lesson.

## Required interpretation
- Lesson 3–7: patch missing; recover from the authoritative source before creating any patch.
- Lesson 45–46: no individual patch was verified in this folder inspection; search other archive locations/source records before concluding they do not exist.
- Do not synthesize missing lesson content from neighboring lessons.
- Preserve all existing patches, ZIP files, README versions, and source snapshots unchanged.
- Any new patch must be a separate append-only file with its own validation and checkpoint.

## Safety
This is a Library/GitHub archive inventory correction only. No Botkeep files, SQLite database, Railway production configuration, or Telegram runtime were changed. No deployment or activation was performed.

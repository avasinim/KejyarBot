#!/usr/bin/env python3
"""Build a Botkeep-compatible source ZIP without secrets, databases, or binaries.

The prerecorded Kejyar MP3s are intentionally excluded because Botkeep's ZIP
uploader rejects binary files. Upload the existing files from voices/ separately
through SFTP after the server has been provisioned.
"""

from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent / "KejyarBot-Botkeep-Source.zip"
MAX_FILES = 200
MAX_UNCOMPRESSED_BYTES = 5 * 1024 * 1024

ALLOWED_SUFFIXES = {".py", ".json", ".svg", ".txt"}
ALLOWED_NAMES = {"README.md", "LICENSE"}
EXCLUDED_DIRS = {
    ".git", ".venv", "venv", "__pycache__", ".pytest_cache",
    "tests", "docs", "node_modules", "voices", "tools",
}
EXCLUDED_FILES = {
    ".env", "bot_backup.py", "bot_before_lesson_voice.py",
    "check_telegram_connection.py",
}


def include(path: Path) -> bool:
    # Never follow symlinks: an allowed-looking filename could point outside
    # the repository and accidentally package a secret or unrelated file.
    if path.is_symlink():
        return False
    relative = path.relative_to(ROOT)
    if any(part in EXCLUDED_DIRS for part in relative.parts):
        return False
    if path.name in EXCLUDED_FILES or path.name.endswith(("-wal", "-shm")):
        return False
    if path.suffix.lower() not in ALLOWED_SUFFIXES and path.name not in ALLOWED_NAMES:
        return False
    # Only text-based source/config/data assets are permitted in the ZIP.
    if path.suffix.lower() in {
        ".mp3", ".wav", ".ogg", ".jpg", ".jpeg", ".png", ".webp",
        ".gif", ".pdf", ".db", ".sqlite", ".sqlite3", ".pyc", ".exe",
    }:
        return False
    return path.is_file()


def main() -> int:
    required = {
        "bot.py",
        "main.py",
        "database.py",
        "voice.py",
        "daily_chat.py",
        "speech.py",
        "course_runtime.py",
        "course_lesson_adapters.py",
        "course_quiz_review.py",
        "courses.json",
        "requirements.txt",
        "course_data/orthography_foundations.json",
        "course_data/orthography_original_lessons.json",
        "course_data/orthography_foundations_quiz_draft.json",
        "course_data/daily_conversation_lessons_01_06.json",
        "course_data/daily_conversation_lessons_07_30.json",
        "course_data/daily_conversation_lessons_31_36.json",
        "course_data/daily_conversation_lessons_37_42.json",
        "course_data/daily_conversation_lessons_43_48.json",
        "course_data/daily_conversation_plan.json",
        "course_data/unified_orthography_lessons_01_12.json",
    }
    files = sorted(
        (path for path in ROOT.rglob("*") if include(path)),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )
    included = {path.relative_to(ROOT).as_posix() for path in files}
    missing = sorted(required - included)
    if missing:
        print("ERROR: required runtime files are missing:", file=sys.stderr)
        print("\n".join(missing), file=sys.stderr)
        return 1

    total_bytes = sum(path.stat().st_size for path in files)
    if len(files) > MAX_FILES:
        print(f"ERROR: {len(files)} files exceeds Botkeep's {MAX_FILES}-file limit.", file=sys.stderr)
        return 1
    if total_bytes >= MAX_UNCOMPRESSED_BYTES:
        print(
            f"ERROR: {total_bytes:,} uncompressed bytes is not below the 5 MiB limit.",
            file=sys.stderr,
        )
        return 1

    OUTPUT.unlink(missing_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())

    print(f"Created: {OUTPUT}")
    print(f"Files: {len(files)} / {MAX_FILES}")
    print(f"Uncompressed: {total_bytes:,} / less than {MAX_UNCOMPRESSED_BYTES:,} bytes")
    print(f"Compressed: {OUTPUT.stat().st_size:,} bytes")
    print("Excluded intentionally: .env, SQLite databases, tests/docs, backups, and MP3 binaries.")
    print("After provisioning, upload the existing voices/*.mp3 files separately using SFTP.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

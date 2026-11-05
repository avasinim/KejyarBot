#!/usr/bin/env python3
"""Validate Course 4's provisional PDF-to-lesson map without downloading PDFs."""
from __future__ import annotations

import ast
import sys
from pathlib import Path

EXPECTED = {
    1: set(range(7, 13)),   # Part 2: Pronoun (cover verified)
    2: set(range(1, 7)),    # Part 1: Noun (catalogue/size corroborated)
    3: set(range(13, 19)),  # Part 3: Adjective (cover verified)
    4: set(range(19, 25)),  # Part 4: Numerals and adverbs (catalogue/size)
    5: set(range(25, 31)),  # Part 5: Verb (catalogue/size)
}


def load_sources(path: Path):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "SOURCES"
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise ValueError("SOURCES assignment not found")


def validate(source_path: Path) -> list[str]:
    errors: list[str] = []
    sources = load_sources(source_path)
    actual_volumes = {row[0] for row in sources}
    if actual_volumes != set(EXPECTED):
        errors.append(f"Expected volumes 1-5; got {sorted(actual_volumes)}")

    seen: dict[int, int] = {}
    for row in sources:
        volume, commit, filename, blob_sha, lessons = row
        if len(commit) != 40 or len(blob_sha) != 40:
            errors.append(f"Volume {volume}: invalid commit/blob SHA length")
        if not filename.lower().endswith(".pdf"):
            errors.append(f"Volume {volume}: filename is not a PDF")
        if not isinstance(lessons, dict):
            errors.append(f"Volume {volume}: lesson map is not a dictionary")
            continue
        lesson_ids = {int(key) for key in lessons}
        if lesson_ids != EXPECTED.get(volume, set()):
            errors.append(
                f"Volume {volume}: expected lessons "
                f"{sorted(EXPECTED.get(volume, set()))}, got {sorted(lesson_ids)}"
            )
        for lesson in lesson_ids:
            if lesson in seen:
                errors.append(
                    f"Lesson {lesson}: mapped twice (volumes {seen[lesson]} and {volume})"
                )
            seen[lesson] = volume

    if set(seen) != set(range(1, 31)):
        errors.append(f"Lesson coverage must be 1-30; got {sorted(seen)}")
    return errors


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("extract_books.py")
    errors = validate(source)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: 5 volumes, 30 unique lessons, six lessons per volume.")
    print("NOTE: This checks mapping structure only, not printed PDF covers or lesson citations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

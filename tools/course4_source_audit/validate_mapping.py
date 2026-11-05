#!/usr/bin/env python3
"""Validate Course 4's provisional PDF-to-lesson map without downloading PDFs."""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

# Exact immutable source identities; volume numbers are repository filenames,
# not the morphology-part numbers printed inside the books.
EXPECTED = {
    1: {
        "commit": "2fb363f0abf3ebd4e753bd71f7c3d22d97cb7f55",
        "filename": "بەرگی ١ حا.pdf",
        "blob": "6a7153f0e50aee37f7f75bf0ab7c5faee5e1dd96",
        "lessons": set(range(7, 13)),
    },
    2: {
        "commit": "0b6c2941afcf91fe88c6c4b44ff954bb543f04cb",
        "filename": "بەرگی ٢.pdf",
        "blob": "c59e2f80004685aab85df203d6f5564deff62d6a",
        "lessons": set(range(1, 7)),
    },
    3: {
        "commit": "c20d44b7c4833e28eda51702e17d430816ef72b3",
        "filename": "بەرگی ٣.pdf",
        "blob": "810aac877c8422924db41db4d0ea4aaf96d53dce",
        "lessons": set(range(13, 19)),
    },
    4: {
        "commit": "e12112f4a9c7ebd6006a3089871aabc835e4a3d3",
        "filename": "بەرگی ٤.PDF",
        "blob": "322fd56eb9f0aa18df1c94ecb89fd4b774dd6234",
        "lessons": set(range(19, 25)),
    },
    5: {
        "commit": "45166d71ba9ccaa3caf320e7edf334b95fa91044",
        "filename": "بەرگی ٥.pdf",
        "blob": "001a3fd91ba07f85cac1e5ac3214725241a72f7e",
        "lessons": set(range(25, 31)),
    },
}


def load_sources(path: Path):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "SOURCES"
            for target in node.targets
        ):
            value = ast.literal_eval(node.value)
            if not isinstance(value, list):
                raise ValueError("SOURCES must be a list")
            return value
    raise ValueError("SOURCES assignment not found")


def validate(source_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        sources = load_sources(source_path)
    except (SyntaxError, ValueError, OSError) as exc:
        return [f"Cannot load SOURCES: {exc}"]

    seen_volumes: set[int] = set()
    seen_lessons: dict[int, int] = {}
    for row in sources:
        if not isinstance(row, tuple) or len(row) != 5:
            errors.append(f"Malformed source row: expected 5 fields, got {row!r}")
            continue
        volume, commit, filename, blob_sha, lessons = row
        if not isinstance(volume, int) or volume not in EXPECTED:
            errors.append(f"Unexpected volume identifier: {volume!r}")
            continue
        if volume in seen_volumes:
            errors.append(f"Volume {volume}: duplicate source row")
        seen_volumes.add(volume)

        expected = EXPECTED[volume]
        if commit != expected["commit"]:
            errors.append(f"Volume {volume}: source commit does not match immutable manifest")
        if filename != expected["filename"]:
            errors.append(f"Volume {volume}: filename does not match immutable manifest")
        if blob_sha != expected["blob"]:
            errors.append(f"Volume {volume}: Git blob SHA does not match immutable manifest")
        if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
            errors.append(f"Volume {volume}: invalid commit SHA format")
        if not isinstance(blob_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", blob_sha):
            errors.append(f"Volume {volume}: invalid blob SHA format")
        if not isinstance(filename, str) or not filename.lower().endswith(".pdf"):
            errors.append(f"Volume {volume}: filename is not a PDF")
        if not isinstance(lessons, dict):
            errors.append(f"Volume {volume}: lesson map is not a dictionary")
            continue

        try:
            lesson_ids = {int(key) for key in lessons}
        except (TypeError, ValueError):
            errors.append(f"Volume {volume}: lesson keys must be integer strings")
            continue
        if len(lesson_ids) != len(lessons):
            errors.append(f"Volume {volume}: duplicate lesson keys after integer conversion")
        if lesson_ids != expected["lessons"]:
            errors.append(
                f"Volume {volume}: expected lessons "
                f"{sorted(expected['lessons'])}, got {sorted(lesson_ids)}"
            )
        for lesson in lesson_ids:
            if lesson in seen_lessons:
                errors.append(
                    f"Lesson {lesson}: mapped twice "
                    f"(volumes {seen_lessons[lesson]} and {volume})"
                )
            seen_lessons[lesson] = volume

    if seen_volumes != set(EXPECTED):
        errors.append(f"Expected each volume exactly once; got {sorted(seen_volumes)}")
    if set(seen_lessons) != set(range(1, 31)):
        errors.append(f"Lesson coverage must be 1-30; got {sorted(seen_lessons)}")
    return errors


def main() -> int:
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("extract_books.py")
    errors = validate(source)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS: immutable source identities and 30 unique lesson mappings match.")
    print("NOTE: This validates manifest structure only; it does not inspect PDF covers or citations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

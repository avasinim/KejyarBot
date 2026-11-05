#!/usr/bin/env python3
"""Fail-closed release gate for Course 4 source-backed lessons."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

EXPECTED_LESSONS = set(range(1, 31))
REQUIRED_LESSON_FIELDS = (
    "source_commit", "source_blob_sha", "pdf_page_start", "pdf_page_end",
    "printed_page_start", "printed_page_end", "evidence_excerpt",
    "reviewer", "reviewed_at",
)


def validate(data: dict, release: bool = False) -> list[str]:
    errors: list[str] = []
    lessons = data.get("lessons")
    if not isinstance(lessons, list):
        return ["lessons must be a list"]
    ids = [x.get("lesson_id") for x in lessons if isinstance(x, dict)]
    if len(ids) != len(lessons) or set(ids) != EXPECTED_LESSONS or len(ids) != 30:
        errors.append("manifest must contain exactly one entry for each lesson 1-30")

    seen: set[int] = set()
    for item in lessons:
        if not isinstance(item, dict):
            continue
        lesson_id = item.get("lesson_id")
        if lesson_id in seen:
            errors.append(f"lesson {lesson_id}: duplicate entry")
        seen.add(lesson_id)
        if item.get("status") not in {"blocked", "in_review", "approved"}:
            errors.append(f"lesson {lesson_id}: invalid status")
        if item.get("source_part") != ((lesson_id - 1) // 6 + 1):
            errors.append(f"lesson {lesson_id}: incorrect source part")
        if release:
            for field in REQUIRED_LESSON_FIELDS:
                value = item.get(field)
                if value is None or value == "":
                    errors.append(f"lesson {lesson_id}: missing {field}")
            for field in ("pdf_page_start", "pdf_page_end", "printed_page_start", "printed_page_end"):
                if not isinstance(item.get(field), int) or item[field] < 1:
                    errors.append(f"lesson {lesson_id}: {field} must be a positive integer")
            if item.get("status") != "approved":
                errors.append(f"lesson {lesson_id}: not approved")
            for field in ("source_commit", "source_blob_sha"):
                if not re.fullmatch(r"[0-9a-f]{40}", str(item.get(field, ""))):
                    errors.append(f"lesson {lesson_id}: invalid {field}")
            for field in ("author_terms", "author_examples"):
                if not item.get(field):
                    errors.append(f"lesson {lesson_id}: {field} is empty")
            for field in ("draft_claims_checked", "dialect_scope_checked", "quiz_reviewed"):
                if item.get(field) is not True:
                    errors.append(f"lesson {lesson_id}: {field} is not true")

    if release:
        for field in ("runtime_tests_passed", "regression_tests_passed", "all_quizzes_reviewed"):
            if data.get(field) is not True:
                errors.append(f"course gate: {field} is not true")
        if data.get("source_mapping_status") != "verified":
            errors.append("course gate: source mapping is not verified")
        if data.get("course_status") != "approved":
            errors.append("course gate: course status is not approved")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("course4_release_gate.json"))
    parser.add_argument("--release", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"BLOCKED: cannot read manifest: {exc}")
        return 2
    errors = validate(data, release=args.release)
    if errors:
        print(f"BLOCKED: {len(errors)} issue(s).")
        for error in errors:
            print(" -", error)
        return 1 if args.release else 0
    print("PASS: manifest structure is valid.")
    if args.release:
        print("PASS: all Course 4 release conditions are approved.")
    else:
        print("INFO: structural check only; this does not approve publication.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

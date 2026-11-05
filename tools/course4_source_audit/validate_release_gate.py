#!/usr/bin/env python3
"""Fail-closed release gate for Course 4 source-backed lessons."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

EXPECTED_LESSONS = set(range(1, 31))


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
        if not release:
            continue

        required = ("source_edition", "source_commit", "source_blob_sha", "reviewer", "reviewed_at")
        for field in required:
            if not item.get(field):
                errors.append(f"lesson {lesson_id}: missing {field}")
        for field in ("source_commit", "source_blob_sha"):
            if not re.fullmatch(r"[0-9a-f]{40}", str(item.get(field, ""))):
                errors.append(f"lesson {lesson_id}: invalid {field}")
        if item.get("status") != "approved":
            errors.append(f"lesson {lesson_id}: not approved")

        claims = item.get("claims")
        if not isinstance(claims, list) or not claims:
            errors.append(f"lesson {lesson_id}: no claim-level evidence ledger")
        else:
            for index, claim in enumerate(claims, start=1):
                prefix = f"lesson {lesson_id}, claim {index}"
                if not isinstance(claim, dict):
                    errors.append(f"{prefix}: malformed claim")
                    continue
                if not claim.get("claim_text") or not claim.get("source_quote"):
                    errors.append(f"{prefix}: missing claim text or source quote")
                if not isinstance(claim.get("pdf_page"), int) or claim["pdf_page"] < 1:
                    errors.append(f"{prefix}: invalid PDF page")
                if not isinstance(claim.get("printed_page"), int) or claim["printed_page"] < 1:
                    errors.append(f"{prefix}: invalid printed page")
                kind, label = claim.get("claim_type"), claim.get("evidence_label")
                if kind not in {"author", "editor", "external"}:
                    errors.append(f"{prefix}: invalid claim_type")
                if label not in {"A", "C", "D"}:
                    errors.append(f"{prefix}: evidence must be A, C or D; OCR-only/U evidence cannot pass")
                if kind == "author" and label != "A":
                    errors.append(f"{prefix}: author-attributed claim requires direct visual evidence A")
                if kind == "editor" and label != "C":
                    errors.append(f"{prefix}: editor explanation must be labelled C")
                if kind == "external" and label != "D":
                    errors.append(f"{prefix}: external comparison must be labelled D")
                if claim.get("review_status") != "approved":
                    errors.append(f"{prefix}: not independently approved")

        quizzes = item.get("quiz_evidence")
        if not isinstance(quizzes, list) or not quizzes:
            errors.append(f"lesson {lesson_id}: quiz evidence ledger is empty")
        else:
            for index, quiz in enumerate(quizzes, start=1):
                if not isinstance(quiz, dict) or not quiz.get("question_id"):
                    errors.append(f"lesson {lesson_id}, quiz {index}: malformed item")
                    continue
                if not quiz.get("source_claim_ids") or not quiz.get("answer_evidence"):
                    errors.append(f"lesson {lesson_id}, quiz {index}: missing evidence mapping")
                if quiz.get("review_status") != "approved":
                    errors.append(f"lesson {lesson_id}, quiz {index}: not approved")

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

#!/usr/bin/env python3
"""Build a text-only Altare runtime containing exactly three approved courses.

The source repository is never modified. All filtering and compatibility edits
are applied only to a temporary deployment copy.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE_IDS = {
    "arami_orthography_foundations",
    "unified_orthography",
    "kurmanji_latin_orthography",
}

RUNTIME_FILES = [
    "bot.py",
    "database.py",
    "daily_chat.py",
    "course_runtime.py",
    "course_lesson_adapters.py",
    "course_quiz_review.py",
    "quiz_option_order.py",
    "latin_course_runtime.py",
    "arami_course1_runtime.py",
    "arami_course1_telegram.py",
    "arami_lesson1_interaction.py",
    "arami_lesson1_telegram.py",
    "arami_lesson5_telegram.py",
    "kurdish_months.py",
    "courses.json",
    "requirements.txt",
    "course_data/unified_orthography_lessons_01_66.json",
    "course_data/latin_courses_manifest_draft.json",
    "course_data/latin_course_1_source_aligned_lessons_01_12.md",
    "course_data/latin_course_1_quiz_answer_key_draft.md",
    "course_data/arami_course1_manifest.json",
    "course_data/arami_course1_source_quiz_banks.json",
    "course_data/arami_course1_lesson_01_content.json",
    "course_data/arami_course1_lesson_01_interactions.json",
    "course_data/arami_course1_lesson_02_vowels_source.md",
    "course_data/arami_course1_lesson_03_vowel_rules_source.md",
    "course_data/arami_course1_lesson_04_source.md",
    "course_data/arami_course1_lesson_05_source.md",
    "course_data/arami_course1_lesson_05_interactions.json",
    "course_data/arami_course1_received_lesson_06_source.md",
    "course_data/arami_course1_lesson_07_source.md",
    "course_data/arami_course1_lesson_08_t_z_combined_source.md",
    "course_data/arami_course1_lesson_09_alef_aa_source.md",
    "course_data/arami_course1_lesson_10_hamza_source.md",
    "course_data/arami_course1_lesson_11_vowels_bore_sara_zhera_source.md",
    "course_data/arami_course1_lesson_12_y_source.md",
    "course_data/arami_course1_lesson_13_w_source.md",
    "course_data/arami_course1_lesson_14_bizroke_hishu_source.md",
    "course_data/arami_course1_lesson_15_l_ll_source.md",
    "course_data/arami_course1_lesson_16_r_rr_source.md",
    "course_data/arami_course1_lesson_16_v_source.md",
    "course_data/arami_course1_lesson_17_he_e_source.md",
    "course_data/arami_course1_lesson_18_k_g_mukriani_source.md",
    "course_data/arami_course1_lesson_19_cluster_source.md",
    "course_data/arami_course1_lesson_20_syllable_cluster_source.md",
]


def replace_once(source: str, old: str, new: str, label: str) -> str:
    count = source.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one source match, found {count}")
    return source.replace(old, new, 1)


def transform_courses_json(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    original_ids = [item.get("id") for item in data.get("courses", [])]
    courses = [item for item in data.get("courses", []) if item.get("id") in COURSE_IDS]
    ids = {item.get("id") for item in courses}
    if ids != COURSE_IDS or len(courses) != 3:
        raise RuntimeError(f"Course manifest mismatch: found {sorted(ids)}")
    data["courses"] = courses
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def transform_latin_manifest(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    courses = [
        item for item in data.get("courses", [])
        if item.get("id") == "kurmanji_latin_orthography"
    ]
    if len(courses) != 1:
        raise RuntimeError("Latin source manifest must contain exactly Latin Course 1")
    data["courses"] = courses
    data["status"] = "runtime_package_filtered_to_latin_course_1"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def transform_bot(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    source = replace_once(
        source,
        "from course_lesson_adapters import adapt_conversation_lessons, adapt_unified_orthography_lessons",
        "from course_lesson_adapters import adapt_unified_orthography_lessons",
        "bot adapter import",
    )
    source = replace_once(
        source,
        "from lesson_image_delivery import send_shared_lesson_image\n",
        "",
        "bot image-delivery import",
    )

    start = source.index("CONVERSATION_DRAFTS = [")
    end = source.index("# The two Kurmanji Latin courses remain separate", start)
    selected_course_loader = '''UNIFIED_ORTHOGRAPHY_DRAFT = load_json("course_data/unified_orthography_lessons_01_66.json")
UNIFIED_LESSONS, UNIFIED_QUIZZES = adapt_unified_orthography_lessons(UNIFIED_ORTHOGRAPHY_DRAFT)
duplicate_ids = set(LESSON_DATA).intersection(UNIFIED_LESSONS)
if duplicate_ids:
    raise ValueError(f"Duplicate lesson IDs across courses: {sorted(duplicate_ids)}")
LESSON_DATA.update(UNIFIED_LESSONS)
QUIZ_DATA.update(UNIFIED_QUIZZES)

'''
    source = source[:start] + selected_course_loader + source[end:]
    source = source.replace(
        "# The two Kurmanji Latin courses remain separate by source part, lesson IDs and quiz keys.",
        "# Only Latin Course 1 is included in this deployment package.",
    )
    source = replace_once(
        source,
        '''LATIN_COURSE_IDS = {
    "kurmanji_latin_orthography",
    "kurmanji_latin_grammar",
}''',
        'LATIN_COURSE_IDS = {"kurmanji_latin_orthography"}',
        "Latin course ID allowlist",
    )

    # Image delivery is deliberately omitted; lesson text and assessments remain intact.
    source = re.sub(
        r"^[ \t]*await send_shared_lesson_image\([^\n]*\)\n",
        "",
        source,
        flags=re.MULTILINE,
    )
    if "send_shared_lesson_image" in source or "lesson_image_delivery" in source:
        raise RuntimeError("Image-delivery code remains in packaged bot.py")

    # The Course 4-only predicate has no callers in the selected runtime.
    marker_start = "def is_course4_grammar_lesson(lesson_id):"
    if marker_start in source:
        start = source.index(marker_start)
        end = source.index("def course_is_active(course_id):", start)
        source = source[:start] + source[end:]

    forbidden = (
        "daily_conversation_lessons_",
        "GRAMMAR_COURSE4",
        "kurmanji_latin_grammar",
        "send_shared_lesson_image",
        "lesson_image_delivery",
    )
    for token in forbidden:
        if token in source:
            raise RuntimeError(f"Out-of-scope runtime reference remains in bot.py: {token}")
    path.write_text(source, encoding="utf-8")


def transform_latin_runtime(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    source = replace_once(
        source,
        '"""Lossless runtime loader for two source-separated Kurmanji Latin course drafts.',
        '"""Lossless runtime loader for the selected Kurmanji Latin orthography course.',
        "Latin runtime docstring",
    )
    source = source.replace(
        'COURSE2_SOURCE_PATH = ROOT / "course_data" / "latin_course_2_source_aligned_lessons_01_12.md"\n',
        "",
    )
    source = source.replace(
        'COURSE2_KEY_PATH = ROOT / "course_data" / "latin_course_2_quiz_answer_key_draft.md"\n',
        "",
    )
    start = source.index("COURSES = (")
    end = source.index("\nLESSON_HEADING", start)
    one_course = '''COURSES = (
    {
        "id": "kurmanji_latin_orthography",
        "source_part": "Part I — Celadet Alî Bedir-Xan — Elfabêya kurdî (Nefel, Stockholm, 2002), printed pages 11–36.",
        "first_heading": "## Ders 1:",
        "lesson_prefix": "kurmanji_latin_orthography",
        "key_path": COURSE1_KEY_PATH,
    },
)'''
    source = source[:start] + one_course + source[end:]
    source = replace_once(
        source,
        '''        # Each Latin course reads only its own source section/document.
        # Course 2 is never inferred as the second half of a combined master.
        source_path = (
            COURSE2_SOURCE_PATH
            if course["id"] == "kurmanji_latin_grammar"
            else COURSE1_SOURCE_PATH
        )''',
        '        source_path = COURSE1_SOURCE_PATH',
        "Latin source selection",
    )
    source = source.replace(
        '"""Return (lesson_data, quiz_data, course_records), validating all 24 lessons."""',
        '"""Return (lesson_data, quiz_data, course_records), validating 12 lessons."""',
    )
    if "kurmanji_latin_grammar" in source or "COURSE2_SOURCE_PATH" in source:
        raise RuntimeError("Latin Course 2 references remain in packaged Latin runtime")
    path.write_text(source, encoding="utf-8")


def transform_arami_telegram(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    source = replace_once(
        source,
        "from lesson_image_delivery import shared_lesson_image_path\n",
        "",
        "Arami image-delivery import",
    )
    start = source.index("def build_lesson_infographic_svg(lesson, source):")
    end = source.index("async def _send_question(", start)
    no_image_delivery = '''async def send_lesson_infographic(message, lesson, source=None, base_dir=None):
    """Compatibility no-op: image assets and delivery are excluded from this package."""
    return False


'''
    source = source[:start] + no_image_delivery + source[end:]
    if "shared_lesson_image_path" in source or "reply_photo" in source or "assets/course1_infographics" in source:
        raise RuntimeError("Arami image-delivery code remains in packaged module")
    path.write_text(source, encoding="utf-8")


def transform_arami_lesson5(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    source = replace_once(
        source,
        "from lesson_image_delivery import send_shared_lesson_image\n",
        "",
        "Arami Lesson 5 image import",
    )
    image_call = '''        await send_shared_lesson_image(
            query.message, "arami_orthography_foundations", lesson_record["id"], base_dir=base_dir
        )
'''
    source = replace_once(source, image_call, "", "Arami Lesson 5 image call")
    if "send_shared_lesson_image" in source or "lesson_image_delivery" in source:
        raise RuntimeError("Arami Lesson 5 image-delivery code remains")
    path.write_text(source, encoding="utf-8")


def validate_package(package: Path) -> None:
    courses = json.loads((package / "courses.json").read_text(encoding="utf-8"))["courses"]
    ids = {item["id"] for item in courses}
    if ids != COURSE_IDS or len(courses) != 3:
        raise RuntimeError(f"Packaged courses are not the exact three selected: {sorted(ids)}")

    latin = json.loads(
        (package / "course_data/latin_courses_manifest_draft.json").read_text(encoding="utf-8")
    )["courses"]
    if len(latin) != 1 or latin[0]["id"] != "kurmanji_latin_orthography":
        raise RuntimeError("Packaged Latin manifest is not restricted to Course 1")

    arami = json.loads(
        (package / "course_data/arami_course1_manifest.json").read_text(encoding="utf-8")
    )
    if len(arami.get("lessons", [])) != 21:
        raise RuntimeError("Arami Course 1 manifest must retain all 21 lessons")
    for lesson in arami["lessons"]:
        content_file = lesson.get("content_file")
        if not content_file or not (package / content_file).is_file():
            raise RuntimeError(f"Missing Arami source for lesson {lesson.get('number')}: {content_file}")

    forbidden_names = {
        "lesson_image_delivery.py",
        "daily_conversation_lessons_01_06.json",
        "daily_conversation_lessons_07_30.json",
        "daily_conversation_lessons_31_36.json",
        "daily_conversation_lessons_37_42.json",
        "grammar_course4_lessons.json",
        "grammar_course4_quiz_overrides.json",
        "latin_course_2_source_aligned_lessons_01_12.md",
        "latin_course_2_quiz_answer_key_draft.md",
    }
    actual_names = {item.name for item in package.rglob("*") if item.is_file()}
    overlap = forbidden_names & actual_names
    if overlap:
        raise RuntimeError(f"Out-of-scope files included: {sorted(overlap)}")

    for item in package.rglob("*"):
        if not item.is_file():
            continue
        if item.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".mp3", ".wav", ".ogg", ".mp4"}:
            raise RuntimeError(f"Media file must not be packaged: {item.relative_to(package)}")
        if item.suffix == ".py":
            source = item.read_text(encoding="utf-8")
            if "lesson_image_delivery" in source or "send_shared_lesson_image" in source:
                raise RuntimeError(f"Image delivery reference remains: {item.relative_to(package)}")
            compile(source, str(item), "exec")


def build(output_dir: Path) -> tuple[Path, Path]:
    package = output_dir / "runtime"
    if package.exists():
        shutil.rmtree(package)
    package.mkdir(parents=True)

    for relative in RUNTIME_FILES:
        source = ROOT / relative
        if not source.is_file():
            raise FileNotFoundError(f"Required runtime file is missing from repository: {relative}")
        target = package / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    transform_courses_json(package / "courses.json")
    transform_latin_manifest(package / "course_data/latin_courses_manifest_draft.json")
    transform_bot(package / "bot.py")
    transform_latin_runtime(package / "latin_course_runtime.py")
    transform_arami_telegram(package / "arami_course1_telegram.py")
    transform_arami_lesson5(package / "arami_lesson5_telegram.py")
    validate_package(package)

    archive = output_dir / "kejyarbot-altare-three-courses.zip"
    if archive.exists():
        archive.unlink()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zipped:
        for item in sorted(package.rglob("*")):
            if item.is_file():
                zipped.write(item, item.relative_to(package).as_posix())

    manifest = output_dir / "ALTARE_UPLOAD_FILES.txt"
    manifest.write_text(
        "Upload the files inside the ZIP to the Altare bot root, preserving folders.\n"
        "Do not upload this manifest as a runtime file.\n\n"
        + "\n".join(RUNTIME_FILES)
        + "\n",
        encoding="utf-8",
    )
    return archive, manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist" / "altare-three-courses")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive, manifest = build(args.output_dir)
    print(f"Package: {archive}")
    print(f"Upload manifest: {manifest}")
    print(f"Runtime files: {len(RUNTIME_FILES)}")


if __name__ == "__main__":
    main()

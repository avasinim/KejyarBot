import json
import tempfile
import unittest
from pathlib import Path

from arami_course1_runtime import (
    AramiCourseError, COURSE_ID, LESSON_1_ID,
    load_arami_course1, get_arami_lesson2_audio_path,
    load_arami_lesson1_interactions, load_arami_lesson1_content,
)


class AramiCourseRuntimeTests(unittest.TestCase):
    def fixture(self, root):
        course_dir = root / "course_data"
        course_dir.mkdir()
        manifest = {
            "course_id": COURSE_ID,
            "course_total_lessons": 4,
            "safety": {"separate_from_latin_courses": True},
            "lessons": [
                {"id": LESSON_1_ID,
                 "content_source": "user_supplied_immutable",
                 "audio_files": [{"file": "بزوێنی ی.ogg", "label": "دەنگی بزوێنی ی"}],
                 "content_status": "source_pages_1_to_4_structured_for_Telegram_reading; original wording preserved"},
                {"id": "arami_course1_lesson_02",
                 "audio_asset": "دەنگەکانی ئەلفبێ.ogg",
                 "audio_commit": "5642e5310cc856f7bfd8c821086a9f2febe419e6",
                 "audio_status": "user_confirmed_asset_repository_root; original_recording_preserved"},
                {"id": "arami_course1_lesson_03"},
                {"id": "arami_course1_lesson_04"},
            ],
        }
        (course_dir / "arami_course1_manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
        )
        (root / "دەنگەکانی ئەلفبێ.ogg").write_bytes(b"OGG test")
        (root / "بزوێنی ی.ogg").write_bytes(b"OGG test")
        return manifest

    def test_repository_manifest_declares_21_lessons_in_round_one(self):
        repo_root = Path(__file__).resolve().parents[1]
        manifest = load_arami_course1(repo_root)
        self.assertEqual(manifest["round"], 1)
        self.assertEqual(manifest["round_title"], "ڕێنووسی سەرەتاییی کوردی")
        self.assertEqual(manifest["course_total_lessons"], 21)
        self.assertEqual(manifest["safety"]["course_total_lessons"], 21)
        self.assertEqual(len(manifest["lessons"]), 21)
        self.assertEqual(manifest["lessons"][0]["title"], "پیتەکان و دەنگەکان")
        self.assertEqual(manifest["lessons"][-1]["number"], 21)

    def test_source_audit_matches_all_21_existing_lesson_source_files(self):
        repo_root = Path(__file__).resolve().parents[1]
        manifest = load_arami_course1(repo_root)
        expected_numbers = list(range(1, 22))
        self.assertEqual(
            manifest["source_audit"]["lesson_numbers_with_source_content"],
            expected_numbers,
        )
        for lesson in manifest["lessons"]:
            source_path = repo_root / lesson["content_file"]
            self.assertTrue(source_path.is_file(), f"missing source for lesson {lesson['number']}")

    def test_rejects_course_size_that_disagrees_with_declared_total(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self.fixture(root)
            manifest["course_size"] = 3
            path = root / "course_data" / "arami_course1_manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaises(AramiCourseError):
                load_arami_course1(root)

    def test_loads_four_isolated_namespaced_lessons(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = self.fixture(Path(temp))
            loaded = load_arami_course1(temp)
            self.assertEqual(loaded["course_id"], COURSE_ID)
            self.assertEqual(loaded["lessons"][0]["id"], LESSON_1_ID)
            self.assertEqual(len(manifest["lessons"]), 4)

    def test_loads_only_verified_eight_vowel_interactions(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            source_bank = Path(__file__).resolve().parents[1] / "course_data" / "arami_course1_lesson_01_interactions.json"
            target = root / "course_data" / source_bank.name
            target.write_text(source_bank.read_text(encoding="utf-8"), encoding="utf-8")
            bank = load_arami_lesson1_interactions(root)
            for mode in ("practice", "assessment"):
                vowel = [item for item in bank[mode] if item["section_id"] == "lesson1_vowel_count"]
                self.assertEqual(len(vowel), 1)
                self.assertEqual(vowel[0]["options"][vowel[0]["answer_index"]], "٨ بزوێن")

    def test_rejects_interaction_bank_with_wrong_vowel_answer(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            source_bank = Path(__file__).resolve().parents[1] / "course_data" / "arami_course1_lesson_01_interactions.json"
            target = root / "course_data" / source_bank.name
            bank = json.loads(source_bank.read_text(encoding="utf-8"))
            vowel = next(item for item in bank["practice"] if item["section_id"] == "lesson1_vowel_count")
            vowel["options"][vowel["answer_index"]] = "٦ بزوێن"
            target.write_text(json.dumps(bank, ensure_ascii=False), encoding="utf-8")
            with self.assertRaises(AramiCourseError):
                load_arami_lesson1_interactions(root)

    def test_rejects_unverified_chart_color_answer(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            source_bank = Path(__file__).resolve().parents[1] / "course_data" / "arami_course1_lesson_01_interactions.json"
            target = root / "course_data" / source_bank.name
            bank = json.loads(source_bank.read_text(encoding="utf-8"))
            bank["practice"][0]["section_id"] = "lesson1_chart_categories"
            target.write_text(json.dumps(bank, ensure_ascii=False), encoding="utf-8")
            with self.assertRaises(AramiCourseError):
                load_arami_lesson1_interactions(root)

    def test_resolves_only_confirmed_lesson2_audio(self):
        with tempfile.TemporaryDirectory() as temp:
            self.fixture(Path(temp))
            path = get_arami_lesson2_audio_path(temp)
            self.assertEqual(path.name, "دەنگەکانی ئەلفبێ.ogg")

    def test_lesson1_uses_its_own_uploaded_recording(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = self.fixture(Path(temp))
            self.assertEqual(manifest["lessons"][0]["audio_files"], [{"file": "بزوێنی ی.ogg", "label": "دەنگی بزوێنی ی"}])
            loaded = load_arami_course1(temp)
            self.assertEqual(loaded["lessons"][0]["audio_files"][0]["file"], "بزوێنی ی.ogg")

    def test_lesson1_cannot_claim_the_lesson2_recording(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = self.fixture(Path(temp))
            manifest["lessons"][0]["audio_asset"] = "دەنگەکانی ئەلفبێ.ogg"
            path = Path(temp) / "course_data" / "arami_course1_manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaises(AramiCourseError):
                load_arami_course1(temp)

    def test_rejects_wrong_audio_assignment(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = self.fixture(Path(temp))
            manifest["lessons"][1]["audio_asset"] = "voices/lesson_start.mp3"
            path = Path(temp) / "course_data" / "arami_course1_manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaises(AramiCourseError):
                load_arami_course1(temp)

    def test_rejects_course_overlap_or_wrong_count(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = self.fixture(Path(temp))
            manifest["lessons"].pop()
            path = Path(temp) / "course_data" / "arami_course1_manifest.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaises(AramiCourseError):
                load_arami_course1(temp)

    def test_missing_audio_is_not_silently_substituted(self):
        with tempfile.TemporaryDirectory() as temp:
            self.fixture(Path(temp))
            (Path(temp) / "دەنگەکانی ئەلفبێ.ogg").unlink()
            with self.assertRaises(AramiCourseError):
                get_arami_lesson2_audio_path(temp)

    def test_loads_complete_source_lesson_with_eight_sections(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            source = Path(__file__).resolve().parents[1] / "course_data" / "arami_course1_lesson_01_content.json"
            target = root / "course_data" / source.name
            target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
            lesson = load_arami_lesson1_content(root)
            self.assertEqual(lesson["lesson_id"], LESSON_1_ID)
            self.assertEqual(len(lesson["sections"]), 8)
            self.assertEqual(len(lesson["objectives"]), 5)
            self.assertIn("٣٤ پیت", lesson["sections"][0]["body"])
            self.assertIn("٨", lesson["sections"][1]["body"])

    def test_rejects_incomplete_source_lesson(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            target = root / "course_data" / "arami_course1_lesson_01_content.json"
            target.write_text(json.dumps({
                "course_id": COURSE_ID, "lesson_id": LESSON_1_ID,
                "sections": [], "objectives": [], "conclusion": ""
            }), encoding="utf-8")
            with self.assertRaises(AramiCourseError):
                load_arami_lesson1_content(root)


    def test_audio_catalog_lesson_assignments_match_manifest_without_reuse(self):
        repo_root = Path(__file__).resolve().parents[1]
        manifest = json.loads((repo_root / "course_data" / "arami_course1_manifest.json").read_text(encoding="utf-8"))
        catalog = json.loads((repo_root / "course_data" / "arami_course1_audio_catalog.json").read_text(encoding="utf-8"))
        catalog_by_file = {item["filename"]: item for item in catalog["assets"]}
        assigned = {}
        for lesson in manifest["lessons"]:
            files = {item["file"] for item in lesson.get("audio_files", [])}
            for filename in files:
                self.assertNotIn(filename, assigned, f"{filename} is reused across lessons")
                assigned[filename] = lesson["id"]
                self.assertIn(filename, catalog_by_file)
                self.assertEqual(catalog_by_file[filename]["lesson_id"], lesson["id"])

    def test_l_and_ll_recordings_belong_only_to_lesson_15(self):
        repo_root = Path(__file__).resolve().parents[1]
        manifest = json.loads((repo_root / "course_data" / "arami_course1_manifest.json").read_text(encoding="utf-8"))
        lesson15 = next(item for item in manifest["lessons"] if item["number"] == 15)
        self.assertEqual(
            [item["file"] for item in lesson15["audio_files"]],
            ["دەنگی ل.ogg", "دەنگی ڵ.ogg"],
        )
        catalog = json.loads((repo_root / "course_data" / "arami_course1_audio_catalog.json").read_text(encoding="utf-8"))
        for filename in ("دەنگی ل.ogg", "دەنگی ڵ.ogg"):
            asset = next(item for item in catalog["assets"] if item["filename"] == filename)
            self.assertEqual(asset["lesson_id"], "arami_course1_lesson_15")

if __name__ == "__main__":
    unittest.main()

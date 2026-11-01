import json
import tempfile
import unittest
from pathlib import Path

from arami_course1_runtime import (
    AramiCourseError, COURSE_ID, LESSON_1_ID,
    load_arami_course1, get_arami_lesson1_audio_path,
    load_arami_lesson1_interactions, load_arami_lesson1_content,
)


class AramiCourseRuntimeTests(unittest.TestCase):
    def fixture(self, root):
        course_dir = root / "course_data"
        course_dir.mkdir()
        manifest = {
            "course_id": COURSE_ID,
            "safety": {"separate_from_latin_courses": True},
            "lessons": [
                {"id": LESSON_1_ID,
                 "content_source": "user_supplied_immutable",
                 "content_status": "source_pages_1_to_4_structured_for_Telegram_reading; original wording preserved",
                 "audio_asset": "دەنگەکانی ئەلفبێ.ogg",
                 "audio_commit": "5642e5310cc856f7bfd8c821086a9f2febe419e6",
                 "audio_status": "user_confirmed_asset_repository_root"},
                {"id": "arami_course1_lesson_02"},
                {"id": "arami_course1_lesson_03"},
                {"id": "arami_course1_lesson_04"},
            ],
        }
        (course_dir / "arami_course1_manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
        )
        (root / "دەنگەکانی ئەلفبێ.ogg").write_bytes(b"OGG test")
        return manifest

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

    def test_resolves_only_confirmed_lesson1_audio(self):
        with tempfile.TemporaryDirectory() as temp:
            self.fixture(Path(temp))
            path = get_arami_lesson1_audio_path(temp)
            self.assertEqual(path.name, "دەنگەکانی ئەلفبێ.ogg")

    def test_rejects_wrong_audio_assignment(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = self.fixture(Path(temp))
            manifest["lessons"][0]["audio_asset"] = "voices/lesson_start.mp3"
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
                get_arami_lesson1_audio_path(temp)

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


if __name__ == "__main__":
    unittest.main()

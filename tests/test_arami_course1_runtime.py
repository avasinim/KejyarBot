import json
import tempfile
import unittest
from pathlib import Path

from arami_course1_runtime import (
    AramiCourseError, COURSE_ID, LESSON_1_ID,
    load_arami_course1, get_arami_lesson1_audio_path,
)


class AramiCourseRuntimeTests(unittest.TestCase):
    def fixture(self, root):
        course_dir = root / "course_data"
        course_dir.mkdir()
        manifest = {
            "course_id": COURSE_ID,
            "safety": {"separate_from_latin_courses": True},
            "lessons": [
                {"id": LESSON_1_ID, "content_status": "do_not_edit",
                 "audio_asset": "دەنگەکانی ئەلفبێ.ogg",
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

    def test_resolves_only_confirmed_lesson1_audio(self):
        with tempfile.TemporaryDirectory() as temp:
            self.fixture(Path(temp))
            path = get_arami_lesson1_audio_path(temp)
            self.assertEqual(path.name, "دەنگەکانی ئەلفبێ.ogg")

    def test_rejects_wrong_audio_assignment(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = self.fixture(Path(temp))
            manifest["lessons"][0]["audio_asset"] = "voices/lesson_start.mp3"
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


if __name__ == "__main__":
    unittest.main()

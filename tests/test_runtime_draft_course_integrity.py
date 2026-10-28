"""Runtime integrity checks for the isolated multi-course candidate.

These tests intentionally verify that draft material is loaded for integration
checks without making it available to learners.
"""
import json
import unittest
from pathlib import Path
from unittest.mock import patch

import bot


class RuntimeDraftCourseIntegrityTests(unittest.TestCase):
    @staticmethod
    def _load_course_data(filename):
        path = Path(__file__).resolve().parents[1] / "course_data" / filename
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)["lessons"]

    def test_daily_conversation_drafts_have_complete_practice_structure(self):
        filenames = (
            "daily_conversation_lessons_01_06.json",
            "daily_conversation_lessons_07_30.json",
            "daily_conversation_lessons_31_36.json",
            "daily_conversation_lessons_37_42.json",
            "daily_conversation_lessons_43_48.json",
        )
        lessons = [
            lesson
            for filename in filenames
            for lesson in self._load_course_data(filename)
        ]
        self.assertEqual([lesson["number"] for lesson in lessons], list(range(1, 49)))
        for lesson in lessons:
            with self.subTest(lesson=lesson["number"]):
                self.assertTrue(lesson["title"].strip())
                self.assertTrue(lesson["objective"].strip())
                self.assertGreaterEqual(len(lesson["dialogue"]), 2)
                self.assertGreaterEqual(len(lesson["vocabulary"]), 3)
                self.assertTrue(lesson["exercises"])
                self.assertTrue(lesson["comprehension"])
                self.assertTrue(lesson["role_play"].strip())
                self.assertTrue(lesson["quiz"])
                for question in lesson["quiz"]:
                    self.assertTrue(question["q"].strip())
                    self.assertGreaterEqual(len(question["options"]), 3)
                    self.assertTrue(all(option.strip() for option in question["options"]))
                    self.assertIsInstance(question["answer"], int)
                    self.assertGreaterEqual(question["answer"], 0)
                    self.assertLess(question["answer"], len(question["options"]))
                    self.assertTrue(question["explanation"].strip())

    def test_daily_conversation_quiz_prompts_are_not_exact_duplicates(self):
        filenames = (
            "daily_conversation_lessons_01_06.json",
            "daily_conversation_lessons_07_30.json",
            "daily_conversation_lessons_31_36.json",
            "daily_conversation_lessons_37_42.json",
            "daily_conversation_lessons_43_48.json",
        )
        seen = {}
        for filename in filenames:
            for lesson in self._load_course_data(filename):
                for question in lesson["quiz"]:
                    prompt = " ".join(
                        question["q"].casefold().strip().rstrip("؟?!،.").split()
                    )
                    with self.subTest(lesson=lesson["number"], prompt=prompt):
                        self.assertNotIn(
                            prompt,
                            seen,
                            msg=(
                                f"Repeated quiz prompt in lessons {seen.get(prompt)} "
                                f"and {lesson['number']}: {question['q']}"
                            ),
                        )
                        seen[prompt] = lesson["number"]

    def test_unified_orthography_drafts_have_complete_practice_structure(self):
        lessons = self._load_course_data("unified_orthography_lessons_01_12.json")
        self.assertEqual([lesson["number"] for lesson in lessons], list(range(1, 13)))
        for lesson in lessons:
            with self.subTest(lesson=lesson["number"]):
                for field in ("title", "objective", "role_play"):
                    self.assertTrue(lesson[field].strip())
                for field in ("key_points", "examples", "exercises", "comprehension"):
                    self.assertTrue(lesson[field])
                self.assertTrue(lesson["quiz"])
                for question in lesson["quiz"]:
                    self.assertTrue(question["q"].strip())
                    self.assertGreaterEqual(len(question["options"]), 3)
                    self.assertTrue(all(option.strip() for option in question["options"]))
                    self.assertIsInstance(question["answer"], int)
                    self.assertGreaterEqual(question["answer"], 0)
                    self.assertLess(question["answer"], len(question["options"]))
                    self.assertTrue(question["explanation"].strip())

    def test_all_82_manifest_lessons_are_loaded_without_id_collisions(self):
        expected = {
            "orthography_basic": [f"وانە_{n}" for n in range(1, 23)],
            "daily_conversation": [f"daily_conversation_{n:02d}" for n in range(1, 49)],
            "unified_orthography": [f"unified_orthography_{n:02d}" for n in range(1, 13)],
        }
        self.assertEqual(len(bot.LESSON_DATA), 82)
        for course_id, lesson_ids in expected.items():
            with self.subTest(course=course_id):
                self.assertEqual(bot.COURSE_LESSON_ORDER[course_id], lesson_ids)
                self.assertTrue(all(lesson_id in bot.LESSON_DATA for lesson_id in lesson_ids))
        self.assertEqual(len(bot.LESSON_DATA), len(set(bot.LESSON_DATA)))

    def test_original_lesson_content_does_not_repeat_course_or_decorative_headers(self):
        for lesson_id in bot.COURSE_LESSON_ORDER["orthography_basic"]:
            with self.subTest(lesson=lesson_id):
                content = bot.LESSON_DATA[lesson_id]["content"]
                self.assertNotIn("📚 کۆرسی ١:", content)
                self.assertNotIn("╭━━━━━━━━━━━━━━━━━━╮", content)
                self.assertNotIn("کەویار", content)
        lesson = bot.LESSON_DATA["وانە_1"]
        self.assertIn("ئەلفبێی زمانی کوردی", lesson["content"])
        self.assertIn("تەواوکردنی وانە", lesson["content"])

    def test_draft_course_lessons_and_quizzes_are_loaded_but_review_gated(self):
        for course_id in ("daily_conversation", "unified_orthography"):
            with self.subTest(course=course_id):
                self.assertFalse(bot.course_is_active(course_id))
                for lesson_id in bot.COURSE_LESSON_ORDER[course_id]:
                    self.assertFalse(bot.can_open(12345, lesson_id))
                    self.assertIn("draft_editorial_review", bot.LESSON_DATA[lesson_id]["review_status"])
                    self.assertTrue(bot.LESSON_DATA[lesson_id]["content"].strip())
                    questions = bot.QUIZ_DATA[lesson_id]
                    self.assertTrue(questions)
                    self.assertTrue(all(q.get("question") and q.get("explanation") for q in questions))

    def test_every_loaded_quiz_has_valid_questions_and_answer_options(self):
        for lesson_id, questions in bot.QUIZ_DATA.items():
            with self.subTest(lesson=lesson_id):
                self.assertIn(lesson_id, bot.LESSON_DATA)
                self.assertTrue(questions)
                for question_number, question in enumerate(questions, start=1):
                    with self.subTest(question=question_number):
                        self.assertTrue(question.get("question", "").strip())
                        options = question.get("options")
                        self.assertIsInstance(options, list)
                        self.assertGreaterEqual(len(options), 3)
                        self.assertTrue(all(isinstance(option, str) and option.strip() for option in options))
                        self.assertIn(question.get("answer"), options)
                        self.assertTrue(question.get("explanation", "").strip())

    def test_all_48_conversation_lessons_stay_locked_even_with_fake_completion(self):
        # A stale database row or a crafted callback must not bypass the
        # course-level activation gate, even if every draft lesson appears done.
        all_draft_ids = bot.COURSE_LESSON_ORDER["daily_conversation"]
        self.assertEqual(len(all_draft_ids), 48)
        with patch.object(bot, "get_completed_lessons", return_value=all_draft_ids):
            for lesson_id in all_draft_ids:
                with self.subTest(lesson=lesson_id):
                    self.assertFalse(bot.can_open(12345, lesson_id))

    def test_progress_and_quiz_catalog_lessons_are_scoped_to_active_courses(self):
        active_lessons = bot.active_course_lessons()
        self.assertEqual(active_lessons, bot.COURSE_LESSON_ORDER["orthography_basic"])
        self.assertTrue(all(lesson.startswith("وانە_") for lesson in active_lessons))
        for course_id in ("daily_conversation", "unified_orthography"):
            self.assertTrue(
                set(bot.COURSE_LESSON_ORDER[course_id]).isdisjoint(active_lessons)
            )

    def test_active_course_lessons_include_namespaced_lessons_when_course_activates(self):
        with patch.object(
            bot, "course_is_active",
            side_effect=lambda course_id: course_id == "daily_conversation",
        ):
            active_lessons = bot.active_course_lessons()
        self.assertEqual(active_lessons, bot.COURSE_LESSON_ORDER["daily_conversation"])
        self.assertEqual(len(active_lessons), 48)
        self.assertTrue(all(lesson.startswith("daily_conversation_") for lesson in active_lessons))

    def test_draft_course_completions_never_grant_legacy_badges(self):
        draft_ids = (
            bot.COURSE_LESSON_ORDER["daily_conversation"]
            + bot.COURSE_LESSON_ORDER["unified_orthography"]
        )
        with patch.object(bot, "get_completed_lessons", return_value=draft_ids), \
             patch.object(bot, "add_badge") as add_badge:
            bot.check_badges(12345)
        add_badge.assert_not_called()

    def test_next_lesson_never_crosses_course_boundaries(self):
        for course_id in ("daily_conversation", "unified_orthography"):
            lesson_ids = bot.COURSE_LESSON_ORDER[course_id]
            with self.subTest(course=course_id):
                for current, following in zip(lesson_ids, lesson_ids[1:]):
                    self.assertEqual(bot.next_course_lesson(current), following)
                self.assertIsNone(bot.next_course_lesson(lesson_ids[-1]))

    def test_badges_use_course_local_numbers_and_skip_inactive_courses(self):
        recorded = []
        course_title = next(
            course["title"] for course in bot.COURSES
            if course["id"] == "daily_conversation"
        )
        with (
            patch.object(
                bot, "get_completed_lessons",
                return_value=["وانە_1", "daily_conversation_02", "unified_orthography_01"],
            ),
            patch.object(
                bot, "course_is_active",
                side_effect=lambda course_id: course_id in {"orthography_basic", "daily_conversation"},
            ),
            patch.object(bot, "add_badge", side_effect=lambda user_id, badge: recorded.append(badge)),
        ):
            bot.check_badges(12345)
        self.assertIn("🏅 کۆرسی ڕێنووسی — وانەی 1", recorded)
        self.assertIn(f"🏅 {course_title} — وانەی 2", recorded)
        self.assertEqual(len(recorded), 2)
        self.assertFalse(any("unified_orthography" in badge for badge in recorded))

    def test_course_one_progression_does_not_spill_into_course_two(self):
        legacy_ids = bot.COURSE_LESSON_ORDER["orthography_basic"]
        conversation_ids = bot.COURSE_LESSON_ORDER["daily_conversation"]
        self.assertEqual(legacy_ids, [f"وانە_{n}" for n in range(1, 23)])
        self.assertEqual(bot.next_course_lesson(legacy_ids[-1]), None)
        self.assertNotIn(legacy_ids[-1], conversation_ids)
        self.assertEqual(conversation_ids[0], "daily_conversation_01")

    def test_every_loaded_lesson_belongs_to_exactly_one_manifest_course(self):
        manifest_ids = [
            lesson_id
            for course in bot.COURSES
            for lesson_id in course.get("lesson_ids", [])
        ]
        self.assertEqual(len(manifest_ids), len(set(manifest_ids)))
        self.assertEqual(set(manifest_ids), set(bot.LESSON_DATA))
        self.assertEqual(set(bot.LESSON_COURSE), set(bot.LESSON_DATA))
        for course in bot.COURSES:
            expected = [lesson for lesson in course.get("lesson_ids", []) if lesson in bot.LESSON_DATA]
            self.assertEqual(bot.COURSE_LESSON_ORDER[course["id"]], expected)
            for lesson_id in expected:
                self.assertEqual(bot.LESSON_COURSE[lesson_id], course["id"])

    def test_course_four_remains_planned_and_empty(self):
        course = next(course for course in bot.COURSES if course["id"] == "grammar")
        self.assertEqual(course["status"], "planned")
        self.assertEqual(bot.COURSE_LESSON_ORDER["grammar"], [])


    @staticmethod
    def _normalized_text(value):
        import re
        return re.sub(r"\\s+", " ", value.casefold().strip().rstrip("؟?!،,.؛:")).strip()

    def test_draft_lessons_have_no_exact_duplicate_vocabulary_dialogue_or_quiz_options(self):
        filenames = (
            "daily_conversation_lessons_01_06.json",
            "daily_conversation_lessons_07_30.json",
            "daily_conversation_lessons_31_36.json",
            "daily_conversation_lessons_37_42.json",
            "daily_conversation_lessons_43_48.json",
            "unified_orthography_lessons_01_12.json",
        )
        for filename in filenames:
            for lesson in self._load_course_data(filename):
                with self.subTest(file=filename, lesson=lesson["number"]):
                    vocabulary = lesson.get("vocabulary", [])
                    terms = [
                        item[0] if isinstance(item, list) else item
                        for item in vocabulary
                        if (item[0] if isinstance(item, list) else item)
                    ]
                    normalized_terms = [self._normalized_text(term) for term in terms]
                    self.assertEqual(
                        len(normalized_terms), len(set(normalized_terms)),
                        msg=f"Duplicate vocabulary term in {filename}, lesson {lesson['number']}",
                    )

                    dialogue = lesson.get("dialogue", [])
                    dialogue_lines = [
                        item[1] if isinstance(item, list) and len(item) > 1 else item
                        for item in dialogue
                    ]
                    normalized_lines = [
                        self._normalized_text(line)
                        for line in dialogue_lines
                        if isinstance(line, str) and line.strip()
                    ]
                    self.assertEqual(
                        len(normalized_lines), len(set(normalized_lines)),
                        msg=f"Duplicate dialogue line in {filename}, lesson {lesson['number']}",
                    )

                    for question in lesson.get("quiz", []):
                        normalized_options = [
                            self._normalized_text(option)
                            for option in question.get("options", [])
                        ]
                        self.assertEqual(
                            len(normalized_options), len(set(normalized_options)),
                            msg=(
                                f"Duplicate quiz options in {filename}, lesson "
                                f"{lesson['number']}: {question.get('q')}"
                            ),
                        )


    def test_source_quiz_answers_map_to_the_exact_runtime_correct_options(self):
        course_files = (
            ("daily_conversation", (
                "daily_conversation_lessons_01_06.json",
                "daily_conversation_lessons_07_30.json",
                "daily_conversation_lessons_31_36.json",
                "daily_conversation_lessons_37_42.json",
                "daily_conversation_lessons_43_48.json",
            )),
            ("unified_orthography", ("unified_orthography_lessons_01_12.json",)),
        )
        for course_id, filenames in course_files:
            for filename in filenames:
                for lesson in self._load_course_data(filename):
                    lesson_id = f"{course_id}_{lesson['number']:02d}"
                    runtime_questions = bot.QUIZ_DATA[lesson_id]
                    source_questions = lesson["quiz"]
                    with self.subTest(lesson=lesson_id):
                        self.assertEqual(len(runtime_questions), len(source_questions))
                        for source, runtime in zip(source_questions, runtime_questions):
                            with self.subTest(question=source["q"]):
                                self.assertEqual(runtime["question"], source["q"])
                                self.assertEqual(runtime["options"], source["options"])
                                self.assertEqual(
                                    runtime["answer"], source["options"][source["answer"]]
                                )
                                self.assertEqual(runtime["explanation"], source["explanation"])


    def test_daily_conversation_role_plays_are_not_generic_duplicates(self):
        filenames = (
            "daily_conversation_lessons_01_06.json",
            "daily_conversation_lessons_07_30.json",
            "daily_conversation_lessons_31_36.json",
            "daily_conversation_lessons_37_42.json",
            "daily_conversation_lessons_43_48.json",
        )
        seen = {}
        for filename in filenames:
            for lesson in self._load_course_data(filename):
                prompt = self._normalized_text(lesson.get("role_play", ""))
                with self.subTest(lesson=lesson["number"], title=lesson["title"]):
                    self.assertTrue(prompt)
                    self.assertNotIn(
                        prompt,
                        seen,
                        msg=(
                            f"Repeated role-play instruction in lessons "
                            f"{seen.get(prompt)} and {lesson['number']}"
                        ),
                    )
                    seen[prompt] = lesson["number"]


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DailyConversationContentTests(unittest.TestCase):
    def test_lesson_38_uses_toman_consistently_in_its_price_dialogue(self):
        path = ROOT / "course_data" / "daily_conversation_lessons_37_42.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        lesson = next(item for item in payload["lessons"] if item["number"] == 38)
        dialogue_text = " ".join(line for turn in lesson["dialogue"] for line in turn)
        self.assertIn("پەنجا هەزار تمەنە", dialogue_text)
        self.assertNotIn("دینار", dialogue_text)


if __name__ == "__main__":
    unittest.main()

    def test_requested_dialogue_wording_updates(self):
        expected = {
            1: ("course_data/daily_conversation_lessons_01_06.json", "کات باش کەژیار خاتوو!"),
            2: ("course_data/daily_conversation_lessons_01_06.json", "منیش دانیشتوی ئەم شارەم."),
            4: ("course_data/daily_conversation_lessons_01_06.json", "بەڵێ، ئەمانە دایک و باوکمن و ئەمەش خوشکە بچوکەکەمە."),
            5: ("course_data/daily_conversation_lessons_01_06.json", "پێشتر پەیوەندیم پێوە بگرە تا لە ماڵەوە بم."),
            8: ("course_data/daily_conversation_lessons_07_30.json", "دەمهەوێت میوە و سەبزی بکڕم."),
            13: ("course_data/daily_conversation_lessons_07_30.json", "سەرم دەهێشێت"),
            23: ("course_data/daily_conversation_lessons_07_30.json", "حەزم لە خوێندن و بیرکردنەوەیە. تۆ چی؟"),
            24: ("course_data/daily_conversation_lessons_07_30.json", "جارێک بیگوژێنەوە."),
            27: ("course_data/daily_conversation_lessons_07_30.json", "دایکیشم ماڵدارە و لە ماڵەوەیە."),
            37: ("course_data/daily_conversation_lessons_37_42.json", "بەڵێ، فەرموو. ئەمڕۆ خواردنی ڕۆژمان هەیە."),
            38: ("course_data/daily_conversation_lessons_37_42.json", "سڵاو، ئەم مانتۆیە چەندە؟"),
        }
        for lesson_number, (relative_path, expected_line) in expected.items():
            payload = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
            lesson = next(item for item in payload["lessons"] if item["number"] == lesson_number)
            dialogue_text = " ".join(line for turn in lesson["dialogue"] for line in turn)
            with self.subTest(lesson=lesson_number):
                self.assertIn(expected_line, dialogue_text)

    def test_dialogue_uses_requested_terms_and_speakers(self):
        paths = [
            ROOT / "course_data" / "daily_conversation_lessons_01_06.json",
            ROOT / "course_data" / "daily_conversation_lessons_07_30.json",
            ROOT / "course_data" / "daily_conversation_lessons_37_42.json",
        ]
        payloads = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
        all_dialogue = [
            (lesson["number"], speaker, line)
            for payload in payloads
            for lesson in payload["lessons"]
            for speaker, line in lesson["dialogue"]
        ]
        text = " ".join(f"{speaker} {line}" for _, speaker, line in all_dialogue)
        self.assertNotIn("سوپاس", text)
        self.assertNotIn("بە تەنها", text)
        self.assertIn("بە تەنیا دێم", text)
        self.assertIn(("چێشلێنەر", "بەڵێ، فەرموون. چی دەتەوێت؟"), [(s, line) for _, s, line in all_dialogue])
        self.assertIn(("چێشلێنەر", "بەڵێ، فەرموو. ئەمڕۆ خواردنی ڕۆژمان هەیە."), [(s, line) for _, s, line in all_dialogue])
        self.assertIn(("فەرمانبەر", "لە ڕەفی سێیەم، لای چەپ."), [(s, line) for _, s, line in all_dialogue])

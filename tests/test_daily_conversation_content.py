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

"""Adapter for the separate 22-lesson orthography quiz draft.

This module is deliberately not imported by bot.py yet. It defines a conversion
boundary before runtime integration; quiz.json remains the only runtime quiz source.
"""
from __future__ import annotations

from typing import Any


def convert_quiz_draft(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    """Convert indexed answers to the legacy question shape, without wiring runtime."""
    if not isinstance(data, dict):
        raise ValueError("Quiz draft must be an object")
    if data.get("course_id") != "orthography_foundations":
        raise ValueError("Unexpected course_id")
    quizzes = data.get("quizzes")
    if not isinstance(quizzes, list) or len(quizzes) != 22:
        raise ValueError("Expected exactly 22 lesson quiz groups")

    converted: dict[str, list[dict[str, Any]]] = {}
    seen_lessons: set[int] = set()
    for group in quizzes:
        if not isinstance(group, dict):
            raise ValueError("Each quiz group must be an object")
        number = group.get("lesson_number")
        if not isinstance(number, int) or isinstance(number, bool) or not 1 <= number <= 22:
            raise ValueError("Invalid lesson_number")
        if number in seen_lessons:
            raise ValueError(f"Duplicate lesson_number: {number}")
        expected_lesson_id = f"lesson_{number:02d}"
        if group.get("lesson_id") != expected_lesson_id:
            raise ValueError(f"lesson_id must match lesson_number: {expected_lesson_id}")
        seen_lessons.add(number)
        questions = group.get("questions")
        if not isinstance(questions, list) or not questions:
            raise ValueError(f"Lesson {number} has no questions")
        output_questions = []
        for question in questions:
            if not isinstance(question, dict):
                raise ValueError(f"Lesson {number} question must be an object")
            options = question.get("options")
            index = question.get("correct_option_index")
            if not isinstance(options, list) or len(options) < 2:
                raise ValueError(f"Lesson {number} has invalid options")
            if any(not isinstance(option, str) or not option.strip() for option in options):
                raise ValueError(f"Lesson {number} has empty/non-text option")
            if len(set(options)) != len(options):
                raise ValueError(f"Lesson {number} has duplicate options")
            if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < len(options):
                raise ValueError(f"Lesson {number} has invalid correct_option_index")
            if not isinstance(question.get("question"), str) or not question["question"].strip():
                raise ValueError(f"Lesson {number} has empty question")
            if not isinstance(question.get("explanation"), str) or not question["explanation"].strip():
                raise ValueError(f"Lesson {number} has empty explanation")
            output_questions.append({"question": question["question"], "options": options[:], "answer": options[index], "explanation": question["explanation"]})
        converted[f"lesson_{number:02d}"] = output_questions
    if seen_lessons != set(range(1, 23)):
        raise ValueError("Lesson numbers must cover 1 through 22 exactly")
    return converted

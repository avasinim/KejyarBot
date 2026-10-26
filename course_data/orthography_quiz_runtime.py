"""Isolated session helpers for the draft 22-lesson orthography course.

This module deliberately does not touch the legacy quiz state, database rewards,
or bot handlers. Runtime wiring must wait for course-specific progress/reward
storage and integration tests.
"""

COURSE_ID = "orthography_foundations"
SESSION_KEY = "orthography_foundations_quiz"


def build_quiz_session(converted_quizzes, lesson_number):
    """Build a validated session using the adapter's lesson_01..lesson_22 keys."""
    if not isinstance(lesson_number, int) or isinstance(lesson_number, bool):
        raise ValueError("lesson_number must be an integer")
    if not 1 <= lesson_number <= 22:
        raise ValueError("lesson_number must be between 1 and 22")
    if not isinstance(converted_quizzes, dict):
        raise ValueError("converted_quizzes must be a mapping")

    lesson_id = f"lesson_{lesson_number:02d}"
    questions = converted_quizzes.get(lesson_id)
    if not isinstance(questions, list) or not questions:
        raise ValueError(f"missing questions for {lesson_id}")

    for question in questions:
        if not isinstance(question, dict):
            raise ValueError("each question must be a mapping")
        if not isinstance(question.get("question"), str) or not question["question"].strip():
            raise ValueError("question text is required")
        options = question.get("options")
        if not isinstance(options, list) or len(options) < 2:
            raise ValueError("at least two options are required")
        if any(not isinstance(option, str) or not option.strip() for option in options):
            raise ValueError("options must be non-empty strings")
        if question.get("answer") not in options:
            raise ValueError("answer must match one of the options")

    # Return fresh session-owned containers so answer progression cannot mutate
    # the validated source quiz data or the legacy quiz session.
    return {
        "course_id": COURSE_ID,
        "lesson_id": lesson_id,
        "index": 0,
        "questions": [dict(q, options=list(q["options"])) for q in questions],
        "score": 0,
        "question_message_id": None,
    }


def make_answer_callback(option_index):
    """Return a callback string reserved for this course's own answer handler."""
    if not isinstance(option_index, int) or isinstance(option_index, bool) or option_index < 0:
        raise ValueError("option_index must be a non-negative integer")
    return f"orthography_quiz_answer_{option_index}"


def parse_answer_callback(callback_data):
    """Parse only this course's namespaced answer callbacks; return None otherwise."""
    prefix = "orthography_quiz_answer_"
    if not isinstance(callback_data, str) or not callback_data.startswith(prefix):
        return None
    suffix = callback_data[len(prefix):]
    if not suffix.isdigit():
        return None
    return int(suffix)


def apply_answer(session, option_index):
    """Score one answer and advance this session; never awards persistent rewards.

    Returns a result dictionary. Duplicate answers after completion are rejected.
    """
    if not isinstance(session, dict) or session.get("course_id") != COURSE_ID:
        raise ValueError("not an orthography course quiz session")
    if not isinstance(option_index, int) or isinstance(option_index, bool) or option_index < 0:
        raise ValueError("option_index must be a non-negative integer")
    questions = session.get("questions")
    index = session.get("index")
    if not isinstance(questions, list) or not isinstance(index, int) or isinstance(index, bool):
        raise ValueError("invalid quiz session")
    if index >= len(questions):
        raise ValueError("quiz session is already complete")
    question = questions[index]
    options = question["options"]
    if option_index >= len(options):
        raise ValueError("option_index is out of range")

    selected = options[option_index]
    correct = selected == question["answer"]
    if correct:
        session["score"] = session.get("score", 0) + 1
    session["index"] = index + 1
    return {
        "correct": correct,
        "selected": selected,
        "answer": question["answer"],
        "explanation": question["explanation"],
        "completed": session["index"] >= len(questions),
        "score": session["score"],
        "question_number": index + 1,
    }


def make_start_callback(lesson_number):
    """Build a short, course-specific Telegram callback for a lesson."""
    if not isinstance(lesson_number, int) or isinstance(lesson_number, bool):
        raise ValueError("lesson_number must be an integer")
    if not 1 <= lesson_number <= 22:
        raise ValueError("lesson_number must be between 1 and 22")
    return f"ofquiz_start_{lesson_number:02d}"


def parse_start_callback(callback_data):
    """Return a lesson number only for a valid callback in this course namespace."""
    prefix = "ofquiz_start_"
    if not isinstance(callback_data, str) or not callback_data.startswith(prefix):
        return None
    suffix = callback_data[len(prefix):]
    if len(suffix) != 2 or not suffix.isdigit():
        return None
    number = int(suffix)
    return number if 1 <= number <= 22 else None

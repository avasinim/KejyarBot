"""Pure presentation view-models for Arami Course 1, Lesson 1.

No lesson text is authored here. The module only turns the approved interaction
bank and the session engine's current state into safe, Telegram-neutral views.
"""
from arami_lesson1_interaction import current_question, session_result


COURSE_CALLBACK_PREFIX = "arami1:"


def lesson_action_payload(action):
    """Build namespaced callback data; never reuse generic or Latin callbacks."""
    if action not in {"practice", "assessment", "back", "resume"}:
        raise ValueError("unsupported Arami Lesson 1 action")
    return f"{COURSE_CALLBACK_PREFIX}{action}"


def question_view(session):
    """Return one question at a time without leaking the answer before submit."""
    question = current_question(session)
    if question is None:
        return None
    return {
        "question_id": question["id"],
        "section_id": question["section_id"],
        "prompt": question["prompt"],
        "options": list(question["options"]),
        "selected_index": session.get("selected_index"),
        "submitted": False,
        "mode": session["mode"],
    }


def answer_feedback(question, answer_record):
    """Reveal correctness only after the interaction engine records submission."""
    if not isinstance(answer_record, dict):
        raise ValueError("a submitted answer record is required")
    if answer_record.get("question_id") != question.get("id"):
        raise ValueError("answer record does not match the displayed question")
    if not isinstance(answer_record.get("correct"), bool):
        raise ValueError("answer record has no valid correctness result")
    return {
        "question_id": question["id"],
        "section_id": question["section_id"],
        "correct": answer_record["correct"],
        "selected_index": answer_record.get("selected_index"),
        "correct_index": question["answer_index"],
    }


def result_view(session):
    """Build a compact final score and exact missed-section references."""
    result = session_result(session)
    return {
        "mode": result["mode"],
        "score": f'{result["correct"]}/{result["total"]}',
        "percentage": result["percentage"],
        "correct": result["correct"],
        "incorrect": result["incorrect"],
        "missed": list(result["missed"]),
        "can_retry_missed": bool(result["missed"]),
    }

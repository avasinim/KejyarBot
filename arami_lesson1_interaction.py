"""Isolated, content-agnostic interaction engine for Arami Course 1 Lesson 1.

The engine never authors or edits lesson text. Question records are supplied by
the lesson's approved data file; this module only validates and tracks attempts.
"""
from copy import deepcopy

from quiz_option_order import randomized_question_copy

ALLOWED_MODES = {"practice", "assessment"}
ALLOWED_TYPES = {"recognize", "classify", "match", "complete"}


class InvalidQuestionBank(ValueError):
    """Raised when an interaction bank is malformed or ambiguous."""


def validate_question_bank(question_bank):
    if not isinstance(question_bank, list) or not question_bank:
        raise InvalidQuestionBank("question bank must be a non-empty list")

    seen_ids = set()
    for position, item in enumerate(question_bank):
        if not isinstance(item, dict):
            raise InvalidQuestionBank(f"question {position} must be an object")
        question_id = item.get("id")
        kind = item.get("type")
        prompt = item.get("prompt")
        options = item.get("options")
        answer_index = item.get("answer_index")
        section_id = item.get("section_id")

        if not isinstance(question_id, str) or not question_id.strip():
            raise InvalidQuestionBank(f"question {position} has no stable id")
        if question_id in seen_ids:
            raise InvalidQuestionBank(f"duplicate question id: {question_id}")
        seen_ids.add(question_id)

        if kind not in ALLOWED_TYPES:
            raise InvalidQuestionBank(f"unsupported question type: {kind}")
        if not isinstance(prompt, str) or not prompt.strip():
            raise InvalidQuestionBank(f"question {question_id} has no prompt")
        if not isinstance(section_id, str) or not section_id.strip():
            raise InvalidQuestionBank(f"question {question_id} has no lesson section link")
        if not isinstance(options, list) or len(options) < 2:
            raise InvalidQuestionBank(f"question {question_id} needs at least two options")
        if any(not isinstance(option, str) or not option.strip() for option in options):
            raise InvalidQuestionBank(f"question {question_id} has an empty option")
        if len(options) != len(set(options)):
            raise InvalidQuestionBank(f"question {question_id} has duplicate options")
        if (
            not isinstance(answer_index, int)
            or isinstance(answer_index, bool)
            or answer_index < 0
            or answer_index >= len(options)
        ):
            raise InvalidQuestionBank(f"question {question_id} has an invalid answer index")
    return True


def create_session(question_bank, mode):
    """Create a fresh, isolated attempt; source records remain unchanged."""
    if mode not in ALLOWED_MODES:
        raise ValueError("mode must be practice or assessment")
    validate_question_bank(question_bank)
    return {
        "mode": mode,
        "questions": randomized_question_copy(question_bank),
        "index": 0,
        "selected_index": None,
        "answers": [],
        "closed": False,
    }


def current_question(session):
    _validate_session(session)
    if session["closed"] or session["index"] >= len(session["questions"]):
        return None
    return deepcopy(session["questions"][session["index"]])


def select_answer(session, option_index):
    """Selection is not submission and never changes score."""
    question = current_question(session)
    if question is None:
        raise ValueError("there is no active question")
    options = question["options"]
    if (
        not isinstance(option_index, int)
        or isinstance(option_index, bool)
        or option_index < 0
        or option_index >= len(options)
    ):
        raise ValueError("selected option is out of range")
    session["selected_index"] = option_index
    return option_index


def submit_answer(session):
    """Claim the current item exactly once and return correctness feedback."""
    question = current_question(session)
    if question is None:
        raise ValueError("there is no active question")
    selected = session.get("selected_index")
    if (
        not isinstance(selected, int)
        or isinstance(selected, bool)
        or selected < 0
        or selected >= len(question["options"])
    ):
        raise ValueError("select an answer before submitting")

    record = {
        "question_id": question["id"],
        "section_id": question["section_id"],
        "selected_index": selected,
        "correct": selected == question["answer_index"],
    }
    session["answers"].append(record)
    session["selected_index"] = None
    session["index"] += 1
    if session["index"] >= len(session["questions"]):
        session["closed"] = True
    return deepcopy(record)


def session_result(session):
    _validate_session(session)
    if not session["closed"]:
        raise ValueError("the session is not complete")
    total = len(session["questions"])
    correct = sum(1 for answer in session["answers"] if answer["correct"])
    return {
        "mode": session["mode"],
        "total": total,
        "correct": correct,
        "incorrect": total - correct,
        "percentage": round((correct / total) * 100),
        "missed": [
            {
                "question_id": answer["question_id"],
                "section_id": answer["section_id"],
            }
            for answer in session["answers"]
            if not answer["correct"]
        ],
    }


def retry_missed(session):
    """Return a new practice attempt containing only missed source questions."""
    result = session_result(session)
    missed_ids = {item["question_id"] for item in result["missed"]}
    missed_questions = [
        question for question in session["questions"]
        if question["id"] in missed_ids
    ]
    if not missed_questions:
        return None
    return create_session(missed_questions, "practice")


def _validate_session(session):
    if not isinstance(session, dict):
        raise ValueError("invalid session")
    if session.get("mode") not in ALLOWED_MODES:
        raise ValueError("invalid session mode")
    if not isinstance(session.get("questions"), list) or not session["questions"]:
        raise ValueError("invalid session question list")
    if not isinstance(session.get("answers"), list):
        raise ValueError("invalid session answers")
    index = session.get("index")
    if not isinstance(index, int) or isinstance(index, bool):
        raise ValueError("invalid session index")
    if index < 0 or index > len(session["questions"]):
        raise ValueError("session index out of range")
    if not isinstance(session.get("closed"), bool):
        raise ValueError("invalid session completion state")



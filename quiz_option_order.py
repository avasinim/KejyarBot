"""Per-attempt option ordering without changing source question records."""
from copy import deepcopy
import random


def randomized_question_copy(questions, rng=None):
    """Copy questions and shuffle options while preserving each correct answer.

    Source banks are never mutated. Both answer-text quiz records and
    answer-index interaction records are supported.
    """
    if not isinstance(questions, list):
        raise ValueError("questions must be a list")
    shuffle = rng.shuffle if rng is not None else random.shuffle
    copied = deepcopy(questions)

    for position, question in enumerate(copied):
        if not isinstance(question, dict):
            raise ValueError(f"question {position} must be an object")
        options = question.get("options")
        if not isinstance(options, list) or len(options) < 2:
            raise ValueError(f"question {position} needs at least two options")
        if any(not isinstance(option, str) or not option.strip() for option in options):
            raise ValueError(f"question {position} has an empty or invalid option")
        normalized_options = [option.strip().casefold() for option in options]
        if len(normalized_options) != len(set(normalized_options)):
            raise ValueError(f"question {position} has duplicate options")

        if "answer_index" in question:
            correct_index = question["answer_index"]
            if (
                not isinstance(correct_index, int)
                or isinstance(correct_index, bool)
                or not 0 <= correct_index < len(options)
            ):
                raise ValueError(f"question {position} has an invalid answer index")
            correct_answer = options[correct_index]
            shuffle(options)
            question["answer_index"] = options.index(correct_answer)
        elif isinstance(question.get("answer"), int) and not isinstance(question.get("answer"), bool):
            correct_index = question["answer"]
            if not 0 <= correct_index < len(options):
                raise ValueError(f"question {position} has an invalid answer index")
            correct_answer = options[correct_index]
            shuffle(options)
            question["answer"] = correct_answer
        else:
            correct_answer = question.get("answer")
            if (
                not isinstance(correct_answer, str)
                or sum(option == correct_answer for option in options) != 1
            ):
                raise ValueError(
                    f"question {position} must contain its correct answer exactly once"
                )
            shuffle(options)
            question["answer"] = correct_answer

    return copied

"""SQLite persistence isolated from the legacy lesson/quiz progress columns.

No XP or rewards are granted here. The draft course must not affect legacy
course progress; runtime integration can use this ledger after approval.
"""
import sqlite3
import re

COURSE_ID = "orthography_foundations"
LESSON_ID_PATTERN = re.compile(r"^lesson_(0[1-9]|1[0-9]|2[0-2])$")


def _validate_user_id(user_id):
    if not isinstance(user_id, int) or isinstance(user_id, bool):
        raise ValueError("user_id must be an integer")


def _validate_course_id(course_id):
    if not isinstance(course_id, str) or not course_id.strip():
        raise ValueError("course_id is required")


def _validate_lesson_id(lesson_id):
    if not isinstance(lesson_id, str) or not LESSON_ID_PATTERN.fullmatch(lesson_id):
        raise ValueError("lesson_id must be lesson_01 through lesson_22")


def init_course_progress(db_path):
    """Create the course-specific ledger without altering legacy tables."""
    conn = sqlite3.connect(str(db_path), timeout=10)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS course_quiz_completions (
                user_id INTEGER NOT NULL,
                course_id TEXT NOT NULL,
                lesson_id TEXT NOT NULL,
                completed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, course_id, lesson_id)
            )
            """
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def record_course_quiz_completion(db_path, user_id, lesson_id, course_id=COURSE_ID):
    """Record completion once; return True only for a new completion."""
    _validate_user_id(user_id)
    _validate_course_id(course_id)
    _validate_lesson_id(lesson_id)

    init_course_progress(db_path)
    conn = sqlite3.connect(str(db_path), timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        cur = conn.execute(
            """
            INSERT OR IGNORE INTO course_quiz_completions(user_id, course_id, lesson_id)
            VALUES (?, ?, ?)
            """,
            (user_id, course_id, lesson_id),
        )
        created = cur.rowcount == 1
        conn.commit()
        return created
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_course_completed_lessons(db_path, user_id, course_id=COURSE_ID):
    """Return this course's completed lesson IDs, never legacy course IDs."""
    _validate_user_id(user_id)
    _validate_course_id(course_id)
    init_course_progress(db_path)
    conn = sqlite3.connect(str(db_path), timeout=10)
    try:
        rows = conn.execute(
            """
            SELECT lesson_id FROM course_quiz_completions
            WHERE user_id=? AND course_id=? ORDER BY lesson_id
            """,
            (user_id, course_id),
        ).fetchall()
        return [row[0] for row in rows]
    finally:
        conn.close()

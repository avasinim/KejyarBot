import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = str(BASE_DIR / "kejyar.db")


def init_db():
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            score INTEGER DEFAULT 0,
            xp INTEGER DEFAULT 0,
            level TEXT DEFAULT 'A1.1 🌱',
            correct_answers INTEGER DEFAULT 0,
            completed_lessons TEXT DEFAULT '',
            badges TEXT DEFAULT '',
            tests INTEGER DEFAULT 0,
            coins INTEGER DEFAULT 0,
            chests INTEGER DEFAULT 0
        )
        """)
        # Add the quiz-completion ledger to existing databases without destroying data.
        cur.execute("PRAGMA table_info(users)")
        columns = {row[1] for row in cur.fetchall()}
        if "completed_quizzes" not in columns:
            cur.execute("ALTER TABLE users ADD COLUMN completed_quizzes TEXT DEFAULT ''")
        cur.execute("""
        CREATE TABLE IF NOT EXISTS speech_quota (
            user_id INTEGER NOT NULL,
            quota_date TEXT NOT NULL,
            used INTEGER NOT NULL DEFAULT 0 CHECK (used >= 0),
            PRIMARY KEY (user_id, quota_date)
        )
        """)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def reserve_speech_quota(user_id, quota_date, limit=20):
    """Atomically reserve one speech generation for this user and UTC date."""
    if limit < 1:
        return False
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute(
            "INSERT OR IGNORE INTO speech_quota(user_id, quota_date, used) VALUES (?, ?, 0)",
            (user_id, quota_date),
        )
        cur = conn.execute(
            "UPDATE speech_quota SET used=used+1 "
            "WHERE user_id=? AND quota_date=? AND used < ?",
            (user_id, quota_date, limit),
        )
        reserved = cur.rowcount == 1
        conn.commit()
        return reserved
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def refund_speech_quota(user_id, quota_date):
    """Refund a reserved slot after generation or delivery fails."""
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute(
            "UPDATE speech_quota SET used=used-1 "
            "WHERE user_id=? AND quota_date=? AND used > 0",
            (user_id, quota_date),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_speech_quota_used(user_id, quota_date):
    """Return the durable number of reserved speech slots for a user and date."""
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        row = conn.execute(
            "SELECT used FROM speech_quota WHERE user_id=? AND quota_date=?",
            (user_id, quota_date),
        ).fetchone()
        return row[0] if row else 0
    finally:
        conn.close()


def get_user(user_id):
    # Explicitly close SQLite connections; the connection context manager
    # commits or rolls back but does not close the connection.
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO users(user_id) VALUES(?)", (user_id,))
        cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        row = cur.fetchone()
        conn.commit()
        return row
    finally:
        conn.close()


def calculate_level(xp):
    if xp<50:return 'A1.1 🌱'
    if xp<100:return 'A1.2 🌿'
    if xp<150:return 'A2.1 📘'
    if xp<300:return 'A2.2 📖'
    if xp<450:return 'B1.1 🚀'
    if xp<600:return 'B1.2 🔥'
    if xp<800:return 'B2.1 🏆'
    return 'B2.2 👑'


def update_level(user_id):
    user = get_user(user_id)
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute(
            "UPDATE users SET level=? WHERE user_id=?",
            (calculate_level(user[2]), user_id),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def add_score(user_id, points):
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute(
            "UPDATE users SET score=score+?, xp=xp+? WHERE user_id=?",
            (points, points, user_id),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    add_coins(user_id, 5)
    update_level(user_id)


def add_xp(user_id, amount):
    """Add XP/score without awarding the lesson-specific coin bonus."""
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute(
            "UPDATE users SET score=score+?, xp=xp+? WHERE user_id=?",
            (amount, amount, user_id),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    update_level(user_id)


def add_coins(user_id, amount):
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute(
            "UPDATE users SET coins=coins+? WHERE user_id=?",
            (amount, user_id),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def open_chest(user_id):
    """Consume one chest and award coins atomically; return 0 if none remain."""
    get_user(user_id)
    import random
    reward = random.choice([10, 20, 50, 100])
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        cur = conn.cursor()
        cur.execute(
            "UPDATE users SET chests=chests-1, coins=coins+? "
            "WHERE user_id=? AND chests>0",
            (reward, user_id),
        )
        if cur.rowcount != 1:
            conn.rollback()
            return 0
        conn.commit()
        return reward
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def add_chest(user_id):
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute(
            "UPDATE users SET chests=chests+1 WHERE user_id=?",
            (user_id,),
        )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_user_level(user_id):
    return get_user(user_id)[3]


def complete_lesson(user_id, lesson_id):
    """Record a lesson exactly once; return True only for the first completion."""
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        conn.execute(
            "INSERT OR IGNORE INTO users(user_id) VALUES(?)",
            (user_id,),
        )
        row = conn.execute(
            "SELECT completed_lessons FROM users WHERE user_id=?",
            (user_id,),
        ).fetchone()
        old = row[0] if row and row[0] else ""
        items = old.split(",") if old else []
        if lesson_id in items:
            conn.commit()
            return False
        items.append(lesson_id)
        cur = conn.execute(
            "UPDATE users SET completed_lessons=? WHERE user_id=?",
            (",".join(items), user_id),
        )
        if cur.rowcount != 1:
            raise RuntimeError("Lesson completion update did not affect exactly one user row")
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()



def complete_lesson_with_rewards(user_id, lesson_id, points=10, coins=5, chests=1):
    """Atomically record first completion and grant its score, coins, and chest."""
    get_user(user_id)
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        cur = conn.cursor()
        cur.execute(
            "SELECT completed_lessons, xp FROM users WHERE user_id=?",
            (user_id,),
        )
        row = cur.fetchone()
        old = row[0] if row and row[0] else ""
        items = old.split(",") if old else []
        if lesson_id in items:
            conn.commit()
            return False
        items.append(lesson_id)
        new_xp = (row[1] or 0) + points
        cur.execute(
            """UPDATE users
               SET completed_lessons=?, score=score+?, xp=?, coins=coins+?,
                   chests=chests+?, level=?
               WHERE user_id=?""",
            (",".join(items), points, new_xp, coins, chests,
             calculate_level(new_xp), user_id),
        )
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_completed_lessons(user_id):
    x=get_user(user_id)[5]
    return x.split(',') if x else []


def add_badge(user_id, badge):
    """Add a badge without losing another badge written concurrently."""
    get_user(user_id)
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        cur = conn.cursor()
        cur.execute("SELECT badges FROM users WHERE user_id=?", (user_id,))
        row = cur.fetchone()
        old = row[0] if row and row[0] else ""
        items = old.split(",") if old else []
        if badge not in items:
            items.append(badge)
            cur.execute(
                "UPDATE users SET badges=? WHERE user_id=?",
                (",".join(items), user_id),
            )
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_badges(user_id):
    x=get_user(user_id)[6]
    return x.split(',') if x else []


def complete_quiz(user_id, quiz_id):
    """Record a quiz atomically; return True only on its first completion."""
    get_user(user_id)
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        cur = conn.cursor()
        cur.execute("SELECT completed_quizzes FROM users WHERE user_id=?", (user_id,))
        row = cur.fetchone()
        old = row[0] if row and row[0] else ""
        items = old.split(",") if old else []
        if quiz_id in items:
            conn.commit()
            return False
        items.append(quiz_id)
        cur.execute(
            "UPDATE users SET completed_quizzes=?, tests=tests+1 WHERE user_id=?",
            (",".join(items), user_id),
        )
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def complete_quiz_with_rewards(user_id, quiz_id, points=20):
    """Atomically record a first quiz completion and grant its XP/score."""
    get_user(user_id)
    conn = sqlite3.connect(DB_NAME, timeout=10)
    try:
        conn.execute("BEGIN IMMEDIATE")
        cur = conn.cursor()
        cur.execute(
            "SELECT completed_quizzes, xp FROM users WHERE user_id=?",
            (user_id,),
        )
        row = cur.fetchone()
        old = row[0] if row and row[0] else ""
        items = old.split(",") if old else []
        if quiz_id in items:
            conn.commit()
            return False
        items.append(quiz_id)
        new_xp = (row[1] or 0) + points
        cur.execute(
            """UPDATE users
               SET completed_quizzes=?, tests=tests+1, score=score+?, xp=?, level=?
               WHERE user_id=?""",
            (",".join(items), points, new_xp, calculate_level(new_xp), user_id),
        )
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

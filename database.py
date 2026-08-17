import sqlite3

DB_NAME = "kejyar.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
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
    conn.commit()
    conn.close()


def get_user(user_id):
    conn=sqlite3.connect(DB_NAME)
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE user_id=?",(user_id,))
    user=cur.fetchone()
    if not user:
        cur.execute("INSERT INTO users(user_id) VALUES(?)",(user_id,))
        conn.commit()
        cur.execute("SELECT * FROM users WHERE user_id=?",(user_id,))
        user=cur.fetchone()
    conn.close()
    return user


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
    user=get_user(user_id)
    conn=sqlite3.connect(DB_NAME)
    cur=conn.cursor()
    cur.execute('UPDATE users SET level=? WHERE user_id=?',(calculate_level(user[2]),user_id))
    conn.commit();conn.close()


def add_score(user_id,points):
    conn=sqlite3.connect(DB_NAME);cur=conn.cursor()
    cur.execute('UPDATE users SET score=score+?, xp=xp+? WHERE user_id=?',(points,points,user_id))
    conn.commit();conn.close()
    add_coins(user_id,5)
    update_level(user_id)


def add_coins(user_id,amount):
    conn=sqlite3.connect(DB_NAME);cur=conn.cursor()
    cur.execute('UPDATE users SET coins=coins+? WHERE user_id=?',(amount,user_id))
    conn.commit();conn.close()


def open_chest(user_id):
    user=get_user(user_id)
    if user[9]<=0:
        return 0
    import random
    reward=random.choice([10,20,50,100])
    conn=sqlite3.connect(DB_NAME);cur=conn.cursor()
    cur.execute('UPDATE users SET chests=chests-1, coins=coins+? WHERE user_id=?',(reward,user_id))
    conn.commit();conn.close()
    return reward


def add_chest(user_id):
    conn=sqlite3.connect(DB_NAME);cur=conn.cursor()
    cur.execute('UPDATE users SET chests=chests+1 WHERE user_id=?',(user_id,))
    conn.commit();conn.close()


def get_user_level(user_id):
    return get_user(user_id)[3]


def complete_lesson(user_id,lesson_id):
    conn=sqlite3.connect(DB_NAME);cur=conn.cursor()
    old=get_user(user_id)[5]
    items=old.split(',') if old else []
    if lesson_id not in items:items.append(lesson_id)
    cur.execute('UPDATE users SET completed_lessons=? WHERE user_id=?',(','.join(items),user_id))
    conn.commit();conn.close()


def get_completed_lessons(user_id):
    x=get_user(user_id)[5]
    return x.split(',') if x else []


def add_badge(user_id,badge):
    conn=sqlite3.connect(DB_NAME);cur=conn.cursor()
    old=get_user(user_id)[6]
    items=old.split(',') if old else []
    if badge not in items:items.append(badge)
    cur.execute('UPDATE users SET badges=? WHERE user_id=?',(','.join(items),user_id))
    conn.commit();conn.close()


def get_badges(user_id):
    x=get_user(user_id)[6]
    return x.split(',') if x else []

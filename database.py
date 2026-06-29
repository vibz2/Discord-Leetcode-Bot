import sqlite3

DB_NAME = "data.db"

POINTS = {
    "easy": 1,
    "medium": 3,
    "hard": 5
}


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS solves (
        user_id TEXT NOT NULL,
        username TEXT NOT NULL,
        problem_id INTEGER NOT NULL,
        difficulty TEXT NOT NULL,
        points INTEGER NOT NULL,
        solved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        UNIQUE(user_id, problem_id)
    )
    """)

    conn.commit()
    conn.close()


def add_solve(
    user_id: str,
    username: str,
    problem_id: int,
    difficulty: str
):
    difficulty = difficulty.lower()

    if difficulty not in POINTS:
        return False, (
            "Difficulty must be easy, medium, or hard."
        )

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO solves (
            user_id,
            username,
            problem_id,
            difficulty,
            points
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            str(user_id),
            str(username),
            int(problem_id),
            str(difficulty),
            POINTS[difficulty]
        ))

        conn.commit()

        return True, POINTS[difficulty]

    except sqlite3.IntegrityError:
        return False, (
            "You already logged this problem."
        )

    finally:
        conn.close()


def get_leaderboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        username,
        SUM(points) AS total_points
    FROM solves
    GROUP BY user_id
    ORDER BY total_points DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_user_stats(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        COUNT(*),
        COALESCE(SUM(points), 0)
    FROM solves
    WHERE user_id = ?
    """, (str(user_id),))

    total_solves, total_points = cursor.fetchone()

    cursor.execute("""
    SELECT
        difficulty,
        COUNT(*)
    FROM solves
    WHERE user_id = ?
    GROUP BY difficulty
    """, (str(user_id),))

    counts = {
        "easy": 0,
        "medium": 0,
        "hard": 0
    }

    for difficulty, count in cursor.fetchall():
        counts[difficulty] = count

    conn.close()

    return {
        "solves": total_solves,
        "points": total_points,
        "easy": counts["easy"],
        "medium": counts["medium"],
        "hard": counts["hard"]
    }

def clear_user_data(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM solves
    WHERE user_id = ?
    """, (str(user_id),))

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted

def clear_all_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM solves
    """)

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted
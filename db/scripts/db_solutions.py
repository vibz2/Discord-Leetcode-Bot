from db import get_connection

POINTS = {
    "easy": 2,
    "medium": 4,
    "hard": 6
}

def submission_exists(
    user_id,
    problem_slug,
    timestamp
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 1
    FROM solutions
    WHERE user_id = ?
    AND problem_slug = ?
    AND timestamp = ?
    LIMIT 1
    """, (str(user_id), problem_slug, int(timestamp)))

    result = cursor.fetchone()

    conn.close()

    return result is not None

def has_solved_before(user_id, problem_slug):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 1
    FROM solutions
    WHERE user_id = ?
    AND problem_slug = ?
    LIMIT 1
                   """, (str(user_id), problem_slug))
    
    result = cursor.fetchone()
    conn.close()

    return result is not None

def add_solution(user_id, problem_id, problem_slug, difficulty, timestamp):
    difficulty = difficulty.lower()

    if difficulty not in POINTS:
        return False, (
            "Difficulty must be easy, medium, or hard."
        )

    repeat = has_solved_before(user_id, problem_slug)

    base_points = POINTS[difficulty]

    if repeat:
        points = int(0.5 * base_points)
    else:
        points = base_points

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO solutions (
        user_id,
        problem_id,
        problem_slug,
        difficulty,
        points,
        timestamp
                   ) VALUES (?, ?, ?, ?, ?, ?)
                   """, (user_id, problem_id, problem_slug, difficulty, points, timestamp))
    
    conn.commit()
    conn.close()

    return points

def clear_user_data(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM solutions
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
    DELETE FROM solutions
    """)

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted
from db import get_connection

def get_leaderboard():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        users.discord_username,
        SUM(solutions.points) AS total_points
    FROM solutions
    JOIN users
        ON solutions.user_id = users.discord_id
    GROUP BY solutions.user_id
    ORDER BY total_points DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_user_stats(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT (DISTINCT problem_slug)
    FROM solutions
    WHERE user_id = ?
                   """, (str(user_id),))
    
    unique_solutions = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COALESCE(SUM (points), 0)
    FROM solutions
    WHERE user_id = ?
                   """, (str(user_id),))
    
    total_points = cursor.fetchone()[0]

    cursor.execute("""
    SELECT difficulty, COUNT(DISTINCT problem_slug)
    FROM solutions
    WHERE user_id = ?
    GROUP BY difficulty
                   """, (str(user_id),))
    
    counts = {
        "easy": 0,
        "medium": 0,
        "hard": 0
    }

    for difficult, count in cursor.fetchall():
        counts[difficult] = count

    return {
        "solutions": unique_solutions,
        "points": total_points,
        "easy": count["easy"],
        "medium": count["medium"],
        "hard": count["hard"]
    }

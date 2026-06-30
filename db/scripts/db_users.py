from db.scripts.init_db import get_connection

def link_user(discord_id, discord_username, leetcode_username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO users (
        discord_id,
        discord_username,
        leetcode_username
                   ) Values (?, ?, ?)
                   """, (str(discord_id), discord_username, leetcode_username))

    conn.commit()
    conn.close()

def get_leetcode_username(discord_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT leetcode_username
    FROM users
    WHERE discord_id = ?
    """, (str(discord_id),))

    result = cursor.fetchone()

    conn.close()

    if result is None:
        return None

    return result[0]
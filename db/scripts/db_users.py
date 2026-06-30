from db import get_connection

def link_user(discord_id, discord_username, leetcode_username):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO OR REPLACE INTO users (
        discord_id,
        discord_username,
        leetcode_username
                   ) Values (?, ?, ?)
                   """, (str(discord_id), discord_username, leetcode_username))

    conn.commit()
    conn.close()
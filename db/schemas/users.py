def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        discord_id TEXT PRIMARY KEY,
        discord_username TEXT NOT NULL,
        leetcode_username TEXT NOT NULL
                   )
                   """)
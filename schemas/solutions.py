def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS solutions (
        user_id TEXT NOT NULL,
        problem_slug TEXT NOT NULL,
        points INTEGER NOT NULL,
        timestamp INTEGER NOT NULL,
        FOREIGN KEY (user_id)
            REFERENCES users(discord_id)
                   )
                   """)
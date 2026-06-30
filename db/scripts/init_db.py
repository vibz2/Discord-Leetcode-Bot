import sqlite3
from db.schemas import SCHEMAS

DB_NAME = "/data/data.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    for schema in SCHEMAS:
        schema(cursor)

    conn.commit()
    conn.close()



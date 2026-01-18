import sqlite3
from typing import Optional, Dict

DB_NAME = "users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password BLOB NOT NULL,
                role TEXT NOT NULL
            )
        """)
        conn.commit()


def add_user(username: str, password: bytes, role: str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()


def get_user(username: str) -> Optional[Dict]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT username, password, role FROM users WHERE username=?",
            (username,)
        )
        row = cursor.fetchone()

    if row:
        return {
            "username": row[0],
            "password": row[1],
            "role": row[2]
        }

    return None

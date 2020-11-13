import sqlite3

MASTER_PASSWORD = "123456"

conn = sqlite3.connect("passwords.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

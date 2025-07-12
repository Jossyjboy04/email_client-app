# db_handler.py

import sqlite3
from config import DB_PATH
from datetime import datetime

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Submissions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            key TEXT,
            value TEXT,
            timestamp TEXT
        )
    ''')

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            phone TEXT
        )
    ''')

    # Processed emails table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS processed_emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message_id TEXT UNIQUE,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

def save_key_values(sender, data_dict):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().isoformat(timespec="seconds")

    for key, value in data_dict.items():
        cursor.execute('''
            INSERT INTO submissions (sender, key, value, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (sender, key, value, now))

    conn.commit()
    conn.close()

def email_exists_in_users(email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def get_user_name(email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT first_name FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "there"

def is_email_processed(message_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM processed_emails WHERE message_id = ?", (message_id,))
    result = cursor.fetchone()
    conn.close()
    return bool(result)

def mark_email_as_processed(message_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat(timespec="seconds")
    cursor.execute('''
        INSERT OR IGNORE INTO processed_emails (message_id, timestamp)
        VALUES (?, ?)
    ''', (message_id, timestamp))
    conn.commit()
    conn.close()

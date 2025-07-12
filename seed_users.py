# seed_users.py
from db_handler import init_db
import sqlite3
from config import DB_PATH

init_db()
users = [
    ("Joseph", "Oloriojekabe", "olorijoseph2002@gmail.com", "07038640142"),
    ("Adebowale", "Ademola", "fadebowaley@gmail.com", "08012345678"),
    ("Mcfadipe", "Ezekiel", "ezekielmcfadipe@gmail.com", "09150981401"),
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for user in users:
    cursor.execute('''
        INSERT OR IGNORE INTO users (first_name, last_name, email, phone)
        VALUES (?, ?, ?, ?)
    ''', user)

conn.commit()
conn.close()
print("✅ Users seeded successfully.")

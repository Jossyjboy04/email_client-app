import sqlite3

conn = sqlite3.connect("submissions.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM submissions ORDER BY timestamp DESC")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

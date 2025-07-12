import sqlite3
import csv

from config import DB_PATH

def export_to_csv():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM submissions")
    rows = cursor.fetchall()

    with open("submissions_export.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([col[0] for col in cursor.description])  # Header
        writer.writerows(rows)

    conn.close()
    print("✅ Exported to submissions_export.csv")

if __name__ == "__main__":
    export_to_csv()


import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM market_data;")
rows = cursor.fetchall()

print(f"Total rows found: {len(rows)}")
for row in rows:
    print(row)

conn.close()
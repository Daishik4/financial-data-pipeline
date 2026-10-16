import sqlite3
import requests

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS market_data
(trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
symbol TEXT,price INT)""")


response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
data = response.json()

insert_sql = "INSERT INTO market_data(symbol,price) VALUES (?,?)"

cleaned_symbol = data['symbol'].strip()
cleaned_price = float(data['price'])
cursor.execute(insert_sql,(cleaned_symbol,cleaned_price))

conn.commit()
conn.close ()
print("Data inserted successfully")


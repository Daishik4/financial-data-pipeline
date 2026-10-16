from pipeline import response
import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import requests

load_dotenv()
db_pass = os.getenv("DB_PASSWORD")
engine = create_engine(f"postgresql://postgres:{db_pass}@localhost:5432/postgres")

response = requests.get("https://api.binance.com/api/v3/ticker/price")
data_df = pd.DataFrame(response.json())

data_df = data_df[data_df['symbol'].str.contains("USDT")]
data_df['price'] = data_df["price"].astype(float)
data_df['trade_time'] = pd.Timestamp.now()
 
data_df.to_sql("market_data",engine,if_exists="append",index=False)

print("Data successfully bulk-inserted into PostgreSQL!")

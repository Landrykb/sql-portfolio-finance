"""
Fraud Joins — Finance Domain
BleepxQuery SwiftLink Training Program
"""
import sqlite3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load datasets
conn = sqlite3.connect(':memory:')
pd.read_csv('../../datasets/finance_stocks.csv').to_sql('finance_stocks', conn, index=False, if_exists='replace')
pd.read_csv('../../datasets/market_index.csv').to_sql('market_index', conn, index=False, if_exists='replace')

# Stock-Market Index Matches by Ticker
df0 = pd.read_sql_query("""SELECT f.ticker, COUNT(*) as market_count FROM finance_stocks f JOIN market_index m ON f.date = m.date GROUP BY f.ticker ORDER BY market_count DESC""", conn)
print(f"Stock-Market Index Matches by Ticker: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")

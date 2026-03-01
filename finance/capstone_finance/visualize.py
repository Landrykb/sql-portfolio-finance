"""
Capstone Finance — Finance Domain
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

# Stock vs Market Index
df0 = pd.read_sql_query("""SELECT f.date, ROUND(AVG(f.close),2) as avg_close, ROUND(AVG(m.index_close),2) as avg_index FROM finance_stocks f LEFT JOIN market_index m ON f.date = m.date GROUP BY f.date ORDER BY f.date""", conn)
print(f"Stock vs Market Index: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")

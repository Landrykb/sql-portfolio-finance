"""
Transaction Select — Finance Domain
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

# Total Close Price by Date
df0 = pd.read_sql_query("""SELECT date, ROUND(SUM(close),2) as total FROM finance_stocks GROUP BY date ORDER BY date""", conn)
print(f"Total Close Price by Date: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")

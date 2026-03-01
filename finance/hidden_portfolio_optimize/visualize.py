"""
Hidden Portfolio Optimize — Finance Domain
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

# Portfolio: Close vs Volume
df0 = pd.read_sql_query("""SELECT ticker, ROUND(AVG(close),2) as avg_close, ROUND(AVG(volume),0) as avg_volume FROM finance_stocks GROUP BY ticker ORDER BY avg_close DESC""", conn)
print(f"Portfolio: Close vs Volume: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")

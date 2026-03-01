"""
Cte Fraud — Finance Domain
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

# Total Volume by Ticker (CTE)
df0 = pd.read_sql_query("""WITH TickerStats AS (SELECT ticker, SUM(volume) as total_volume FROM finance_stocks GROUP BY ticker) SELECT ticker, total_volume FROM TickerStats ORDER BY total_volume DESC""", conn)
print(f"Total Volume by Ticker (CTE): {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")

"""
Finance Domain — Run All Solved Queries
BleepxQuery SwiftLink Training Program
"""
import sqlite3
import pandas as pd
import os

# Load datasets
conn = sqlite3.connect(':memory:')
datasets_dir = os.path.join(os.path.dirname(__file__), 'datasets')
pd.read_csv(os.path.join(datasets_dir, 'finance_stocks_sample.csv')).to_sql('finance_stocks', conn, index=False, if_exists='replace')
pd.read_csv(os.path.join(datasets_dir, 'market_index_sample.csv')).to_sql('market_index', conn, index=False, if_exists='replace')

print("Datasets loaded. Running queries...\n")

queries = {
    'hidden_fraud_detection': """WITH MarketAvg AS (
  SELECT
    date,
    ROUND(AVG(volume), 2) AS market_avg_volume
  FROM finance_stocks
  GROUP BY date
)
SELECT
  f.ticker,
  f.date,
  CAST(f.volume AS INTEGER) AS volume,
  CAST(m.market_avg_volume AS INTEGER) AS market_avg_volume,
  ROUND(f.volume / m.market_avg_volume, 2) AS volume_ratio,
  CASE
    WHEN f.volume > 3 * m.market_avg_volume THEN 'RED FLAG'
    WHEN f.volume > 2 * m.market_avg_volume THEN 'WARNING'
    ELSE 'NORMAL'
  END AS alert_level
FROM finance_stocks f
INNER JOIN MarketAvg m ON f.date = m.date
WHERE f.volume > 2 * m.market_avg_volume
ORDER BY volume_ratio DESC
LIMIT 15;""",
    'hidden_portfolio_optimize': """WITH TickerMetrics AS (
  SELECT 
  ticker, date, open, close, high, low, volume,
  ROUND((close - open) / open * 100, 3) AS day_return_pct,
  ROUND((high - low) / open * 100, 3) AS volatility_pct
  FROM finance_stocks
  WHERE open > 0
),
Ranked AS (
  SELECT 
  ticker, 
  date, 
  ROUND(open, 2) AS open_price,
  ROUND(close, 2) AS close_price,
  ROUND(high - low, 2) AS price_spread, 
  volume,
  day_return_pct,
  volatility_pct,
  CASE 
    WHEN day_return_pct > 5 THEN 'STRONG BUY'
    WHEN day_return_pct > 0 THEN 'BUY'
    WHEN day_return_pct > -5 THEN 'HOLD'
    ELSE 'SELL' 
  END AS recommendation,
  ROW_NUMBER() OVER (ORDER BY day_return_pct DESC) AS performance_rank
  FROM TickerMetrics
)
SELECT 
  ticker, 
  date, 
  open_price, 
  close_price, 
  price_spread, 
  volume, 
  day_return_pct, 
  volatility_pct, 
  recommendation, 
  performance_rank
FROM Ranked
WHERE performance_rank <= 20
ORDER BY performance_rank;
""",
}

for name, sql in queries.items():
    try:
        df = pd.read_sql_query(sql, conn)
        print(f"✓ {name}: {len(df)} rows")
    except Exception as e:
        print(f"✗ {name}: {e}")

conn.close()
print("\nDone!")

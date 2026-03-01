-- Hidden Portfolio Optimize
-- Domain: Finance
-- Level: Master
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 10
-- Date: 3/2/2026

WITH TickerMetrics AS (
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


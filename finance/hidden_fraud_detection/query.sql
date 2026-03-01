-- Hidden Fraud Detection
-- Domain: Finance
-- Level: Master
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 4
-- Date: 3/1/2026

WITH MarketAvg AS (
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
LIMIT 15;

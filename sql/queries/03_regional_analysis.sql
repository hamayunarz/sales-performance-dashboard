SELECT
  "Region",
  COUNT(*) AS total_orders,
  ROUND(SUM("Sales")::numeric, 2) AS total_sales,
  ROUND(SUM("Profit")::numeric, 2) AS total_profit
FROM cleaned_superstored
GROUP BY "Region"
ORDER BY total_sales DESC;
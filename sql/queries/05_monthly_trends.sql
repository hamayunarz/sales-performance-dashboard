SELECT 
    DATE_TRUNC('month', "Order.Date") AS month,
    COUNT(*) AS total_orders,
    ROUND(SUM("Sales")::numeric, 2) AS total_sales,
    ROUND(SUM("Profit")::numeric, 2) AS total_profit
FROM cleaned_superstored
GROUP BY DATE_TRUNC('month', "Order.Date")
ORDER BY month;
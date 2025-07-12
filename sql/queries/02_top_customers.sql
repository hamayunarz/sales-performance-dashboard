SELECT 
    "Customer.ID",
    "Customer.Name",
    COUNT(*) AS order_count,
    ROUND(SUM("Sales")::numeric, 2) AS total_sales,
    ROUND(SUM("Profit")::numeric, 2) AS total_profit
FROM cleaned_superstored
GROUP BY "Customer.ID", "Customer.Name"
ORDER BY total_sales DESC
LIMIT 10;
-- Sales Performance Summary
SELECT 
    COUNT(*) AS total_orders,
    COUNT(DISTINCT "Customer.ID") AS unique_customers,
    ROUND(SUM("Sales")::numeric, 2) AS total_sales,
    ROUND(SUM("Profit")::numeric, 2) AS total_profit,
    ROUND(AVG("Sales")::numeric, 2) AS avg_order_value,
    ((SUM("Profit") / SUM("Sales")) * 100, 2) AS profit_margin_percent
FROM cleaned_superstored

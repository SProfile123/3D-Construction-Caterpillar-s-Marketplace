-- Top Performing Product Categories
SELECT Category, SUM(Sales) AS Revenue, SUM(Profit) AS Profit
FROM printer_sales
GROUP BY Category
ORDER BY Revenue DESC;

-- Profit Margin by Region
SELECT Region, ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS ProfitMargin
FROM printer_sales
GROUP BY Region
ORDER BY ProfitMargin DESC;

-- Monthly Trend
SELECT DATE_TRUNC('month', OrderDate) AS Month, SUM(Sales) AS MonthlySales
FROM printer_sales
GROUP BY Month
ORDER BY Month;

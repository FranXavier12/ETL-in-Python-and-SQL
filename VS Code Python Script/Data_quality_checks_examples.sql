SELECT state, city, COUNT(customerID) AS CustomerCount
FROM customers
GROUP BY state, city
ORDER BY CustomerCount DESC;

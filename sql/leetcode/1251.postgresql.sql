-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    Prices.product_id,
    COALESCE(ROUND(SUM(UnitsSold.units * Prices.price)::NUMERIC / SUM(UnitsSold.units), 2), 0) AS average_price

FROM Prices 

LEFT JOIN UnitsSold
ON (UnitsSold.product_id = Prices.product_id) 
    AND (UnitsSold.purchase_date >= Prices.start_date) 
    AND (UnitsSold.purchase_date <= Prices.end_date) 

GROUP BY
    Prices.product_id


-- =============================================================================
-- Solution 1
-- =============================================================================

SELECT
    Prices.product_id,
    CASE
        WHEN SUM(UnitsSold.units) IS NULL THEN 0
        ELSE ROUND(SUM(UnitsSold.units * Prices.price) / SUM(UnitsSold.units)::NUMERIC, 2)
    END AS average_price

FROM Prices 

LEFT JOIN UnitsSold
ON (UnitsSold.product_id = Prices.product_id) 
    AND (UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date) 

GROUP BY
    Prices.product_id
    
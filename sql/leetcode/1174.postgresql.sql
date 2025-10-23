-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)::NUMERIC / COUNT(*) * 100, 2) AS immediate_percentage

FROM Delivery

INNER JOIN (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date

    FROM Delivery

    GROUP BY
        customer_id
) AS tbl_first_order
ON (Delivery.customer_id = tbl_first_order.customer_id) 
    AND (Delivery.order_date = tbl_first_order.first_order_date)


-- =============================================================================
-- Solution 1
-- =============================================================================

SELECT
    ROUND(100.0 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*), 2) AS immediate_percentage

FROM Delivery

WHERE 
    (customer_id, order_date) IN (
        SELECT
            customer_id,
            MIN(order_date)

        FROM Delivery

        GROUP BY
            customer_id
    )
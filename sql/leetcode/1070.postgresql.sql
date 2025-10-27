-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    product_id,
    year AS first_year,
    quantity,
    price

FROM Sales

WHERE
    (product_id, year) IN (
        SELECT
            product_id,
            MIN(year) AS year

        FROM Sales

        GROUP BY
            product_id
    )


-- =============================================================================
-- Solution 1
-- =============================================================================

SELECT
    Sales.product_id,
    Sales.year AS first_year,
    quantity,
    price

FROM Sales

INNER JOIN (
    SELECT
        product_id,
        MIN(year) AS year

    FROM Sales

    GROUP BY
        product_id
) AS tbl_temp
ON (Sales.product_id = tbl_temp.product_id)
    AND (Sales.year = tbl_temp.year)
    
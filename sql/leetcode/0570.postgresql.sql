-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    Employee.name

FROM Employee

INNER JOIN (
    SELECT
        managerId

    FROM Employee

    GROUP BY
        managerId

    HAVING
        COUNT(managerId) >= 5
) AS tbl_count
ON Employee.id = tbl_count.managerId

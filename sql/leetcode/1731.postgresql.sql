-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    tbl_manager.employee_id,
    tbl_manager.name,
    COUNT(Employees.employee_id) AS reports_count,
    ROUND(AVG(Employees.age)) AS average_age

FROM Employees

LEFT JOIN Employees AS tbl_manager
ON Employees.reports_to = tbl_manager.employee_id

WHERE
    tbl_manager.employee_id IS NOT NULL

GROUP BY
    tbl_manager.employee_id,
    tbl_manager.name


-- =============================================================================
-- Solution 1
-- =============================================================================

SELECT
    tbl_manager.employee_id,
    tbl_manager.name,
    COUNT(Employees.employee_id) AS reports_count,
    ROUND(AVG(Employees.age)) AS average_age

FROM Employees

INNER JOIN Employees AS tbl_manager
ON Employees.reports_to = tbl_manager.employee_id

GROUP BY
    tbl_manager.employee_id,
    tbl_manager.name

ORDER BY
    tbl_manager.employee_id
    
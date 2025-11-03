-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    Employee.employee_id,
    Employee.department_id

FROM Employee

INNER JOIN (
    SELECT 
        employee_id,
        COUNT(department_id) AS cnt
    
    FROM Employee 
    
    GROUP BY 
        employee_id
) AS tbl_count
ON Employee.employee_id = tbl_count.employee_id

WHERE
    primary_flag = 'Y'
    OR tbl_count.cnt = 1


-- =============================================================================
-- Solution 1
-- =============================================================================

SELECT
    employee_id,
    department_id

FROM Employee

WHERE
    primary_flag = 'Y'
    OR employee_id IN (
        SELECT employee_id 
        FROM Employee 
        GROUP BY employee_id 
        HAVING COUNT(department_id) = 1
    )

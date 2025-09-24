-- =============================================================================
-- My Answer
-- =============================================================================

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT
        CASE
            WHEN N > 0 THEN (
                SELECT DISTINCT 
                    Employee.salary 
                FROM Employee 
                ORDER BY Employee.salary DESC 
                LIMIT 1 OFFSET N-1
            )
            ELSE NULL
        END
  );
END;
$$ LANGUAGE plpgsql;

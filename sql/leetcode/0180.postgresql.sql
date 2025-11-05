-- =============================================================================
-- My Answer
-- =============================================================================

SELECT DISTINCT
    num AS ConsecutiveNums

FROM (
    SELECT
        id,
        num,
        LAG(num, 1) OVER () AS prev,
        LAG(num, 2) OVER () AS prev_prev

    FROM Logs
)

WHERE
    num = prev
    AND num = prev_prev


-- =============================================================================
-- Solution 1
-- =============================================================================

WITH tbl_cte AS (
    SELECT
        num,
        LEAD(num, 1) OVER () AS num1,
        LEAD(num, 2) OVER () AS num2
    
    FROM Logs
)


SELECT DISTINCT
    num AS ConsecutiveNums

FROM tbl_cte

WHERE
    num = num1
    AND num = num2

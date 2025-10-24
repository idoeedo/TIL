-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    ROUND(SUM(CASE WHEN is_immediate = True THEN 1 ELSE 0 END)::NUMERIC / COUNT(DISTINCT player_id), 2) AS fraction

FROM (
    SELECT
        player_id,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn,
        CASE 
            WHEN event_date - LAG(event_date) OVER (PARTITION BY player_id ORDER BY event_date) = 1 THEN True
            ELSE False
        END AS is_immediate

    FROM Activity
)

WHERE
    rn <= 2


-- =============================================================================
-- Solution 1
-- =============================================================================

SELECT
    ROUND(COUNT(DISTINCT player_id)::NUMERIC / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction

FROM Activity

WHERE
    (player_id, event_date - INTERVAL '1 day')
    IN (
        SELECT 
            player_id, 
            MIN(event_date) AS first_login 
        FROM Activity 
        GROUP BY 
            player_id
    )
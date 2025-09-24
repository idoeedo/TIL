-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    machine_id,
    ROUND((SUM(CASE activity_type WHEN 'start' THEN - timestamp ELSE timestamp END) / COUNT(DISTINCT process_id))::NUMERIC, 3) AS processing_time

FROM Activity

GROUP BY
    machine_id

-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    today.id

FROM Weather AS today

LEFT JOIN Weather AS yesterday
ON today.recorddate = yesterday.recorddate + INTERVAL '1 day'

WHERE
    today.temperature > yesterday.temperature

-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users

FROM Activity

WHERE
    activity_date BETWEEN '2019-07-27'::DATE - INTERVAL '29 DAYS' AND '2019-07-27'::DATE

GROUP BY
    activity_date

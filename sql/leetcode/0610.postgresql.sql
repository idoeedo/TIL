-- =============================================================================
-- My Answer
-- =============================================================================

SELECT
    x,
    y,
    z,
    CASE
        WHEN x+y+z - GREATEST(x, y, z) > GREATEST(x, y, z) THEN 'Yes'
        ELSE 'No'
    END AS triangle
    
FROM Triangle


-- =============================================================================
-- Solution 1
-- =============================================================================

SELECT
    x,
    y,
    z,
    CASE
        WHEN x+y>z AND x+z>y AND z+y>x THEN 'Yes'
        ELSE 'No'
    END AS triangle

FROM Triangle


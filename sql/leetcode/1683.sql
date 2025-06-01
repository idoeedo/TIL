-- Write your PostgreSQL query statement below

SELECT
    tweet_id

FROm Tweets

WHERE
    LENGTH(content) > 15

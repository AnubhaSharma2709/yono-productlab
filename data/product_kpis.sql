-- KPI 1: Onboarding completion rate
-- Denominator: users who started onboarding
-- Numerator: users who completed onboarding

WITH onboarding AS (
    SELECT
        COUNT(DISTINCT CASE
            WHEN event_name = 'onboarding_started'
            THEN user_id
        END) AS started_users,

        COUNT(DISTINCT CASE
            WHEN event_name = 'onboarding_completed'
            THEN user_id
        END) AS completed_users
    FROM events
)
SELECT
    started_users,
    completed_users,
    ROUND(
        100.0 * completed_users /
        NULLIF(started_users, 0),
        2
    ) AS onboarding_completion_rate_pct
FROM onboarding;

-- KPI 2: Transaction success rate
-- Denominator: all recorded transactions
-- Numerator: successful transactions

SELECT
    COUNT(*) AS total_transactions,

    SUM(CASE
        WHEN transaction_status = 'SUCCESS'
        THEN 1 ELSE 0
    END) AS successful_transactions,

    ROUND(
        100.0 * SUM(CASE
            WHEN transaction_status = 'SUCCESS'
            THEN 1 ELSE 0
        END) / NULLIF(COUNT(*), 0),
        2
    ) AS transaction_success_rate_pct
FROM transactions;

-- KPI 3: Active users by event date
-- A user is active on a day if at least one event is recorded.

SELECT
    DATE(event_timestamp) AS activity_date,
    COUNT(DISTINCT user_id) AS daily_active_users
FROM events
GROUP BY DATE(event_timestamp)
ORDER BY activity_date;




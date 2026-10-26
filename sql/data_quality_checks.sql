
-- 1. Onboarding event counts
SELECT
    event_name,
    COUNT(*) AS event_count,
    COUNT(DISTINCT user_id) AS unique_users
FROM events
WHERE event_name IN (
    'onboarding_started',
    'profile_details_submitted',
    'identity_verification_completed',
    'onboarding_completed'
)
GROUP BY event_name
ORDER BY event_count DESC;


-- 2. Transaction status distribution
SELECT
    transaction_status,
    COUNT(*) AS transaction_count,
    ROUND(
        100.0 * COUNT(*) /
        (SELECT COUNT(*) FROM transactions),
        2
    ) AS percentage
FROM transactions
GROUP BY transaction_status
ORDER BY transaction_count DESC;


-- 3. Transaction types
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(AVG(amount), 2) AS average_amount
FROM transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;


-- 4. Events by device
SELECT
    device_type,
    COUNT(*) AS event_count,
    COUNT(DISTINCT user_id) AS unique_users
FROM events
GROUP BY device_type
ORDER BY event_count DESC;

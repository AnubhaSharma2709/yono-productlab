
-- Onboarding funnel: distinct users at each stage

WITH funnel AS (
    SELECT
        COUNT(DISTINCT CASE
            WHEN event_name = 'onboarding_started'
            THEN user_id
        END) AS started,

        COUNT(DISTINCT CASE
            WHEN event_name = 'profile_details_submitted'
            THEN user_id
        END) AS profile_submitted,

        COUNT(DISTINCT CASE
            WHEN event_name = 'identity_verification_completed'
            THEN user_id
        END) AS identity_verified,

        COUNT(DISTINCT CASE
            WHEN event_name = 'onboarding_completed'
            THEN user_id
        END) AS completed
    FROM events
)
SELECT
    '1. Onboarding started' AS funnel_stage,
    started AS users,
    100.0 AS pct_of_starters
FROM funnel

UNION ALL

SELECT
    '2. Profile submitted',
    profile_submitted,
    ROUND(100.0 * profile_submitted / NULLIF(started, 0), 2)
FROM funnel

UNION ALL

SELECT
    '3. Identity verified',
    identity_verified,
    ROUND(100.0 * identity_verified / NULLIF(started, 0), 2)
FROM funnel

UNION ALL

SELECT
    '4. Onboarding completed',
    completed,
    ROUND(100.0 * completed / NULLIF(started, 0), 2)
FROM funnel;

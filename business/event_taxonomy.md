# YONO ProductLab — Event Taxonomy

## 1. Purpose

Define the events tracked in the simulated mobile banking application. These events will support onboarding funnel analysis, activation, feature adoption, retention and transaction analysis.

All event data will be synthetic and will not represent actual SBI YONO telemetry.

## 2. Common Event Properties

Each event should contain:

- `event_id`: Unique identifier for the event.
- `user_id`: Synthetic identifier for the user.
- `event_name`: Name of the event.
- `event_timestamp`: Timestamp when the event occurred.
- `session_id`: Identifier for the simulated session.
- `device_type`: Mobile operating system or device category.
- `app_version`: Simulated application version.
- `acquisition_channel`: Channel associated with the user.
- `event_properties`: Additional attributes relevant to the event.

User-level attributes such as signup date and customer segment will be maintained in the users dataset rather than unnecessarily repeated in every event.

## 3. Onboarding Events

| Event name | Meaning |
|---|---|
| `onboarding_started` | User begins onboarding |
| `profile_details_submitted` | User submits profile details |
| `identity_verification_completed` | Simulated identity verification succeeds |
| `onboarding_completed` | User completes the onboarding journey |
| `login_succeeded` | User successfully logs in |
| `login_failed` | Login attempt fails |

## 4. Product Engagement Events

| Event name | Meaning |
|---|---|
| `home_viewed` | User views the home screen |
| `account_details_viewed` | User views account information |
| `transaction_history_viewed` | User opens transaction history |
| `bill_payment_started` | User starts a bill payment |
| `bill_payment_completed` | User completes a simulated bill payment |
| `fund_transfer_started` | User starts a simulated transfer |
| `fund_transfer_completed` | User completes a simulated transfer |
| `feature_help_viewed` | User opens feature-related help |

## 5. Transaction Events

| Event name | Meaning |
|---|---|
| `transaction_initiated` | User initiates a transaction |
| `transaction_succeeded` | Transaction succeeds |
| `transaction_failed` | Transaction fails |
| `transaction_cancelled` | User or system cancels the transaction |

Each transaction event should include a `transaction_id` where applicable, a `transaction_type` and relevant simulated context.

The transaction outcome will be represented consistently in the transactions dataset. Multiple event records for one transaction must not be counted as multiple transactions.

## 6. User and Session Properties

The users dataset will contain:

- `user_id`
- `signup_date`
- `acquisition_channel`
- `customer_segment`

The events dataset will contain:

- `event_id`
- `user_id`
- `event_name`
- `event_timestamp`
- `session_id`
- `device_type`
- `app_version`
- `event_properties`

The transaction dataset will contain:

- `transaction_id`
- `user_id`
- `transaction_timestamp`
- `transaction_type`
- `amount`
- `transaction_status`

## 7. Event Tracking Rules

1. Each event record must have a unique `event_id`.
2. Every event must reference a valid synthetic user.
3. Timestamps must use a consistent, documented timezone.
4. Transaction outcomes must use a controlled set of statuses.
5. Event names must follow a consistent naming convention.
6. Event sequences must be plausible, but users may abandon journeys or encounter failures.
7. Missing or duplicate records, if intentionally simulated, must be documented.
8. Event properties must not contain real customer information or confidential data.

## 8. Analytical Use Cases

- Onboarding conversion and step-level drop-off.
- Seven-day activation.
- Daily and cohort-based user retention.
- Feature adoption and repeat usage.
- Transaction initiation-to-completion conversion.
- Failure and cancellation analysis by transaction type, device and app version.

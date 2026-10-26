
# YONO ProductLab — Synthetic Data Design

## Purpose
Generate synthetic digital banking product data for product
analytics practice. This dataset does not represent real SBI
YONO customers, transactions, telemetry, or internal metrics.

## Analysis Period
90 days.

## Target Population
5,000 synthetic users.

## Tables
- users: one row per synthetic user
- events: one row per simulated app event
- transactions: one row per simulated transaction

## Acquisition Channels
- Organic Search
- Referral
- Paid Campaign
- Direct

## Customer Segments
- New-to-Banking
- Existing Banking Customer
- Digital-First Customer

## Device Types
- Android
- iOS
- Web

## Transaction Types
- Fund Transfer
- Bill Payment
- Recharge

## Transaction Statuses
- SUCCESS
- FAILED
- CANCELLED

## Data Quality Requirements
- Every user has a unique user_id.
- Every event has a unique event_id.
- Every transaction has a unique transaction_id.
- Every event and transaction references a valid user.
- Timestamps use a consistent ISO format.
- Transaction amounts are non-negative.
- All records are synthetic.
- Simulation assumptions must be documented.

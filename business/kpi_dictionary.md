# YONO ProductLab — KPI Dictionary

## 1. Activation Rate

**Business question:** What percentage of new users become activated users?

**Definition:** Percentage of eligible new users who complete the defined activation event within seven days of signup.

**Formula:**

Activation Rate = Users activated within 7 days / Eligible new users × 100

**Grain:** Unique user.

**Time window:** Seven days from each user's signup timestamp.

**Important rule:** The activation event must be explicitly defined before analysis.

## 2. Funnel Conversion Rate

**Business question:** At which stage do users abandon onboarding?

**Formula:**

Stage Conversion Rate = Unique users reaching the next stage / Unique users reaching the previous stage × 100

**Grain:** Unique user within the defined funnel analysis period.

**Important rule:** We must define the event order and whether users must complete steps within the same session.

## 3. Funnel Drop-off Rate

**Business question:** Which onboarding step has the largest loss of users?

**Formula:**

Stage Drop-off Rate = 100 − Stage Conversion Rate

**Grain:** Unique user within the defined funnel.

## 4. Daily Active Users (DAU)

**Business question:** How many unique users actively use the product each day?

**Formula:** Count distinct users who perform at least one qualifying active event on a calendar day.

**Important rule:** Login attempts alone will not automatically qualify as meaningful product activity. The qualifying event list must be documented.

## 5. Feature Adoption Rate

**Business question:** What proportion of active users use a particular feature?

**Formula:**

Feature Adoption Rate = Unique active users using the feature / Unique active users in the defined population × 100

**Important rule:** Numerator and denominator must use the same population and time window.

## 6. Retention Rate

**Business question:** What percentage of a signup cohort returns after signup?

**Formula:**

Day-N Retention = Users from a signup cohort active on cohort day N / Eligible users in that signup cohort × 100

**Important rule:** We will distinguish exact-day retention from rolling retention and state which definition is used in every report.

## 7. Transaction Success Rate

**Business question:** What proportion of initiated transactions succeed?

**Formula:**

Transaction Success Rate = Successfully completed eligible transactions / Eligible initiated transactions × 100

**Grain:** Unique transaction.

**Important rule:** Retries, duplicate events, cancellations and reversals must be handled consistently. A transaction is not counted as successful merely because a success event was recorded more than once.

## 8. Repeat Feature Usage

**Business question:** Which features encourage repeat usage?

**Definition:** Percentage of eligible users who use a feature on at least two distinct days during the defined observation period.

**Formula:**

Repeat Usage Rate = Eligible feature users active on 2+ distinct days / Eligible users who used the feature at least once × 100

## Reporting Standards

- Store metric definitions and assumptions alongside the analysis.
- Use unique-user counts for user metrics and unique transaction IDs for transaction metrics.
- Document the observation period and reporting timezone.
- Handle missing data and duplicate records explicitly.
- Validate KPI totals against the underlying SQL results.
- Label all findings as synthetic-data results.

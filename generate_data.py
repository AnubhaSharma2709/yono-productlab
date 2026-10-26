
def generate_events(users, signup_dates):
    """Generate simulated events with coherent onboarding sequences."""
    events = []

    for user_id, signup_date in signup_dates.items():
        started_onboarding = random.random() < 0.92

        if not started_onboarding:
            continue

        # One session for the initial onboarding journey.
        onboarding_session = make_id("SES")
        device = random.choice(DEVICES)
        app_version = random.choice(APP_VERSIONS)

        # Ensure the initial onboarding timestamp is within the
        # simulation period.
        onboarding_start = random_timestamp(
            signup_date,
            min(signup_date + timedelta(hours=2), END_DATE),
        )

        events.append(
            (
                make_id("EVT"),
                user_id,
                "onboarding_started",
                onboarding_start.isoformat(sep=" "),
                onboarding_session,
                device,
                app_version,
                None,
                json.dumps({"source": "synthetic_generator"}),
            )
        )

        # Some users abandon onboarding before completing it.
        onboarding_complete = random.random() < 0.78

        if onboarding_complete:
            previous_time = onboarding_start

            onboarding_steps = [
                "profile_details_submitted",
                "identity_verification_completed",
                "onboarding_completed",
            ]

            for event_name in onboarding_steps:
                # Each step happens after the previous step.
                previous_time += timedelta(
                    minutes=random.randint(2, 15)
                )

                events.append(
                    (
                        make_id("EVT"),
                        user_id,
                        event_name,
                        previous_time.isoformat(sep=" "),
                        onboarding_session,
                        device,
                        app_version,
                        None,
                        json.dumps(
                            {"source": "synthetic_generator"}
                        ),
                    )
                )

        # Only users who completed onboarding generate
        # regular post-onboarding activity in this simulation.
        if not onboarding_complete:
            continue

        activity_days = random.randint(1, 20)

        for _ in range(activity_days):
            activity_start = signup_date + timedelta(
                days=random.randint(0, 89)
            )

            if activity_start > END_DATE:
                continue

            event_time = random_timestamp(
                activity_start,
                min(
                    activity_start + timedelta(hours=12),
                    END_DATE,
                ),
            )

            event_name = random.choice(
                [
                    "login_succeeded",
                    "login_failed",
                    "home_viewed",
                    "account_details_viewed",
                    "transaction_history_viewed",
                    "bill_payment_started",
                    "bill_payment_completed",
                    "fund_transfer_started",
                    "fund_transfer_completed",
                    "feature_help_viewed",
                ]
            )

            events.append(
                (
                    make_id("EVT"),
                    user_id,
                    event_name,
                    event_time.isoformat(sep=" "),
                    make_id("SES"),
                    random.choice(DEVICES),
                    random.choice(APP_VERSIONS),
                    None,
                    json.dumps(
                        {"source": "synthetic_generator"}
                    ),
                )
            )

    events.sort(key=lambda row: row[3])
    return events

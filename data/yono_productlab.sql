
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    signup_date TEXT NOT NULL,
    acquisition_channel TEXT NOT NULL,
    customer_segment TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    event_name TEXT NOT NULL,
    event_timestamp TEXT NOT NULL,
    session_id TEXT,
    device_type TEXT,
    app_version TEXT,
    acquisition_channel TEXT,
    event_properties TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    transaction_timestamp TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL CHECK (amount >= 0),
    transaction_status TEXT NOT NULL
        CHECK (transaction_status IN (
            'SUCCESS',
            'FAILED',
            'CANCELLED'
        )),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


PRAGMA table_info(users);
PRAGMA table_info(events);
PRAGMA table_info(transactions);


PRAGMA foreign_key_list(events);
PRAGMA foreign_key_list(transactions);




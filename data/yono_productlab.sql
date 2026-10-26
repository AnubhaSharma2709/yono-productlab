
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    signup_date TEXT NOT NULL,
    acquisition_channel TEXT NOT NULL,
    customer_segment TEXT NOT NULL
);

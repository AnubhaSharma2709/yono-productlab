
import sqlite3
from pathlib import Path

DB_PATH = (
    Path(__file__).resolve().parent
    / "data"
    / "yono_productlab.db"
)


def main():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")

        print("=== ROW COUNTS ===")
        for table in ["users", "events", "transactions"]:
            count = connection.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]
            print(f"{table}: {count:,}")

        print("\n=== UNIQUE IDENTIFIERS ===")
        checks = {
            "Duplicate user IDs": """
                SELECT COUNT(*) - COUNT(DISTINCT user_id)
                FROM users
            """,
            "Duplicate event IDs": """
                SELECT COUNT(*) - COUNT(DISTINCT event_id)
                FROM events
            """,
            "Duplicate transaction IDs": """
                SELECT COUNT(*) - COUNT(DISTINCT transaction_id)
                FROM transactions
            """,
        }

        for label, query in checks.items():
            result = connection.execute(query).fetchone()[0]
            print(f"{label}: {result}")

        print("\n=== ORPHAN RECORDS ===")
        orphan_checks = {
            "Events without users": """
                SELECT COUNT(*)
                FROM events e
                LEFT JOIN users u ON e.user_id = u.user_id
                WHERE u.user_id IS NULL
            """,
            "Transactions without users": """
                SELECT COUNT(*)
                FROM transactions t
                LEFT JOIN users u ON t.user_id = u.user_id
                WHERE u.user_id IS NULL
            """,
        }

        for label, query in orphan_checks.items():
            result = connection.execute(query).fetchone()[0]
            print(f"{label}: {result}")

        print("\n=== TRANSACTION QUALITY ===")
        invalid_amounts = connection.execute("""
            SELECT COUNT(*)
            FROM transactions
            WHERE amount < 0
        """).fetchone()[0]

        invalid_statuses = connection.execute("""
            SELECT COUNT(*)
            FROM transactions
            WHERE transaction_status NOT IN (
                'SUCCESS', 'FAILED', 'CANCELLED'
            )
        """).fetchone()[0]

        print(f"Negative transaction amounts: {invalid_amounts}")
        print(f"Invalid transaction statuses: {invalid_statuses}")

        print("\n=== DATE RANGE ===")
        for table, column in [
            ("users", "signup_date"),
            ("events", "event_timestamp"),
            ("transactions", "transaction_timestamp"),
        ]:
            result = connection.execute(
                f"SELECT MIN({column}), MAX({column}) FROM {table}"
            ).fetchone()
            print(f"{table}: {result[0]} to {result[1]}")


if __name__ == "__main__":
    main()

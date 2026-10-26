
import sqlite3
from pathlib import Path

db_path = Path(r"D:\yono-productlab\data\yono_productlab.db")

print("Database exists:", db_path.exists())
print("Database size:", db_path.stat().st_size, "bytes")

with sqlite3.connect(db_path) as connection:
    print("Database opened:", connection.execute(
        "PRAGMA database_list"
    ).fetchall())

    tables = connection.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
    """).fetchall()

    print("Tables:", tables)

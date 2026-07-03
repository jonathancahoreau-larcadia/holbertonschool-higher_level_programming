#!/usr/bin/python3
"""Create and populate the SQLite products database."""

import sqlite3


def create_database():
    """Create the Products table and insert example products."""
    connection = sqlite3.connect("products.db")

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
            """
        )

        cursor.execute(
            """
            INSERT OR REPLACE INTO Products (
                id,
                name,
                category,
                price
            )
            VALUES (?, ?, ?, ?)
            """,
            (1, "Laptop", "Electronics", 799.99)
        )

        cursor.execute(
            """
            INSERT OR REPLACE INTO Products (
                id,
                name,
                category,
                price
            )
            VALUES (?, ?, ?, ?)
            """,
            (2, "Coffee Mug", "Home Goods", 15.99)
        )

        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    create_database()

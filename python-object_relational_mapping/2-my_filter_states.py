#!/usr/bin/python3
"""Lists states from a MySQL database filtered by name.

The script connects to a local MySQL server using credentials
provided on the command line, queries the `states` table for a
single state name, and prints each matching row ordered by `id`.
"""
import sys
import MySQLdb


def main():
    """Connect to the database, query filtered states, and print results.

    Expects four command line arguments in the following order:
    username, password, database name, and state name to filter.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY states.id ASC".format(name)
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

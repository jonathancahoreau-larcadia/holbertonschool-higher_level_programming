#!/usr/bin/python3
"""Lists all states from a MySQL database.

The script connects to a local MySQL server using credentials
provided on the command line, queries the `states` table, and
prints each row ordered by `id`.
"""
import sys
import MySQLdb


def main():
    """Connect to the database, query states, and print results.

    Expects three command line arguments in the following order:
    username, password, database name.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

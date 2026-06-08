#!/usr/bin/python3
"""Lists cities and their states from a MySQL database.

Connects to a local MySQL server using credentials provided on the
command line, queries the `cities` table joined with `states`, and
prints each matching row ordered by city `id` as tuples
``(city_id, city_name, state_name)``.
"""
import sys
import MySQLdb


def main():
    """Connect to the database, query cities joined with states, and print results.

    Expects three command line arguments in the following order:
    username, password, database name.

    The function executes a SELECT that returns
    `(cities.id, cities.name, states.name)` ordered by `cities.id`.
    Results are printed one tuple per line.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name  "
                "FROM cities "
                "JOIN states "
                "ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

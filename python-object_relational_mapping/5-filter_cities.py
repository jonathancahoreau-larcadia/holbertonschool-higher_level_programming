#!/usr/bin/python3
"""Lists city names from a MySQL database for a given state.

Connects to a local MySQL server using credentials provided on the
command line, queries `cities` joined with `states` filtered by the
state name, and prints matching city names separated by commas.
"""
import sys
import MySQLdb


def main():
    """Connect to the database, query city names for a state,
    and print results.

    Expects four command line arguments in the following order:
    username, password, database name, and state name.

    The function executes a SELECT that returns cities whose state
    name matches the given argument, ordered by `cities.id`.
    City names are printed as a comma-separated list.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT cities.name  "
                "FROM states "
                "JOIN cities "
                "ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC",
                (state_name,)
                )
    query_rows = cur.fetchall()
    city = [row[0] for row in query_rows]
    print(", ".join(city))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

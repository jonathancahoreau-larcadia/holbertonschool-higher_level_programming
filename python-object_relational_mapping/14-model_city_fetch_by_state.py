#!/usr/bin/python3
"""Fetch cities by state from a MySQL database using SQLAlchemy.

This script connects to a MySQL database using credentials provided on the
command line, queries the `City` model joined with `State`, and prints
city information grouped by state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State
from model_city import City


if __name__ == "__main__":
    """Run the state-city join query and print results.

    Expects three command line arguments: username, password, and database.
    Opens a SQLAlchemy session, executes the query, prints matching rows,
    and then closes the session.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, database),
        pool_pre_ping=True
    )

    session = Session(engine)

    city_join = session.query(State, City).join(
        City, City.state_id == State.id).order_by(City.id)

    for state, city in city_join:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

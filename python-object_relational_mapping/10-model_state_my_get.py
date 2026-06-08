#!/usr/bin/python3
"""Search for a state by name in a MySQL database using SQLAlchemy.

This script connects to a MySQL database using credentials passed on the
command line, queries the `states` table for a specific state name, and
search for a state by name and print its id."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    search = session.query(State).filter(
        State.name == state_name).order_by(State.id).first()

    if search is None:
        print("Not found")
    else:
        print("{}".format(search.id))

    session.close()

#!/usr/bin/python3
"""Fetch and print all State objects from a MySQL database.

This script connects to a MySQL database using SQLAlchemy and prints all
records from the `states` table in the format `id: name`, ordered by
state id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, database),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()

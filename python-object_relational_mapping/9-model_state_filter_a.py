#!/usr/bin/python3
"""Fetch and print states with names containing the letter A from MySQL.

This script connects to a MySQL database using SQLAlchemy and queries
for all State objects whose name contains the letter "A" or "a".
Matching rows are printed as `id: name`, ordered by state id.
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
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    result_a = session.query(State).filter(
        State.name.like("%a%")).order_by(State.id).all()

    for state in result_a:
        print("{}: {}".format(state.id, state.name))

    session.close()

#!/usr/bin/python3
"""Fetch and print the first State object from a MySQL database.

This script connects to a MySQL database using SQLAlchemy and retrieves
the first row from the `states` table ordered by `id`. It prints the
result as `id: name`, or `Nothing` if no rows exist.
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

    result = session.query(State).order_by(State.id).first()
    if result is None:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))

    session.close()

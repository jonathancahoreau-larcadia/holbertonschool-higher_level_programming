#!/usr/bin/python3
"""Insert a new State into a MySQL database using SQLAlchemy.

This script connects to a MySQL database using credentials passed on the
command line, creates a new `State` with the name 'Louisiana', adds it to
the session, commits the transaction, and prints the new state's id.

Usage: ./11-model_state_insert.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    """Run script: connect, insert a `State('Louisiana')`, commit, print id.

    The script reads database credentials from command line arguments,
    creates a SQLAlchemy session, inserts a new `State` with the name
    'Louisiana', commits the transaction, and prints the new record's id.
    """

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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()

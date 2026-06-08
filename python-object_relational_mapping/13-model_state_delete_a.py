#!/usr/bin/python3
"""Delete State objects whose name contains the letter A from MySQL.

Connects to a MySQL database using SQLAlchemy, queries the `states`
table for State objects whose name contains the letter `a`, deletes
matching records, commits the transaction, and closes the session.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    """Run script: connect, delete states with 'a' in the name, commit, close.

    Reads database credentials from command line arguments, opens a
    SQLAlchemy session, performs the delete, and closes the session.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(username, password, database),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    session = Session(engine)

    delete_state = session.query(State).filter(State.name.like("%a%")).all()

    for state in delete_state:
        session.delete(state)
    session.commit()
    session.close()

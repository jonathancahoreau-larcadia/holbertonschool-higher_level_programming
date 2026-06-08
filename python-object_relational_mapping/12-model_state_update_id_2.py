#!/usr/bin/python3
"""Update the `states` table: set name of state with id=2 to 'New Mexico'.

Connects to a MySQL database using SQLAlchemy, locates the `State`
record with `id == 2`, updates its `name` to "New Mexico", commits the
change, and closes the session.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":

    """Run script: connect, update state id 2 to 'New Mexico', commit, close.

    Reads database credentials from command line arguments, opens a
    SQLAlchemy session, performs the update, and closes the session.
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

    update_state = session.query(State).filter(State.id == 2).first()
    update_state.name = "New Mexico"
    session.commit()
    session.close()

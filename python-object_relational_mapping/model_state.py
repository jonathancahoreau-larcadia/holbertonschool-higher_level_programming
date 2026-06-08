#!/usr/bin/python3
"""SQLAlchemy state model for the `states` table.

Defines the `State` ORM mapping for a MySQL database table named
`states`, with an integer primary key `id` and a string `name`.
"""

from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state row in the `states` table."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

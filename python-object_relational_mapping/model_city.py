#!/usr/bin/python3

from sqlalchemy import Integer, String, Column
from model_state import Base


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)







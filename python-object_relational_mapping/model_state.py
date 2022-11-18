#!/usr/bin/python3
"""
This module contein the State class which
inherits of the Base created of the declarative_base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """This class create a objects for database"""
    __tablename__ = 'states'
    id = Column(Integer(), nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    State()

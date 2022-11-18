#!/usr/bin/python3
"""This module contein and print all elemets of the class"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_filter_a():
    """Print te elemets in the class with contain a letter a in State.name"""
    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir, pool_pre_ping=True)
    Session = sessionmaker(engine)
    state = Session().query(State).order_by(State.id)\
        .filter(State.name.like('%a%'))

    for elemets in state:
        print(f"{elemets.id}: {elemets.name}")


if __name__ == '__main__':
    model_state_filter_a()

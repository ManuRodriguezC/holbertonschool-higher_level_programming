#!/usr/bin/python3
"""This module contein and print all elemets of the class"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_fetch_first():
    """This function print the first element in the class"""

    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    state = Session().query(State).order_by(State.id).first()

    print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    model_state_fetch_first()

    
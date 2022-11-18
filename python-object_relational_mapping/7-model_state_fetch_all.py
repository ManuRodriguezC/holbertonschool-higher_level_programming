#!/usr/bin/python3
"""This module contein and print all elemets of the class"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def model_state_fetch_all():
    """This function print all elemtes of the class"""

    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    states = Session().query(State).order_by(State.id).all()

    for elemet in states:
        print(f"{elemet.id}: {elemet.name}")


if __name__ == '__main__':
    model_state_fetch_all()

#!/usr/bin/python3
"""This module contein and print all elemets of the class"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_update():
    """Update the name if the State id 2 in the State objects"""
    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir)
    Session = sessionmaker(engine)
    conect = engine.connect()
    session = Session(bind=conect)

    state = session.query(State).filter(State.id == 2)

    for element in state:
        element.name = "New Mexico"

    session.commit()


if __name__ == '__main__':
    model_update()

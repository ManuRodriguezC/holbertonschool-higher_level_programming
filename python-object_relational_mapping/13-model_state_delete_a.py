#!/usr/bin/python3
"""This module contein and print all elemets of the class"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_delete():
    """This method delete all elemets that contain letter a in the name"""
    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir, pool_pre_ping=True)

    Session = sessionmaker(engine)
    conect = engine.connect()
    session = Session(bind=conect)

    state = session.query(State).filter(State.name.like('%a%'))

    for elements in state:
        session.delete(elements)
    session.commit()
    session.close()


if __name__ == '__main__':
    model_state_delete()

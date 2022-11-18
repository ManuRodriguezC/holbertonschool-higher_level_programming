#!/usr/bin/python3
"""This module contein and print all elemets of the class"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_insert():
    """ This method add a object state to the basedata"""
    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir, pool_pre_ping=True)

    Session = sessionmaker(engine)
    conect = engine.connect()
    session = Session(bind=conect)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == '__main__':
    model_state_insert()

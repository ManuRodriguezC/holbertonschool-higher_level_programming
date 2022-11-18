#!/usr/bin/python3
"""This module contein and print all elemets of the class"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def model_state_my_get():
    """
    This method print the id of the state,
    in the case of not found print Not found
    """
    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir, pool_pre_ping=True)
    Session = sessionmaker(engine)
    state = Session().query(State).order_by(State.id).filter(State.name == argv[4])
    
    for elemet in state:
        print(elemet.id)
        return
    print("Not found")


if __name__ == '__main__':
    model_state_my_get()

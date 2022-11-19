#!/usr/bin/python3
"""This module relate two tables in a database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State


def city_fetch_by_state():
    """
    This method print all elemets that contein
    same state.id and cities.state_id
    """
    dir = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])

    engine = create_engine(dir, pool_pre_ping=True)
    Session = sessionmaker(engine)

    sc = Session().query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    for stat, cit in sc:
        print(f"{stat.name}: ({cit.id}) {cit.name}")


if __name__ == '__main__':
    city_fetch_by_state()

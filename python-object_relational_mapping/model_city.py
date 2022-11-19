#!/usr/bin/python3
"""This module create a city class"""
from sqlalchemy import Column, Integer, String, ForeignKey
import model_state
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Created a new class with owner attribues"""
    __tablename__=  "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
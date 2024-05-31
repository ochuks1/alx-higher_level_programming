#!/usr/bin/python3
"""
This file contains the class definition of a State and an instance Base using SQLAlchemy.

State class:
    - Inherits from Base
    - Links to the MySQL table 'states'
    - Has class attributes id (primary key) and name
    - Establishes a relationship with City objects
    - If the State object is deleted, all linked City objects are automatically deleted
    - The reference from a City object to its State should be named 'state'

Usage: import relationship_state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State class definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

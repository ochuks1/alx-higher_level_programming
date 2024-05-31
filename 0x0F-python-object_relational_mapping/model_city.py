#!/usr/bin/python3
"""
This file contains the class definition of a City and an instance Base using SQLAlchemy.

City class:
    - Inherits from Base
    - Links to the MySQL table 'cities'
    - Has class attributes id (primary key), name, and state_id (foreign key)

Usage: import model_city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

class City(Base):
    """City class definition"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

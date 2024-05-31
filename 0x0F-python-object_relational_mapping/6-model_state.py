#!/usr/bin/python3

"""
This script contains the class definition of a State and an instance Base using SQLAlchemy.

State class:
    - Inherits from Base
    - Links to the MySQL table 'states'
    - Has class attributes id (primary key) and name

Usage: ./6-model_state.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

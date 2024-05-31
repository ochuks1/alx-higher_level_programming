#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database `hbtn_0e_6_usa` using SQLAlchemy
and prints the new state's id.

Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, dbname = sys.argv[1:4]

    # Create the engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the new State object “Louisiana”
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id after creation
    print(new_state.id)

    # Close the session
    session.close()

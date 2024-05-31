#!/usr/bin/python3
"""
This script changes the name of the State object with id = 2 to "New Mexico" in the database `hbtn_0e_6_usa` using SQLAlchemy.

Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, dbname = sys.argv[1:4]

    # Create the engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Change the name of the State where id = 2 to "New Mexico"
    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()

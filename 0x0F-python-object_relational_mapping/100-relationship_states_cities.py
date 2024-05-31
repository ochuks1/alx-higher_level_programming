#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco" in the database `hbtn_0e_100_usa` using SQLAlchemy.

Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, dbname = sys.argv[1:4]

    # Create the engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" with the City "San Francisco"
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()

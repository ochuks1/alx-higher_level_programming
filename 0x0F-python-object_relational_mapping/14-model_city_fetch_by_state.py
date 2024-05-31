#!/usr/bin/python3
"""
This script prints all City objects from the database `hbtn_0e_14_usa` using SQLAlchemy.

Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username, password, dbname = sys.argv[1:4]

    # Create the engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)

    # Create a configured "Session" class and a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, sorted by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).one()
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

#!/usr/bin/python3
"""Script to create the State “California” with the City “San Francisco”."""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    addstate = State(name="California")
    addcity = City(name="San Francisco")
    addstate.cities.append(addcity)
    session.add(addstate)
    session.commit()

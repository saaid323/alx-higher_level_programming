#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_city = session.query(State, City)
    state_city = state_city.filter(State.id == City.state_id)
    state_city = state_city.order_by(State.id, City.id).all()
    current_state_id = None
    current_state_name = None
    for state, city in state_city:
        if state.id != current_state_id:
            current_state_id = state.id
            current_state_name = state.name
            print(f"{current_state_id}: {current_state_name}")
        print(f"\t{city.id}: {city.name}")
    session.close()

#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = session.query(State.name, City.id, City.name)
    city = city.filter(State.id == City.state_id)
    for state_name, city_id, city_name in city:
        print(f"{state_name}: ({city_id}) {city_name}")
    session.close()

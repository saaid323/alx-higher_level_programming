#!/usr/bin/python3
"""script that changes the name of a State object from the database
hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    change = session.query(State).get(2)
    change.name = "New Mexico"
    session.commit()
    session.close()

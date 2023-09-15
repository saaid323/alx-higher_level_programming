#!/usr/bin/python3
"""script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    dele = session.query(State).filter(State.name.like('%a%')).all()
    for i in dele:
        session.delete(i)
    session.commit()
    session.close()

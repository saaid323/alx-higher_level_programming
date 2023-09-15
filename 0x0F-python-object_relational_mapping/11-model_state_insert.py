#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    add_name = State(name="Louisiana")
    session.add(add_name)
    session.commit()
    print(add_name.id)
    session.close()

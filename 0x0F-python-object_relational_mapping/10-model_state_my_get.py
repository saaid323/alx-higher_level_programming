#!/usr/bin/python3
"""script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    st_id = session.query(State).filter(State.name == sys.argv[4]).all()
    if st_id:
        for i in st_id:
            print(i.id)
    else:
        print("Not found")
    session.close()

#!/usr/bin/python3
"""
List all the State Object from the database
hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import session, sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State()
    state.name = "Louisiana"
    session.add(state)
    session.commit()
    session.close()

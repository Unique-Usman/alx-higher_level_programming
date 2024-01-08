#!/usr/bin/python3
"""
List all the State Object from the database
hbtn_0e_6_usa
"""
import sys
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import session, sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = (
        session.query(City.id, City.name, State.name)
        .outerjoin(State, State.id == City.state_id)
        .order_by(City.id.asc())
        .all()
        )
    for result in results:
        print(f"{result[2]}: ({result[0]}) {result[1]}")

    # Close the session
    session.close()

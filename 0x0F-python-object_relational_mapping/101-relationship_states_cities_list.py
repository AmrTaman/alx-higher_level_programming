#!/usr/bin/python3

"""
the quries
"""

from relationship_city import City
import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (sys.argv[1], sys.argv[2],
                            sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities):
            print("\t{}: {}".format(city.id, city.name))
    session.close()

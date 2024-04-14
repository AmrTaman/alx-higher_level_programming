#!/usr/bin/python3

"""
queries and sqlalchemy
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).filter(func.binary(State.name).like('%a%')).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()

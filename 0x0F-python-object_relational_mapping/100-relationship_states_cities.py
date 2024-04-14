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
    cal = State(name="California")
    san = City(name="San Francisco")
    cal.cities.append(san)
    session.add(cal)
    session.commit()
    session.close()

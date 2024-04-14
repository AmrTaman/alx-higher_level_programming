#!/usr/bin/python3

"""
using sqlalchemy to query some data
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                      .format(sys.argv[1], sys.argv[2],
                      sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
new = State(name="Louisiana")
session.add(new)
session.commit()
print(new.id)
session.close()

#!/usr/bin/python3

"""
this module is the mapping declare module
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()


class State(Base):
    """
    define a sqlalchemy for a db class state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", back_populates="state")

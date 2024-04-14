#!/usr/bin/python3

"""
mapping the City class to the cities table in db
"""


from model_state import Base
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import relationship


class City(Base):
    """
    class mapper
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")

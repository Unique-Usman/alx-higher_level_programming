#!/usr/bin/python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 
"""
Defines a class definition of City which contains state id
of the their respective state
"""
Base = declarative_base()


class City(Base):
    """
    State class
    """
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("states.id"), cascade = "allvdelete delete-orpahn")















































































                      )

#!/usr/bin/python3
"""Print a class city that inherits from BaseModel"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class City(BaseModel):
    """Class attributes."""
     __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")

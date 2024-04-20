#!/usr/bin/python3
"""Print a class Review that inherits from BaseModel."""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


class Review(BaseModel):
    """class attributes."""
     __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

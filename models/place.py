#!/usr/bin/python3
"""Defines place class"""
import models
from os import getenv
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Add or replace in the class"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """class attribute reviews"""
            vr = models.storage.all()
            lst = []
            rslt = []
            for ky in vr:
                review = ky.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lst.append(vr[ky])
            for elmn in lst:
                if (elmn.place_id == self.id):
                    rslt.append(elmn)
            return (rslt)

        @property
        def amenities(self):
            """ class attribute amenity """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Amenity to attribute"""
            if obj is not None and isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

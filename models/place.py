#!/usr/bin/python3
""" The place class for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """The class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: str of description
        number_rooms: num of room(int)
        number_bathrooms: num of bathroom(int)
        max_guest: maximum guest(int)
        price_by_night:: price for night(int)
        latitude: latitude(flaot)
        longitude: longitude(float)
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey("cities.id", ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place')
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:
        @property
        def reviews(self):
            """Reviews relationship with Places"""
            list_of_reviews = []
            for key, val in models.storage.items():
                if type(val).__name__ == "Review":
                    if val.place_id == self.id:
                        list_of_reviews.append(val)
            return (list_of_reviews)

        @property
        def amenities(self):
            """ Returns the list of amenities """
            temp = []
            for id in self.amenity_ids:
                key = 'Amenity.{}'.format(id)
                if key in models.storage.all().keys():
                    temp.append(models.storage.all()[key])
            return temp

        @amenities.setter
        def amenities(self, obj=None):
            if obj and type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)

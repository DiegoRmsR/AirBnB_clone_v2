#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import amenity_link

class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if 'HBNB_TYPE_STORAGE' in environ and environ ['HBNB_TYPE_STORAGE'] ==
    'db':
        place_amenities = relationship('Place', secondary='amenity_link',
                                       back_populates='amenities')

#!/usr/bin/python3
"""Module contains a Place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel
    Public class attributes:
        city_id: string - City id
        user_id: string - User id
        name: string - Place name
        description: string - Place description
        number_rooms: integer - Number of rooms
        number_bathrooms: integer - Number of bathrooms
        max_guest: integer - Max number of guests
        price_by_night: integer - Price by night
        latitude: float - Place latitude
        longitude: float - Place longitude
        amenity_ids: list of string - Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

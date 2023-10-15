#!/usr/bin/python3
"""Module contains a Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel
    Public class attributes:
        name: string - Amenity name
    """
    name = ""

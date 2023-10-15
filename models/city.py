#!/usr/bin/python3
"""Module contains a City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel
    Public class attributes:
        state_id: string - State id
        name: string - City name
    """
    state_id = ""
    name = ""

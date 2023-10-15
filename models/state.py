#!/usr/bin/python3
"""Module contains a State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel
    Public class attributes:
        name: string - state name
    """
    name = ""

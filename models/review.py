#!/usr/bin/python3
"""Module contains a Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel
    Public class attributes:
        place_id: string - Place id
        user_id: string - User id
        text: string - Review text
    """
    place_id = ""
    user_id = ""
    text = ""

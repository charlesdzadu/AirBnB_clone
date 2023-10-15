#!/usr/bin/python3
"""Module contains a User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    Public class attributes:
        email: string - user email
        password: string - user password
        first_name: string - user first name
        last_name: string - user last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

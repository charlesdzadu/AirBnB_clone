#!/usr/bin/python3
""" Module contains a base model class in wich
any other subclasses will inherit from.
"""

from datetime import datetime
from uuid import uuid4
from models.engine.file_storage import FileStorage


class BaseModel:
    """ A  Base Model class from wich
    any subclass will inherit from.
    """

    def __init__(self, *args, **kwargs):
        """ Initializes the base model class. """

        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    tmp_dtime = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, tmp_dtime)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            FileStorage().new(self)

    def save(self):
        """
        Updates the updated_at attribute
        with the current datetime.
        """

        self.updated_at = datetime.now()
        FileStorage().save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """

        tmp_dict = {}
        tmp_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                tmp_dict[key] = value.isoformat()
            else:
                tmp_dict[key] = value
        return dict(tmp_dict)

    def __str__(self):
        """
        String representation of the instance.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__
        )

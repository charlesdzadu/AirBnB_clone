#!/usr/bin/python3
"""
File Storage Module for Json Serialization and Storage
persistance.
"""

import json
import os


class FileStorage:
    """
    File Storage custom class contains methods and attributes to handle
    data persistance between sessions. It perfom adding and retrieve data from
    json files.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary with all objects. """
        return FileStorage.__objects

    def new(self, obj):
        """
        Create a new dictionary that have to be added to __objects
        Args:
            obj: The object to be added to the dictionary.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Add a new object to storage file (JSON file)
        """

        tmp_dict = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            for key, value in FileStorage.__objects.items():
                tmp_dict[key] = value.to_dict()
            json.dump(tmp_dict, f)

    def class_map(self):
        """
        Returns a dictionary with the class names and the class objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        cls_map = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        return cls_map

    def reload(self):
        """
        Read JSON file and recreate objects and add to __objects
        If the file doesnt exist, do nothing.
        """

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                tmp_dict = json.loads(f.read())
                for objs in tmp_dict.values():
                    cls_key = objs["__class__"]
                    cls_name = self.class_map()[cls_key]
                    self.new(cls_name(**objs))
        except FileNotFoundError:
            pass

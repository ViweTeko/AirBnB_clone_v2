#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON formatas an engine

    Attributes:
            __file_path: Name of file objects are saved in
            __objects: Dictionary of instantiated objects
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.

        Returns a dictionary of type objects if cls specified
        """
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            dict_cls = {}
            for a, b in self.__objects.items():
                if type(b) == cls:
                    dict_cls[a] = b
                return dict_cls
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        here = {x: self.__objects[x].to_dict() for x in self.__objects.keys()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(here, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for key in json.load(f).values():
                    name = key['__class__']
                    del key['__class__']
                    self.new(eval(name)(**key))
        except FileNotFoundError:
            pass

    def close(self):
        """Closes an object"""
        self.reload()

    def delete(self, obj=None):
        """Deletes a given __objects if it exists"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

#!/usr/bin/python3
"""
The 'file_storage' module
Defines the class 'FileStorage' that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class definition """
    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "State": State, "City": City, "Amenity": Amenity,
               "Review": Review}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[k] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        my_dict = {}
        for key in FileStorage.__objects:
            my_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
                for key, val in new_obj.items():
                    obj = self.class_dict[val['__class__']](**val)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

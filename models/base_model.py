#!/usr/bin/python3
"""
The 'base_model' module
Defines the 'BaseModel' class
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ class definition """
    def __init__(self, *args, **kwargs):
        """ Initialize public intstance attr """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns string representation of a class """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute
        'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
        pass

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        _dict = self.__dict__.copy()
        _dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                _dict[k] = v.isoformat()
            else:
                _dict[k] = v
        return _dict

#!/usr/bin/python3
""" module with BaseClass for AirBnB project"""
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """ initialises class """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ returns a string representation of the class """
        clsName = self.__class__.__name__
        return ("[{}] ({}) {} ".format(clsName, self.id, self.__dict__))

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__

        return my_dict

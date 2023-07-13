#!/usr/bin/python3
"""
This module defines the FileStorage class.
"""

import json


class FileStorage:
    """
    The FileStorage class serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: Dictionary of objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the object in __objects with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists).
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    module_name = class_name.lower()
                    module = __import__("models.{}".format(module_name), fromlist=[class_name])
                    class_ = getattr(module, class_name)
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

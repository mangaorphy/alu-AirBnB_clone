#!/usr/bin/python3
import json
import os

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file"""
        """(path: __file_path) exists ; otherwise, do nothing."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                json_obj = json.load(json_file)
                for key in json_obj.keys():

                    # By providing the dict value stored in json_obj[key] as
                    # kwargs, genrate an object with the same attributes
                    self.__objects[key] = eval(
                        json_obj[key]['__class__'])(**json_obj[key])
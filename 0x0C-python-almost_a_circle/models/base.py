#!/usr/bin/python3
""" Module that contains class Base """
from json import dumps, loads
from os import path
from models.rectangle import Rectangle
from models.square import Square


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' that writes the JSON string'''
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''return list of the JSON string representation'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def load_from_file(cls):
        '''that returns the list of the JSON string representation'''
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new_one = Rectangle(1, 1)
        elif cls is Square:
            new_one = Square(1)
        else:
            new_one = None
        new_one.update(**dictionary)
        return new_one

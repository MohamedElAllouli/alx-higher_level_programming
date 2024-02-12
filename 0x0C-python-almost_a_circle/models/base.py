#!/usr/bin/python3
""" Module that contains class Base """
from json import dumps, loads
import os.path


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

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        namefile = "{}.csv".format(cls.__name__)

        if os.path.exists(namefile) is False:
            return []

        with open(namefile, 'r') as readF:
            reader = csv.reader(readF)
            csvlist = list(reader)

        if cls.__name__ == "Rectangle":
            listofkeys = ['id', 'width', 'height', 'x', 'y']
        else:
            listofkeys = ['id', 'size', 'x', 'y']

        mat = []

        for csvofelem in csvlist:
            dictofcsv = {}
            for kv in enumerate(csvofelem):
                dictofcsv[listofkeys[kv[0]]] = int(kv[1])
            mat.append(dict_csv)

        listofins = []

        for index in range(len(matr)):
            listofins.append(cls.create(**mat[index]))

        return listofins

#!/usr/bin/python3
""" class Student"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        """Sets the necessary attributes for the Student object
        Args:
        first_name (str): first name of the student.
        last_name (str): last name of the student.
        age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """etrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)

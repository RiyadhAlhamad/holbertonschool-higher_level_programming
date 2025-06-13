#!/usr/bin/python3
"""
Module that contains class student
"""


class Student:
    """class student

    Args:
        first_name: first name of student
        last_name: last name of studen
        age: the age of studen
    """

    def __init__(self, first_name, last_name, age):
        """Instantiation method for first, last and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance
        return:
            self.__dict
            or
            result
        """
        if attrs is None:
            return self.__dict__
        result = {}

        for attr_name in attrs:
            if attr_name == "first_name":
                result["first_name"] = self.first_name
            elif attr_name == "last_name":
                result["last_name"] = self.last_name
            elif attr_name == "age":
                result["age"] = self.age
        return result

#!/usr/bin/python3
"""
Module that contains class_to_json function
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

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance
        return:
            self.__dict"""
        return self.__dict__

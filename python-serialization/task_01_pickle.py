#!/usr/bin/env python3
"""Custom class serialization using pickle module"""
import pickle


class CustomObject:
    """Custom class for demonstrating pickle serialization"""

    def __init__(self, name, age, is_student):
        """
        Initialize CustomObject instance

        Args:
            name (str): name of the person
            age (int): age of the person
            is_student (bool): whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in the specified format
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file

        Args:
            filename (str): name of the file to save the serialized object
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return the instance

        Args:
            filename (str): name of the file to load the object from

        Returns:
            CustomObject: deserialized instance or None if error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None

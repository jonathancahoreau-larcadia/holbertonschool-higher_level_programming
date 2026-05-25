#!/usr/bin/env python3
"""Serialize and deserialize Python objects using pickle.

This module defines a simple custom object type that can be saved to a
binary file and restored from it using Python's pickle module.
"""

import pickle


class CustomObject:
    """A simple object with serialization support."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age value.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes to standard output."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a binary file.

        Args:
            filename (str): The file path where the object will be stored.

        Returns:
            None: Returns None on failure.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load a pickled object from a binary file.

        Args:
            filename (str): The file path from which to load the object.

        Returns:
            CustomObject | None: The deserialized object, or None on failure.
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None

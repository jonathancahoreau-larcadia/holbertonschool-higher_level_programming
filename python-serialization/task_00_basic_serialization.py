#!/usr/bin/env python3
"""Serialize Python data to JSON and read it back from a file.

This module provides helpers for writing Python objects to a file as JSON
and loading them back using the built-in json module.
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to a file.

    Args:
        data: The Python data structure to serialize.
        filename (str): The path of the file to write.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it to Python objects.

    Args:
        filename (str): The path of the file to read.

    Returns:
        The Python object represented by the JSON data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

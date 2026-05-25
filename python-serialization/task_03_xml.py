#!/usr/bin/env python3
"""Serialize and deserialize Python dictionaries to XML files.

This module provides a simple XML serializer and deserializer for a
flat dictionary of string-convertible values.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The data to serialize. Keys become XML element tags.
        filename (str): The path of the XML file to write.
    """

    root = ET.Element("data.xml")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary.

    Args:
        filename (str): The path of the XML file to read.

    Returns:
        dict: The deserialized dictionary with string values.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary

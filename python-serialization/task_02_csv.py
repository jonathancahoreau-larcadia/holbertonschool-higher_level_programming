#!/usr/bin/env python3
"""Convert CSV data to JSON and save it to a file.

This module provides a helper function to read a CSV file, convert its
rows to a list of dictionaries, and write the resulting data as JSON to
`data.json` using UTF-8 encoding.
"""

import csv
import json


def convert_csv_to_json(filename):
    """Read a CSV file and write its contents to `data.json` as JSON.

    Args:
        filename (str): Path to the source CSV file.

    Returns:
        bool: True on success, False if the source file was not found.
    """
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False

"""Utilities for generating personalized invitation files.

This module provides a helper function to render a text template
for a list of attendees and write each rendered invitation to a
separate output file named ``output_N.txt``.

Functions
---------
generate_invitations(template, attendees)
    Generate a personalized invitation file for each attendee.
"""
import os


def generate_invitations(template, attendees):
    """Generate a personalized invitation file for each attendee."""

    if not isinstance(template, str):
        print("Invalid template type: expected str.")
        return

    if not isinstance(attendees, list):
        print("Invalid attendees type: expected list.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Invalid attendee type: expected dict.")
            return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if attendees == []:
        print("No data provided, no output files generated.")
        return

    n = 1

    for attendee in attendees:
        try:
            while os.path.exists(f"output_{n}.txt"):
                n += 1
        except OSError:
            print("Error checking existing files")
            return

        temp_template = template

        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        temp_template = temp_template.replace("{name}", str(name))
        temp_template = temp_template.replace(
            "{event_title}",
            str(event_title)
        )
        temp_template = temp_template.replace(
            "{event_date}",
            str(event_date)
        )
        temp_template = temp_template.replace(
            "{event_location}",
            str(event_location)
        )
        try:
            with open(
                f"output_{n}.txt",
                "w",
                encoding="utf-8"
            ) as file:
                file.write(temp_template)
        except OSError:
            print(f"output_{n}.txt n'a pas  été créé.")
            return
        n += 1

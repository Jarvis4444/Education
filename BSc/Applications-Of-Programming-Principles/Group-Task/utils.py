"""
Module that contains functions used by other modules in route planning.

'time_to_datetime' parses a string object to a datetime object
'load_prev_plan_spec' loads basic details of a planned journey from a file.

Exceptions:
    :raises ValueError: Time is incorrect format.
    :raises ValueError: Line from file is missing data.
    :raises OSError: System-related error - unable to find/access/read file.
    :raises IndexError: Sequence subscript is out of range.
    :raises ValueError: Invalid data read from the file.
"""
from datetime import datetime  # Standard module for using dates and times


def time_to_datetime(time):
    """Tries to parse string to datetime, with format YYYY/MM/DD HH:MM"""
    try:
        date = datetime.strptime(time, '%Y/%m/%d %H:%M')
        return date
    except ValueError:
        raise ValueError('The time must have the format YYYY/MM/DD HH:MM')


def load_prev_plan_spec(filepath):
    """
    Attempt to read journey plan data from a given file into a tuple:
        -Create empty list, "details".
        -Populate "details" with one line read from the file per element.
        -Check validity of arrival time, positioned at the 3rd element.
        -Create tuple, "journey", using elements from "details".
    If any exception is raised:
        set journey to a tuple containing 3 elements, all set to equal "None".

    :param filepath: The given filepath where the journey is stored.
    :return journey: A tuple detailing a journey plan: (to, from, arrival).
    """
    try:
        details = []
        with open(filepath) as file:
            for count, line in enumerate(file):
                if line == "\n":
                    raise ValueError('This line is missing data.')
                else:
                    details.append(line.rstrip("\n"))
        file.close()
        time_to_datetime(details[2])
        journey = (details[0], details[1], details[2])
        return journey
    except (OSError, IndexError, ValueError):
        journey = (None, None, None)
        return journey

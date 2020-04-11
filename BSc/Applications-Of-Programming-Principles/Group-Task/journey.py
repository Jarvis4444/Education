"""
This module creates Journey objects.

Classes:
    Journey: Manages data associated with a journey between two travel points.

Raises:
    :exception ValueError: Journey duration equals nil, or is negative.
"""
from utils import time_to_datetime  # function for parsing string to datetime


class Journey:
    """Creates an object detailing locations by name and valid journey time."""
    def __init__(self, start_location, end_location):
        """
        The constructor for the Journey class.

        Parameters:
            :param start_location: tuple (str,str) name and departure time
            :param end_location: tuple (str,str) name and arrival time
        """
        self._start_location = start_location
        self._end_location = end_location
        # Checks if end_time is after start_time
        self.is_journey_valid_duration()

    # Starting location name
    @property
    def start_place(self):
        start_place = self._start_location[0]
        return start_place

    # Starting location departure time, Format: YYYY/DD/MM HH:MM
    @property
    def start_time(self):
        start_time = self._start_location[1]
        return start_time

    # Destination location name
    @property
    def end_place(self):
        end_place = self._end_location[0]
        return end_place

    # Destination arrival time, Format: YYYY/DD/MM HH:MM
    @property
    def end_time(self):
        end_time = self._end_location[1]
        return end_time

    # Stores duration of a journey in seconds
    @property
    def journey_duration_seconds(self):
        journey_duration_seconds = (
            time_to_datetime(self.end_time) -
            time_to_datetime(self.start_time)).seconds
        return journey_duration_seconds

    def is_journey_valid_duration(self):
        """Checks journey duration is greater than zero."""
        if self.journey_duration_seconds <= 0:
            raise ValueError("Journey must end after the start time")

    def time(self):
        """
        :return journey_time_hh_mm: tuple (int, int) of journey duration
        """
        journey_time_hh_mm = (self.journey_duration_seconds//3600,
                              (self.journey_duration_seconds//60) % 60)
        return journey_time_hh_mm

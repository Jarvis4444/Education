"""
This module creates TravelPoint objects.

Classes:
    TravelPoint: TravelPoint stores data on name, departure and arrival times.

Raises:
    :exception ValueError: No date arguments passed in.
    :exception ValueError: Date argument is not format: 'YYYY/MM/DD HH:MM'
"""
from utils import time_to_datetime  # function for parsing string to datetime


class TravelPoint:
    """This class creates an object with valid data about a travel location."""

    def __init__(self, location_name, departure_time=None, arrival_time=None):
        """
        The constructor for TravelPoint class.

        Parameters:
            :param location_name: (str) A location's name.
            :param departure_time: (str) A location's departure time.
            :param arrival_time: (str) A location's arrival time.
        """
        self._location_name = location_name
        self._departure_time = departure_time
        self._arrival_time = arrival_time

        # Checks if time arguments match format: "YYYY/MM/DD HH:MM"
        self.check_departure_time()
        self.check_arrival_time()

        # Checks for at least one departure or arrival time.
        self.check_at_least_one_date()

    # Starting location
    @property
    def location(self):
        return self._location_name

    # Departure time
    @property
    def departure_time(self):
        return self._departure_time

    # Arrival time
    @property
    def arrival_time(self):
        return self._arrival_time

    def check_departure_time(self):
        """Checks format of departure time"""
        if self._departure_time is not None:
            try:
                time_to_datetime(self._departure_time)
            except ValueError:
                raise ValueError(
                    "The departure_time must have the format YYYY/MM/DD HH:MM")

    def check_arrival_time(self):
        """Checks format of arrival time"""
        if self._arrival_time is not None:
            try:
                time_to_datetime(self._arrival_time)
            except ValueError:
                raise ValueError(
                    "The arrival_time must have the format YYYY/MM/DD HH:MM")

    def check_at_least_one_date(self):
        """Checks there is at least one date argument for TravelPoint"""
        if self._departure_time is None and self._arrival_time is None:
            raise ValueError(
                "At least one of arrival or departure time must be set")

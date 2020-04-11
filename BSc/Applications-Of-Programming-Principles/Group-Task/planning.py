"""
A module that creates a class called JourneyOptions.

Classes:
    JourneyOptions: stores different journeys and compares their times.
"""
from operator import itemgetter  # Callable object that fetches items
from utils import time_to_datetime  # function for parsing string to datetime


class JourneyOptions:
    """
    This class creates an object of journeys and alternative journeys.
    It sorts these journeys to determine shortest and longest routes.
    """
    def __init__(self, journey, alternatives=None):
        """The constructor for the JourneyOptions class.

        Parameters:
            :param journey: Contains travel tuples and journey duration
            :param alternatives: Tuple of journey objects
        """
        self.default = journey
        self.alt_journeys = alternatives

    @property
    def sort_journeys(self):
        """
        Function to sort journey objects by earliest arrival.

        Create and populate list, unsorted_journeys, with tuples.
        The tuples are pairs of all journey objects and their arrival datetime.
        Create variable, sorted_journeys, and store sorted list in variable.

        :return sorted_journeys: sorted list by earliest arrival.
        """
        unsorted_journeys = [
            (self.default, time_to_datetime(self.default.time()))]

        for journey in self.alt_journeys:
            unsorted_journeys.append(
                (journey, time_to_datetime(journey.time())))

        sorted_journeys = sorted(unsorted_journeys, key=itemgetter(1))
        return sorted_journeys

    def earliest_arrival(self):
        """
        Function to return earliest journey object.

        If there are alternative journeys:
            Set the variable, "earliest_journey", to the first
            element of the first tuple from a list which is returned
            by calling the method "sort_journeys".
        Otherwise:
            set variable "earliest_journey" to the default journey.

        :return earliest_journey: Earliest journey object.
        """
        if self.alt_journeys is not None:
            earliest_journey = self.sort_journeys[0][0]
        else:
            earliest_journey = self.default
        return earliest_journey

    def latest_arrival(self):
        """
        Function to return earliest journey object.

        If there are alternative journeys:
            Set the variable, "latest_journey", to the first
            element of the last tuple from a list which is returned
            by calling the method "sort_journeys".
        Otherwise:
            set variable "latest_journey" to the default journey.

        :return latest_journey: Latest journey object.
        """
        if self.alt_journeys is not None:
            latest_journey = self.sort_journeys[
                self.sort_journeys.__len__()-1][0]
        else:
            latest_journey = self.default
        return latest_journey

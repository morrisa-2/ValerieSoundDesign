"""
A collection of note durations, listed in order of playback.
"""

from src.main.Python.Controllers.DBConnection import DBConnection

class Rhythm:

    def __init__(self, intentName:str, durations:list[float]):
        """
        Non-default constructor.
        :param intentName: Name of the intent to which this rhythm is
        primarily applied. Note that this does not exclude it from being
        selected by variations of a different intent, only that it is more
        likely to be selected by a variation of the given intent. Must be
        the name of an existing intent in the database.
        :param durations: Optional list of note durations. Each
        element in the list must be numeric and can be a maximum
        of five notes long.
        """
        if not DBConnection.validateIntent(intentName):
            raise Exception("Unrecognized Intent name.")
        else:
            self.intentName = intentName
            length = len(durations)
            if length == 0:
                raise Exception("Durations parameter must contain at least one value.")
            elif not isinstance(durations,list):
                raise TypeError("Durations parameter must be a list.")
            elif len(durations) > 5:
                raise Exception("Durations parameter must be at most five values long.")
            else:
                isNum = [isinstance(element,(float,int,complex)) for element in durations]
                if False in isNum:
                    raise TypeError("Durations parameter must be a list of numeric values.")
                else:
                    durations = tuple([float(num) for num in durations])
                    self.durations = durations

    def __str__(self):
        return " ".join([str(dur) for dur in self.durations])

    def __len__(self):
        return len(self.durations)

    def __eq__(self, other):
        if not isinstance(other, Rhythm):
            return False
        else:
            return self.durations == other.getDurations()

    def getDurations(self):
        """
        :return: Durations of this rhythm as a tuple of floats.
        """
        return self.durations

    def getIntentName(self):
        """
        :return: Name of the intent to which this rhythm belongs
        as a string.
        """
        return self.intentName

    def positionOf(self, duration:float):
        """
        Gets the position of the given duration.
        :param duration: Duration to get the position of.
        :return: Position of the given duration
        """
        if not isinstance(duration,(float,int,complex)):
            raise TypeError("Duration must be a numeric value.")
        else:
            return self.durations.index(duration)

    def getAt(self, position:int):
        """
        Gets the duration at the given position.
        :param position: Position to get the duration at.
        :return: Duration at the given position.
        """
        return self.durations[position]
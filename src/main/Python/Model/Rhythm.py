"""
A collection of note durations, listed in order of playback.
"""

class Rhythm:

    def __init__(self, durations=None):
        """
        Non-default constructor.
        :param durations: Optional list of note durations. Each
        element in the list must be numeric and can be a maximum
        of five notes long.
        """
        if durations is None:
            self.durations = []
        elif not isinstance(durations,list):
            raise TypeError("Durations parameter must be a list.")
        elif len(durations) > 5:
            raise Exception("Durations must be at most 5 notes long.")
        else:
            isNum = [isinstance(element,(float,int,complex)) for element in durations]
            if False in isNum:
                raise TypeError("Durations must be a list of numeric values.")
            else:
                durations = [float(num) for num in durations]
                self.durations = durations

    def __str__(self):
        return " ".join([str(dur) for dur in self.durations])

    def __len__(self):
        return len(self.durations)

    def add(self, duration, position=None):
        """
        Adds the given duration to the given position in the rhythm,
        or to the end of the rhythm if there is no argument given.
        :param duration: Note duration to add.
        :param position: Position to add the given note duration at.
        """
        if position is None:
            position = len(self.durations)

        if not isinstance(duration,(float,int,complex)):
            raise TypeError("Duration must be a numeric value.")
        else:
            self.durations.insert(position,float(duration))

    def remove(self, duration):
        """
        Removes the first instance of the given duration from this rhythm.
        Raises a ValueError if the given duration is not in this rhythm.
        :param duration: Duration to remove.
        """
        if not isinstance(duration,(float,int,complex)):
            raise TypeError("Duration must be a numeric value.")
        else:
            self.durations.remove(duration)

    def removeAt(self, position=-1):
        """
        Removes the duration at the given position in this rhythm.
        If no position argument is given, removes the last duration.
        :param position: Position to remove a duration from.
        """
        self.durations.pop(position)

    def positionOf(self, duration):
        """
        Gets the position of the given duration.
        :param duration: Duration to get the position of.
        :return: Position of the given duration
        """
        if not isinstance(duration,(float,int,complex)):
            raise TypeError("Duration must be a numeric value.")
        else:
            return self.durations.index(duration)

    def getAt(self, position):
        """
        Gets the duration at the given position.
        :param position: Position to get the duration at.
        :return: Duration at the given position.
        """
        return self.durations[position]
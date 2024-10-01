"""
Hard-coding intent info before the DB is functional
"""

from src.main.Python.Model.Pitch import Pitch
from src.main.Python.Model.Contour import Contour
from src.main.Python.Model.Rhythm import Rhythm
from src.main.Python.Model.Modality import Modes, Modality
import src.main.Python.Model.ValConstants as vc

class Alert:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "Alert"
        toReturn["CentralPitch"] = Pitch("F#",7)
        toReturn["PitchRange"] = 11
        toReturn["Mode"] = Modes.LYDIAN
        toReturn["Contour"] = Contour.DESCENDING
        toReturn["Tempo"] = vc.FAST
        toReturn["Key"] = "C"
        toReturn["Interval"] = vc.TRI
        durations = [2,2]
        toReturn["Rhythm"] = Rhythm("Alert",durations)
        return toReturn


class Goodbye:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "Goodbye"
        toReturn["CentralPitch"] = Pitch("F#", 5)
        toReturn["PitchRange"] = 8
        toReturn["Mode"] = Modes.IONIAN
        toReturn["Contour"] = Contour.DESCENDING
        toReturn["Tempo"] = vc.SLOW
        toReturn["Key"] = "D"
        toReturn["Interval"] = vc.P4
        durations = [0.5, 2]
        toReturn["Rhythm"] = Rhythm("Goodbye", durations)
        return toReturn

class Hello:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "Hello"
        toReturn["CentralPitch"] = Pitch("D", 5)
        toReturn["PitchRange"] = 9
        toReturn["Mode"] = Modes.IONIAN
        toReturn["Contour"] = Contour.NO_PRIORITY
        toReturn["Tempo"] = vc.FAST
        toReturn["Key"] = "D"
        toReturn["Interval"] = vc.MAJ3RD
        durations = [1, 2]
        toReturn["Rhythm"] = Rhythm("Hello", durations)
        return toReturn

class No:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "No"
        toReturn["CentralPitch"] = Pitch("F#", 5)
        toReturn["PitchRange"] = 7
        toReturn["Mode"] = Modes.AEOLIAN
        toReturn["Contour"] = Contour.DESCENDING
        toReturn["Tempo"] = vc.FAST
        toReturn["Key"] = "C"
        toReturn["Interval"] = vc.MIN2ND
        durations = [0.5, 1]
        toReturn["Rhythm"] = Rhythm("No", durations)
        return toReturn

class Query:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "Query"
        toReturn["CentralPitch"] = Pitch("C#", 5)
        toReturn["PitchRange"] = 9
        toReturn["Mode"] = Modes.AEOLIAN
        toReturn["Contour"] = Contour.ASCENDING
        toReturn["Tempo"] = vc.MODERATE
        toReturn["Key"] = "E"
        toReturn["Interval"] = vc.MAJ2ND
        durations = [0.5, 1]
        toReturn["Rhythm"] = Rhythm("Query", durations)
        return toReturn

class ThankYou:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "Query"
        toReturn["CentralPitch"] = Pitch("A#", 5)
        toReturn["PitchRange"] = 9
        toReturn["Mode"] = Modes.IONIAN
        toReturn["Contour"] = Contour.DESCENDING
        toReturn["Tempo"] = vc.SLOW
        toReturn["Key"] = "A#"
        toReturn["Interval"] = vc.MAJ2ND
        durations = [1, 0.5, 1]
        toReturn["Rhythm"] = Rhythm("ThankYou", durations)
        return toReturn

class Unsure:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "Unsure"
        toReturn["CentralPitch"] = Pitch("C#", 5)
        toReturn["PitchRange"] = 9
        toReturn["Mode"] = Modes.AEOLIAN
        toReturn["Contour"] = Contour.NO_PRIORITY
        toReturn["Tempo"] = vc.MODERATE
        toReturn["Key"] = "F"
        toReturn["Interval"] = vc.MIN3RD
        durations = [0.5, 0.5, 2]
        toReturn["Rhythm"] = Rhythm("Unsure", durations)
        return toReturn

class Yes:

    def getParams(self):
        """
        Gets parameters for the intent of this type
        :return: A dictionary whose pairs are intent parameters and their
        respective values.
        """
        toReturn = {}
        toReturn["Name"] = "Yes"
        toReturn["CentralPitch"] = Pitch("G", 5)
        toReturn["PitchRange"] = 5
        toReturn["Mode"] = Modes.IONIAN
        toReturn["Contour"] = Contour.ASCENDING
        toReturn["Tempo"] = vc.FAST
        toReturn["Key"] = "G"
        toReturn["Interval"] = vc.P4
        durations = [0.5, 1]
        toReturn["Rhythm"] = Rhythm("Yes", durations)
        return toReturn
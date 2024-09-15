"""
Module which takes in an Intent and produces semi-random Variations based on
the parameters of that intent.

Invariant:
 -  The desired Intent is passed in upon construction, and can be set afterward.
 -  The "clock" instance variable keeps track of tempo for each intent.
 -  The "connection" instance variable
 -  Any number of variations can be produced for each intent through the generate() function.
"""
from src.main.Python.Model.Variation import Variation
from src.main.Python.Controllers import SCConnection
from src.main.Python.Model.Intent import Intent

class VariationGen:
    def __init__(self,intent):
        self.intent = intent
        self.connection = SCConnection.SCConnection()

    def setIntent(self,intent):
        """
        Changes this VariationGen's intent to the
        given Intent object.
        :param intent: Intent to produce variations of.
        """
        if not (isinstance(intent,Intent)):
            raise TypeError("Intent argument must be an Intent object.")
        else:
            self.intent = intent

    def _generate(self,ordinal,filepath):
        """
        Generates a single variation of this intent
        as a wav file, saved to the given directory and
        labeled with the given ordinal number.
        :param ordinal: Whole number which signifies the
        order of generation.
        :param filepath: Path to the directory in
        which to store the generated wav file.
        """
        var = Variation(self.intent)
        self.connection.exportVariation(var,ordinal,filepath)

    def generate(self,numberToGen,filepath):
        """
        Generates the specified number of variations to the
        given filepath as wav files.
        :param numberToGen: Number of variations to generate.
        :param filepath: Path to the directory in
        which to store the generated wav files.
        """
        # TODO: Check validity of filepath
        for i in range(numberToGen):
            self._generate(i,filepath)
    def __str__(self):
        """
        Returns a string representation of this
        VariationGen.
        :return: A string representing this VariationGen.
        Ex. "VarGen: MyVarGen (Intent)"
        """
        return "VarGen: " + self.__name__ + " (" + str(self.intent) + ")"

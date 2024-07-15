"""
Module which takes in an Intent and produces semi-random Variations based on
the parameters of that intent.

Invariant:
 -  The desired Intent is passed in upon construction, and can be set afterward.
 -  Any number of variations can be produced for each intent through the generate() function.
"""
import src.main.Variation as Variation

class VariationGen:
    def __init__(self,intent):
        # TODO: Check whether intent is valid.
        self.intent = intent

    def generate(self):
        var = Variation.Variation(self.intent)


    def __str__(self):
        """
        Returns a string representation of this
        VariationGen.
        :return: A string representing this VariationGen.
        Ex. "VarGen: MyVarGen (Intent)"
        """
        return "VarGen: " + self.__name__ + " (" + self.intent.__class__.__name__ + ")"

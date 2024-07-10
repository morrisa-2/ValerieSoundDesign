"""
Module which takes in an Intent and produces semi-random Variations based on
the parameters of that intent.

Invariant:
 -  The desired Intent is passed in upon construction, and can be set afterward.
 -  Any number of variations can be produced for each intent through the generate() function.
"""


class VariationGen:
    def __init__(self,intent):
        if (intent is type(src.main.Intents.Intent)):
            self.intent = intent
        else:
            self.intent = src.main.Intents.Intent

    def generate(self):
        pass

    def getIntent(self):
        return self.intent
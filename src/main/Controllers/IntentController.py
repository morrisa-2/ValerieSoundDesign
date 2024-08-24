"""
Handles all events related to the intent scroll window.
Selects intents to generate, adds and removes intents,
sends selected intents to the IntentInfoController and ExportController.
"""

from MainScenesController import MainScenesController

class IntentController:

    # TODO: Implement marked methods in IntentController

    def __init__(self, mainController):
        if not isinstance(mainController, MainScenesController):
            raise TypeError("Please input a MainScenesController object.")
        else:
            self.mainController = mainController

    # IMPLEMENT
    # Needs mouseEvent?
    def selectIntent(self):
        """
        Selects an intent from the list of available intents
        to generate new variations and edit information.
        """

    # IMPLEMENT
    def _sendToExport(self):
        """
        Sends the selected intent to the ExportController.
        """


    # IMPLEMENT
    def _sendToInfo(self):
        """
        Sends the selected intent to the IntentInfoController.
        """


    # IMPLEMENT
    def addIntent(self,name):
        """
        Adds an intent of the given name to the list of
        available intents. Generates a pop-up alert if an
        intent of the given name already exists.
        :param name: Name to add to the list.
        """

    # IMPLEMENT
    def removeIntent(self,name):
        """
        Removes an intent of the given name from the list
        of available intents. Generates a pop-up alert if no
        intent of the given name exists in the list.
        :param name: Name of intent to remove from the list.
        """
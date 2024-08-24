"""
Handles events related to the intent info window.
Gets intent info from the DB, receives signal to display
the selected intent from the IntentController, updates DB
when info is modified, displays error message when
incompatible info is input.
"""

from MainScenesController import MainScenesController

class IntentInfoController:

    # TODO: Implement marked methods in IntentInfoController

    # IMPLEMENT
    def __init__(self, mainController):
        if not isinstance(mainController, MainScenesController):
            raise TypeError("Please input a MainScenesController object.")
        else:
            self.mainController = mainController

    # IMPLEMENT
    def populate(self):
        """
        Fills the info window fields with information about the
        selected intent.
        """

    # IMPLEMENT
    def updateDB(self, fieldModified):
        """
        Updates the database at the modified field with
        the new information that field contains.
        Generates a pop-up alert if the modified field
        contains an invalid input.
        :param fieldModified: Feature to modify in the
        database entry for the selected intent.
        """

    # IMPLEMENT
    def _updateIntent(self, fieldModified):
        """
        Updates the intent table in the database at the
        modified field with the new information that
        field contains. Generates a pop-up alert if there
        is no such feature in the intent table.
        :param fieldModified: Feature to modify in the
        database entry for the selected intent.
        """

    # IMPLEMENT
    def _updateRhythm(self, fieldModified):
        """
        Updates the rhythm table in the database at the
        modified field with the new information that
        field contains. Generates a pop-up alert if there
        is no such feature in the rhythm table.
        :param fieldModified: Feature to modify in the
        database entry for the selected intent's rhythm.
        """
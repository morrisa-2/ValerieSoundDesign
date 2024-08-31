"""
Handles events related to the export window.
Takes in export settings, sends file information to the database,
receives intent name from IntentController, sends
signal to SCConnection to begin recording.
"""

from MainScenesController import MainScenesController

class ExportController:

    # TODO: Implement marked methods in ExportController

    # IMPLEMENT
    def __init__(self, mainController):
        if not isinstance(mainController, MainScenesController):
            raise TypeError("Please input a MainScenesController object.")
        else:
            self.mainController = mainController

    # IMPLEMENT
    # No need for args, comes through fields & IntentController?
    def _sendToDB(self):
        """
        Sends the file currently specified in the export window's
        fields to the database. Generates a pop-up alert if the
        fields are incomplete.
        """

    # IMPLEMENT
    def browseFiles(self):
        """
        Opens a file browser to select a directory to generate
        new audio files at.
        """

    # IMPLEMENT
    def generate(self):
        """
        Generates a single variation on the selected intent as an
        audio file, sending requisite information to the database
        and creating a .wav file at the provided directory.
        """

    # IMPLEMENT
    def generateBatch(self, numberToGen):
        """
        Generates a batch of audio files and inserts them into
        the database.
        :param numberToGen: Number of variations to generate.
        """
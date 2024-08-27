"""
Handles events related to the archive of generated sounds.
Sends file information to the PlaybackController, displays
sounds in order of date and time generated, allows filtering
by intent and favorite.
"""

from MainScenesController import MainScenesController

# TODO: Implement marked methods in ArchiveController

class ArchiveController:

    def __init__(self, mainController):
        """
        Non-default constructor.
        :param mainController: MainScenesController object to
        attach this ArchiveController to.
        """
        if not isinstance(mainController,MainScenesController):
            raise TypeError("Please input a MainScenesController object.")
        else:
            self.mainController = mainController
            self.toDisplay = self.getAllFiles()

    # IMPLEMENT
    def _addFileToDisplay(self, args):
        """
        Adds the file with the given dictionary of specifications to
        the list of files to display in the archive.
        :param args: Dictionary of specifications to add to the
        list of files to display.
        """

    # IMPLEMENT
    def getAllFiles(self):
        """
        Gets a 2D matrix of all the files stored in the database, sorted by
        time of generation.
        :return: A 2D matrix of all the files stored in the database,
        sorted by time of generation.
        """

    # IMPLEMENT
    def filterByIntent(self, intentName):
        """
        Filters the sounds to be displayed by an intent. Generates a pop-up
        alert if the given intent does not exist.
        :param intentName: Name of intent to filter by.
        """

    # TODO: Consider more dynamic rating system
    # IMPLEMENT
    def filterByFavoriteStatus(self, favorite):
        """
        Filters the sounds to be displayed by whether they have been
        favorited or not.
        :param favorite: True if displaying only favorited files,
        False if displaying only unfavorited files.
        """
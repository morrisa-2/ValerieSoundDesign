"""
Handles events related to audio playback.
Receives audio file location to play from ArchiveController,
plays audio files via the Simpleaudio module.
"""

from simpleaudio import WaveObject, PlayObject
from src.main.Python.Controllers.MainScenesController import MainScenesController
from src.main.Python.Controllers.DBConnection import DBConnection

class PlaybackController:

    # TODO: Implement marked methods in PlaybackController

    # IMPLEMENT
    def __init__(self, mainController):
        if not isinstance(mainController, MainScenesController):
            raise TypeError("Please input a MainScenesController object.")
        else:
            self.mainController = mainController

    # IMPLEMENT
    def play(self, mouseEvent):
        """
        Plays the selected audio file when its play button is
        pressed in the archive.
        :param mouseEvent: Does it need this??????
        """
        fileName = DBConnection.
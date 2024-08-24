"""
Handles events related to creating a new intent.
Receives signal to open and generate new window from IntentController,
passes all info input to the DB, signals for the IntentController
to add a new intent to the list.
"""

from MainScenesController import MainScenesController
from DBConnection import DBConnection
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QDialog, QDialogButtonBox
from PyQt6.QtCore import QRegularExpression

class AddIntentDialogController(QDialog):

    # TODO: Implement marked methods of AddIntentDialogController
    # TODO: Add PyQt elements

    noteName = QRegularExpression("^(A|B|C|D|E|F|G)\\^(b|#)")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Intent")

        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept())
        self.buttonBox.rejected.connect(self.reject())

        self.layout = QVBoxLayout()

    # IMPLEMENT
    def setMainController(self, mainController):
        if not isinstance(mainController, MainScenesController):
            raise TypeError("Please input a MainScenesController.")
        else:
            self.mainController = mainController

    # Does this need mouseEvent?
    # IMPLEMENT
    def addNewIntent(self, mouseEvent):
        """
        Adds a new intent to the list of available intents with the
        desired specifications.
        :param mouseEvent:
        :return:
        """

    # IMPLEMENT
    def _addToDB(self):
        """
        Adds the specifications of this intent to the database.
        Raises an alert if there are incomplete fields or if the
        desired parameters are unacceptable.
        """

    # IMPLEMENT
    def _addToList(self):
        """
        Adds the name of this intent to the list of intents.
        Raises an alert if the name of this intent matches one
        that is already listed.
        """
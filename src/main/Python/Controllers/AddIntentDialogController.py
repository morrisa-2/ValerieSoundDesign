"""
Handles events related to creating a new intent.
Receives signal to open and generate new window from IntentController,
passes all info input to the DB, signals for the IntentController
to add a new intent to the list.
"""

from MainScenesController import MainScenesController
from DBConnection import DBConnection
from PyQt6.QtWidgets import QGroupBox, QLabel, QLineEdit, QVBoxLayout, QDialog, QDialogButtonBox
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

class AddIntentDialogController(QDialog):

    # TODO: Implement marked methods of AddIntentDialogController
    # TODO: Add PyQt elements

    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Intent")

        window = QGroupBox()
        self.layout = QVBoxLayout(window)
        self._assignLineEdits(self.layout)
        self._assignComboBoxes(self.layout)
        self._assignButtonBox(self.layout)

    def _assignButtonBox(self, layout):
        """
        Generates and assigns the DialogButtonBox object for this controller.
        :param layout: Layout to apply DialogButtonBox to.
        """
        if not isinstance(layout,QVBoxLayout):
            raise TypeError("Please input a QVboxLayout object.")
        else:
            QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel

            self.buttonBox = QDialogButtonBox(QBtn)
            self.buttonBox.accepted.connect(self.accept())
            self.buttonBox.rejected.connect(self.reject())

            layout.addWidget(self.buttonBox)

    def _assignLineEdits(self, layout):
        """
        Generates and assigns the LineEdit objects for this controller.
        :param layout: Layout to apply LineEdits to.
        """
        if not isinstance(layout,QVBoxLayout):
            raise TypeError("Please input a QVboxLayout object.")
        else:
            self.nameLE = QLineEdit().setPlaceholderText("Name")
            layout.addWidget(self.nameLE)

            # The LineEdits below must have a Validator assigned to them that
            # ensures they only receive correctly formatted input.
            noteNameRegex = QRegularExpression("^(A|B|C|D|E|F|G)\\^(b|#)")
            noteNameValid = QRegularExpressionValidator(noteNameRegex)

            self.noteNameLE = QLineEdit().setPlaceholderText("Central Note Name (Ex. Ab, G#)")
            self.noteNameLE.setValidator(noteNameValid)
            layout.addWidget(self.noteNameLE)

            self.keyCenterLE = QLineEdit().setPlaceholderText("Key (Ex. C, G#)")
            self.keyCenterLE.setValidator(noteNameValid)
            layout.addWidget(self.keyCenterLE)

            self.octaveLE = QLineEdit().setPlaceholderText("Octave")
            # Octave must be single digit, negatives permitted
            self.octaveLE.setInputMask("#")
            layout.addWidget(self.octaveLE)

            self.pitchRangeLE = QLineEdit().setPlaceholderText("Pitch Range")
            # Pitch range can be up to two digits, positive only
            self.pitchRangeLE.setInputMask("09")
            layout.addWidget(self.pitchRangeLE)

            self.tempoLE = QLineEdit().setPlaceholderText("Tempo")
            # Tempo must be at least two digits in length, positive only
            self.tempoLE.setInputMask("099")
            layout.addWidget(self.tempoLE)

            self.intervalLE = QLineEdit().setPlaceholderText("Interval")
            # Interval must be a maximum of two digits, positive non-zero only
            intervalRegex = QRegularExpression("\\d\\d")
            intervalValid = QRegularExpressionValidator(intervalRegex)
            self.intervalLE.setValidator(intervalValid)
            layout.addWidget(self.intervalLE)

    def _assignComboBoxes(self, layout):
        """
        Generates and assigns the ComboBox objects for this controller.
        :param layout: Layout to apply ComboBoxes to.
        """
        self.modalityCB = QLineEdit().setPlaceholderText("Mode")
        self.contourCB = QLineEdit().setPlaceholderText("Contour")

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
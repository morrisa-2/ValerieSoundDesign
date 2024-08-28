"""
Handles all interactions with the SQL database.
"""

from datetime import datetime
import mysql.connector

class DBConnection:

    # TODO: Implement marked methods in DBConnection

    @staticmethod
    def _connect():
        """
        Establishes a connection to the SQL database.
        Raises a ConnectionError if the connection is
        unsuccessful.
        :return: A connection to the database.
        """
        try:
            connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Nziceai4!"
            )
            return connection
        except:
            raise ConnectionError("Cannot connect to the SQL database.")

    @staticmethod
    def _disconnect(connection):
        """
        Attempts to disconnect from the SQL database.
        Raises a RuntimeError if disconnection is unsuccessful.
        """
        if not isinstance(connection, mysql.connector.connection.MySQLConnection):
            raise TypeError("Please input an SQL connection.")
        else:
            try:
                connection.close()
            except:
                raise RuntimeError("Cannot disconnect.")

    @staticmethod
    # IMPLEMENT
    def validateIntent(intentName):
        """
        Checks whether the given intent exists.
        :param intentName: Name of intent to check.
        :return: True if an intent of the given name
        exists in the DB, false otherwise.
        """
        pass

    @staticmethod
    # IMPLEMENT
    def getIntentInfo(intentName):
        """
        Given the name of an intent, returns that intent's
        specifications. Raises a ValueError if the given
        intent does not exist.
        :param intentName: Name of intent to get info of.
        :return: A dictionary of that intent's parameters.
        """
        if not isinstance(intentName,str):
            raise TypeError("Intent name must be a string.")
        else:
            try:
                pass
            except:
                raise ValueError("Cannot get information for the given intent.")

    @staticmethod
    # IMPLEMENT
    def getRhythmByIntent(intentName):
        """
        Gets the rhythm associated with the given intent.
        Raises a ValueError if the given intent does not exist.
        :param intentName: Name of intent to get the rhythm of.
        :return: The rhythm of this intent as a list.
        """
        if not isinstance(intentName, str):
            raise TypeError("Intent name must be a string.")
        else:
            try:
                pass
            except:
                raise ValueError("Cannot get information for the given intent.")

    @staticmethod
    # IMPLEMENT
    def addIntent(args):
        """
        Adds an intent of the given parameters to the DB.
        Raises a ValueError if the given parameters are not
        acceptable. To be accepted, parameters must match
        the desired type of the columns in the DB and
        the name of each intent must be unique.
        :param args: Dictionary of parameters to apply to
        this new intent.
        """
        if not isinstance(args, dict):
            raise TypeError("Arguments must be passed through a dictionary.")
        else:
            try:
                pass
            except:
                raise ValueError("Given parameters are unacceptable.")

    @staticmethod
    # IMPLEMENT
    def addRhythm(args):
        """
        Adds a rhythm of the given parameters to the DB.
        Raises a ValueError if the given parameters are not
        acceptable. To be accepted, parameters must match
        the desired type of the columns in the DB.
        :param args: Dictionary of parameters to store this
        rhythm with.
        """
        if not isinstance(args, dict):
            raise TypeError("Arguments must be passed through a dictionary.")
        else:
            try:
                pass
            except:
                raise ValueError("Given parameters are unacceptable.")

    @staticmethod
    # IMPLEMENT
    def getAllRhythms():
        """
        Gets a dictionary representing all available rhythms from the DB.
        :return: A dictionary that represent each rhythm in the DB,
        keyed by intent name.
        Ex. {"Hello": (1.0, 0.5, 1.0), "Goodbye": (2.0, 2.0)}
        """
        try:
            pass
        except:
            raise RuntimeError("Cannot get rhythms from database.")

    @staticmethod
    # IMPLEMENT
    def getFileByTimeStamp(dateTime):
        """
        Gets information about the audio file generated at
        the given date and time. Raises a ValueError if there
        is no file stored in the DB that was generated at the
        given time.
        :param dateTime: Date and time to search for an audio
        file at in the DB as a datetime object.
        :return: A dictionary of information about the audio
        file generated at the given date and time.
        """
        if not isinstance(dateTime,datetime):
            raise TypeError("Please input a datetime object.")
        else:
            try:
                pass
            except:
                raise ValueError("There is no file that was generated at the given date and time.")

    @staticmethod
    # IMPLEMENT
    def getMostRecentAudio():
        """
        Gets information about the most recently generated
        audio file.
        :return: A dictionary of information about the audio
        file generated most recently.
        """
        try:
            pass
        except:
            raise RuntimeError("Cannot find the most recently generated audio file.")

    @staticmethod
    # IMPLEMENT
    def addNewFile(args):
        """
        Adds a new file of the given specifications to the DB.
        Raises a ValueError if the given arguments are
        not acceptable. Arguments are acceptable if their types
        match the columns of the DB.
        :param args: Dictionary of arguments to generate this
        audio file with in the DB.
        """
        if not isinstance(args, dict):
            raise TypeError("Arguments must be passed through a dictionary.")
        else:
            try:
                pass
            except:
                raise ValueError("Arguments not acceptable.")

    @staticmethod
    # IMPLEMENT
    def favoriteFile(dateTime):
        """
        Favorites the file generate at the given date and time.
        Raises a ValueError if no file exists that was generated
        at the given date and time.
        :param dateTime: Date and time of generated file to favorite.
        """
        if not isinstance(dateTime,datetime):
            raise TypeError("Please input a datetime object.")
        else:
            try:
                pass
            except:
                raise ValueError("There is no file that was generated at the given date and time.")

    @staticmethod
    # IMPLEMENT
    def unfavoriteFile(dateTime):
        """
        Unavorites the file generate at the given date and time.
        Raises a ValueError if no file exists that was generated
        at the given date and time.
        :param dateTime: Date and time of generated file to favorite.
        """
        if not isinstance(dateTime, datetime):
            raise TypeError("Please input a datetime object.")
        else:
            try:
                pass
            except:
                raise ValueError("There is no file that was generated at the given date and time.")
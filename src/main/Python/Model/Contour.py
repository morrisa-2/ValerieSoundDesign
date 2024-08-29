"""
Models an intent's contour.
"""

from enum import Enum

class Contour(Enum):
    DESCENDING = "Descending"
    ASCENDING = "Ascending"
    NO_PRIORITY = "No Priority"
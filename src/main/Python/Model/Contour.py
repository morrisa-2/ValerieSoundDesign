"""
Models an intent's contour.
"""

from enum import Enum

class Contour(Enum):
    DESCENDING = 1
    ASCENDING = 2
    NO_PREFERENCE = 3
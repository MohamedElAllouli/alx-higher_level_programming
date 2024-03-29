#!/usr/bin/python3
"""class LockedClass"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes

    Attributes:
    first_name : first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates instances of Locked Class."""

        self.first_name = "first_name"

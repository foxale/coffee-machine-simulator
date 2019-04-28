# coding=utf-8
from src.exceptions import TurnedOff


class CoffeeMachine:
    """The CoffeeMachine serves coffee-like beverages"""

    def __init__(self):
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self):
        """Just turn the CoffeeMachine on."""
        self._is_on = True

    def turn_off(self):
        """It's over. Turn is off, for God's sake."""
        self._is_on = False


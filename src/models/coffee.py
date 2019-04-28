# coding=utf-8
from src.utils import Mililiters


class Coffee:
    """Who doesn't love a proper cup of coffee on Monday morning?"""

    def __init__(self, volume: Mililiters, with_milk: bool = False):
        self._volume = volume
        self._milk = with_milk

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._volume == other._volume and self._milk == other._milk

    @property
    def volume(self):
        return self._volume

    @property
    def milk(self):
        return self._milk

# coding=utf-8
from src.utils import Mililiters


class Coffee:
    """Who doesn't love a proper cup of coffee on Monday morning?"""

    def __init__(self, volume: Mililiters):
        self._volume = volume

    @property
    def volume(self):
        return self._volume

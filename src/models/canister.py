# -*- coding: utf-8 -*-
from src.exceptions import NotEnoughWater
from src.utils import Mililiters


class Canister:
    """The Canister contains the water needed for preparing beverages"""

    def __init__(self, capacity: Mililiters = 1000):
        self._capacity: Mililiters = capacity
        self._water_level: Mililiters = capacity

    @property
    def water_level(self) -> Mililiters:
        return self._water_level

    @property
    def capacity(self) -> Mililiters:
        return self._capacity

    def get_water(self, volume: Mililiters = 0) -> Mililiters:
        """Request a given amount of water to be pumped out of the Canister"""
        if self._water_level < volume:
            raise NotEnoughWater
        self._water_level -= volume
        return volume


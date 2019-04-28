# -*- coding: utf-8 -*-
from src.exceptions import NotEnoughMilk
from src.exceptions import NotEnoughSubstance
from src.exceptions import NotEnoughWater
from src.utils import Mililiters


class Canister:
    """The Canister contains the substance needed for preparing beverages"""

    error_when_empty = NotEnoughSubstance

    def __init__(self, capacity: Mililiters = 1000):
        self._capacity: Mililiters = capacity
        self._fill_level: Mililiters = capacity

    @property
    def fill_level(self) -> Mililiters:
        return self._fill_level

    @property
    def capacity(self) -> Mililiters:
        return self._capacity

    def get_substance(self, volume: Mililiters = 0) -> Mililiters:
        """Pump out a given amount of substance out of the Canister"""
        if self._fill_level < volume:
            raise self.error_when_empty
        self._fill_level -= volume
        return volume

    def refill(self) -> None:
        """Refill the Canister to the brim"""
        self._fill_level = self._capacity


class WaterCanister(Canister):
    """The WaterCanister contains water needed for preparing beverages"""

    def __init__(self, capacity: Mililiters = 1000):
        super().__init__(capacity=capacity)
        self.error_when_empty = NotEnoughWater

    def get_water(self, volume: Mililiters = 0) -> Mililiters:
        """Pump out a given amount of water out of the WaterCanister"""
        return super().get_substance(volume=volume)


class MilkCanister(Canister):
    """The MilkCanister contains milk needed for preparing beverages"""

    def __init__(self, capacity: Mililiters = 1000):
        super().__init__(capacity=capacity)
        self.error_when_empty = NotEnoughMilk

    def get_milk(self, volume: Mililiters = 0) -> Mililiters:
        """Pump out a given amount of milk out of the MilkCanister"""
        return super().get_substance(volume=volume)


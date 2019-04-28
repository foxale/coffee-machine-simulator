# coding=utf-8
from typing import Dict

from src.exceptions import NotEnoughWater
from src.exceptions import TurnedOff
from src.models.canister import Canister
from src.models.coffee import Coffee
from src.utils import Mililiters


class CoffeeMachine:
    """The CoffeeMachine serves coffee-like beverages"""

    _serving_to_ml: Dict[str, Dict[str, Mililiters]] = {
        'coffee': {
            'small': 100,
            'medium': 150,
            'large': 250,
            'default': 150
        },
        'espresso': {
            'single': 50,
            'double': 100,
            'default': 50
        },
        'default': {
            'single': 50,
            'double': 100,
            'small': 100,
            'medium': 150,
            'large': 250,
            'default': 100,
        }
    }

    @staticmethod
    def _get_servings_mapping(beverage: str = 'default') -> Dict[str, Mililiters]:
        """Get a mapping between the beverage and its servings"""
        try:
            return CoffeeMachine._serving_to_ml[beverage]
        except KeyError:
            # TODO: inform about switching to default value
            return CoffeeMachine._serving_to_ml['default']

    @staticmethod
    def get_beverage_volume(beverage: str = 'default', serving: str = 'default') -> Mililiters:
        """Get volume of the specific serving of the specific beverage"""
        _beverage_serving_to_ml = CoffeeMachine._get_servings_mapping(beverage)
        try:
            return _beverage_serving_to_ml[serving]
        except KeyError:
            # TODO: inform about switching to default value
            return _beverage_serving_to_ml['default']

    def __init__(self, canister_capacity: Mililiters = 1000):
        self._is_on = False
        self._canister = Canister(capacity=canister_capacity)

    @property
    def is_on(self):
        return self._is_on

    def turn_on(self):
        """Just turn the CoffeeMachine on."""
        self._is_on = True

    def turn_off(self):
        """It's over. Turn is off, for God's sake."""
        self._is_on = False

    def prepare_coffee(self, serving: str = 'default'):
        """Preparing Coffee never was so simple."""
        _coffee_volume = self.get_beverage_volume(beverage='coffee', serving=serving)
        if self._is_on is False:
            raise TurnedOff
        try:
            _water_needed = self._canister.get_water(volume=_coffee_volume)
        except NotEnoughWater:
            raise NotEnoughWater from NotEnoughWater
        else:
            # TODO: use the water to brew coffee instead of mocking the process
            return Coffee(volume=_water_needed)

    @property
    def water_level(self):
        """Check the remaining water in the canister"""
        return self._canister.water_level

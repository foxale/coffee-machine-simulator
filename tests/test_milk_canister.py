# -*- coding: utf-8 -*-

"""
tests.test_milk_canister
~~~~~~~~~~~~~~~~~~~
This script contains tests for the MilkCanister model.
"""

from pytest import fixture, mark, raises

from src.exceptions import CoffeeMachineException
from src.exceptions import NotEnoughMilk
from src.models.canister import MilkCanister
from src.utils import Mililiters


@fixture()
def create_milk_canister(request):
    """Create MilkCanister object for testing."""
    try:
        _canister_capacity = request.param
    except AttributeError:
        _canister_capacity = TestMilkCanister.capacity_default
    _canister = MilkCanister(capacity=_canister_capacity)
    return _canister


class TestMilkCanister:

    capacity_default = 1000

    @mark.parametrize(
        ('create_milk_canister', 'milk_volume', 'expectation'),
        [(100, 200, raises(NotEnoughMilk)),
         (0, 1, raises(NotEnoughMilk))],
        indirect=['create_milk_canister']
    )
    def test_fill_level_raise_not_enough_milk(self,
                                              create_milk_canister: MilkCanister,
                                              milk_volume: Mililiters,
                                              expectation: CoffeeMachineException):
        """Test an edge case, when there is not enough milk to get from the MilkCanister"""
        with expectation:
            create_milk_canister.get_milk(volume=milk_volume)

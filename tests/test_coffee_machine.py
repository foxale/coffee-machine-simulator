from typing import List

import pytest

from src.exceptions import NotEnoughMilk
from src.exceptions import NotEnoughWater
from src.exceptions import TurnedOff
from src.models.coffee import Coffee
from src.models.coffee_machine import CoffeeMachine


@pytest.fixture()
def create_coffee_machine():
    """Create CoffeeMachine object for testing."""
    _coffee_machine = CoffeeMachine()
    return _coffee_machine


def assert_all_elements_are_equal(elements: List):
    assert len(set(elements)) == 1


class TestCoffeeMachine:

    def test_initialization(self, create_coffee_machine):
        """Test CoffeeMachine object initialization"""
        pass

    def test_turn_on_and_off(self, create_coffee_machine):
        """Test if we can properly turn the CoffeeMachine on and off"""
        create_coffee_machine.turn_off()
        assert create_coffee_machine.is_on is False
        create_coffee_machine.turn_on()
        assert create_coffee_machine.is_on is True
        create_coffee_machine.turn_off()
        assert create_coffee_machine.is_on is False

    def test_prepare_coffee(self, create_coffee_machine):
        """Test the main CoffeeMachine functionality - preparing coffee"""
        create_coffee_machine.turn_on()
        _result = create_coffee_machine.prepare_coffee()
        assert type(_result) is Coffee

    def test_prepare_coffee_raise_exception_when_off(self, create_coffee_machine):
        """You can't get no Coffee, when the CoffeeMachine is turned off"""
        create_coffee_machine.turn_off()
        with pytest.raises(TurnedOff):
            create_coffee_machine.prepare_coffee()

    @pytest.mark.xfail(
        raises=AssertionError,
        reason='''Initializing Canister with 0 or filled with substance is a still 
               unresolved issue''')
    def test_water_level(self, create_coffee_machine):
        """Test checking the water level in WaterTank"""
        assert create_coffee_machine.water_level == 0

    def test_get_beverage_volume_default(self, create_coffee_machine: CoffeeMachine):
        """Test getting beverage volume, when beverage is default, missing or incorrect"""
        default_beverage_volumes = [
            create_coffee_machine.get_beverage_volume(),
            create_coffee_machine.get_beverage_volume(beverage='default'),
            create_coffee_machine.get_beverage_volume(beverage='default', serving='can'),
            create_coffee_machine.get_beverage_volume(beverage='default', serving='default'),
            create_coffee_machine.get_beverage_volume(beverage='coke'),
            create_coffee_machine.get_beverage_volume(beverage='coke', serving='default'),
            create_coffee_machine.get_beverage_volume(beverage='coke', serving='can'),
        ]
        assert_all_elements_are_equal(elements=default_beverage_volumes)

    def test_prepare_coffee_raise_exception_when_not_enough_water(
            self,
            create_coffee_machine: CoffeeMachine):
        """Test preparing coffee with not enough water in the WaterCanister"""
        coffee_volume = create_coffee_machine.get_beverage_volume(beverage='coffee')
        create_coffee_machine.turn_on()
        while create_coffee_machine.water_level >= coffee_volume:
            create_coffee_machine.prepare_coffee()
        with pytest.raises(NotEnoughWater):
            create_coffee_machine.prepare_coffee()

    def test_prepare_coffee_with_milk(self, create_coffee_machine: CoffeeMachine):
        """Test preparing coffee with milk"""
        create_coffee_machine.turn_on()
        _coffee_with_milk_1 = create_coffee_machine.prepare_coffee(with_milk=True)
        _coffee_with_milk_2 = create_coffee_machine.prepare_coffee_with_milk()
        assert _coffee_with_milk_1 == _coffee_with_milk_2

    def test_prepare_coffee_raise_exception_when_not_enough_milk(
            self,
            create_coffee_machine: CoffeeMachine):
        """Test preparing coffee with not enough milk in the MilkCanister"""
        create_coffee_machine.turn_on()
        while create_coffee_machine.milk_level >= create_coffee_machine.milk_serving:
            create_coffee_machine.prepare_coffee(with_milk=True)
            create_coffee_machine.refill_water()
        with pytest.raises(NotEnoughMilk):
            create_coffee_machine.prepare_coffee(with_milk=True)


import pytest

from src.exceptions import TurnedOff
from src.models.coffee import Coffee
from src.models.coffee_machine import CoffeeMachine


@pytest.fixture()
def create_coffee_machine():
    """Create CoffeeMachine object for testing."""
    _coffee_machine = CoffeeMachine()
    return _coffee_machine


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






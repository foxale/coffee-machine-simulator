import pytest

from src.models.coffee_machine import CoffeeMachine


@pytest.fixture()
def create_coffee_machine():
    """Create CoffeeMachine object for testing"""
    _coffee_machine = CoffeeMachine()
    return _coffee_machine


class TestCoffeeMachine:

    def test_coffee_machine_initialization(self, create_coffee_machine):
        """Test CoffeeMachine object initialization"""
        pass

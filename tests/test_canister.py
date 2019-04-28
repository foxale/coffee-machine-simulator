
import pytest
from pytest import mark

from src.exceptions import CoffeeMachineException
from src.exceptions import NotEnoughWater
from src.models.canister import Canister
from src.utils import Mililiters


@pytest.fixture()
def create_canister(request):
    """Create CoffeeMachine object for testing."""
    try:
        _canister_capacity = request.param
    except AttributeError:
        _canister_capacity = TestCanister.capacity_default
    _canister = Canister(capacity=_canister_capacity)
    return _canister


class TestCanister:

    capacity_default = 1000

    def test_initialization(self, create_canister):
        """Test Canister object initialization"""
        pass

    @mark.parametrize(
        ('create_canister', 'water_to_get', 'expected'),
        [(1000, 500, 500),
         (500, 500, 0),
         (600, 0, 600)],
        indirect=['create_canister']
    )
    def test_water_level(self, create_canister: Canister, water_to_get: Mililiters, expected: Mililiters):
        """Test if we can get an actual water level of the Canister"""
        assert create_canister.water_level == create_canister.capacity
        create_canister.get_water(volume=water_to_get)
        assert create_canister.water_level == expected

    @mark.parametrize(
        ('create_canister', 'water_volume', 'expectation'),
        [(100, 200, pytest.raises(NotEnoughWater)),
         (0, 1, pytest.raises(NotEnoughWater))],
        indirect=['create_canister']
    )
    def test_water_level_raise_not_enough_water(self, create_canister: Canister, water_volume: Mililiters, expectation: CoffeeMachineException):
        """Test an edge case, when there is not enough water to get from the Canister"""
        with expectation:
            create_canister.get_water(volume=water_volume)

    @pytest.mark.xfail(
        raises=AssertionError,
        reason='''Filling container functionality not implemented yet,
               so the container is automatically filled to the brim''')
    def test_water_level(self, create_coffee_machine):
        """Test checking the water level in Container"""
        assert create_coffee_machine.water_level == 0




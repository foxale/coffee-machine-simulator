from pytest import fixture, mark, raises

from src.exceptions import CoffeeMachineException
from src.exceptions import NotEnoughWater
from src.models.canister import WaterCanister
from src.utils import Mililiters


@fixture()
def create_water_canister(request):
    """Create WaterCanister object for testing."""
    try:
        _canister_capacity = request.param
    except AttributeError:
        _canister_capacity = TestWaterCanister.capacity_default
    _canister = WaterCanister(capacity=_canister_capacity)
    return _canister


class TestWaterCanister:

    capacity_default = 1000

    @mark.parametrize(
        ('create_water_canister', 'water_volume', 'expectation'),
        [(100, 200, raises(NotEnoughWater)),
         (0, 1, raises(NotEnoughWater))],
        indirect=['create_water_canister']
    )
    def test_fill_level_raise_not_enough_water(self,
                                               create_water_canister: WaterCanister,
                                               water_volume: Mililiters,
                                               expectation: CoffeeMachineException):
        """Test an edge case, when there is not enough water to get from the WaterCanister"""
        with expectation:
            create_water_canister.get_water(volume=water_volume)


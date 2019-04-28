from random import randrange

from pytest import fixture, mark, raises

from src.exceptions import CoffeeMachineException
from src.exceptions import NotEnoughSubstance
from src.models.canister import Canister
from src.utils import Mililiters


@fixture()
def create_canister(request):
    """Create Canister object for testing."""
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
        ('create_canister', 'substance_to_get', 'expected'),
        [(1000, 500, 500),
         (500, 500, 0),
         (600, 0, 600)],
        indirect=['create_canister']
    )
    def test_fill_level(self, create_canister: Canister, substance_to_get: Mililiters, expected: Mililiters):
        """Test if we can get an actual fill level of the Canister"""
        assert create_canister.fill_level == create_canister.capacity
        create_canister.get_substance(volume=substance_to_get)
        assert create_canister.fill_level == expected

    @mark.parametrize(
        ('create_canister', 'substance_volume', 'expectation'),
        [(100, 200, raises(NotEnoughSubstance)),
         (0, 1, raises(NotEnoughSubstance))],
        indirect=['create_canister']
    )
    def test_fill_level_raise_not_enough_substance(self, create_canister: Canister, substance_volume: Mililiters, expectation: CoffeeMachineException):
        """Test an edge case, when there is not enough substance to get from the Canister"""
        with expectation:
            create_canister.get_substance(volume=substance_volume)

    @mark.xfail(
        raises=AssertionError,
        reason='''Filling container functionality not implemented yet,
               so the Container is automatically filled to the brim''')
    def test_fill_level(self, create_canister: Canister):
        """Test checking the substance level in Container"""
        assert create_canister.fill_level == 0

    def test_refill(self, create_canister: Canister):
        """Test refilling Container with substance, after getting some/all of it"""
        _volume = create_canister.capacity
        create_canister.get_substance(volume=randrange(1, _volume))
        assert create_canister.fill_level != create_canister.capacity
        create_canister.refill()
        assert create_canister.fill_level == create_canister.capacity
        create_canister.get_substance(volume=_volume)
        assert create_canister.fill_level == 0
        create_canister.refill()
        assert create_canister.fill_level == create_canister.capacity





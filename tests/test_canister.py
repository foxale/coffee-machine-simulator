# -*- coding: utf-8 -*-

"""
tests.test_canister
~~~~~~~~~~~~~~~~~~~
This script contains tests for the Canister model.
"""

from random import randrange

from pytest import fixture, mark, raises

from src.exceptions import NotEnoughRefillable
from src.exceptions import CoffeeMachineException
from src.models.canister import Canister
from src.utils import Refillable


@fixture()
def create_canister(request) -> Canister:
    """Create Canister object for testing."""
    try:
        _canister_capacity = request.param
    except AttributeError:
        _canister_capacity = TestCanister.capacity_default
    _canister = Canister(capacity=_canister_capacity)
    return _canister


class TestCanister:
    capacity_default: Refillable = 1000

    def test_initialization(self, create_canister: Canister) -> None:
        """Test Canister object initialization"""
        pass

    def test_initial_attribute_values(self, create_canister: Canister) -> None:
        """Test checking the initial attribute values of the Container"""
        assert create_canister.capacity == TestCanister.capacity_default
        assert create_canister.fill_level == 0

    @mark.parametrize(
        ('create_canister', 'quantity_of_refillable_to_get', 'expected_fill_level'),
        [(1000, 500, 500),
         (500, 500, 0),
         (600, 0, 600)],
        indirect=['create_canister']
    )
    def test_fill_level(self,
                        create_canister: Canister,
                        quantity_of_refillable_to_get: Refillable,
                        expected_fill_level: Refillable) -> None:
        """Test if we can get an actual fill level of the Canister"""
        create_canister.refill()
        assert create_canister.fill_level == create_canister.capacity
        create_canister._get_refillable(quantity=quantity_of_refillable_to_get)
        assert create_canister.fill_level == expected_fill_level

    @mark.parametrize(
        ('create_canister', 'quantity_of_refillable_to_get', 'expected_exception'),
        [(100, 200, raises(NotEnoughRefillable)),
         (0, 1, raises(NotEnoughRefillable))],
        indirect=['create_canister']
    )
    def test_fill_level_raise_not_enough_refillable(self,
                                                    create_canister: Canister,
                                                    quantity_of_refillable_to_get: Refillable,
                                                    expected_exception: CoffeeMachineException
                                                    ) -> None:
        """Test an edge case, when there is not enough substance to get from the Canister"""
        with expected_exception:
            create_canister._get_refillable(quantity=quantity_of_refillable_to_get)

    def test_refill(self, create_canister: Canister) -> None:
        """Test refilling Container with substance, after getting some/all of it"""
        _max_quantity = create_canister.capacity
        create_canister.refill()
        create_canister._get_refillable(quantity=randrange(1, _max_quantity))
        assert create_canister.fill_level != create_canister.capacity
        create_canister.refill()
        assert create_canister.fill_level == create_canister.capacity
        create_canister._get_refillable(quantity=_max_quantity)
        assert create_canister.fill_level == 0
        create_canister.refill()
        assert create_canister.fill_level == create_canister.capacity

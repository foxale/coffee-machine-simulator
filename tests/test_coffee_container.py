# -*- coding: utf-8 -*-

"""
tests.test_coffee__container
~~~~~~~~~~~~~~~~~~~
This script contains tests for the CoffeeBeansContainer model.
"""

from pytest import fixture, mark, raises

from src.exceptions import CoffeeMachineException
from src.exceptions import NotEnoughCoffeeBeans
from src.models.container import CoffeeBeansContainer
from src.utils import Grams


@fixture
def create_coffee_beans_container(request) -> CoffeeBeansContainer:
    """Create CoffeeBeansContainer object for testing."""
    try:
        _container_capacity = request.param
    except AttributeError:
        _container_capacity = TestCoffeeBeansContainer.capacity_default
    _container = CoffeeBeansContainer(capacity=_container_capacity)
    return _container


class TestCoffeeBeansContainer:
    capacity_default: Grams = 300

    @mark.parametrize(
        ('create_coffee_beans_container', 'coffee_weight', 'expected_exception'),
        [(300, 350, raises(NotEnoughCoffeeBeans)),
         (0, 1, raises(NotEnoughCoffeeBeans))],
        indirect=['create_coffee_beans_container']
    )
    def test_fill_level_raise_not_enough_coffee_beans(
            self,
            create_coffee_beans_container: CoffeeBeansContainer,
            coffee_weight: Grams,
            expected_exception: CoffeeMachineException
    ) -> None:
        """Test an edge case, when there is not enough coffee to get from the CoffeeBeansContainer"""
        with expected_exception:
            create_coffee_beans_container.get_coffee(weight=coffee_weight)

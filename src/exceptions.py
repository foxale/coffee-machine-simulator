# -*- coding: utf-8 -*-

"""
src.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains the set of CoffeeMachine's exceptions.
"""


class CoffeeMachineException(Exception):
    """There was an ambiguous exception that occurred while using CoffeeMachine."""


class TurnedOff(CoffeeMachineException):
    """An action was performed on a Machine turned off"""


class NotEnoughWater(CoffeeMachineException):
    """There is not enough water to continue an action"""

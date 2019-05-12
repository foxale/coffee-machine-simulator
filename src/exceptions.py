# -*- coding: utf-8 -*-

"""
src.exceptions
~~~~~~~~~~~~~~~~~~~
This module contains exceptions related to the CoffeeMachine.
"""


class CoffeeMachineException(Exception):
    """There was an ambiguous exception that occurred while using CoffeeMachine."""


class TurnedOff(CoffeeMachineException):
    """An action was performed on a Machine turned off"""


class CanisterException(Exception):
    """There was an ambiguous exception that occurred while using Canister."""


class NotEnoughSubstance(CanisterException):
    """There is not enough substance to continue an action"""


class NotEnoughWater(NotEnoughSubstance, CoffeeMachineException):
    """There is not enough water to continue preparing a beverage"""


class NotEnoughMilk(NotEnoughSubstance, CoffeeMachineException):
    """There is not enough water to continue preparing a beverage"""

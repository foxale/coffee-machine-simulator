# -*- coding: utf-8 -*-

"""
src.views.view
~~~~~~~~~~~~~~~~~~~
This script contains the main and only view of the application.
It is implemented as a CLI; it requires Click module.
"""

import click

from src.utils import Mililiters


def present_coffee_machine(water_canister_fill_level: Mililiters,
                           milk_canister_fill_level: Mililiters,
                           is_on: bool):
    print(f'''
    ---===---
    CoffeeMachine with: 
        - WaterCanister ({water_canister_fill_level} ml) 
        - MilkCanister ({milk_canister_fill_level} ml)
    Turned {"ON" if is_on else "OFF"}
    ---===---
    ''')


def prompt_user_with_actions_on_coffee_machine(coffee_machine_is_on: bool = False):
    choice = click.prompt(
        'What would you like to do now?', 
        type=click.Choice([
            f'turn the coffee machine {"OFF" if coffee_machine_is_on else "ON"}',
            'drink small coffee',
            'drink medium coffee',
            'drink large coffee',
            'drink small coffee with milk',
            'drink medium coffee with milk',
            'drink large coffee with milk',
            'refill water',
            'refill milk',
            'go away'
        ]))
    return choice


def present_coffee(volume, milk):
    click.echo(f'''
    Yes! {volume}ml Coffee{" with milk" if milk else ""} is ready!''')


def show_error(text):
    click.echo(f'''
    No, no, no - {text}''')


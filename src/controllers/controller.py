# coding=utf-8
from src.exceptions import NotEnoughMilk
from src.exceptions import NotEnoughWater
from src.exceptions import TurnedOff
from src.models.coffee_machine import CoffeeMachine
from src.views import view


class Controller:

    def __init__(self):
        self.play = False
        self.coffee_machine = CoffeeMachine(
            water_canister_capacity=500,
            milk_canister_capacity=200
        )
        self.coffee_machine.turn_on()
        self.view = view

    def run(self):
        self.play = True
        while self.play:
            self.present_coffee_machine()
            self.get_user_action()

    def present_coffee_machine(self) -> None:
        view.present_coffee_machine(water_canister_fill_level=self.coffee_machine.water_level,
                                    milk_canister_fill_level=self.coffee_machine.milk_level,
                                    is_on=self.coffee_machine.is_on)

    def get_user_action(self):
        choice = self.view.prompt_user_with_actions_on_coffee_machine(coffee_machine_is_on=self.coffee_machine.is_on)
        if 'turn the coffee machine' in choice:
            self.coffee_machine.turn_on() if 'ON' in choice else self.coffee_machine.turn_off()
        elif 'drink' in choice:
            _, serving, beverage, *_ = choice.split(' ')
            with_milk = 'with milk' in choice
            self.prepare_beverage(beverage=beverage, serving=serving, with_milk=with_milk)
        elif choice == 'go away':
            self.play = False
        elif choice == 'refill water':
            self.coffee_machine.refill_water()
        elif choice == 'refill milk':
            self.coffee_machine.refill_milk()

    def prepare_beverage(self, beverage, serving, with_milk):
        if beverage == 'coffee':
            self.prepare_coffee(serving=serving, with_milk=with_milk)

    def prepare_coffee(self, serving: str, with_milk: bool):
        try:
            coffee = self.coffee_machine.prepare_coffee(serving=serving, with_milk=with_milk)
        except NotEnoughWater:
            self.view.show_error('Not enough water! Refill the water container!')
        except NotEnoughMilk:
            self.view.show_error('Not enough milk! Refill the milk container!')
        except TurnedOff:
            self.view.show_error('Coffee machine turned off. Turn it on to make beverage!')
        else:
            self.view.present_coffee(milk=coffee.milk, volume=coffee.volume)
from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    started = False
    weight = 100
    fuel = 10
    fuel_consumption = 5.0
    distance = 1

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        required_fuel_amount = self.fuel_consumption * distance
        if self.fuel < required_fuel_amount:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel = self.fuel - required_fuel_amount
            return self.fuel


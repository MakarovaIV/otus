"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 1

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, value):
        if (self.cargo + value) > self.max_cargo:
            raise CargoOverload()
        else:
            self.cargo = self.cargo + value

    def remove_all_cargo(self):
        cargo_before_remove = self.cargo
        self.cargo = 0
        return cargo_before_remove

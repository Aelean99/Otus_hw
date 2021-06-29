"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base, exceptions


class Plane(base.Vehicle):
    max_cargo: int

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo: int = 0

    def load_cargo(self, value):
        if (self.cargo + value) > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo += value

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo

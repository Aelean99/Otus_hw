"""
создайте класс `Plane`, наследник `Vehicle`
"""
import homework_02


class Plane(homework_02.Vehicle):
    cargo: int
    max_cargo: int

    def __init__(self, max_cargo, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, value):
        if (self.cargo + value) > self.max_cargo:
            raise homework_02.CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo

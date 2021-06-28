from abc import ABC

import homework_02


class Vehicle(ABC):
    started = False

    def __init__(self, weight: float = 100, fuel: float = 20, fuel_consumption: float = 7):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __repr__(self):
        return f"Current weight {self.weight}, fuel {self.fuel}, fuel_consumption {self.fuel_consumption}, " \
               f"started {self.started}"

    def start(self):
        # Если транспорт ещё не заведён
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise homework_02.LowFuelError

    def move(self, distance: int):
        # Пробуем поехать не заведя машину? :)
        try:
            self.start()
        except homework_02.LowFuelError:
            raise homework_02.NotEnoughFuel

        self.fuel = self.fuel - distance * self.fuel_consumption

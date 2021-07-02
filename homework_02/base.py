from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    started = False
    distance: int

    def __init__(self, weight: float = 100, fuel: float = 20, fuel_consumption: float = 7):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def __repr__(self):
        return f"Current weight {self.weight}, fuel {self.fuel}, fuel_consumption {self.fuel_consumption}, " \
               f"started {self.started}, distance {self.distance}"

    def start(self):
        # Если транспорт ещё не заведён
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance: int):
        if self.fuel > self.fuel_consumption > 0:
            fuel_need = self.fuel_consumption * distance
            if self.fuel - fuel_need < 0:
                raise exceptions.NotEnoughFuel
            else:
                self.fuel -= fuel_need
        else:
            raise exceptions.NotEnoughFuel

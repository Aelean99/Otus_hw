"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base, engine


class Car(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        super(Car, self).__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def __repr__(self):
        return f"Current weight {self.weight}, fuel {self.fuel}, fuel_consumption {self.fuel_consumption}, " \
               f"started {self.started}, engine {self.engine}"

    def set_engine(self, my_engine: engine.Engine):
        self.engine = my_engine

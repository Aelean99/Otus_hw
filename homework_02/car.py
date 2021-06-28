"""
создайте класс `Car`, наследник `Vehicle`
"""
import homework_02


class Car(homework_02.Vehicle):
    def __init__(self, engine, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def __repr__(self):
        return f"Current weight {self.weight}, fuel {self.fuel}, fuel_consumption {self.fuel_consumption}, " \
               f"started {self.started}, engine {self.engine}"

    def set_engine(self, engine: homework_02.Engine):
        self.engine = engine

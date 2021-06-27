"""
создайте класс `Car`, наследник `Vehicle`
"""
import homework_02


class Car(homework_02.Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = None

    def set_engine(self, engine: homework_02.Engine):
        self.engine = engine

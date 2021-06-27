"""
Домашнее задание №2
Классы и модули
"""
# ORIGINAL IMPORTS
# from . import base, car, engine, exceptions, plane
#
#
# __all__ = [
#     "base",
#     "car",
#     "engine",
#     "exceptions",
#     "plane",
# ]

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload, LowFuelError, NotEnoughFuel
from homework_02.plane import Plane
from homework_02.engine import Engine
from homework_02.car import Car


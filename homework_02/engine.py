"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    volume: str
    pistons: str

    def __repr__(self):
        return f"Engine volume {self.volume}, pistons {self.pistons}"

from dataclasses import dataclass
from typing import List


@dataclass
class GuitarProperties:
    serial_number: str
    price: float
    builder: str
    model: str
    type: str
    backwood: str
    topwood: str




@dataclass
class AvailableGuitar:
    from .guitar_app import Guitar
    guitars: List[Guitar]
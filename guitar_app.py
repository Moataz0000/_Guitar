from dataclasses import dataclass, asdict
from typing import Union

@dataclass
class GuitarProperties:
    serial_number: str
    price: float
    builder: str
    model: str
    type: str
    backwood: str
    topwood: str

class Guitar:
    def __init__(self, properties: GuitarProperties) -> None:
        self.properties = properties

    def getSerialNumber(self) -> str:
        return self.properties.serial_number

    def getPrice(self) -> float:
        return self.properties.price

    def getBuilder(self) -> str:
        return self.properties.builder

    def getModel(self) -> str:
        return self.properties.model

    def getType(self) -> str:
        return self.properties.type

    def getBackwood(self) -> str:
        return self.properties.backwood

    def getTopwood(self) -> str:
        return self.properties.topwood

    def getAllInfo(self):
        return asdict(self.properties)


guitar1 = Guitar(properties=GuitarProperties(
    serial_number="Guitar1",
    price=200.0,
    builder="Guitar",
    model="Guitar",
    type="Guitar",
    backwood="Guitar",
    topwood="Guitar",

))

print(guitar1.getAllInfo())
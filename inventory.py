from typing import List

from .class_data import AvailableGuitar, GuitarProperties
from .guitar_app import Guitar


class Inventory:

    def __init__(self):
        self.available_guitars: List[AvailableGuitar] = []

    def addGuitar(self, guitar: Guitar) -> None:
        guitar = Guitar(
            properties=guitar.properties,
        )
        self.available_guitars.append(guitar)
        print('Guitar added!')


    def getGuitars(self):
        for guitar in self.available_guitars:
            if guitar.properties != None:
                yield guitar
            print('No Guitar Available')




inv = Inventory()

inv.addGuitar(
    Guitar(
        properties=GuitarProperties(
            serial_number='test',
            price=12,
            builder='test',
            model='test',
            type='test',
            backwood='test',
            topwood='test',
        )
    )
)


inv.getGuitars()


print("Program End!")



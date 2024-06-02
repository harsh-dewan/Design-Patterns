from typing import override
from Beverage import Beverage


class Coffee(Beverage):

    def __init__(self, name, size, flavour):
        self.name = name
        self.size = size
        self.flavour = flavour

    @override
    def nameOfBeverage(self) -> str:
        return "Name of the Beverage is: " + self.name

    def getBeverageDetails(self) -> str:
        return "Size: " + self.size + " " + " Flavour is: " + self.flavour

    @override
    def getDetails(self) -> str:
        return self.getBeverageDetails()


from abc import ABC
from typing import override
from Beverage import Beverage
from BeverageFactory import BeverageFactory
from Coffee import Coffee
from Customization import Customization


class CoffeeFactory(BeverageFactory, Customization):

    @override
    def createBeverage(self) -> Beverage:
        return Coffee("Coffee", "Large", "Choco")

    @override
    def addCustomizations(self) -> str:
        return super().addSugar() + " " + super().addMilk()




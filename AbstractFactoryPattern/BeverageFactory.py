from abc import ABC, abstractmethod

from Beverage import Beverage


class BeverageFactory(ABC):

    @abstractmethod
    def createBeverage(self) -> Beverage:
        pass

    @abstractmethod
    def addCustomizations(self) -> str:
        pass


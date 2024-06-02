from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def nameOfBeverage(self) -> str:
        pass

    @abstractmethod
    def getDetails(self) -> str:
        pass

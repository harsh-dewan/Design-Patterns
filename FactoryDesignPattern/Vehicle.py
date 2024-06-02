from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def getDetails(self) -> str:
        pass

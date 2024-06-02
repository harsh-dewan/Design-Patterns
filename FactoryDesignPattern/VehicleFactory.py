from abc import ABC, abstractmethod

from Vehicle import Vehicle


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

    def getVehicleDetails(self) -> str:
        v1 = self.create_vehicle()
        return v1.getDetails()

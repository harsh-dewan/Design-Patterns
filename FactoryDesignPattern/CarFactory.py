from Car import Car
from Vehicle import Vehicle
from VehicleFactory import VehicleFactory


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()




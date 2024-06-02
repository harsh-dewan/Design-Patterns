from Truck import Truck
from Vehicle import Vehicle
from VehicleFactory import VehicleFactory


class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()



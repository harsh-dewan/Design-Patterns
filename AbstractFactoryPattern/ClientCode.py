from CoffeeFactory import CoffeeFactory
from SoftDrinkFactory import SoftDrinkFactory
from TeaFactory import TeaFactory


class ClientCode:

    def __init__(self):
        self.b1 = CoffeeFactory()
        self.b2 = TeaFactory()
        self.b3 = SoftDrinkFactory()

    def getDetails(self):
        print(self.b1.createBeverage().nameOfBeverage())
        print(self.b1.createBeverage().getDetails())
        print(self.b1.addCustomizations())
        print(self.b2.createBeverage().nameOfBeverage())
        print(self.b2.createBeverage().getDetails())
        print(self.b2.addCustomizations())
        print(self.b3.createBeverage().nameOfBeverage())
        print(self.b3.createBeverage().getDetails())
        print(self.b3.addCustomizations())


c1 = ClientCode()
c1.getDetails()

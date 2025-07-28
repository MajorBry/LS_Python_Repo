class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'

class Vehicle:
    def __init__(self, year):
        self.year = year

class Truck(TowingMixin, Vehicle):
    def __init__(self, year):
        super().__init__(year)

class Car(Vehicle):
    def __init__(self, year):
        super().__init__(year)

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006

class Vehicle:
    _vehicle_count = 0
    
    def __init__(self):
        Vehicle._vehicle_count += 1

    @classmethod
    def vehicles(cls):
        return Vehicle._vehicle_count

class SignalMixin:
    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')

class Car(Vehicle, SignalMixin):
    def __init__(self):
        super().__init__()

class Truck(Vehicle, SignalMixin):
    def __init__(self):
        super().__init__()

class Boat(Vehicle):
    def __init__(self):
        super().__init__()

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())
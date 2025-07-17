"""
Problem:  Write the code needed to make the following code work as shown:
    Input:  
    Output:  
    Rules
        Explicit
            - 
        Implicit
            - Add 1 to a variable each time any Vehicle is created
            - Car, Truck, and Boat and all subclasses of Vehicle
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:  

Algorithm
    Objective: Keep track of the number of vehicles created.
        - initialize a vehicle-count as 0
        - when any type of vehicle is created, add 1 to vehicle-count
        - when the vehicles() method is called, return the current number stored in vehicle-count

Implementation by Code
    - _vehicle_count
"""
class Vehicle:
    _vehicle_count = 0
    
    def __init__(self):
        Vehicle._vehicle_count += 1

    @classmethod
    def vehicles(cls):
        return Vehicle._vehicle_count

class Car(Vehicle):
    def __init__(self):
        super().__init__()

class Truck(Vehicle):
    def __init__(self):
        super().__init__()

class Boat(Vehicle):
    def __init__(self):
        super().__init__()

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8
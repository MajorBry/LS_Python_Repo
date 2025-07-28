class Engine:
    def start(self):
        pass

class Car:
    accessories = ['heated seats', 'cup-holders']
    name = 'Sharalanda'
    def __init__(self, engine):
        self.engine = engine
        self.air_pressure_log = []

    def start(self):
        return self.engine.start()

class Driver:
    def __init__(self, car):
        self.car = car

    def drive(self):
        return self.car.start()

engine = Engine()
car = Car(engine)
driver = Driver(car)

car2 = Car(engine)
car3 = Car(engine)

car2.accessories.append('AC')
car2.name = 'Mr. Monkeyjocks'
print(car2.name)

print(car3.accessories)
print(car3.name)

car4 = Car(engine)
print(car2.name)
print(car3.name)
print(car4.name)
car2.air_pressure_log.append('14.7 psi')
print(car3.air_pressure_log)
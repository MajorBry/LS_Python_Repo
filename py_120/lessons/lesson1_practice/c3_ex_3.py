class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0
        self._on = False
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Name must be a string')
        self._color = color

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    def spray_paint(self, color):
        self._color = color # ← Doesn't use setter method

    def engine_on(self):
        if not self._on:
            self._on = not self._on
            print(f"The {self._model} comes to life as its engine starts.")
        else:
            print(f"The {self._model}'s engine whines as the ignition is engaged, but the engine is already running")

    def accelerate(self):
        print(f"The {self._model} accelerates slightly.")
        self._speed += 1
        self.current_speed()

    def brake(self):
        if self._speed > 0:
            print(f"As you brake, your seatbelt pushes against you and the {self._model} slows down.")
                    
            self._speed -= 1
            self.current_speed()
        else:
            print(f"You brake and the {self._model} remains motionless.")

    def engine_off(self):
        if self._on:
            if self._speed > 0:
                print(f"The {self._model}'s engine shuts off and you slowly roll to a halt.")
                self._speed = 0
                self._on = not self._on
            else:
                print(f"The {self._model} rests as its engine stops.")
                self._on = not self._on
        else: 
            print(f"The {self._model}'s engine is already off")

    def current_speed(self):
        print(f"The {self._model}'s current _speed is {self._speed} mph.")

my_car = Car('Camry', '2025', 'gray')
print(my_car.model, my_car.year, my_car.color)
my_car.spray_paint('orange')
# my_car.model = 'Avalon' # ← Causes an error since model has no setter
print(my_car.model, my_car.year, my_car.color)
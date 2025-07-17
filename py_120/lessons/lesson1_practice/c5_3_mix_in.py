class ColorMixin:
    def set_color(self, color):
        self._color = color
    
    def get_color(self):
        return self._color

class Car(ColorMixin):
    def __init__(self, color):
        self.set_color(color)
    
class SmartLight(ColorMixin):
    def __init__(self, color):
        self.set_color(color)

class House(ColorMixin):
    def __init__(self, color):
        self.set_color(color)

car = Car('red')
print(car.get_color())           # red

car.set_color('green')
print(car.get_color())           # green

smart_light = SmartLight('cool white')
print(smart_light.get_color())   # cool white

smart_light.set_color('goldenrod')
print(smart_light.get_color())   # goldenrod

house = House('sky blue')
print(house.get_color())         # sky blue

house.set_color('lavender')
print(house.get_color())         # lavender

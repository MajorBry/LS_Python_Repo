class Animal:
    bananas = 'yes, please'
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    def __init__(self, color):
        super().__init__(color)

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)


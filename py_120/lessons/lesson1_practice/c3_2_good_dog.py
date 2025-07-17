class GoodDog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'{self.name} is {age} years old.')
    
    def speak(self):
        return f'{self.name} says arf!'

sparky = GoodDog('Sparky', 5)
print(sparky.speak())

rover = GoodDog('Rover', 3)
print(rover.speak())
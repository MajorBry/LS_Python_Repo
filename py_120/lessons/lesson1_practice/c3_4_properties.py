class GoodDog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f'{self._name} says arf!'

    @property    
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')
        if age < 0:
            raise ValueError("Age can't be negative")
        self._age = age

sparky = GoodDog('Sparky', 5)
print(sparky.name)
print(sparky.age)
sparky.name = 'Fireplug'
print(sparky.name)
sparky.age = 6
print(sparky.age)
# sparky.set_age(-1)
# sparky.set_name(42)
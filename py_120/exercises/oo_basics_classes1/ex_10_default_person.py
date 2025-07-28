class Person:
    def __init__(self, name='John Doe'):
        self._name = name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1._name)    # John Doe
print(person2._name)    # Pepe Le Pew

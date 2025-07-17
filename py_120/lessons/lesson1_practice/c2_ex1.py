# How do we create a class and an object in Python?
#   class ClassName:
#       ...
# Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.
# What class you create doesn't matter, provided it satisfies the above requirements.
class Food:
    def __init__(self, name):
        self.name = name
        print(f'Mmmm, {name}!')

bacon = Food('bacon')
burrito = Food('burrito')
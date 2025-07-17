class Pet:
    def play(self):
        print('I am playing')

    def eat(self):
        print('I eat Frisky')

class Predator:
    def hunt(self):
        print('I am hunting')

    def eat(self):
        print('I eat prey')

class Cat(Pet, Predator): # first inherited class in class statement is first place python looks?
    def purr(self):
        print('I am purring')

cat = Cat()
cat.purr()
cat.play()
cat.hunt()
cat.eat()
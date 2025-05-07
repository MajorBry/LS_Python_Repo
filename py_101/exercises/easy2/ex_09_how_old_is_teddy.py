import random
def ask_name():
    name = input('What is your name? ')
    return (name if name else 'Teddy')

name = ask_name()
age = random.randint(20, 100)
print(f'{name} is {age} years old!')
class GoodDog:
    def __init__(self, name, iteration=[]):
        self.name = name

        if iteration:
            iteration.append(iteration.pop() + 1)
        else:
            iteration.append(1)
        
        print(f'{name} is good dog #{iteration[0]}!')
    
    def speak(self, i=[]):
        if i:
            i.append(i.pop() + 1)
        else:
            i.append(1)
        print(f'{self.name} says, "bow wow! ({i[0]})"')

sparky = GoodDog('Sparky')
ben = GoodDog('Ben')
dale = GoodDog('Dale')
sparky.speak()
sparky.speak()
sparky.speak()
sparky.speak()
sparky.speak()
ben.speak()
dale.speak()
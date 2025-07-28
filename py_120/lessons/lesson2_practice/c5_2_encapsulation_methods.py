class Dog:
    def walk(self):
        print('Walking the dog.')

    def _chase_car(self):
        print('I am chasing a car!')

    def __goto_vet(self):
        print('The vet! Run and hide!')

    def a_day_in_the_life(self):
        self.walk()
        self._chase_car()
        self.__goto_vet()

rover = Dog()

rover.a_day_in_the_life()   # Walking the dog.
                            # I am chasing a car!
                            # The vet! Run and hide!
                            
rover.walk()                # Walking the dog.
rover._chase_car()          # I am chasing a car!
rover._Dog__goto_vet()      # The vet! Run and hide!
rover.__goto_vet()
# AttributeError: 'Dog' object has no attribute '__goto_vet'.

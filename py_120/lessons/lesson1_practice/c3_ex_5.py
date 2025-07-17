class Person:
    def __init__(self, firstname, lastname):
        if firstname.isalpha() and lastname.isalpha():
            self._firstname = firstname.capitalize()
            self._lastname = lastname.capitalize()
        else:
            raise ValueError('arguments passed to "firstname" and "lastname" instance variables must contain alphabetic characters only')
    
    @property
    def name(self):
        return self._firstname + ' ' + self._lastname
    
    @name.setter
    def name(self, name):
        # ↑ name parameter is tuple
        if type(name) == tuple:
            if len(name) == 2:
                if name[0].isalpha() and name[1].isalpha():
                    self._firstname = name[0].capitalize()
                    self._lastname = name[1].capitalize()
                else:
                    raise ValueError('arguments passed to "firstname" and "lastname" instance variables must contain alphabetic characters only')
            else:
                raise IndexError("name tuple must have 2 elements")
        else:
            raise TypeError("name must be of type tuple")

hal = Person('hal', 'albertson')
print(hal.name)

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
# friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.

class Person:
    def __init__(self, name):
        self._name = name
        self.separate_name()
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self._name == other._name

    def separate_name(self):
        names_list = self._name.split()
        if len(names_list) == 2:
            self.first_name = names_list[0]
            self.last_name = names_list[1]
        elif len(names_list) == 1:
            self.first_name = names_list[0]
            self.last_name = ''
        else:
            raise ValueError('name must include a first and/or last name')
    
    @property
    def name(self):
        return self._first_name + ' ' + self._last_name
    
    @name.setter
    def name(self, name):
        self._name = name
        self.separate_name()
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams
"""
Problem:  Modify the Person class definition to facilitate the following methods. Note that there is no name= setter method now.
    Input:  
    Output:  
    Rules
        Explicit
            - 
        Implicit
            - include __str__ instance method
            - include __repr__ instance method
            - include Person.last_name property (getter and setter)
            - include Person.first_name property (getter and setter)
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:  

Algorithm
    - separate first name and last name
        + split first word from second word in name
            * first_name is the first word and last_name is the second word
            * if there is no second word, last_name is ''
            * if there are more than 2 words, raise exception

Implementation by Code
    - initializer should include name as parameter, and should initialize _last_name and _first_name as instance variables
    - class must try to separate _last_name and _first_name from name
"""
class Person:
    def __init__(self, name):
        self._name = name
        self.separate_name()
    
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

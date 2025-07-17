class Cat:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'Cat({repr(self.name)})'
    
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name == other.name
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name != other.name

fuzzy = Cat('Fuzzy')
fluffy = Cat('Fluffy')
fluffy2 = Cat('Fluffy')
print(fuzzy == fluffy)        # False
print(fluffy == fluffy)       # True
print(fuzzy != fluffy)        # True
print(fuzzy != fuzzy)         # False
print(fluffy == fluffy2)      # True
print(fluffy != fluffy2)      # False

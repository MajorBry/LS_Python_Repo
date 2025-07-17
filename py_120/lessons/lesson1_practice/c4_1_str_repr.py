class Cat:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f'Cat({repr(self.name)})'

cat = Cat('Fuzzy')
print(str(cat))
print(repr(cat))
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

# ↓ dict comprehension key = string, value = len(string).
# ↓ ! Only keys with odd lengths in dict.
my_dict = {key: len(key) for key in my_set if len(key) % 2 != 0}
print(my_dict)
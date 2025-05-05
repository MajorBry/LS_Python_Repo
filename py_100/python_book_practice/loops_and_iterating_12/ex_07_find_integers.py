# ↓ Returns a list of all integers in parameter tuple
def find_integers(iterable):
    return [x for x in iterable if type(x) == int]


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)
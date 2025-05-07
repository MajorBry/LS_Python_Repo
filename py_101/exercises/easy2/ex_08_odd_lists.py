def oddities(list_):
    return [list_[num] for num in range(len(list_)) if num % 2 == 0]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

#Bonus: use list slicing.
def oddities2(list_):
    return list_[::2]

print(oddities2([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities2([1, 2, 3, 4]) == [1, 3])        # True
print(oddities2(["abc", "def"]) == ['abc'])     # True
print(oddities2([123]) == [123])                # True
print(oddities2([]) == [])                      # True
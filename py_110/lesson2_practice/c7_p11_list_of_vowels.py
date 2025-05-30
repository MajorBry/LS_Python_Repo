VOWELS = frozenset({'a', 'e', 'i', 'o', 'u'})

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []
for sublist in dict1.values():
    for string in sublist:
        for char in string:
            if char in VOWELS:
                list_of_vowels.append(char)

list_of_vowels2 = [char 
                   for sublist in dict1.values() 
                   for string in sublist 
                   for char in string if char in VOWELS]

print(list_of_vowels)
print(list_of_vowels2)
def remove_vowels(list_of_strings):
    VOWELS = frozenset({'a','e','i','o','u','A','E','I','O','U'})

    new_list = []
    for string in list_of_strings:
        for vowel in VOWELS:
            string = string.replace(vowel, '')
        new_list.append(string)
    return new_list

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
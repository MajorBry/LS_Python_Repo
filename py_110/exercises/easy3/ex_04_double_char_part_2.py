def is_valid_consonant(char):
    VOWELS = frozenset({'a', 'e', 'i', 'o', 'u'})
    if char.isalpha() and char not in VOWELS:
        return True
    return False

def double_consonants(string):
    substring_list = []
    for char in string:
        if is_valid_consonant(char):
            substring_list.append(char*2)
        else:
            substring_list.append(char)
    return ''.join(substring_list)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
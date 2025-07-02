"""
Problem:  Create a function that finds how many times each lowercase letter occurs in a string..
    Input:  string
    Output:  dictionary, {lowercase_letter:count}
    Rules
        Explicit
            - returned dictionary has keys for each lowercase letter in the string, and the values represent how often the corresponding letter occurs in the string
            - dict-values are integers
        Implicit
            - skip uppercase letters, punctuation, etc.
            - return an empty dictionary if there are no lowercase letters in the string
    Questions
        - ()

Examples/ Test Cases
↓ ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def is_lowercase_letter(char):
    return char.isalpha() and char.casefold() == char

def count_letters(string):
    letter_count_dict = {}
    
    for char in string:
        if is_lowercase_letter(char) and char not in letter_count_dict:
            letter_count_dict[char] = string.count(char)

    return letter_count_dict

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)
expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)
expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)
print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

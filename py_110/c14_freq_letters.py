"""
Problem: create a program that determines the frequency of each character in a string.
    Input:  string
    Output:  dictionary of each character as key and frequency (count) as value
    Rules
        Explicit
            - each letter and the number of times that letter occurs should be recorded in the dictionary
            - key-value pair order is not important
        Implicit
            - ignores spaces
            - (?)input string does not include special characters
            - (?)input string will not be empty

Examples/ Test Cases
    statement = "The Flintstones Rock"
    output = {
        'T': 1,
        'h': 1,
        'e': 2,
        'F': 1,
        'l': 1,
        'i': 1,
        'n': 2,
        't': 2,
        's': 2,
        'o': 2,
        'R': 1,
        'c': 1,
        'k': 1
    }
    print(character_frequency(statement) == output)

Data Structures: Use dictionary to record output

Algorithm
    High Level
        1. find the number of times each letter occurs in a string
        2. record how many times each letter occurs in a dictionary
        3. return the dictionary
    Lower
        1. iterate through each character in given string
            - check to see if the character is in the dictionary
                - if yes, add 1 to the value in dictionary
                - if no, add the character to the dictionary and initialize it with value
        2. return the dictionary

Code
    Pseudocode
        def function
            char_dictionary = {}
            loop through each char (no index needed)
                ternary expression value += 1 if key in char_dictionary else add key to char_dict with value 1
            return dictionary
"""
def character_frequency(string):
    string = string.replace(' ', '') # ← Removes spaces
    char_dictionary = {}
    for char in string:
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    return char_dictionary

statement = "The Flintstones Rock"
output = {
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}
print(character_frequency(statement) == output) # Order of members doesn't matter in dictionary comparisons
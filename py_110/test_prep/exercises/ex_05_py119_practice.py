"""
Problem:  Create a function that takes a string argument and returns the character that occurs most often in the string.
    Input:  string
    Output:  string, of 1 char
    Rules
        Explicit
            - If there are multiple characters with the same greatest frequency, return the one that appears first in the string.
        Implicit
            - When counting characters, consider uppercase and lowercase versions to be the same.
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def most_common_char(string):
    char_dict = {}
    
    for char in string.casefold():
        if char not in char_dict:
            char_dict[char] = string.casefold().count(char)
    
    highest_count = max(char_dict.values())

    for char, char_count in char_dict.items():
        if char_count == highest_count:
            return char


print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')
my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')
my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

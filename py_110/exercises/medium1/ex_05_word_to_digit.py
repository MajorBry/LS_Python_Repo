"""
Problem:  make function that converts written numbers to digits.
    Input:  string: ,
     with written numbers inside
    Output:  string: ,
     having written numbers replaced with digits
    Rules
        Explicit
            - Assume the string does not contain any punctuation
        Implicit
            - assume written numbers are words (surrounded by spaces)
    Questions
        - ()

Examples/ Test Cases
↓ See Below ↓

Data Structures:  

Algorithm
    1. make a copy of string
    2. for each word from WRITTEN_NUMBERS,
        + Find the index location of the word in the string
        + check to see if there are other letters surrounding the word (see if it's a subword, helper function)
            - if it is a subword, change nothing
            - if it is not a subword, replace the characters of the word in the copied-string with the corresponding digit
        + after of a word, set the string equal to the copied-string
    3. return the fully processed string

Implementation by Code
    - 
"""
def replace_word(old_word, new_word, string):
    index = 0
    old_word_length = len(old_word)
    new_word_length = len(new_word)

    while True:
        index = string.find(old_word, index)
        if index < 0: # ← Applies when word is not found in string
            return string

        if index == 0: # ← word is first in string
            if index + old_word_length >= len(string): # ← word is last in string
                return new_word # the string IS only one word
            
            substring = string[index : index + old_word_length + 1]
            if not substring[-1].isalpha():
                string = string.replace(old_word, new_word, 1)
        elif index + old_word_length >= len(string): # ← word is last in string
            substring = string[index - 1 : index + old_word_length]
            if not substring[0].isalpha(): # ← Determines whether word is not a subword
                return string[0:index] + new_word
        else:
            substring = string[index - 1 : index + old_word_length + 1]
            if not substring[0].isalpha() and not substring[-1].isalpha(): # ← Determines whether word is not a subword
                string = string[0:index] + string[index:].replace(old_word, new_word, 1)
        index += new_word_length

def word_to_digit(string):
    WRITTEN_NUMBERS = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        }

    for word, digit in WRITTEN_NUMBERS.items():
        string = replace_word(word, str(digit), string)

    return string
    

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True

print(word_to_digit("Everyone is my number one!") == "Everyone is my number 1!")
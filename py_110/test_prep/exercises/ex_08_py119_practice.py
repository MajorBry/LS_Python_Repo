"""
Problem:  Create a function that finds the length of the longest vowel substring of a string.
    Input:  string, all lowercase alphabetic chars
    Output:  integer, length of longest vowel substring
    Rules
        Explicit
            - input is non-empty
            - vowels of interest are "a", "e", "i", "o", and "u"
            - count number of consecutive vowels for longest substring
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ below tests print True ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
VOWELS = {"a", "e", "i", "o", "u"}

def vowels_in_a_row(index, string):
    num = 0
    for char in string[index:]:
        if char in VOWELS:
            num += 1
        else:
            return num
    return num

def longest_vowel_substring(string):
    num = 0

    for index, char in enumerate(string):
        if char in VOWELS:
            number_in_a_row = vowels_in_a_row(index, string)
            if number_in_a_row > num:
                num = number_in_a_row

    return num



print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
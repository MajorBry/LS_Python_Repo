"""
Problem:  Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. There will always be exactly one such integer in the input list.
    Input:  list, of integers
    Output:  integer, that appears an odd number of times
    Rules
        Explicit
            - there will always be exactly one integer in the input list that appears an odd number of times
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def odd_fellow(numbers):
    occurrence_dict = {}
    for number in numbers:
        occurrence_dict[number] = occurrence_dict.setdefault(number, 0) + 1
    
    for digit, occurrences in occurrence_dict.items():
        if occurrences % 2 == 1:
            return digit

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

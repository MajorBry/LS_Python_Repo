"""
Problem:  Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.
    Input:  list, of numbers
    Output:  number
    Rules
        Explicit
            - all numbers in input list are the same except one
            - The list will always contain at least 3 numbers, and there will always be exactly one number that is different.
        Implicit
            - input elements and output can be integers and/or floats
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
def what_is_different(numbers):
    for i in range(len(numbers)):
        if numbers[i] == numbers[i + 1] == numbers[i + 2]:
            continue
        elif numbers[i] == numbers[i + 1]:
            return numbers[i + 2]
        elif numbers[i] == numbers[i + 2]:
            return numbers[i + 1]
        else:
            return numbers[i]

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

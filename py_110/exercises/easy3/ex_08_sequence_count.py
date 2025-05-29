"""
Problem:  create a function named sequence
    Input:  2 integers, count and multiplier_starter
    Output:  list with count elements
    Rules
        Explicit
            - each element in returned list should be a multiple of multiplier_starter
            - first number is the multiplier_starter
            - if count is 0, return []
            - count will always be >= 0
        Implicit
            - the value of each element is equal to the multiplier_starter * (index + 1)
    Questions
        - 

Examples/ Test Cases
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

Data Structures:  list

Algorithm
    - initialize an empty numbers list, and a counter
    - loop count times, adding the next multiple of multiplier_starter to the list each time
    - return the numbers list

Implementation by Code
    - 
"""


def sequence(count, multiplier_starter):
    numbers = []
    for i in range(1, count + 1):
        numbers.append(multiplier_starter * i)
    return numbers

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

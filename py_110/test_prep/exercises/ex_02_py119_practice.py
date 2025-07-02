"""
Problem:  Create a function that the minimum sum of 5 consecutive numbers in a list.
    Input:  list, of integers
    Output:  integer, min sum of 5 consecutive elements
    Rules
        Explicit
            - If the list contains fewer than 5 elements, the function should return None.
            - positive, negative, and 0 integers allowed in list
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  use list to hold result of sums

Algorithm
    - Note: there are a total of n - 4 sums from the given list, where n is the length of the list.

Implementation by Code
    - 
"""
def minimum_sum(numbers):
    if len(numbers) < 5:
        return None
    
    number_of_sums = len(numbers) - 4
    sums = [sum(numbers[count:(count + 5)]) for count in range(number_of_sums)]
    return min(sums)

# Following return True
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

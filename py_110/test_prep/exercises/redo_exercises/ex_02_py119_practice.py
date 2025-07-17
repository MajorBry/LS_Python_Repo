"""
Problem:  create a function that finds the minimum sum of 5 consecutive numbers in a list of numbers
    Input:  list, of numbers
    Output:  number, sum of numbers
    Rules
        Explicit
            - if the input list contains less than 5 elements, return None
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:  

Algorithm
    - if the number of numbers in the list is > 5, return None
    - iterate through list, taking 5 consecutive numbers at a time and summing them
        + store sums in a list
    - return the smallest sum in the sums list
        

Implementation by Code
    - 
"""
def minimum_sum(numbers):
    MIN_LENGTH = 5
    list_length = len(numbers)
    if len(numbers) < MIN_LENGTH:
        return None
    
    sums_list = []
    for i in range(list_length - MIN_LENGTH + 1):
        sum_of_five = sum(numbers[i:i+MIN_LENGTH])
        sums_list.append(sum_of_five)
    return min(sums_list)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

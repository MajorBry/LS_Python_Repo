"""
Problem:  Create a function that determines the index at which the sum of elements before the index is equivalent to the sum of elements after the index.
    Input:  list, of integers
    Output:  integer, index of N
    Rules
        Explicit
            - return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N
                + if there is no index that would make this happen, return -1
            - if you are given a list with multiple answers, return the index with the smallest value
            - The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.
        Implicit
            - exclude the number at the index from both sides
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
def equal_sum_index(numbers):
    if sum(numbers) == 0:
        return 0
    
    for i in range(len(numbers)):
        sum1 = sum(numbers[:i])
        sum2 = sum(numbers[i + 1:])
        if sum1 == sum2:
            return i
    return -1


print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)
# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

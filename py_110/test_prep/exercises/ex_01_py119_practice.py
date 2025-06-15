"""
Problem:  make function to show number value ranking of a list of numbers
    Input:  list, of number
    Output:  list, of number ranking
    Rules
        Explicit
            - When counting numbers, only count unique values.
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  

Algorithm
    - For each list_number in list, iterate through all unique_numbers and count how many are smaller than the current list_number
        + store count in list of numbers


Implementation by Code
    - Use set of list values to find unique values
    - Initialize list of 0s based on how many numbers there are using a list comprehension.
"""
def smaller_numbers_than_current(numbers):
    rank = [0 for number in numbers]
    unique_numbers = set(numbers)
    
    for index, number in enumerate(numbers):
        for unique_number in unique_numbers:
            if number > unique_number:
                rank[index] += 1
                
    return rank

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])
my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

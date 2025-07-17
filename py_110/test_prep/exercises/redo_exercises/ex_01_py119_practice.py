"""
Problem:  function that determines how many numbers are less than each number in a list within that list.
    Input:  list, of numbers
    Output:  list, of number rank
    Rules
        Explicit
            - only count unique values
        Implicit
            - lowest number's rank is 0
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:

Algorithm
    - set a variable equal to the coerced set of list elements
    - assign a counters variable to an empty list
    - for each element in the list:
        + set a counter to 0
        + for each element in the coerced set:
            * increment counter by 1 each time a set member is less than the list element
        + append the counter to the counters list
    - return the counters list

Implementation by Code
    - use set to make a collection of unique values
"""
def smaller_numbers_than_current(numbers):
    unique_numbers = set(numbers)
    return [sum([1 for unique_number in unique_numbers if number > unique_number]) for number in numbers]

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])
my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

"""
Problem:  create a function that splits an input list into two and returns those nested inside of a list
    input: list
    output: list with two elements (each element is a list)
    rules
        explicit
            -put the first half of the original list elements in the first element of the return list
            -put the second half of the original list elements in the second element of the return list
            -If the original list contains an odd number of elements, place the middle element in the first half list.
            -return list always contains 2 lists
        implicit
            -if there is only one element in the original list, that element goes in the first element of the return list
            -if the original list is empty, return two empty lists nested in the return list

Examples/Tests
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

Data Structures: Use lists

Algorithm
    return a list with a slice of the original list in the first element and a slice of the original list in the second element
"""
import math
def halvsies(lst):
    half_index = math.ceil(len(lst)/2)
    return [lst[:half_index], lst[half_index:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

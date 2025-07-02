"""
Problem:  Create a function that determines which two numbers in a list are closest together in value.
    Input:  list, of integers
    Output:  tuple, of 2 integers
    Rules
        Explicit
            -  If there are multiple pairs that are equally close, return the pair that occurs first in the list
        Implicit
            - (?)'return the pair that occurs first in the list' indicates that the pair of numbers where the first number's index is the lowest, or if those are tied, where the second number's index is lower than another pair
            - numbers are all integers, but make this work for other numbers
            - (?)list always has at least 1 pair
    Questions
        - ()

Examples/ Test Cases
↓↓

Data Structures:  store values in a tuple

Algorithm
    - iterate through each element of the list
        + select a first value and iterate through the rest of the values (values having greater indices in list), finding the difference between first and current value
        + if current difference is lower than (not equal to) last difference
            * store current difference values in tuple
    - return difference tuple


Implementation by Code
    - 
"""
def difference(a, b):
    return abs(a - b)

def closest_numbers(numbers):
    lowest_difference = difference(numbers[0], numbers[1])
    closest_pair = (numbers[0], numbers[1])
    
    for index, number1 in enumerate(numbers):
        for number2 in numbers[index + 1:]:
            current_difference = difference(number1, number2)
            if current_difference < lowest_difference:
                lowest_difference = current_difference
                closest_pair = (number1, number2)
    
    return closest_pair

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

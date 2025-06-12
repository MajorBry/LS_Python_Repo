"""
Problem:  make a function to create the maximum rotation of an input number.
    Input:  integer
    Output:  integer, rotated
    Rules
        Explicit
            - rotate each set of last digits in the integer
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ See below ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def rotate_list(lst):
    if type(lst) == list:
        if not lst:
            return []
        return lst[1:] + [lst[0]]

def rotate_rightmost_digits(number, count):
    number_list = list(str(number))
    last_digits = number_list[-count:]
    number_list = number_list[:-count] + rotate_list(last_digits)
    return int(''.join(number_list))

def max_rotation(number):
    for i in range(len(str(number)), 1, -1):
        number = rotate_rightmost_digits(number, i)
    return number

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True
# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

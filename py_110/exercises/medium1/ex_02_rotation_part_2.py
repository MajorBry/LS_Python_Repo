"""
Problem:  create function to rotate the digits in a number
    Input:  integer_number, and integer_count
    Output:  integer
    Rules
        Explicit
            - 
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases


Data Structures:  

Algorithm
    - get number and count
    - coerce number to string
    - coerce string to list
    - get slice of count elements from the end of the list
    - use helper function (made in last exercise) to rotate list elements so the first is brought to the end
    - replace the last elements of the list with the rotated elements
    - join the elements into one string
    - covert the string to an integer
    - return the integer

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


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

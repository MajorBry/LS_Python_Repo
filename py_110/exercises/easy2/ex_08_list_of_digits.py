"""
Problem:  write a function that creates a list of digits in a number
    Input:  integer, positive
    Output:  list, of digits
    Rules
        Explicit
            - list contains an element for each digit in the order it was included in the number
            - input is positive
        Implicit
            - input is not zero
    Questions
        - N/A

Examples/ Test Cases
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

Data Structures:  list

Algorithm
    - coerce integer to string
    - coerce string to list
    - iterate over list and coerce each element in list to integer
    - return digit list

Implementation by Code
    - 
"""
def digit_list(number):
    return [int(element) for element in str(number)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

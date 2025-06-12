"""
Problem:  create a function that returns the next sequential 'featured number', as specified below
    Input:  integer
    Output:  next featured number
    Rules
        Explicit
            - featured number has each digit only appearing once, is odd, and is a multiple of 7
        Implicit
            - return error message string: "There is no possible number that fulfills those requirements." if the number of digits in the number would extend past 10.
            - the returned next featured number is not the same as the input
            - the returned number is greater than the input number
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def is_odd(number):
    return number % 2 != 0

def is_multiple_of_seven(number):
    return number % 7 == 0

def has_unique_digits(number):
    number_list = list(str(number))
    number_set = set(number_list)
    return len(number_list) == len(number_set)

def next_featured(first_number):
    OUT_OF_BOUNDS = 10_000_000_000 # ← 11 digits is where next featured number does not exist
    PRIMARY_ADDEND = 14
    SECONDARY_ADDEND = 2

    if not is_odd(first_number):
        number = first_number + 1
    else:
        number = first_number + 2
    while number < OUT_OF_BOUNDS:
        if is_multiple_of_seven(number):
            if has_unique_digits(number):
                return number
            number += PRIMARY_ADDEND
        else:
            number += SECONDARY_ADDEND
    return "There is no possible number that fulfills those requirements."

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True
error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

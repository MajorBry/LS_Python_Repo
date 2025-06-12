"""
Problem:  make 2 functions, 1) to create a group of denominators to form an egyptian fraction and 2) to create a rational number which the egyptian fraction represents.
    Input:  
        - function 1: rational number (Fraction)
        - function 2: list, of egyptian fraction denominators
    Output:  
        - function 2: rational number (Fraction)
        - function 1: list, of egyptian fraction denominators
    Rules
        Explicit
            - egyptian fractional representation is the sum of fractions each having a numerator of 1 and distinct denominators
        Implicit
            - input is positive
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
from fractions import Fraction
def egyptian(number):
    egyptian_list = []
    denominator = 1
    
    while True:
        new_fraction = Fraction(1, denominator)
        if number - new_fraction >= 0:
            egyptian_list.append(denominator)
            number -= new_fraction
        if number == 0:
            return egyptian_list
        denominator += 1

def unegyptian(lst):
    result = 0
    for den in lst:
        result += Fraction(1, den)
    return result

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]
# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))

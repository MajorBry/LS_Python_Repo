"""
Problem:  Create a function that finds the greatest product of 4 consecutive digits.
    Input:  string, of numeric digits
    Output:  integer, greatest product of 4 consecutive digits
    Rules
        Explicit
            - string input will always have more than 4 digits
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:  break up string input into list elements, and convert each to int

Algorithm
    - convert input to a collection of numbers
    - multiply each consecutive set of numbers in the collection, and store their products in a new products collection
        + NOTE: the length of the numbers collection - 3 is equivalent to the number of products (number of product process iterations)
            * Use the number of iterations to determine the loop number
        + NOTE: index notation from 0 to 3 plus the current iteration number can be used to access the collection numbers needed
        + 
    - find the maximum value in the products collection and return it

Implementation by Code
    - convert string input to a list of integers
"""
def string_to_list_of_integers(string):
    return [int(char) for char in string]

def greatest_product(digit_string):
    multiplicands = 4
    digits = string_to_list_of_integers(digit_string)
    number_of_products = len(digits) - (multiplicands - 1)
    products = [digits[i] * digits[i + 1] * digits[i + 2] * digits[i + 3] for i in range(number_of_products)]

    return max(products)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

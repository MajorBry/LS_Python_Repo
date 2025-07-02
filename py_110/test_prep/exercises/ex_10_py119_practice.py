"""
Problem:  Create a function that counts the number of even-numbered substrings in a string.

    Input:  string, of digits (integers)
    Output:  integer, number of possible even-numbered substrings
    Rules
        Explicit
            - If a substring occurs more than once, you should count each occurrence as a separate substring.
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases


Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def is_even_string(number_string):
    # print(number_string)
    return int(number_string) % 2 == 0

def even_substrings(string):
    evens_count = 0
    for index1, digit1 in enumerate(string):
        for index2, digit2 in enumerate(string[index1:]):
            # print(string[index1:index2 + 1])
            if is_even_string(string[index1:index1 + index2 + 1]):
                evens_count += 1
    return evens_count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

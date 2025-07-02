"""
Problem:  Create a function that finds the sum of all multiples of 7 and 11 less than a given number.


    Input:  integer
    Output:  integer, sum
    Rules
        Explicit
            - the returned sum includes all multiples of 7 or 11 that are less than the argument as operands
            - if a number is a multiple of both 7 and 11, it is only added as an operand once
            - if the argument is negative, return 0
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
    - For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.
↓↓ See Test Cases Below ↓↓

Data Structures:  

Algorithm
    - guard clause: if function argument passed to the function is negative, return 0.
    - find the integer quotients (q) of input integer divided by 7, and 11.
    - add the unique multiples of 7 and 11 from 1 to q to a collection object.
    - sum the values from the collection and return the sum.

Implementation by Code
    - Use set as collection object to store only unique multiples of 7 and 11.
"""
def seven_eleven(umbrella_number):
    if umbrella_number < 7:
        return 0
    
    multiples_of_7 = range(0, umbrella_number, 7)
    multiples_of_11 = range(0, umbrella_number, 11)
    multiples_of_7_and_11 = set(multiples_of_7) | set(multiples_of_11)
    return sum(multiples_of_7_and_11)


print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
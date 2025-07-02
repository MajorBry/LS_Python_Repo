"""
Problem:  Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equals the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.
    Input:  list, of integers
    Output:  integer
    Rules
        Explicit
            - returned integer is the number that when added to the sum of the numbers from the input list is equivalent to the nearest prime number greater than the original sum.
            - The list will always contain at least 2 integers.
            - All values in the list must be positive (> 0).
            - There may be multiple occurrences of the various numbers in the list.
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:  

Algorithm
    - Need a procedure to determine next prime number.
    - subtract sum of list numbers from prime number to get the integer return value

Implementation by Code
    - 
"""
def is_prime(test_number):
    if test_number == 1:
        return False
    if test_number == 2:
        return True
    if test_number % 2 == 0:
        return False
    
    for divisor in range(3, int(test_number**(1/2)) + 1, 2):
        if test_number % divisor == 0:
            return False
    
    return True

def next_prime(number):
    while True:
        number += 1
        
        if is_prime(number):
            return number

def nearest_prime_sum(numbers):
    total = sum(numbers)

    return next_prime(total) - total

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37
# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

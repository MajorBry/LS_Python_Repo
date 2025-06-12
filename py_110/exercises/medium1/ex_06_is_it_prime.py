"""
Problem:  make is_prime function
    Input:  integer, positive
    Output:  bool, True if prime, otherwise False
    Rules
        Explicit
            - No add-on packages
            - Find the solution programmatically
            - Prime numbers are divisible only be themselves and 1
            - Has to be able to handle very large prime numbers
        Implicit
            - even numbers (except for 2) are not prime
            - 1 is not prime
            - odd numbers are only evenly divisible by other odd numbers
            - the smallest number that an odd number is evenly divisible by is 3, which means only numbers 1/3 or less than the input number may be factors
            - all non-prime numbers are divisible by prime numbers
    Questions
        - ()

Examples/ Test Cases
↓ See Below ↓

Data Structures:  

Algorithm
    Note: it seems like a faster (more efficient) solution may come from recognizing that when a divisor is not a factor of the test number (and no numbers less than the divisor are factors), neither will any numbers greater than test number / divisor be factors of the test number.  Therefore, if there are any factors of the test number, at least one must be less than or equal to the square root of the test number.
    - Use prime-number-divisors to determine whether the test number has any factors

Implementation by Code
    - carefully examine recursive behavior
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

print(is_prime(1) == False)                       # True
print(is_prime(2) == True)                        # True
print(is_prime(3) == True)                        # True
print(is_prime(4) == False)                       # True
print(is_prime(5) == True)                        # True
print(is_prime(6) == False)                       # True
print(is_prime(7) == True)                        # True
print(is_prime(8) == False)                       # True
print(is_prime(9) == False)                       # True
print(is_prime(10) == False)                      # True
print(is_prime(23) == True)                       # True
print(is_prime(24) == False)                      # True
print(is_prime(997) == True)                      # True
print(is_prime(998) == False)                     # True
print(is_prime(3_297_061) == True)                # True
print(is_prime(23_297_061) == False)              # True
print(is_prime(1_227_340_408_265_021_263) == True)  # True
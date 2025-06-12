"""
Problem:  write a fibonacci number function
    Input:  integer
    Output:  integer, nth fibonacci number
    Rules
        Explicit
            - each number in the fibonacci sequence is equal to the sum of the previous 2 numbers (starting with 1 and 1)
            - no use of recursion
        Implicit
            - if 1 or 2 is the input, output is simply 1
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
def fibonacci(number):
    num1 = 1
    num2 = 1

    if number == 1 or number == 2:
        return 1
    
    for _ in range(number - 2):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num3

# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(40) == 102334155)     # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True
for _ in range(10000):
    fibonacci(1900)

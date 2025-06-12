def fibonacci(number, memoization_table={}):
    if number == 1 or number == 2:
        return 1
    elif number in memoization_table:
        return memoization_table[number]
    
    fib1 = memoization_table.setdefault((number - 2), fibonacci(number - 2))
    fib2 = memoization_table.setdefault((number - 1), fibonacci(number - 1))
    #print(number, memoization_table)
    return fib1 + fib2

# print(fibonacci(1) == 1)              # True
# print(fibonacci(2) == 1)              # True
# print(fibonacci(3) == 2)              # True
# print(fibonacci(4) == 3)              # True
# print(fibonacci(5) == 5)              # True
# print(fibonacci(6) == 8)              # True
# print(fibonacci(12) == 144)           # True
# print(fibonacci(20) == 6765)          # True
# print(fibonacci(40) == 102334155)     # True
# print(fibonacci(75) == 2111485077978050)  # True
for _ in range(10000):
    fibonacci(1900)

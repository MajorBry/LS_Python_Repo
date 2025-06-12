import sys
sys.set_int_max_str_digits(50_000)

def fibonacci(number, memoization_table={}):
    if number == 1 or number == 2:
        return 1
    elif number in memoization_table:
        return memoization_table[number]
    
    fib1 = memoization_table.setdefault((number - 2), fibonacci(number - 2))
    fib2 = memoization_table.setdefault((number - 1), fibonacci(number - 1))
    #print(number, memoization_table)
    return fib1 + fib2

def find_fibonacci_index_by_length(number_digits):
    i = 1
    while True:
        if len(str(fibonacci(i))) >= number_digits:
            return i
        i += 1

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)
# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)

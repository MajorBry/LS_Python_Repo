# ↓ Assume argument is always a positive integer.
def factorial(num):
    product = 1
    for i in range(1,num + 1):
        product *= i
    return product

for i in range(1,9):
    print(factorial(i))

print(factorial(25))

# ↓ Refactored to handle negative numbers
def factors(number):
    divisor = number
    result = []
    while divisor > 0:  # ← changed from: while divisor != 0
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-1))
print(factors(0))
print(factors(2))
print(factors(10))
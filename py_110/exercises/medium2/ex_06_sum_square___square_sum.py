def square_sum(iterable):
    return sum(iterable)**2

def sum_square(iterable):
    squares = [number**2 for number in iterable]
    return sum(squares)

def sum_square_difference(number):
    sequence = range(1, number + 1)
    return square_sum(sequence) - sum_square(sequence)

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

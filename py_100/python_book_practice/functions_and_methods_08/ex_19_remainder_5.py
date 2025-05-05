# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

numbers_list = [numbers_1, numbers_2, numbers_3, numbers_4]

i = 1
for x in numbers_list:
    if any(remainders_5(x)):
        print(f'numbers_{i} contains at least one number not evenly divisible by 5.')
    i += 1

def double_numbers(numbers):
    for ind, number in enumerate(numbers):
        numbers[ind] = number * 2

my_numbers = [1, 4, 3, 7, 2, 6]
double_numbers(my_numbers)
print(my_numbers) # [2, 8, 6, 14, 4, 12]
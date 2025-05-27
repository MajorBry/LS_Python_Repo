def double_odd_numbers(numbers):
    transformed_numbers = []
    for ind, number in enumerate(numbers):
        if ind % 2 == 1:
            transformed_numbers.append(number * 2)
        else:
            transformed_numbers.append(number)
    return transformed_numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_numbers(my_numbers))

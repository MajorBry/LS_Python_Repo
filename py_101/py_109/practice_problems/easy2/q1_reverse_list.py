numbers = [1, 2, 3, 4, 5]

numbers_reversed1 = list(reversed(numbers))
numbers_reversed2 = numbers[::-1]

numbers_reversed3 = []
for x in range(len(numbers)):
    numbers_reversed3.append(numbers[len(numbers) - x -1])


print(numbers_reversed1)
print(numbers_reversed2)
print(numbers_reversed3)
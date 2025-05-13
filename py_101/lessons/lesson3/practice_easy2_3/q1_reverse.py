numbers = [1, 2, 3, 4, 5]

reversed_numbers1 = numbers.copy()
reversed_numbers1.reverse()

reversed_numbers2 = []
for number in numbers:
    reversed_numbers2.insert(0,number)

reversed_numbers3 = numbers[::-1] # ← My personal favorite

reversed_numbers4 = list(reversed(numbers))

print(numbers)
print(reversed_numbers1)
print(reversed_numbers2)
print(reversed_numbers3)
print(reversed_numbers4)
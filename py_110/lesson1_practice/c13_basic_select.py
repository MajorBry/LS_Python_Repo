# numbers = [1, 3, 9, 11, 1, 4, 1]
# ones = []

# for current_num in numbers:
#     if current_num == 1:
#         ones.append(current_num)

# # ones = [number for number in numbers if number == 1]

# print(ones)

fruits = ['apple', 'banana', 'pear']
transformed_elements = []

for current_element in fruits:
    transformed_elements.append(current_element + 's')

# OR
# transformed_elements = [fruit + 's' for fruit in fruits]

print(transformed_elements)
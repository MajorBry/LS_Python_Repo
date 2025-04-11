# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

flattened_list = []
i = 0
while i < len(my_list):
    flattened_list.extend(my_list[i])
    i += 1

# Assumptions:
# 1. my_list has only 2 levels of nesting.
# 2. my_list only contains lists of numbers
# ↓ ! No for loops.
i = 0
while i < len(flattened_list):
    if flattened_list[i] % 2 == 0:
        print(flattened_list[i])
    i += 1

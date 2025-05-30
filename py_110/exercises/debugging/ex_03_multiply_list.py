def multiply_list(lst):
    new_list = []
    for item in lst:
        new_list.append(item * 2)

    return new_list

print(multiply_list([1, 2, 3]) == [2, 4, 6])
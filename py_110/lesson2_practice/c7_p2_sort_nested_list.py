lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_list = []
for sublist in lst:
    new_list.append(sorted(sublist))
print(new_list)

new_list2 = [sorted(sublist) for sublist in lst]
print(new_list2)
print(lst)
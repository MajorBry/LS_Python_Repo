lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_lst = []
for subdict in lst:
    new_dict = {}
    for key in subdict.keys():
        new_dict[key] = subdict[key] + 1
    new_lst.append(new_dict)
print(lst)
print(new_lst)

new_lst2 = [{key: value + 1 for key, value in subdict.items()} for subdict in lst]
print(lst)
print(new_lst2)
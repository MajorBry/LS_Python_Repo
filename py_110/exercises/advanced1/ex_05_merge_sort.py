def merge(lst1, lst2):
    new_list = []
    ind1, ind2 = (0, 0)
    len1, len2 = (len(lst1), len(lst2))
    
    while ind1 < len1 and ind2 < len2:
        if lst1[ind1] <= lst2[ind2]:
            new_list.append(lst1[ind1])
            ind1 += 1
        else:
            new_list.append(lst2[ind2])
            ind2 += 1

    new_list.extend(lst1[ind1:])
    new_list.extend(lst2[ind2:])

    return new_list

def nest_list(lst):
    len_lst = len(lst)
    half_index = len_lst // 2

    if half_index:
        new_lst1 = merge_sort(lst[:half_index])
        new_lst2 = merge_sort(lst[half_index:])
        return merge(new_lst1, new_lst2)
    else:
        return lst

def merge_sort(lst):
    nested_list = nest_list(lst)
    
    return nested_list

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])
original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)
original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)

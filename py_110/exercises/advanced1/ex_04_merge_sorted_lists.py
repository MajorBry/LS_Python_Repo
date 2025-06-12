"""
Algorithm:
    1. compare element from each list corresponding to list index:
        + if an el1 <= el2: append el1 to new list
            * increment list1 index
        + else: append el2 to new list
            * increment list2 index
        + if there are more elements in both lists:
            * loop back to 1,
        + else:
            * extend new_list with whichever list still has elements after the corresponding index
    3. 
        
"""
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

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

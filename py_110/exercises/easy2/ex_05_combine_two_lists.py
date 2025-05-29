"""
Problem:  make a function that shuffles two lists together, alternatingly, into one new list
    input: 2 lists
    output: 1 new list
    rules
        explicit
            - input lists are non-empty
            - input lists have the same length
            - new list contains all elements from both input lists, with each element taken in alternation
        implicit
            - function doesn't mutate its arguments
            - first element comes from the first list

E/Tests
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

Data Structures:  lists

Algorithm
    - iterate through indices in len(list), appending elements from list1 then list2 to new_list

"""
def interleave(list1, list2):
    new_list = []
    for i in range(0,len(list1)):
        new_list.append(list1[i])
        new_list.append(list2[i])
    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

def interleave_zip(list1, list2):
    new_list = []
    for pair in zip(list1, list2):
        new_list.extend(pair)
    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave_zip(list1, list2) == expected)   # True
"""
Problem:  make a function that moves the first element to the end of the list
    Input:  list
    Output:  new list
    Rules
        Explicit
            - Do not mutate the input list (return a new list)
            - if input is empty, return empty list
            - if the input is not a list, return None
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ See below ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def rotate_list(lst):
    if type(lst) == list:
        if not lst:
            return []
        return lst[1:] + [lst[0]]


# All of these examples should print True
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])
# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)
# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

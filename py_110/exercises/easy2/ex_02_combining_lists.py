"""
Problem: create union function
    Input: 2 lists
    Output: 1 set
    rules
        explicit
            -both arguments will always be lists
    assumptions
        -both lists contain only hashable elements

Test
    print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

Algorithm
    - coerce both lists to sets and return the union (using union operator) of the two

"""
def union(list1, list2):
    return set(list1) | set(list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
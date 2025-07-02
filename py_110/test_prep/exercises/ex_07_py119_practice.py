"""
Problem:  Make a function that finds pairs of identical integers from a list (exclusive)
    Input:  list, of integers
    Output:  integer, number of identical pairs
    Rules
        Explicit
            - If the list is empty or contains exactly one value, return 0
            - If a certain number occurs more than twice, count each complete pair once ([1,1,1,1]) is two pairs
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ ↓

Data Structures:  Use dictionary to record each integer:count

Algorithm
    - 

Implementation by Code
    - 
"""
def pairs(numbers):
    numbers_count = {}
    for number in numbers:
        numbers_count[number] = numbers_count.setdefault(number, 0) + 1

    number_pairs = [number_count // 2 for number_count in numbers_count.values()]
    return sum(number_pairs)


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

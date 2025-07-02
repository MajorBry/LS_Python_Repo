"""
Problem:  Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.
    Input:  string, of alphanumeric characters
    Output:  integer, count
    Rules
        Explicit
            - 
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓↓ See Test Cases Below ↓↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def distinct_multiples(string):
    multiples_dict = {}

    for char in string.casefold():
        if multiples_dict.get(char) != None:
            multiples_dict[char] += 1
        else:
            multiples_dict[char] = 0

    multiples_count = 0
    for num in multiples_dict.values():
        if num > 0:
            multiples_count += 1
     
    return multiples_count

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

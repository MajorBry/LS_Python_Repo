"""
Problem:  determine and return a list that contains only those dictionaries where all numbers are even
    Input:  list, of dictionaries with nested lists
    Output:  list, of even-numbers-only dictionaries
    Rules
        Explicit
            - all numbers in selected dicts must be even 
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
    Given: lst = [
        {'a': [1, 2, 3]},
        {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
        {'e': [8], 'f': [6, 10]},
    ]
    Output: [{'e': [8], 'f': [6, 10]}]

Data Structures:  

Algorithm
    - iterate to access each dictionary in list
    - iterate to access each list in each key-value pair of each dictionary
    - iterate to access each element of each list in each key-value pair
    - determine whether each element is even
        - for dictionaries where all lists only contain even numbers, add those dictionaries to the new list.

    - Create a function that returns whether a dictionary has lists that only contain even numbers.
        - Use this function as the selection criteria for a list comprehension on the original list.

Implementation by Code
    - 
"""

def dict_value_sublists_only_contain_even_integers(dictionary):
    for number_list in dictionary.values():
        for number in number_list:
            if number % 2 != 0:
                return False
    return True

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

selected_dictionary_list = [dictionary for dictionary in lst if dict_value_sublists_only_contain_even_integers(dictionary)]
print(selected_dictionary_list)
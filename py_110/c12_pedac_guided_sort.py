"""
Problem:  create a function that sorts a list of strings based on the highest number of adjacent consonants
    Input:  list, of strings
    Output:  list, sorted input list
    Rules
        Explicit
            - list elements maintain relative order except where sorted (i.e. if two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other)
            - 'adjacent' consonants are next to each other in the same word or with a space between
        Implicit
            - string elements may contain multiple words
            - (y)words are sorted with words having the highest number of adjacent consonants coming first (descending)
            - (y)a 'word' is any sequence of characters separated by a whitespace character (including spaces, newlines, etc.), contained within one string
            - (y)a 'consonant' is a letter (a-z) that is not in (a, e, i, o, u, y)
            + having solo consonants doesn't affect a string's sort order
            + character comparison is case insensitive
    
    Questions
        - Can inputs contain special characters and/or whitespace characters other than spaces ' '? (no, ask/answer)
        - How to handle letter case? (case insensitive, ask/answer)
        - Will input be an empty list? (no, ask/answer)
        - Will input list contain empty strings?  If so, how should empty strings be handled? (no, ask/answer)
        + If a string has no adjacent consonants, does it rank the same (for sort order) as strings with no consonants? (yes, ask/answer)

Examples/ Test Cases
    my_list = ['aa', 'baa', 'ccaa', 'dddaa']
    print(sort_by_consonant_count(my_list))
    # ['dddaa', 'ccaa', 'aa', 'baa']

    my_list = ['can can', 'toucan', 'batman', 'salt pan']
    print(sort_by_consonant_count(my_list))
    # ['salt pan', 'can can', 'batman', 'toucan']
    
    my_list = ['bar', 'car', 'far', 'jar']
    print(sort_by_consonant_count(my_list))
    # ['bar', 'car', 'far', 'jar']
    
    my_list = ['day', 'week', 'month', 'year']
    print(sort_by_consonant_count(my_list))
    # ['month', 'day', 'week', 'year']
    
    my_list = ['xxxa', 'xxxx', 'xxxb']
    print(sort_by_consonant_count(my_list))
    # ['xxxx', 'xxxb', 'xxxa']

Data Structures:  Use lists for storing and organizing strings.

Algorithm
    - Iterate through each string (element) of the input strings (list)
        - Loop through each character in the current string
            - If character is a consonant: add 1 to consonant counter (initialized to -1) and check consonant counter against string sort number (initialized to 0).  If consonant counter > string sort number, set string sort number to consonant counter.
            - If character is a space, move on to next character
            - If character is not a consonant or space: set consonant counter to -1
        - Record string sort number for use in sorting list.
    - Sort list according to string sort numbers.

Code
    - Create two functions, a helper function and a main function.
    - Remember that we don't want to mutate the caller, so either create a shallow copy of the list (list of strings means a deepcopy isn't necessary) or use non-destructive methods only.
    - May use a set to determine which characters are consonants.
    - Use casefold() method for string comparisons, or include both capitalized and lowercase consonants
"""
def highest_adjacent_consonant_count(string):
    CONSONANTS = 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'
    consonant_counter = -1
    string_sort_number = 0
    for char in string:
        if char in CONSONANTS:
            consonant_counter += 1
            if consonant_counter > string_sort_number:
                string_sort_number = consonant_counter
        elif char.isspace():
            continue
        else:
            consonant_counter = -1
    return string_sort_number

# ↓ strings local variable is a list of strings
def sort_by_consonant_count(strings):
    def sort_by_dict(string):
        nonlocal sort_order
        return sort_order[string]
    sort_order = {}

    for string in strings:
        sort_order [string] = highest_adjacent_consonant_count(string)
    return sorted(strings, key=sort_by_dict, reverse=True)

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])
# ['xxxx', 'xxxb', 'xxxa']
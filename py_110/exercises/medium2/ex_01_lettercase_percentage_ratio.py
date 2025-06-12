"""
Problem:  make function that finds the percentages of uppercase, lowercase, and other characters in a string
    Input:  string, always has at least 1 char
    Output:  dictionary, has 'uppercase', 'lowercase', and 'neither' keys, each having string values
    Rules
        Explicit
            - values of dictionary members are strings having a percentage
            - percentage should have a two-point precision after decimal point
        Implicit
            - if percentage is less than 1, a 0 should still appear before the decimal point
            - anything that is not a letter is in the 'neither' category
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  dictionary stores percentages as strings

Algorithm
    - 

Implementation by Code
    - Use f-strings with formatting to set values
    - Dictionary values could be floats and convert to strings before returning
"""
def letter_percentages(string):
    number_chars = len(string)
    number_uppercase_chars = 0
    number_lowercase_chars = 0
    number_neither_chars = 0
    
    for char in string:
        if char.isalpha():
            if char.islower():
                number_lowercase_chars += 1
            else:
                number_uppercase_chars += 1
        else:
            number_neither_chars += 1
    
    return {'lowercase':f'{number_lowercase_chars/number_chars*100:.2f}',
            'uppercase':f'{number_uppercase_chars/number_chars*100:.2f}',
            'neither':f'{number_neither_chars/number_chars*100:.2f}'}

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)
expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)
expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
